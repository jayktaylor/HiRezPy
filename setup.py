"""
MIT License

Copyright (c) 2017 Jayden Bailey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from setuptools import setup, find_packages
import re

version = ''
rme = ''
req = []

with open('hirezpy/__init__.py') as f:
    # thanks Danny for this 10/10 regex
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("Invalid version")

with open('requirements.txt') as f:
    req = f.read().splitlines()

with open('README.md') as f:
    rme = f.read()

setup(name='HiRezPy',
    author='jaydenkieran',
    author_email='jaydenkieran@gmail.com',
    url='https://github.com/jaydenkieran/HiRezPy',
    download_url='https://github.com/jaydenkieran/HiRezPy/tarball/0.1.1',
    version=version,
    packages=find_packages(),
    license='MIT',
    description='Library for accessing Hi-Rez Studios APIs',
    long_description=rme,
    install_requires=req,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers'
    ],
    keywords='hirez smite paladins api wrapper library'
)
