import mysql.connector
midsbuyId = ["5425367899", "5425367890", "5425267890", "5925267890", "5925287890", 
            "5925287880", "5925287888", "5925287088", "5925287089", "5925207089",
            "5925207081", "5925206081", "5925206082", "5925206083", "5925206084",
            "5920206077", "5920206072", "5920206073", "5920206074", "5920206078"]
invalidGameIds = ["5925967890", "5920206071", "5920206076", "5920206075"]

# playerIdAndName = { "5925267890" : "KifahflowZiahs"}

class MidsbuyDatabase:
    def __init__(self, host, user, passwd, database):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
    # create the connection
    def create_connection(self, host, user, passwd, database):
        try:
            conn = mysql.connector.connect(
                host=host,  # change it with hostname your that your provider gave you
                user=user,       # change it with username your that your provider gave you
                passwd=passwd,    # so on
                database=database  # change it with  your own database
            )
            print("Si guul leh baabu kugu xirnay salka xogta.") # message for successfull connection
            return conn
        except:
            # print("Waa lagu haray ku xiritaanka salka xogta!")
            print("")


# # Testing the class and methods
# database = Database("localhost", "root", "12345", "midsbuyproject")
# print("The host is name: ", database.database)

# # create a cursor
# mydb = database.create_connection(database.host, database.user, database.passwd, database.database)
# mycursor = mydb.cursor(buffered=True)


# def sumit_player_id(mycursor, playerId, table_name):
#     mycursor.execute(f"""
#         INSERT INTO {table_name}(playerID)
#         VALUES({playerId})

#     """)
#     database.commit()
