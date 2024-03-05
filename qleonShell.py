from lexer import *


class Shell:
    __HELPCOMMAND = "help()"
    __EXITCOMMAND = "exit()" 
    __VERSION = "1.0"
    __DATECREATION = "Feb 4 2024, 1:41:20"
    __HELPMESSAGE = f'Welcome to QLeon {__VERSION} help utility!.\n\nWe are still working on finalizing the language.\n\nTo exit this help utility and return to the Lexer,\nenter "ex" or "exit".\n'
    __INTERPRETEROUTPUT = "---> "
    __HELPOUTPUT = "help()---> "
    __EXITCOMMANDSHELP = ["ex", "exit"]

    def __init__(self):
        pass

    def qLeonShell(self):
        print(f"\nQLeon {Shell.__VERSION} (v{Shell.__VERSION}, {Shell.__DATECREATION}) on win32")
        print(f'Write "{Shell.__HELPCOMMAND}" for more information')
        while True:
            code = input(f"{Shell.__INTERPRETEROUTPUT}")
            if code == Shell.__HELPCOMMAND:
                print(Shell.__HELPMESSAGE)
                while True:
                    code = input(f"{Shell.__HELPOUTPUT}")
                    if code.lower() not in Shell.__EXITCOMMANDSHELP:
                        self.__messageUnk(code)
                        continue
                    else:
                        print("\nYou are leaving the help and returning to the QLeon lexer.")
                        break
            elif code == Shell.__EXITCOMMAND:
                break  
            else:
                lex = Lexer(code)
                tokens = lex.tokenizer()
                if len(tokens) == 0:
                    self.__messageError(code)
                else:
                    print(f"{tokens}")

    def __messageError(self, code) -> str:
        error = f"Traceback (most recent call last):\nNameError: name '{code}' is not defined"
        print(error)
    def __messageUnk(self, code) -> str:
        message = f"No QLeon documentation found for '{code}'\n"
        print(message)

myQLeon = Shell()
myQLeon.qLeonShell()