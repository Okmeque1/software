def list_arr(array):
    returndict = {}
    print('This will tell you the position of the word and if it is in the file. ')
    word = input("Enter word to choose, leave blank for full function : ")
    if word == "":
        for b in array:
            if b not in returndict:
                returndict[b] = 1
            elif b in returndict:
                returndict[b] = returndict[b] + 1
            

    for b in array:
        if word == b:
            if b in returndict:
                returndict[b] = returndict[b] + 1
            elif b not in returndict:
                returndict[b] = 1
    return returndict
def show_result(file):
    for word in file:
        print(word + ":" + str(file[word]))
def individual_words():
    with open(input("Please enter a valid file name (the full path to the file must be specified if the file in question is not in the same directory as this file): ","r") as f:
        text = f.read()
        for char in [",", ";", ":", ".", "!", "?"]:
            text = text.replace(char, " ")
        return text.split()
def start():
    try:
        show_result(list_arr(individual_words()))
    except FileNotFoundError as e:
        print(f"Error 6510B\n The file that you specified is not a valid file.\nDetails: {e}")
        input("Press ENTER to restart the program, or press CTRL + C to END the program...")
        start()
    except (KeyboardInterrupt, SystemExit, EOFError):
        print("User has chosen to exit. Exiting...")
        exit()
    except Exception as e:
        print(f"Unknown error: {e}\nReview the error chart for more information as well as the Python Manual.")
        input("Press ENTER to restart the program, or press CTRL + C to END the program...")
        start()
start()
