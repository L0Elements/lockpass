"""
TODO:
- rewrite all the methods in order to be compatible with sqlite3
"""
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
import datetime
import time
import sqlite3

class lockpass:
    path = "Data/passwords.db"
    db = None
    cur = None
    def __init__(self):
        self.db = sqlite3.connect(self.path)
        try:
            self.cur = self.db.cursor()
            self.cur.execute("CREATE TABLE password(website, username, password)")
        except sqlite3.OperationalError:
            pass
        
    def addpasswd(self, account_location, account_username, password): 
       #checking if the same password exists, after that creating the entry
        entry = self.cur.execute(f"SELECT * FROM password WHERE website='{account_location}' AND username='{account_username}' AND password='{password}'") 
        if entry.fetchone() == None:
            self.cur.execute(f'''INSERT INTO password VALUES
                             ('{account_location}', '{account_username}', '{password}')
                             ''')           
            self.db.commit()

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