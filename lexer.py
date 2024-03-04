class Lexer:
    __stopWords = [" "]
    __numbers =  "0123456789"

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
                self.__tokens.append(self.__token)
            self.__moveI()
    
    def __extractNumber(self):
        number = ""
        while (self.__chr in Lexer.__numbers) and (self.__i < len(self.__code)):
            number += self.__chr
            self.__moveI()
        return Integer(number, 'INTEGER')

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
    
    def getTokenType(self):
        return self.__tokenType
    
    def getTokenValue(self):
        return self.__tokenValue

class Integer(Token):
    pass

class String(Token):
    pass
     
    

lex = Lexer("5      +     5")
print(lex.getCode())
print("------------------")
lex.tokenizer()
print("------------------")
print(lex.getTokens())


