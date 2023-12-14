import sys
import MySQLdb

def lis_states(username, password, hbtn_0e_0_usa ):
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=hbtn_0e_0_usa)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
    
    
    if __name__ == "__main__":
        lis_states(sys.argv[1], sys.argv[2], sys.argv[3])
        if len(sys.argv) != 4:
           print("Usage: {} username password database".format(sys.argv[0]))
        exit(1)
    username, password, hbtn_0e_0_usa = sys.argv[1], sys.argv[2], sys.argv[3]
    lis_states(username, password, hbtn_0e_0_usa)
        
        
        