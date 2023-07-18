def check():
    risk = 0
    print("The Okmeque1 Password System Checker.")
    print("Program version 1.0.0")
    print("SPONSOR : This is perfect with Okmeque1's PWD.PY generator suite.")
    print("This program does NOT connect to the internet or external storage outside of this function.Please rest assured that this program does not steal information.")
    chkpwd = input("Please enter your password here → ")
    flag = True
    while flag == True:
        spc_cnt = 0
        num_cnt = 0
        lwc_cs = 0
        up_cs = 0
        for x in chkpwd:
            if x.isalnum() == False:
                spc_cnt += 1
            if x.isnumeric() == True:
                num_cnt += 1
            if x.isalpha():
                if x.isupper() == True:
                    up_cs += 1
                if x.islower() == True:
                    lwc_cs += 1
        if spc_cnt <= 1:
            print("You must add more special characters in your password.")
            risk += 1
        if num_cnt <= 1:
            print("You must add more numbers in your password.")
            risk += 1
        if lwc_cs <= 1:
            print("You must add more lowercase letters in your password.")
            risk += 1
        if up_cs <= 1:
            print("You must add more UPPERCASE letters in your password.")
            risk += 1
        if len(chkpwd) <= 10:
            print("Your password LENGTH must be longer in your password.")
            risk += 1
        if len(chkpwd) - lwc_cs == 1:
            print("There are TOO MANY lowercase letters in your password.")
            risk += 1
        if len(chkpwd) - up_cs == 1:
            print("There are TOO MANY UPPERCASE letters in your password.")
            risk += 1            
        print("Special Character count : " + str(spc_cnt))
        print("Number count : " + str(num_cnt))
        print("Lowercase letters : " + str(lwc_cs))
        print("Uppercase letters : " + str(up_cs))
        print("The risk of your account getting hacked is " + str(risk) + "/7")
        flag = False
        return False
check()      