# lsmat

A command-line tool to list contents of Matlab \*.mat files

## Getting Started

Just install the package:

```
python setup.py build
sudo python setup.py install
```

And then run

```
lsmat somematfile.mat
```

in the Terminal.  It works on Unix systems.

By default it will print out all the arrays, which may become inconvenient with large arrays, so one can use the compact argument:


```
lsmat -c somematfile.mat
```
