# apparel-cli-scaffold


<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [About](#about)
- [Installation Quickstart](#installation-quickstart)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## About

`apparel-cli-scaffold` is a command line entry point for Apparel's machine learning services. 
It provides a way to plugin command line tools for Apparel services.

## Installation Quickstart

You can install from pip

```bash
pip install apparel-cli-scaffold
```

After that the `mli` command will be available:

```bash
mli --help

Usage: mli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.
```

The package doesn't provide any commands itself. They are added as plugins.
