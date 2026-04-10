from enum import Enum, auto

class TokenType(Enum):
    NUMBER = auto()
    IDENTIFIER = auto()

    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()

    EQUAL = auto()

    LEFT_PAREN = auto()
    RIGHT_PAREN = auto() 
    VAR = auto()
    PRINT = auto()


    EOF = auto()
keywords = {
    "var": TokenType.VAR,
    "print": TokenType.PRINT,
}
class Token:
    def __init__(self, type, lexeme, literal):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal

    def __repr__(self):
        return f"{self.type.name} {self.lexeme} {self.literal}"
    
    # definindo gramatica basica do compiler
