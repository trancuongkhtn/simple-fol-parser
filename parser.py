from lark import Lark, Transformer

grammar = r"""

    start: call

    call: NAME "(" [args] ")"
    args: expr ("," expr)*

    ?expr: call
        | NAME
        | NUMBER

    %import common.CNAME -> NAME
    %import common.NUMBER
    %import common.WS
    %ignore WS

"""

class MyTransformer( Transformer ) :

    def NUMBER(self, n ) :
        return str( n )
    
    def NAME(self, n ) :
        return str( n )
    
    def args(self,items) :
        return items
    
    def call( self, items ) :
        return [items[0]] + items[1]
    
    def expr( self, items ) :
        return items[0]
    
    def start( self, items ) :
        return items[0]

parser = Lark( grammar, start='start' )
the_transformer = MyTransformer()

def parse( s : str ) -> list | str :    
    tree = parser.parse( s )
    return the_transformer.transform( tree )

# --- test
# s = "eq( add(x, 2), mul( 5, add(x,y) ) )"
# print( parse( s ) )