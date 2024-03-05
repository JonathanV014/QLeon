from lexer import *


HELPCOMMAND = "help()"
EXITCOMMAND = "exit()" 
VERSION = "1.0"
DATECREATION = "Feb 4 2024, 1:41:20"
HELPMESSAGE = f'Welcome to QLeon {VERSION} help utility!.\n\nWe are still working on finalizing the language.\n\nTo exit this help utility and return to the Lexer,\nenter "ex" or "exit".\n'
INTERPRETEROUTPUT = "---> "
HELPOUTPUT = "help()---> "
EXITCOMMANDSHELP = ["ex", "exit"]


print(f"\nQLeon {VERSION} (v{VERSION}, {DATECREATION}) on win32")

print(f'Write "{HELPCOMMAND}" for more information')

def messageError(code) -> str:
    error = f"Traceback (most recent call last):\nNameError: name '{code}' is not defined"
    print(error)
def messageUnk(code) -> str:
    message = f"No QLeon documentation found for '{code}'\n"
    print(message)
            


while True:
    code = input(f"{INTERPRETEROUTPUT}")
    if code == HELPCOMMAND:
        print(HELPMESSAGE)
        while True:
            code = input(f"{HELPOUTPUT}")
            if code.lower() not in EXITCOMMANDSHELP:
                messageUnk(code)
                continue
            else:
                print("\nYou are leaving the help and returning to the QLeon lexer.")
                break
    elif code == EXITCOMMAND:
        break  
    else:
        lex = Lexer(code)
        tokens = lex.tokenizer()
        if len(tokens) == 0:
            messageError(code)
        else:
            print(f"{tokens}")