from tokensClasses import *
class Lexer:
    #Tabla de Simbolos / Para mejorar 
    __stopWords = [" "]
    __numbers =  "0123456789"
    __operations = "+-/*()="

    __letters = "abcñdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZÑ"
    __declarations = ["crt"] #Crear Variable crt = create
    __reserved = ["if", "elif","else", "while", "do"]

    __specialCharacters = [">", "<", "=", "?", "&", "|", "!", "#"]   
    __booleans = ["&&", "||", "!"]
    __comparisons = [">", "<", ">=", "<=", "=?"]
    __commend = ["###"] 


    def __init__(self, code:str):
        self.__code = code
        self.__i = 0
        self.__tokens = []
        self.__chr = self.__code[self.__i]
        self.__token = None
      
    
    def tokenizer(self):
        while self.__i < len(self.__code):

            if self.__chr in Lexer.__numbers: 
                self.__token = self.__extractNumber()

            elif self.__chr in Lexer.__stopWords:
                self.__moveI()
                continue    
                
            elif self.__chr in Lexer.__operations: 
                self.__token = Operation(self.__chr)
                self.__moveI()
    
            elif self.__chr in Lexer.__letters:
                word = self.__extractWord()
                
                if word in Lexer.__declarations:     
                    self.__token = Declaration(word)

                elif word in Lexer.__reserved:
                    self.__token = Reserved(word)
                else: 
                    self.__token = Variable(word)


            elif self.__chr in Lexer.__specialCharacters:
                specialChar = self.__extractEspecialChar()

                if specialChar in Lexer.__comparisons:
                    self.__token = Comparison(specialChar)
                    
                elif specialChar in Lexer.__booleans:
                    self.__token = Boolean(specialChar)

                elif specialChar in Lexer.__commend:
                    self.__token = Commend(specialChar)
                    self.__tokens.append(self.__token)
                    self.__i = len(self.__code)
                    continue
                
            

            self.__tokens.append(self.__token)
        return self.__tokens

    def __extractWord(self):
        word = ""
        while (self.__chr in Lexer.__letters) and (self.__i < len(self.__code)):
            word += self.__chr
            self.__moveI()
        return word                                      

    def __extractEspecialChar(self):
        especialChar = ""
        while (self.__chr in Lexer.__specialCharacters) and (self.__i < len(self.__code)):
            especialChar += self.__chr 
            self.__moveI()
        return especialChar 

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
    
    def getOperations(self):
        return Lexer.__operations

    def getLetters(self):
        return Lexer.__letters
    
    def getDeclarations(self):
        return Lexer.__declarations
    
    def getReserved(self):
        return Lexer.__reserved
    
    def getSpecialCharacters(self):
        return Lexer.__specialCharacters
    
    def getBooleans(self):
        return Lexer.__booleans
    
    def getComparisons(self):
        return Lexer.__comparisons
    
    def getCommend(self):
        return Lexer
    
    def getTokens(self):
        return self.__tokens

    

#lex = Lexer("5+5")
#print(lex.getCode())
#print("------------------")
#lex.tokenizer()
#print("------------------")
#print(lex.getTokens())


