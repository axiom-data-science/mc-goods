mc-goods
==============================
[![Build Status](https://github.com/axiom-data-science/mc-goods/workflows/Tests/badge.svg)](https://github.com/axiom-data-science/mc-goods/actions)
[![codecov](https://codecov.io/gh/axiom-data-science/mc-goods/branch/main/graph/badge.svg)](https://codecov.io/gh/axiom-data-science/mc-goods)
[![License:MIT](https://img.shields.io/badge/License-MIT-lightgray.svg?style=flt-square)](https://opensource.org/licenses/MIT)[![pypi](https://img.shields.io/pypi/v/mc-goods.svg)](https://pypi.org/project/mc-goods)
<!-- [![conda-forge](https://img.shields.io/conda/dn/conda-forge/mc-goods?label=conda-forge)](https://anaconda.org/conda-forge/mc-goods) -->[![Documentation Status](https://readthedocs.org/projects/mc-goods/badge/?version=latest)](https://mc-goods.readthedocs.io/en/latest/?badge=latest)


model_catalogs catalogs for GOODS

--------

<p><small>Project based on the <a target="_blank" href="https://github.com/jbusecke/cookiecutter-science-project">cookiecutter science project template</a>.</small></p>


# To add a catalog

1. Place the new catalog file in the package directory (`mc_goods`).
2. Add catalog name to `__init__` following other catalog files.
3. Add catalog to `setup.py` following others.
4. Git commit and push to repo.
5. Reinstall package since entry_points have changed.
