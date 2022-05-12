# python 3.10

# This program reads rempo player ids from the storage
# Note: This script must not be TERMINATED..
from MidsbuyApp import MidsbuyDatabase
import time
# Configure database
# database = MidsbuyDatabase("localhost", "root", "12345", "midsbuyproject")
# print("The host is name: ", database.database)
# create a cursor
# mydb = database.create_connection(database.host, database.user, database.passwd, database.database)
# mycursor = mydb.cursor(buffered=True)

def read_tempo_ids():
    counter = 1
    while True:
        
        try:

            database = MidsbuyDatabase("localhost", "root", "12345", "midsbuyproject")
            mydb = database.create_connection(database.host, database.user, database.passwd, database.database)
            cursor = mydb.cursor(buffered=True)
        except Exception as exc:
            print(exc)
        #time.sleep(3)
        print("Looping throught the database", counter)

        try:

            cursor.execute(f"""
                SELECT * FROM tempoplayerids;
            """)
            counter2 = 1
            try:
                for playerId in cursor:
                    print(counter, playerId)
                    counter2 += 1

                    # read ids in tempofile
                    with open("tempoIds.txt") as tempofile:
                        # strip new lines
                        contents = list(map(lambda x:x.strip(),tempofile.readlines()))

                    # save the player id to tempoIds.txt file
                    # print(playerId[0], "---", contents) # for debuging
                    if playerId[0] in contents:
                        continue
                    else:
                        file = open("tempoIds.txt", "a")
                        file.write(playerId[0] + '\n') # playedId has tuble
                        # delete the recently saved player id from the tempoids table in the database
                        cursor.execute(f"""
                            DELETE FROM tempoplayerids WHERE playerID = {playerId[0]}
                        """)
                        mydb.commit()
            except Exception as exc:
                print(exc)
        except Exception as exc:
            print(exc)
        counter += 1

# counter = 1
# while True:
#     print("Looping throught the database", counter)
#     read_tempo_ids(mycursor)
#     counter += 1

read_tempo_ids()