import sys
import pathlib
from local.Lockpass import lockpass
class start():
    def error():
        return 0
    def SystemControl():
        path = pathlib.PureWindowsPath("./main.py")
        print(path)
        return 0

    def Argvcheck():
        try:
            command = sys.argv[1]
        except IndexError:
            lockpass.help()
            return 2 #noarguments
        print(sys.argv)
        if command == 'newbook':
            lockpass.newbook("bookone") # type: ignore
if not start.SystemControl():
    start.Argvcheck()
else:
    start.error()