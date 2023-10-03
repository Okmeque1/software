#diskette
def n_factorial():
    input("Enter number : ")
    print("Creator = Okmeque1")
    if n != 1:
        n = n -1
        n_factorial()
    elif n == 1:
        print("Complete.")
        return
n_factorial()
