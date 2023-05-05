<!--
    =====================================
    generator=datazen
    version=3.1.2
    hash=035acc9a20df17a172151cf57e984c39
    =====================================
-->

# userfs ([0.2.0](https://pypi.org/project/userfs/))

[![python](https://img.shields.io/pypi/pyversions/userfs.svg)](https://pypi.org/project/userfs/)
![Build Status](https://github.com/vkottler/userfs/workflows/Python%20Package/badge.svg)
[![codecov](https://codecov.io/gh/vkottler/userfs/branch/master/graphs/badge.svg?branch=master)](https://codecov.io/github/vkottler/userfs)
![PyPI - Status](https://img.shields.io/pypi/status/userfs)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/userfs)

*A system-bootstrapping automation and introspection tool.*

See also: [generated documentation](https://vkottler.github.io/python/pydoc/userfs.html)
(created with [`pydoc`](https://docs.python.org/3/library/pydoc.html)).

## Python Version Support

This package is tested with the following Python minor versions:

* [`python3.7`](https://docs.python.org/3.7/)
* [`python3.8`](https://docs.python.org/3.8/)
* [`python3.9`](https://docs.python.org/3.9/)
* [`python3.10`](https://docs.python.org/3.10/)
* [`python3.11`](https://docs.python.org/3.11/)

## Platform Support

This package is tested on the following platforms:

* `ubuntu-latest`
* `macos-latest`
* `windows-latest`

# Introduction

# Command-line Options

```
$ ./venv3.11/bin/ufs -h

usage: ufs [-h] [--version] [-v] [-C DIR] {build,fetch,noop} ...

A system-bootstrapping automation and introspection tool.

options:
  -h, --help          show this help message and exit
  --version           show program's version number and exit
  -v, --verbose       set to increase logging verbosity
  -C DIR, --dir DIR   execute from a specific directory

commands:
  {build,fetch,noop}  set of available commands
    build             attempt to build a software project from its sources
    fetch             attempt to obtain some software from the internet
    noop              command stub (does nothing)

```

# Internal Dependency Graph

A coarse view of the internal structure and scale of
`userfs`'s source.
Generated using [pydeps](https://github.com/thebjorn/pydeps) (via
`mk python-deps`).

![userfs's Dependency Graph](im/pydeps.svg)
