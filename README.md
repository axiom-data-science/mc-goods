mc-goods
==============================
[![License:MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python Package Index](https://img.shields.io/pypi/v/mc-goods.svg?style=for-the-badge)](https://pypi.org/project/mc-goods)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/mc-goods.svg?style=for-the-badge)](https://anaconda.org/conda-forge/mc-goods)

model_catalogs catalogs for GOODS

--------

<p><small>Project based on the <a target="_blank" href="https://github.com/jbusecke/cookiecutter-science-project">cookiecutter science project template</a>.</small></p>

# How to Use

Install [`model_catalogs`](https://github.com/NOAA-ORR-ERD/model_catalogs) and this package of catalogs will be installed too.

# Installation

If you need to install these yourself, you can with PyPI:

```
pip install mc-goods
```

or with conda-forge:

```
conda install -c conda-forge mc-goods
```

# To add a catalog

1. Place the new catalog file in the package directory (`mc_goods`).
2. Add catalog name to `__init__` following other catalog files.
3. Add catalog to `setup.py` following others.
4. Git commit and push to repo.
5. Reinstall package since entry_points have changed.
