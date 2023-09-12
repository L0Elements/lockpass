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
import sqlite3

class lockpass:
    path = "Data/passwords.db"
    db = sqlite3.connect(path)
    cur = db.cursor()
    def __init__(self):
        try:
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

    def passwdindex(self):
        return self.cur.execute("SELECT * FROM password").fetchall()

    def rmpassword(self, account_location, account_username, password):
        query = (account_location, account_username, password)
        #finding the number of results with the correct properties (usually there has to be only one result)
        results = self.cur.execute("SELECT COUNT(*) FROM password WHERE \
                                   website=? AND \
                                   username = ? AND \
                                   password = ?", query).fetchone()
        if results[0]:
            self.cur.execute("DELETE FROM password WHERE\
                                website=? AND \
                                username = ? AND \
                                password = ?", query)
            self.db.commit()
        else:
            raise EntryNotFoundError("Database entry Not Found")
    
    def changepasswd(self, old= (), new = ()):
        if len(old) == len(new):
            self.rmpassword(old[0], old[1], old[2])
            self.addpasswd(new[0], new[1], new[2])          
        else:
            raise Exception

class EntryNotFoundError(Exception):
    pass

if __name__ == '__main__':
   pass