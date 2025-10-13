# simple-fol-parser

I made a super simple functional parser in Python. It can parse strings like this `foo(x,blah(y,z))` and turn it to `["foo","x",["blah","y","z"]]`. I named it `simple-fol-parser` because It'll be used to parse [FOL](https://en.wikipedia.org/wiki/First-order_logic) terms. The grammar will be context-free and very simlar to [TPTP](https://www.tptp.org/) style.