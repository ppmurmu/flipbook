import re

#to generate tokens
def fliptoken(string: str):
    token_rexes = [
        (re.compile(r"[^\s]+(\.(?i)(jpg|png|bmp|jpeg))"), "image"),
        (re.compile(r"^[0-9]+"), "num"), # integers
        (re.compile(r"[^\s]+(\.(?i)(flip))"), "flipdoc"),
        (re.compile(r"[^\s]+(\.(?i)(gif))"), "gifout"),
        (re.compile(r"[^\s]+(\.(?i)(pdf))"), "pdfout"),
        (re.compile(r"-a"), "apple"),  #applpenewton interpreter
        (re.compile(r"-o"), "convert"), #flipbook interpreter
        (re.compile(r"fc"), "func"), #function
    ]

    tokens = []

    while len(string):
        string = string.lstrip()

        matched = False

        for token_rex, token_type in token_rexes:
            mo = token_rex.match(string)
            if mo:
                matched = True
                token = (mo.group(0), token_type)
                tokens.append(token)
                string  = token_rex.sub('', string)
                string = string.lstrip()
                break 
        
        if not matched:
            raise Exception("Invalid String")
    
    return tokens