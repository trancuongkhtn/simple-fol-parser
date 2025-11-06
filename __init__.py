"""
![x,y] (
    ( nat(x) & multipleof(x,y) ) =>
    div(x,y) > 0
)
"""
from lark import Lark, Transformer
import re
import copy

grammar = r"""
    term : unary | binary | functional | atom | group | quan
    group : "(" term ")"
    
    functional : NAME "(" args ")"
    args: term ("," term)*

    unary : UNARY_OP term
    binary : term (CONNECTIVE term)+
    CONNECTIVE: "=>" | "&" | "or" | "<=>" | "="
    UNARY_OP : "~"
    
    quan : QUANTIFIER "[" vars "]" term
    vars : NAME ("," NAME)*
    QUANTIFIER : "!" | "?"
    
    atom : NUMBER | NAME

    %import common.CNAME -> NAME
    %import common.NUMBER -> NUMBER
    %import common.WS
    %ignore WS

"""

class MyTransformer( Transformer ) :

    def CONNECTIVE( self, token ) :
        return str( token.value )
    
    def UNARY_OP( self, token ) :
        return str( token.value )

    def NAME( self, token ) :
        return str( token.value )
    
    def QUANTIFIER( self, token) :
        return str( token.value )
    
    def quan( self, items ) :
        quantifier = items[0]
        vars = items[1]
        term = items[2]
        x = copy.deepcopy( term )
        for v in sorted( vars, reverse=True ) :
            x = [ quantifier, v, x ]
        return x
    
    def vars( self, items ) :
        return items
    
    def args( self, items ) :
        return items
    
    def atom(self, items ) :        
        return str( items[0] )
    
    def functional( self, items ) :
        return [ items[0] ] + items[1]
    
    def binary( self, items ) :
        return [ items[1], items[0], items[2] ]
    
    def unary( self, items ) :
        return [ items[0], items[1] ]
    
    def group( self, items ) :
        return items[0]
    
    def term( self, items ) :
        return items[0]

parser = Lark( grammar, start='term' )
the_transformer = MyTransformer()

def remove_comments( s ) :
    s = re.sub(re.compile(r"/\*.*?\*/",re.DOTALL ) ,"" ,s)
    s = re.sub(re.compile(r"//.*?\n" ) ,"" ,s)
    return s

def remove_whitespace( s ) :
    s = re.sub(r'[\s]+', '', s)
    return s

def parse( s : str ) -> list | str :    
    tree = parser.parse( s )
    foo = the_transformer.transform( tree )
    return foo