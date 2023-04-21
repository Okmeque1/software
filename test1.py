def longest_consec(strarr, k):
    b = ""
    n = len(strarr)
    if k <= 0 or n == 0 or k > n:
        return ""
    else:
        for a in strarr:
            for c in a:
                b = b + a
                print(b)
longest_consec(["diskette","hello","floppy","the"],2)
