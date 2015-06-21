efacter
=============

This package provides:

0. Facter module to work with structured [facter's](https://puppetlabs.com/facter) facts
0. efacter command line utility, which user the Facter module. efacter allows you to query specific chunks of hashes in complex facts and show them with colour highlighting (or without) in form of either JSON or human readable format (it's just modified and intended JSON, to be honest)

Facter()
-----------

`facter = Facter(['processors.count', 'os.name', 'os.release.full', 'architecture'])`

You can change delimiter used to separate chunks in *self.separator*.
A path to facter and options can be changed in *self.facterCommand*

Defaults are:

```
self.separator = '.'
self.facterCommand = ['facter', '--json', '--external-dir', '/etc/facter/facts.d/']
```

efacter
-----------

```
Usage: efacter.py [options] <fact.element1.element2> [anotherFact.element1] [andAnother] ...

Options:
  -h, --help            show this help message and exit
  -j, --json            Output JSON
  -o, --json-one-string
                        Output JSON as one string (without indent)
  -d DELIMITER, --delimiter=DELIMITER
                        Delimiter for elements (default is '.'))
  -n, --no-colour       Disable colours in the output
```

TODO
-----------
* a path to facter is hard-coded to the Facter() class (even though it can be changed after class has been called). But it would be nice to make it automatically discoverable, depending of OS
