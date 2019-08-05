# Activejson

[![PyPI version](https://badge.fury.io/py/activejson.svg)](https://badge.fury.io/py/activejson)
[![CircleCI](https://circleci.com/gh/dany2691/activejson.svg?style=svg)](https://circleci.com/gh/dany2691/activejson)

> A convenient library to deal with large json data

A convenient library to deal with large json data. The purpose of this package is help to deal with complex json-like data, converting them into a more manageable data structure.

## Installation

OS X & Linux:

From PYPI

```sh
$ pip3 install activejson
```

from the source

```sh
$ git clone https://github.com/dany2691/activejson.git
$ cd activejson
$ python3 setup.py install
```

## Usage example

You can flat a complex dict the next way:

```python
complex_json = {'cat': {'grass': 'feline', 'mud': 'you never know',
                        'horse': 'my joke'},
                'dolphin': [{'tiger': [{'bird': 'blue jay'},
                                      {'fish': 'dolphin'}]},
                            {'cat2': 'feline'}, {'dog2': 'canine'}],
                'dog': 'canine'}
```

```python
from activejson import flatten_json

flatten_complex_json = flatten_json(complex_json)

print(flatten_complex_json)
```

The result could be the next:

```sh
{'cat_grass': 'feline',
 'cat_horse': 'my joke',
 'cat_mud': 'you never know',
 'dog': 'canine',
 'dolphin_0_tiger_0_bird': 'blue jay',
 'dolphin_0_tiger_1_fish': 'dolphin',
 'dolphin_1_cat2': 'feline',
 'dolphin_2_dog2': 'canine'}
```

On the other hand, is possible to convert that dict into an object with dynamic attributes:

```python
from activejson import FrozenJSON

frozen_complex_json = FrozenJSON(complex_json)

print(frozen_complex_json.cat.grass)
print(frozen_complex_json.cat.mud)
print(frozen_b.dolphin[2].dog2)
```

The result could be the next:

```sh
'feline'
'you never know'
'canine'
```

# Development setup

This project uses _pipenv_ for dependecy resolution. It's a kind of mix between
pip and virtualenv. Follow the next instructions to setup the development enviroment.

```sh
$ git clone https://github.com/dany2691/activejson.git
$ cd activejson
$ pipenv shell
$ pipenv install -e .
```

To run the test-suite, inside the pybundler directory:

```shell
$ pytest test/ -vv
```

## Meta

Daniel Omar Vergara Pérez – [@dan1_net](https://twitter.com/dan1_net) – daniel.omar.vergara@gmail.com

[https://github.com/dany2691](https://github.com/dany2691)

## Contributing

1. Fork it (<https://github.com/dany2691/activejson>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
