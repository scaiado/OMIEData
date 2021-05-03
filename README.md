# OMIEData: 

Python package to import data from OMIE (Iberian Peninsula's Electricity Market Operator): https://www.omie.es/

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI version fury.io](https://img.shields.io/pypi/v/OMIEData.svg)](https://pypi.org/project/OMIEData/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/OMIEData.svg)](https://pypi.python.org/pypi/OMIEData/)



## Installation 

The package is uploaded at https://pypi.org/project/OMIEData/, so the usual

```python
python -m pip install OMIEData

```
from the command line should work. 

Aternatively, to install it from GitHub, type:

```python
python -m pip install git+https://github.com/acruzgarcia/OMIEData

```

or use the .whl (or .tar.gz) file within dist folder:

```python
python -m pip install OMIEData-VERSION-py3-none-any.whl

```
or

```python
python -m pip install OMIEData-VERSION.tar.gz

```

## Examples:

A very simple example to download electricity prices and demands:

```python
dateIni = dt.datetime(2012, 3, 11)
dateEnd = dt.datetime(2012, 4, 15)

# This can take time, it is downloading the files from the website..
df = OMIEMarginalPriceImporter(date_ini=dateIni, date_end=dateEnd).read_to_dataframe(verbose=True)
df.sort_values(by='DATE', axis=0, inplace=True)
print(df)
```

Other examples that illustrate the use of the package:

- [example_energy_by_technology.py](https://github.com/acruzgarcia/OMIEData/blob/dev/example/example_energy_by_technology.py)
- [example_marginal_price.py](https://github.com/acruzgarcia/OMIEData/blob/dev/example/example_marginal_price.py)

Enjoy!.
