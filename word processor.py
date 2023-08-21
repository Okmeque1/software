def list_arr(a):
    c = {}
    print('This will LITERALLY process the words by Okmeque1')
    g = input("Enter word to choose,leave blank for full function : ")
    if g == "":
        for b in a:
            if b not in c:
                c[b] = 1
            elif b in c:
                c[b] = c[b] + 1
            

    for b in a:
        if g == b:
            if b in c:
                c[b] = c[b] + 1
            elif b not in c:
                c[b] = 1


    return c
def show_result(d):
    for e in d:
        print(e + ":" + str(d[e]))
def individual_words():
    with open(input("FIle name : "),"r") as f:
        return(f.read().split(" "))

show_result(list_arr(individual_words()))
