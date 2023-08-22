import os
def icmd():
    print("iCMD-Lite - iCMD with limited features : core functionality.\nCopyright (c) Okmeque1 Corporation 2023-2025")
    while True:
        prompt = input("iCMD-Lite>")
        if prompt == 'exit' or prompt == 'return':
                return False
        elif 'cd' in prompt[0:3]:
                os.chdir(prompt[3:])
        os.system(prompt)
icmd()
