import sys
from local.Lockpass import lockpass
class start():
    def error(): #type: ignore
        pass
    def SystemControl(): # type: ignore
        return 0

    def Argvcheck(): # type: ignore
        try:
            command = sys.argv[1]
        except IndexError:
            lockpass.help()
            return 2 #noarguments
        if command == 'newbook':
            passwd = str(input("Write a good password for the book (DON'T FORGET IT) > "))
            descr = str(input("Add a description (facoltative) > "))
            if descr == "":
                descr = "None"
            if not lockpass.newbook(sys.argv[2], descr, passwd): # type: ignore
                print('''Book created succesfully\n''' + "Name: " + sys.argv[2] + "\nDescription: " + descr + "\nPassword: " + passwd)
            else:
                print("an error has occurred: Try to relaunch the program. If the problem persists, contact the support")
        return 0
if not start.SystemControl():
    start.Argvcheck()
else:
    start.error()