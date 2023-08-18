#!/usr/bin/python3
""" module list states
from database"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    # port and host are default local and 3306
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    # link both tables and get base on state_id
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC""")
    result = cur.fetchall()
    # check if second argument of tuple
    # is same as the passed argument
    for i in result:
        print(i)
    # close cursor and db
    cur.close()
    db.close()
