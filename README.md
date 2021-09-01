# Python Benchmarks
A couple of ML-related benchmarks for testing CPU performance of different machines

## Hetzner CPX21 (3 AMD cores, 4GB RAM)
```
============Matrix Multiply=============
AVG = 0.91745 seconds.
----------------------------------------
========Monte Carlo Random Walk=========
AVG = 1.55901 seconds.
----------------------------------------
===========String Processing============
AVG = 0.38183 seconds.
----------------------------------------
===========TFIDF from string============
AVG = 0.97871 seconds.
----------------------------------------
=========Fitting RF in parallel=========
AVG = 4.18186 seconds.
----------------------------------------
```

## MacBook Pro 2020 (2GHz Quad-Core i5, 16GB RAM)
```
============Matrix Multiply=============
AVG = 0.67405 seconds.
----------------------------------------
========Monte Carlo Random Walk=========
AVG = 1.23808 seconds.
----------------------------------------
===========String Processing============
AVG = 0.35248 seconds.
----------------------------------------
===========TFIDF from string============
AVG = 0.62952 seconds.
----------------------------------------
=========Fitting RF in parallel=========
AVG = 2.29664 seconds.
----------------------------------------
```

## Vultr Cloud Compute (4 cores, 8GB RAM)
```
============Matrix Multiply=============
AVG = 0.97056 seconds.
----------------------------------------
========Monte Carlo Random Walk=========
AVG = 1.45590 seconds.
----------------------------------------
===========String Processing============
AVG = 0.35676 seconds.
----------------------------------------
===========TFIDF from string============
AVG = 0.64996 seconds.
----------------------------------------
=========Fitting RF in parallel=========
AVG = 3.64806 seconds.
----------------------------------------
```

## Vultr HFC Compute (3 cores, 8GB RAM)
```
============Matrix Multiply=============
AVG = 0.58813 seconds.
----------------------------------------
========Monte Carlo Random Walk=========
AVG = 0.76691 seconds.
----------------------------------------
===========String Processing============
AVG = 0.20985 seconds.
----------------------------------------
===========TFIDF from string============
AVG = 0.35890 seconds.
----------------------------------------
=========Fitting RF in parallel=========
AVG = 1.63479 seconds.
----------------------------------------
