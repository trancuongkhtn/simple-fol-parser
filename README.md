# Simple FOL Parser

I made a super simple functional parser in Python. It can parse strings like this `foo(x,blah(y,z))` and turn it to `["foo","x",["blah","y","z"]]`. I named it `simple-fol-parser` because It'll be used to parse [FOL](https://en.wikipedia.org/wiki/First-order_logic) terms. The grammar will be context-free and very simlar to [TPTP](https://www.tptp.org/) style.

## Who might need this?
For those who need a python parser to convert functional or FOL-style strings to structured datatype in next 10 seconds, so that you need to understand nothing about what's the difference between lexer and parser, or It's just fine if you don't know what context-free grammar or EBNF is.

## How to use?
Download the package, copy the directory `simple-fol-parser` to your working directory, then put `import simple-fol-parser as parser`. Here's the code:

```python
import simple-fol-parser as parser
s = "![x,y]( ( add(x, 2) = mul( 5, add(x,y) ) ) => gt(x,y) )"
x = parser.parse( s )
print( x )
# ['!', 'x', ['!', 'y', ['=>', ['=', ['add', 'x', '2'], ['mul', '5', ['add', 'x', 'y']]], ['gt', 'x', 'y']]]]
```

## Limitations
- You must install [Lark](https://pypi.org/project/lark/) yourself, but It's easy `pip install lark`
- Binary syntax is now only available for logical connectives (iff, implies, and, or) and equaility. It means `x + y` or `1 * 2` is not available for parsing yet. Use `add(x,y)` or `mul(1,2)` instead.

## Todos
- test test test
- package it and publish to [pypi.org](https://pypi.org/)