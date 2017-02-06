# HiRezPy

[![PyPI](https://img.shields.io/pypi/v/hirezpy.svg)](https://pypi.python.org/pypi/hirezpy/)
[![Versions](https://img.shields.io/pypi/pyversions/hirezpy.svg)](https://pypi.python.org/pypi/hirezpy/)

**HiRezPy** is an asynchronous library developed in Python 3 for accessing information from [Hi-Rez Games](http://www.hirezstudios.com/)' APIs, for both *[Smite](https://www.smitegame.com/)* and *[Paladins](https://www.paladins.com/)*. It is a continuation and rework of my previous project, [`smite-python`](https://github.com/jaydenkieran/smite-python).

## Requirements
* [Python](http://python.org) 3.5 (or higher)
    * The following libraries are required: `aiohttp`
- [Access](https://fs12.formsite.com/HiRez/form48/secure_index.html) to Hi-Rez Studios' API

## Installation
The easiest way to install **HiRezPy** is using `pip`, Python's package manager:

```
pip install -U hirezpy
```

The required dependencies will be installed automatically. After that, you can use the library using `import hirezpy`.

## Example

```py
from hirezpy import Client

client = Client("YOUR_DEV_ID", "YOUR_AUTH_KEY")
r = client.loop.run_until_complete(client.get_friends('Dussed'))

if r is not None:
    for u in r:
        print(u.username)
```

This example will print the username of everyone that is friends with the player **Dussed**. As we didn't specify an endpoint to use, and didn't override the default when initialising our Client object, it defaults to the Smite PC endpoint.
