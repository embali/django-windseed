# Windseed-Django

Repository with Django benchmark to compare with [Windseed] (https://github.com/embali/windseed) 
benchmark


## Prerequisites

- Ubuntu 14.10 x64
- PostgreSQL 9.3
- Python 3.5+
- Django 1.9.4
- uWSGI 2.0.12


## Setup environment and packages

```
pyvenv-3.5 .env

source .env/bin/activate

pip install -r requirements.txt
```


## Performance

- Intel® Pentium(R) CPU 2117U @ 1.80GHz × 2
- 4 Gb RAM

Testing with ab (Apache Benchmark) with various number of requests (n),
concurrency level (c) and page (page):
```
ab -n <n> -c <c> -r http://localhost:8000/?page=<page>
```

```
DEBUG=False

uwsgi --module=djangotest.wsgi:application
      --env DJANGO_SETTINGS_MODULE=djangotest.settings
      --http=127.0.0.1:8000
      --processes <process number>
```

<br/><br/>
**Render page 1/105 (10 000 records total, 48 records per page)**


<br/>
Django + uWSGI (1 process) - time per request (mean)

| | n=100 | n=1000 | n=2000 | n=5000 | n=10000 |
| --- | --- | --- | --- | --- | --- |
| **c=1** | 25 ms | 25 ms | 24 ms | 23 ms | 24 ms |
| **c=50** | 24 ms | 23 ms | 23 ms | 25 ms | 23 ms |
| **c=100** | 23 ms | 24 ms | 24 ms | 23 ms | 23 ms |
| **c=200** | - | 35 ms | 43 ms | 41 ms | 56 ms |
| **c=300** | - | 91 ms | 34 ms | 47 ms | 40 ms |
| **c=500** | - | 56 ms | 31 ms | 38 ms | 32 ms |

<br/>
Django + uWSGI (1 process) - failed requests

| | n=100 | n=1000 | n=2000 | n=5000 | n=10000 |
| --- | --- | --- | --- | --- | --- |
| **c=1** | 0 | 0 | 0 | 0 | 0 |
| **c=50** | 0 | 0 | 0 | 0 | 0 |
| **c=100** | 0 | 0 | 0 | 0 | 0 |
| **c=200** | - | 2 | 120 | 260 | 775 |
| **c=300** | - | 94 | 197 | 662 | 1209 |
| **c=500** | - | 65 | 312 | 869 | 2015 |

<br/><br/>
**Render page 104/105 (10 000 records total, 48 records per page)**

<br/>
Django + uWSGI (1 process) - time per request (mean)

| | n=100 | n=1000 | n=2000 | n=5000 | n=10000 |
| --- | --- | --- | --- | --- | --- |
| **c=1** | 58 ms | 57 ms | 57 ms | 57 ms | 56 ms |
| **c=50** | 58 ms | 57 ms | 57 ms | 57 ms | 57 ms |
| **c=100** | 58 ms | 57 ms | 57 ms | 57 ms | 57 ms |
| **c=200** | - | 130 ms | 94 ms | 117 ms | 131 ms |
| **c=300** | - | 83 ms | 67 ms | 95 ms | 80 ms |
| **c=500** | - | 68 ms | 76 ms | 62 ms | 55 ms |

<br/>
Django + uWSGI (1 process) - failed requests

| | n=100 | n=1000 | n=2000 | n=5000 | n=10000 |
| --- | --- | --- | --- | --- | --- |
| **c=1** | 0 | 0 | 0 | 0 | 0 |
| **c=50** | 0 | 0 | 0 | 0 | 0 |
| **c=100** | 0 | 0 | 0 | 0 | 0 |
| **c=200** | - | 108 | 255 | 728 | 1745 |
| **c=300** | - | 172 | 348 | 1372 | 2362 |
| **c=500** | - | 304 | 672 | 1788 | 3284 |
