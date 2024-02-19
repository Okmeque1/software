# Error chart:

## Note : This chart will only be useful if programs have built-in error handling

6510A FileExistsError : A file that exists is conflicting with the selected file.Delete the old file.


6510B FileNotFoundError : The valid file is not valid.Create the specified file and try again.


6510C Read/Write Error : Drive is read-only.Check permissions and try again.


0280 SyntaxError : The program you got has an error or has been tampered with. Contact support.


0281 Exception : The program you got has an error or has been tampered with. Contact support.


0211 ValueError : The program you got has an error, bad value may have been inputted or an unspecified error with file has bad permissions.Check permissions or try again with correct type(G-Calc needs numbers(1,2,454 or 3.141592)) and try again,else contact support.


0271 OSError : Operating system error.Check your drive and program,aswell as any files and try again.


0251 TypeError : The program you got has an error or has been tampered with. Contact support.


0210 PermissionError : Access violation in file.Check permissions and try again.


0250 EOFError : Possible input fault or code has been tampered with.When ready to input command,press ENTER.Else contact support.


0270 KeyboardInterrupt : User has chosen to exit.No action is needed.


0261 ExceptionRecoveryError : Multiple errors have succeded at once,and since handlers can only handle 1 error,program crashes.Contact support.


05HG NameError : The program you got has an error or an invalid reference was put in.Try again,else contact support.


0199 ImportError : Required module does not exist.Install via 'pip' for best compatability.After installing try again.


0190 KeyError : Either bad key was specified for accessing a dictionary internally or bad value was inputted(this is because programs map for example "T" to "True" and so for the dictionary side it would look like this dictest = {"T":"True"} and this : test = dictest[test]. So if you enter a "T" it works because it converts "T" to "True". But if you put in an "A", that doesn't exist in dictest which then produces error 0190). Try again and input the CORRECT values that are demanded.


0910 IndexError : Bad access value was specified in code or bad value was inputted(this because list looks like this : lst = [1,2,3] and so if you want to access the number 2 you do lst[1] but if you access lst[123] it won't exist and throws error 0910)


0255 ZeroDivisionError : Operation resulted from dividing by 0(invalid).Check parameters and try again


755F RuntimeError : Bad Python interpreter.Reinstall python and try again(you might have a broken hard drive).


760F SystemError : Bad Python interpreter.Reinstall python and try again(you might have a broken hard drive)


765E MemoryError : No more memory(consider upgrading your computer).Close all programs,then reboot and try again.


780F TimeOutError : Operation took to long.Try again.


770A GeneralException : A general exception has occured,which means nothing and that a part of the program has had an exception.Try again.


1E/08 requests.exceptions.ConnectionError : Module REQUESTS cannot access the specified website. Please check your cabling, wifi and if that does not work, contact the website administrator fore more info.


1E/10 Placeholder : for later use


1E/18 Placeholder : for later use


1E/20 Placeholder : for later use


1E/21 Placeholder : for later use
