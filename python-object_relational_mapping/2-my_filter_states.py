#!/usr/bin/python3
""" module list states
from database"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    # port and host are default local and 3306
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    # use string formating to be specific
    cur.execute("SELECT * FROM states WHERE states.name = '{}'\
    ORDER BY states.id ASC".format(argv[4]))
    result = cur.fetchall()
    # check if second argument of tuple
    # is same as the passed argument
    for i in result:
        if i[1] == argv[4]:
            print(i)
    # close cursor and db
    cur.close()
    db.close()
