class Lexer:
    stopWords = [" "]

    def __init__(self, code:str):
        self.__code = code
        self.__i = 0
        self.__tokens = []
        self.__chr = self.__code[self.__i]
        self.__token = None
        self.__clean()

    
    def tokenizer(self):
        while self.__i < len(self.__code):
            print(self.__i)
            self.__moveI()
    
    def __moveI(self):
        self.__i += 1
        if self.__i < len(self.__code):
            self.__chr = self.__code[self.__i]

    def __clean(self):
        for stopWord in Lexer.stopWords:
            self.__code = self.__code.replace(stopWord,"")


    def getCode(self)->str:
        return self.__code
    

lex = Lexer("5      +     5")
print(lex.getCode())
print("------------------")
lex.tokenizer()


