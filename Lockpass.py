"""
Copyright (C) 2023 L0Elements

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""
'''
ERROR TABLE:
0 = Success
1 = Probably a software's problem: autofix process executed
2 = Input-related problem
'''
import os
import datetime
import shutil
import secrets
import time


def error():
#    print("An error has occurred, trying to autofix")
    lockpass.initialize()
#    print("Autofix Done! Try to repeat the command, if the problem persists, contact the support")
    return 0

class lp_utilities:
    def getfilelines(path):
        f = open(path)
        p_list = []
        d_list = []
        e_list = ''
        for line in f:
            if line == '':
                break
            else:
                p_list.append(line)

        for string in p_list:
            for letter in string:
                if letter != '\n':
                    e_list = e_list + letter
                else:
                    pass
            d_list.append(e_list)
            e_list = ''
        return d_list
class lockpass():

    def newbook(name, description, ): # type: ignore
        try:
            list = lockpass.booklist()
            if not name in list: # type: ignore
                os.mkdir("Data/books/" + name) # type: ignore
            else:
                return 2
        except:
            error()
            return 1

        with open("Data/books/" + name +"/.bookinfo", "w") as f: # type: ignore
            f.write("Name:" + name + '\n' + "Created on:" + str(datetime.date.today()) + "\nDescription:" + description) # type: ignore
        i = open("Data/books/" + name + "/.index", "x") #type: ignore
        i.close()
        os.mkdir("Data/books/" + name + "/Recyclebin")
        return 0
    def initialize(): # type: ignore
        try:
            os.mkdir("Data")
        except:
            pass
        try:
            os.mkdir("Data/books")
        except:
            pass
        return 0
    def booklist():	# type: ignore
        try:
            list = os.listdir("Data/Books")
        except FileNotFoundError:
            error()
            return 1
        return list
    def rmbook(name): #type: ignore
        list = lockpass.booklist()
        if name in list: # type: ignore
            shutil.rmtree("Data/books/" + name) # type: ignore
            return 0
        else:
            return 2 #Book does not exist

    def addpasswd(bookname, account_location, account_username, password , type): #type: ignore
        list = lockpass.booklist()
        uuid = secrets.token_hex(32)
        if bookname in list: # type: ignore
            with open("Data/books/" + bookname + "/" + uuid, "w") as f: # type: ignore
                f.write("Id:" + uuid + "\nType: " + type + "\nUserName:" + account_username + "\nLocation:" +
                        account_location + "\nPassword:" + password + "\nCreated on:" + str(datetime.date.today()) )
            l = open("Data/books/" + bookname + "/.index", "a")
            l.write( uuid + '\n')
            l.close()
        else:
            return 2
        return 0

    def passwdindex(bookname):
        blist = lockpass.booklist()
        if not bookname in blist:
            return 2
        else:
            return lp_utilities.getfilelines("Data/books/"+ bookname + "/.index")

    def rmpassword(bookname, id):
        blist = lockpass.booklist()
        plist = lockpass.passwdindex(bookname)

        if bookname in blist and id in plist:
            os.remove("Data/books/" + bookname + '/' + id)
            nlist = []

            for pass_id in plist:
                if pass_id != id:
                    nlist.append(pass_id)
                else:
                    pass
            shutil.move("Data/books/" + bookname + "/.index", "Data/books/" + bookname + "/Recyclebin")
            os.rename("Data/books/" + bookname + "/Recyclebin/.index", "Data/books/" + bookname + "/Recyclebin/.index" + str(time.time()) + ".old" )
            f = open("Data/books/" + bookname + "/.index", 'w')
            f.close()
            del f
            with open("Data/books/" + bookname + "/.index", 'a') as f:
                for npass_id in nlist:
                    if npass_id != id:
                        f.write(npass_id + '\n')
                    else:
                        pass
            return 0
        return 2

    class passwordinfo():
        def all(bookname, id):
            if bookname in lockpass.booklist() and id in lockpass.passwdindex(bookname):
                p = lp_utilities.getfilelines("Data/books/" + bookname + "/" + id)
                var = ''
                a = ''
                n = ''
                dict = {}
                for line in p:
                    for char in line:
                        if char != ':':
                            var = var + char
                        else:
                            n = var
                            var = ''
                    a = var
                    dict[n] = a

                    var = ''
                    a = ''
                    n = ''
                return dict
            else:
                return 2
        def username(bookname, id):
            allinfo = lockpass.passwordinfo.all(bookname, id)
            return allinfo['UserName']
        def passwd(bookname, id):
            allinfo = lockpass.passwordinfo.all(bookname, id)
            return allinfo['Password']
        def AccLocation(bookname, id):
            allinfo = lockpass.passwordinfo.all(bookname, id)
            return allinfo['Location']
        def timecreated(bookname, id):
            allinfo = lockpass.passwordinfo.all(bookname, id)
            return allinfo['Created on']
        def type(bookname, id):
            allinfo = lockpass.passwordinfo.all(bookname, id)
            return allinfo['Type']
        def id(bookname, id):
            allinfo = lockpass.passwordinfo.all(bookname, id)
            return allinfo['Id']

    class bookinfo():

        def all(name):
            if name in lockpass.booklist():
                b = lp_utilities.getfilelines("Data/books/" + name + "/.bookinfo")
                var = ''
                a = ''
                n = ''
                dict = {}
                for line in b:
                    for char in line:
                        if char != ':':
                            var = var + char
                        else:
                            n = var
                            var = ''
                    a = var
                    dict[n] = a

                    var = ''
                    a = ''
                    n = ''
                return dict
            else:
                return 2
        def name(name):
            allinfo = lockpass.bookinfo.all(name)
            return allinfo['Name']
        def timecreated(name):
            allinfo = lockpass.bookinfo.all(name)
            return allinfo['Created on']
        def Description(name):
            allinfo = lockpass.bookinfo.all(name)
            return allinfo['Description']