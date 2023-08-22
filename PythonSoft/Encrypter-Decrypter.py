from cryptography.fernet import Fernet
def enc(key):
    file_enc = input("Please enter a valid file name to encrypt → ")
    with open(file_enc,"rb") as lwe:
        towr = lwe.read()
    key1 = Fernet(key)
    encrypted = key1.encrypt(towr)
    with open(file_enc,"wb") as twrite:
        twrite.write(encrypted)
    print("Encrypted with no errors")
    start()
def dec(key):
    file_dec = input("Please enter a valid file name to decrypt → ")
    with open(file_dec,"rb") as lwd:
        tore = lwd.read()
    key2 = Fernet(key)
    decrypted = key2.decrypt(tore)
    with open(file_dec,"wb") as td:
        td.write(decrypted)
    print("Decrypted with no errors.")
    start()
def start():
    key = input("Please enter a valid file name with a valid key. : ")
    print("Encrypter-Decripter system by Okmeque1")
    print("1 → Encrypt file.")
    print("2 → Decrypt file.")
    a = input("Please choose : ")
    if a == "1":
        enc(key)
    elif a == "2":
        dec(key)
    else:
        return
start()
