#%%
from rich.console import Console
import time
import numpy as np
from typing import List
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import nltk
import re
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

nltk.download("gutenberg")
c = Console(record=True)

# UTILITIES


def timer(f: callable, *args, **kwargs):
    def wrapper(*args, **kwargs):
        tic = time.time()
        result = f(*args, **kwargs)
        tac = time.time()
        c.print(f"-> took {tac - tic:8.5f} seconds.")
        return result

    return wrapper


def benchmark_runner(
    bench_function: callable, title: str = "", n_runs: int = 3, *args, **kwargs
):
    c.print(f"{title:=^40}")
    tic = time.time()
    for run in range(n_runs):
        bench_function(*args, **kwargs)
    tac = time.time()
    c.print("-" * 40)
    c.print(f"AVG = {(tac - tic) / n_runs:.5f} seconds.")
    c.print("-" * 40)


# BENCHMARK FUNCTIONS
@timer
def matrix_multiply(a, b):
    res = np.dot(a, b)
    return res


@timer
def monte_carlo():
    random_returns = np.random.normal(0, 1, (100_000, 365)) + 1
    return random_returns.cumprod(axis=1)


@timer
def string_processing(word_list: List[str]):
    s = " ".join(word_list)
    l = (x.strip().lower() for x in s.split())
    l = (x for x in l if x != "")
    l = (x.upper() if x[0] == "a" else x.lower() for x in l)
    is_year = [re.match(r"\d{4}", x) for x in l]

    return " ".join(l), is_year


@timer
def tfidf_convert(word_list: List[str]):
    cv = CountVectorizer()
    mtx = cv.fit_transform(word_list)
    tfer = TfidfTransformer()
    return tfer.fit_transform(mtx)


@timer
def fit_rf(X, y):
    rf = RandomForestRegressor(n_estimators=2000, n_jobs=-1)
    rf.fit(X, y)
    return "Done."


@timer
def fit_rf_synthetic(X, y):
    rf = RandomForestRegressor(n_estimators=100, n_jobs=-1, max_depth=10)
    rf.fit(X, y)
    return "Done."


@timer
def scatterplotting(df: pd.DataFrame):
    sns.scatterplot(data=df, x="a", y="b")
    plt.savefig("test.png")
    return "Done."


# EXECUTION
# Matrix Multiply
a = np.random.randint(-100, 100, (3_000, 100)).astype(np.int16)
b = np.random.randint(-100, 100, (100, 3_000)).astype(np.int16)

benchmark_runner(matrix_multiply, n_runs=5, title="Matrix Multiply", a=a, b=b)
del a, b


# Monte Carlo
benchmark_runner(monte_carlo, n_runs=5, title="Monte Carlo Random Walk")

# String Processing
emma = nltk.corpus.gutenberg.words("austen-emma.txt")
benchmark_runner(string_processing, n_runs=5, title="String Processing", word_list=emma)

benchmark_runner(tfidf_convert, n_runs=5, title="TFIDF from string", word_list=emma)
del emma

# Fitting RF with all cores
data = sns.load_dataset("tips")
catcols = data.select_dtypes("category").columns
for col in catcols:
    data[col] = data[col].cat.codes

benchmark_runner(
    fit_rf,
    n_runs=5,
    X=data.drop("tip", axis=1),
    y=data.tip,
    title="Fitting RF in parallel",
)

benchmark_runner(
    fit_rf,
    n_runs=1,
    X=np.random.random((5_000, 15)),
    y=np.random.random(5_000),
    title="Fitting RF in parallel on _synthetic_ data",
)


benchmark_runner(
    scatterplotting,
    n_runs=1,
    df=pd.DataFrame(np.random.random((1_000_000, 2)), columns=["a", "b"]),
    title="Scatterplotting 1M points",
)

# SAVE LOG
c.save_text("benchmarks.log")
