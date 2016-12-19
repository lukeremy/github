## this is a python file to create a Cassandra database of 
## heroes and villains from Gotham

# import library, connect to Cassandra cluster
# see cqlsh output for needed info
# cqlsh > DESCRIBE KEYSPACE
from cassandra.cluster import Cluster
cluster = Cluster(['127.0.0.1'],port=9042)
session = cluster.connect('batcave')

# set keyspace 
session.set_keyspace('batcave')

# add table to keyspace
session.execute( """ CREATE TABLE characters (heroname text PRIMARY KEY, firstname text, lastname text, city text, designation text);""")

# add data to table
session.execute(""" INSERT INTO characters (heroname, firstname, lastname, city, designation) values ('Batman', 'Bruce', 'Wayne', 'Gotham', 'hero')""")
session.execute(""" INSERT INTO characters (heroname, firstname, lastname, city, designation) values ('Joker', '???', '???', 'Gotham', 'villain')""")
session.execute(""" INSERT INTO characters (heroname, firstname, lastname, city, designation) values ('Superman', 'Clark', 'Kent', 'Metropolis', 'hero')""")


