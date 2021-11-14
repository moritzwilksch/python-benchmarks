#%%
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import tempfile


#%%
with open("README.md", "r") as f:
    lines = [x for x in f.readlines() if x.startswith("|")]

with tempfile.TemporaryFile() as f:
    f.write("\n".join(lines).encode())
    f.seek(0)
    df = pd.read_table(f, sep="|").drop(["Unnamed: 0", "Unnamed: 7"], axis=1)

df.columns = [x.strip() for x in df.columns]
df = df.loc[~df["Machine"].str.contains("---"), :].assign(
    Machine=lambda x: x["Machine"].str.strip("** ")
)

#%%
meltdf = (
    df.melt(id_vars=["Machine"], var_name="Benchmark", value_name="Time")
    .assign(Benchmark=lambda x: x['Benchmark'].astype("category"))
    .assign(Time=lambda x: x['Time'].astype("float"))
    .assign(Machine=lambda x: x['Machine'].astype("string"))
)

#%%
fig, axes = plt.subplots(5, 1, figsize=(10, 20))
for idx, bm in enumerate(meltdf["Benchmark"].unique()):
    subset = meltdf.loc[meltdf["Benchmark"] == bm, :].copy()
    subset.sort_values(by="Time", inplace=True, ascending=False)
    sns.barplot(data=subset, orient="h", x="Time", y="Machine", palette="RdYlGn", ax=axes[idx])
    axes[idx].set_title(bm, weight="bold")

sns.despine()
plt.tight_layout()
plt.savefig("benchmark_plot.png", dpi=300, facecolor="w")
