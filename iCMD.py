def icmd():
    try:
        import os
        iprompt = 'iCMD>'
        ver = 'iCMD Full 1.03A - Okmeque1 Corporation - (c) Okmeque1 Corporation 2023-2025 All Rights Reserved.'
        print(ver)
        try:
            while True:
                prompt = input(iprompt)
                if prompt == 'exit' or prompt == 'return':
                    return False
                elif prompt == 'ver':
                    print(ver)
                elif 'cd' in prompt[0:3]:
                    os.chdir(prompt[3:])
                elif prompt == 'dsc':
                    print("iCMD - CMD for computers with restricted/no access to CMD.EXE or Linux/Mac Terminal")
                    print("Use at your own risk - Okmeque1 Corporation is not responsible for any damages done to any computers or people using this program.")
                    print("If iCMD gets blocked download the Lite version.")
                    print("Commands depend on your system.The prompt can be changed from the iprompt value in the code")
                    print("Commands may not work depending on your system.")
                    print("Current system : " + os.name)
                else:
                    os.system(prompt)
        except OSError:
            print("STOP : The Operating System has forcibly closed the running process due to a fatal system error.")
            input("Press ENTER to exit...")
            return None
        except ValueError:
            print("STOP : The value for a variable is either invalid or an access violation has occured.")
            input("Press ENTER to exit...")
            return None
        except PermissionError:
            print("STOP : Access Violation has occured in your file.The Operating system will now forcibly close due to this error")
            input("Press ENTER to exit...")
            return None
        except FileNotFoundError:
            print("STOP : The requested file you specified does not exist.The Operating system will forcibly close the program due to reading in an invalid space.")
            input("Press ENTER to exit...")
            return None
        except EOFError:
            print("STOP : The requested operation read beyond the end of the specified file.The Operating system will now forcibly close the program.")
            input("Press ENTER to exit...")
            return None
        except KeyboardInterrupt:
            print("STOP : The user has chosen to exit.Exiting...")
            return None
        except IOError:
            print("STOP : I/O error has occured.This means a device on your system has either malfunctioned or has been unplugged.The Operating system will now forcibly close the program.")
            input("Press ENTER to exit.")
            return None
        except:
            print("STOP : The program has forcibly exited with code 1")
            input("Press ENTER to exit...")
            return None
    except:
        print("STOP : EXCEPTION_IN_EXCEPTION : The program has attempted to recover from an exception causing another exception which caused it to forcibly close.")
        return None
icmd()
