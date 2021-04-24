import sqlite3

class DataAccess(object):
    db = r'C:\Users\Chris\Documents\GitHub\CPE169P-Requirements\Mod2_MP1\sqlite_02\chinook.db'
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
        print(da.executeQuery('SELECT InvoiceId, BillingAddress, \
                Total FROM invoices\
                WHERE Total BETWEEN 14.91 and 18.86 ORDER BY Total'))
        print(da.executeQuery('SELECT albumid, COUNT(trackid) \
                                FROM tracks GROUP BY albumid;'))
        print(da.executeQuery('SELECT Title, Name FROM  albums\
                                INNER JOIN artists ON artists.ArtistId = albums.ArtistId;'))
        print(da.executeQuery('''SELECT trackid, name, albumid FROM tracks WHERE albumid = (SELECT albumid FROM albums WHERE title='Let There Be Rock');'''))
        print(da.executeQuery('''
        SELECT customerid,
            firstname,
            lastname
            FROM customers
            WHERE supportrepid IN (
            SELECT employeeid
            FROM employees
            WHERE country = 'Canada'
        );
        '''))
        
    

