from fliptoken import fliptoken
from flipparser import flipparser

print("flipbook compiler\n")

while(True):
    try:

        input_ = input(">> ")

        # tokenize
        tokens = fliptoken(input_)
        # parser
        output = flipparser(tokens)

        if output:
            print(output)
    except KeyboardInterrupt:
        exit()
        

        