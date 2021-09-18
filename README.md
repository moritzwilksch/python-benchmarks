# Python Benchmarks
A couple of ML-related benchmarks for testing CPU performance of different machines

# Stats Table
Seconds taken for completition (lower is better)  
|Machine | Matrix Multiply | MC Random Walk | String Processing | TFIDF from String | RF |
|-----|:---:|:---:|:---:|:---:|:---:|
|**Hetzner CPX21 (3 AMD cores, 4GB RAM)**| 0.92 |1.56 | 0.38 |0.97 | 4.18 |
|**MacBook Pro 2020 (2GHz QC i5, 16GB RAM)** | 0.67 | 1.24 | 0.35 | 0.63 |2.30 |
|**Vultr Cloud Compute (4 cores, 8GB RAM)**| 0.97 | 1.46 | 0.36 | 0.65| 3.65|
|**Vultr HFC Compute (3 cores, 8GB RAM)**|0.59 | 0.77 | 0.21 | 0.36 | 1.63|
|**Hetzner CCX12 (2 cores, 8GB RAM)**| 1.00 | 1.23 | 0.34 | 0.65 | 2.31|
|**Hetzner CCX22 (4 AMD cores, 16GB RAM)**| 0.83 | 1.01 | 0.34 | 0.68 | 3.42 |
|**Hetzner CCX22 (4 Intel cores, 16GB RAM)**| 0.73 | 1.12 | 0.27 | 0.50 | 3.23 |
|**GCP e2-small (2 cores, 2GB RAM)** | 0.94 | 1.84 | 0.35 | 0.65 | 5.38 |

# Raw Stats

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
```

## Hetzner CCX12 (2 cores, 8GB RAM)
```
============Matrix Multiply=============
AVG = 1.00685 seconds.
----------------------------------------
========Monte Carlo Random Walk=========
AVG = 1.23441 seconds.
----------------------------------------
===========String Processing============
AVG = 0.34189 seconds.
----------------------------------------
===========TFIDF from string============
AVG = 0.64542 seconds.
----------------------------------------
=========Fitting RF in parallel=========
AVG = 2.31264 seconds.
----------------------------------------
```
## Hetzner CCX22 (4 AMD cores, 16GB RAM)
```
============Matrix Multiply=============
AVG = 0.83095 seconds.
----------------------------------------
========Monte Carlo Random Walk=========
AVG = 1.01186 seconds.
----------------------------------------
===========String Processing============
AVG = 0.34142 seconds.
----------------------------------------
===========TFIDF from string============
AVG = 0.68159 seconds.
----------------------------------------
=========Fitting RF in parallel=========
AVG = 3.45099 seconds.
----------------------------------------
```

## Hetzner CCX22 (4 Intel Xeon Gold cores, 16GB RAM)
```
============Matrix Multiply=============
AVG = 0.72997 seconds.
----------------------------------------
========Monte Carlo Random Walk=========
AVG = 1.11520 seconds.
----------------------------------------
===========String Processing============
AVG = 0.26992 seconds.
----------------------------------------
===========TFIDF from string============
AVG = 0.49575 seconds.
----------------------------------------
=========Fitting RF in parallel=========
AVG = 3.22997 seconds.
----------------------------------------
```



## GCP e2-small (2 cores, 2GB RAM)
```
============Matrix Multiply=============
AVG = 0.93765 seconds.
----------------------------------------
========Monte Carlo Random Walk=========
AVG = 1.84276 seconds.
----------------------------------------
===========String Processing============
AVG = 0.35271 seconds.
----------------------------------------
===========TFIDF from string============
AVG = 0.64941 seconds.
----------------------------------------
=========Fitting RF in parallel=========
AVG = 5.38431 seconds.
----------------------------------------

```
