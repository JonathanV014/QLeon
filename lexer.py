class Lexer:
    stopWords = [" "]

    def __init__(self, code:str):
        self.__code = code
        self.__i = 0
        self.__tokens = []
        self.__chr = self.__code[self.__i]
        self.__token = None
        self.__clean()

    def __clean(self):
        for stopWord in Lexer.stopWords:
            self.__code = self.__code.replace(stopWord,"")


    def getCode(self)->str:
        return self.__code
    

lex = Lexer("5      +     5")
print(lex.getCode())


