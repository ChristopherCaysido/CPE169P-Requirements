import sqlite3


class DataAccess(object):
    db = r'C:\Users\Chris\Documents\GitHub\CPE169P-Requirements\Mod2_MP1\Mod2_MP1_ToDo_01\chinook.db'
    def __init__(self):
        """ constructor """
        self.conn = sqlite3.connect(self.db)
        self.cur = self.conn.cursor()
    def close(self):
        """ close db connection """
        self.conn.close()
    def executeQuery(self,query):
        self.cur.execute(query)
        return self.cur.fetchall()
    
    def commit(self):
        """ commit changes to db """
        self.conn.commit()

if __name__=='__main__':
    da = DataAccess()
    if da is not None:
        print(da.executeQuery('select * from employees'))
       

