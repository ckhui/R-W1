# Python Module

## import

import fibo
f = fibo.fib
from fibo import fib, fib2
from fibo import *
from fibo import fib as fibonacci

## run as script

>> python fibo.py <arguments>

## check for name

``` python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

if the module is imported the code is not run

## Search Path

if a module span is imported
search order

- built-in module
- file named spam.py in a list of dir from sys.path
    - dir of the input script 
    - PYTHONPATH
    - installation-dependent default

### Add dir to path
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')

### dir()
>> dir(module)
to find out which names a module defines
>> dir() #without arguements
lists the names that defined currently, but not including buildin functions
>> import builtins
>> dir(builtins)
to list all the buildin functions and variables

## __init__.py
this files are required to make Python treat dir containing the file as packages
- can be empty file
- can set the __all__ variable

### import individual modules
> import sound.effects.echo
> sound.effects.echo.echofilter(input...)
or 
> from sound.effects import echo
> echo.echofilter(input...)
or
> from sound.effects.echo import echofilter
> echofilter(input...)

### __all__ variable
> __all__ = ["item", ... ]
function to be import when 
> from module import *