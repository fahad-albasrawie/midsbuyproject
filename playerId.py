# python 3.10
# This program ask player anme and desplays
# player id and name after some time
# depends on the connection spees

from MidsbuyApp import MidsbuyDatabase
from seleniumprocess  import get_player_name

# Configure database
database = MidsbuyDatabase("localhost", "root", "12345", "midsbuyproject")
# print("The host is name: ", database.database)
# create a cursor
mydb = database.create_connection(database.host, database.user, database.passwd, database.database)
mycursor = mydb.cursor(buffered=True)


# ask the player id

def ask_player_id(mycursor, table_name):
    while True:
        playerId  = input("Enter player id (5425367890): ")
        if playerId == 0:
            break
        
        elif playerId.isdecimal():
            if len(str(playerId)) > 9 and len(str(playerId)) < 11:
                mycursor.execute(f"""
                    INSERT INTO {table_name}(playerID)
                    VALUES({playerId})

                    """)
                mydb.commit()
                print(f"Your id '{playerId}' was successfully sent to our database. ")
                print("We will serve you soon, please wait...")

                print("\n\n\n--------------------")
                print(f"Your ID is:{playerId}.")
                print(f"Your name is: {get_player_name(playerId)}.")
                print("--------------------\n\n\n")
                break
            else:
                print("\aPlease input only numerical values!\n")
        else:
            print("\aPlease check your id length.\n")
            continue
        

ask_player_id(mycursor, 'tempoplayerids')






