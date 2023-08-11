import os
def icmd():
    while True:
        prompt = input(">")
        if prompt == 'exit' or prompt == 'return':
                return False
        os.system(prompt)
icmd()