def counting(k):
    print(k)
    k = k + 1
    inp = input("Next number")
    if int(inp) == k:
        counting(k)
    else:
        print("YOU RUINED IT AT " + str(k))
        print('\a')
        return
counting(0)
         


    