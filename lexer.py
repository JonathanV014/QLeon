class Lexer:
    __stopWords = [" "]
    __numbers =  "0123456789"
    __operations = "+-/*"

    def __init__(self, code:str):
        self.__code = code
        self.__i = 0
        self.__tokens = []
        self.__chr = self.__code[self.__i]
        self.__token = None
        self.__clean()

    
    def tokenizer(self):
        while self.__i < len(self.__code):

            if self.__chr in Lexer.__numbers: 
                self.__token = self.__extractNumber()
                
            elif self.__chr in Lexer.__operations: 
                self.__token = Operation(self.__chr)
                self.__moveI()

            self.__tokens.append(self.__token)
        return self.__tokens

    def __extractNumber(self):
        number = ""
        isFloat = False
        while (self.__chr in Lexer.__numbers or self.__chr == ".") and (self.__i < len(self.__code)):
            if self.__chr == ".":
                isFloat = True
            number += self.__chr
            self.__moveI()
        if isFloat:
            return Float(number)
        else:
            return Integer(number)
        
    def __moveI(self):
        self.__i += 1
        if self.__i < len(self.__code):
            self.__chr = self.__code[self.__i]

    def __clean(self):
        for stopWord in Lexer.__stopWords:
            self.__code = self.__code.replace(stopWord,"")


    def getCode(self)->str:
        return self.__code
    
    def getNumbers(self):
        return Lexer.__numbers
    
    def getStopWords(self):
        return Lexer.__stopWords
    
    def getTokens(self):
        return self.__tokens
    
class Token:
    def __init__(self,  tokenType, tokenValue):
        self.__tokenType = tokenType
        self.__tokenValue = tokenValue
    
    def __repr__(self):
        return self.__tokenValue
    
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
    

lex = Lexer("5+5")
print(lex.getCode())
print("------------------")
lex.tokenizer()
print("------------------")
print(lex.getTokens())


