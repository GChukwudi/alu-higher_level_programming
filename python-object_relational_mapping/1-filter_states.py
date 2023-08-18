#!/usr/bin/python3
""" module list states
from database"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    # port and host are default local and 3306
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    result = cur.fetchall()
    # display elements with N
    # only by taking comparing their first letter in tuple
    for i in result:
        if i[1][0] == 'N':
            print(i)
    # close cursor and db
    cur.close()
    db.close()
