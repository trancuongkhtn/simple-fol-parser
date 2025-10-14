# simple-fol-parser

I made a super simple functional parser in Python. It can parse strings like this `foo(x,blah(y,z))` and turn it to `["foo","x",["blah","y","z"]]`. I named it `simple-fol-parser` because It'll be used to parse [FOL](https://en.wikipedia.org/wiki/First-order_logic) terms. The grammar will be context-free and very simlar to [TPTP](https://www.tptp.org/) style.

## How to use?
Download the package, copy `parser.py` file to your directory then `import parser`. Here's the code:

```
import parser
s = "eq( add(x, 2), mul( 5, add(x,y) ) )"
x = parser.parse( s )
print( x )
# ['eq', ['add', 'x', '2'], ['mul', '5', ['add', 'x', 'y']]]
```

## Limitations
A bunch. This is just version 1.0.0
- You must install [Lark](https://pypi.org/project/lark/) yourself, but It's easy `pip install lark`
- It works only for letters and numbers. That means `add(1,2)` is ok. But `+(1,2)` is not. I haven't tested much.
- We don't have binary operator syntax yet. It means `x + y` or `1 = 2` is not available for parsing yet. Use `add(x,y)` or `add(1,2)` instead.
- Of course, quantifier syntax is not ready yet: `![X,Y]( X = Y | ~ X != Y )`

## Todos
- test test test
- enforce it to FOL level (qunatifier, connectives, some basic binary operators)
- package it and publish to [pypi.org](https://pypi.org/)