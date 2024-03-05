class Token:
    def __init__(self,  tokenType, tokenValue):
        self.__tokenType = tokenType
        self.__tokenValue = tokenValue
    
    def __repr__(self) -> str:
        return type(self).__name__   #alternativa self.__tokenValue
   
    def getTokenType(self):
        return self.__tokenType
    
    def getTokenValue(self):
        return self.__tokenValue

class Integer(Token):
    def __init__(self, tokenValue):
        super().__init__("INTEGER", tokenValue)

class Float(Token):
    def __init__(self, tokenValue):
        super().__init__("FLOAT", tokenValue)

class Operation(Token):
    def __init__(self, tokenValue):
        super().__init__("OPERATION", tokenValue)

class Declaration(Token):
    def __init__(self, tokenValue):
        super().__init__("DECLARATION", tokenValue)

class Boolean(Token):
    def __init__(self, tokenValue):
        super().__init__("BOOLEAN", tokenValue)

class Reserved(Token):
    def __init__(self, tokenValue):
        super().__init__("RESERVED", tokenValue)

class Variable(Token):
    def __init__(self, tokenValue):
        super().__init__("VARIABLE", tokenValue)

class Comparison(Token):
    def __init__(self, tokenValue):
        super().__init__("COMPARISON", tokenValue)

class Commend(Token):
    def __init__(self, tokenValue):
        super().__init__("COMMEND", tokenValue)