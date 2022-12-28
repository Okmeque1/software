#diskette
def n_factorial():
    input("Enter number : ")
    if n != 1:
        n = n -1
        n_factorial()
    elif n == 1:
        print("Complete.")
        return
n_factorial()
