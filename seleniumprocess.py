from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from MidsbuyApp import MidsbuyDatabase
database = MidsbuyDatabase("localhost", "root", "12345", "midsbuyproject")
# read tempo id from txt
def get_playerId():
    # read ids in tempofile
    with open("tempoIds.txt") as tempofile:
        # strip new lines
        contents = list(map(lambda x:x.strip(),tempofile.readlines()))
        player_id = contents[0]
        file = open("tempoIds.txt", "w")
        # delete the served id
        for playerId in contents[:-1]:
            file.write(playerId + '\n')

    return player_id

def get_player_name(playerId):
    s = Service("geckodriver/geckodriver.exe")
    browser = webdriver.Firefox(service=s)
    while True:
        try: 
            browser.get('https://www.midasbuy.com/midasbuy/ot/buy/pubgm') # data Entry page
            browser.maximize_window() # For maximizing window
            break
        except:
            print("Qalad baan la kulmeyna...")
    browser.maximize_window() # For maximizing window
    browser.implicitly_wait(20) # gives an implicit wait for 20 seconds
    try:
        browser.maximize_window() # For maximizing window
        PlayerIdElem = browser.find_element(By.CLASS_NAME, 'input')
        PlayerIdElem.send_keys(playerId)
        #print("Waan gelinay xog...")
        counter = 1
        while True:
            try:
                browser.maximize_window() # For maximizing window
                PlayerIdElem.send_keys(Keys.ENTER)
                # class2 = "pc-show-mod"
                counter +=1
                #print("Waan helnay...", counter)
                nickname2 = browser.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[3]/div/div/div/div[1]/div[1]/p")
                for i in nickname2:
                    print(i.text)
                    thePlayerName = i.text
                browser.quit()
                break
            
            except Exception as exc:
                print("Wali", exc)

                counter +=1 
    except Exception as exc:
        browser.maximize_window() # For maximizing window
        print("Qadalad baa jiree sug...", exc)
    
    # send the player name to the database
    # create connection to the data base
    mydb = database.create_connection(database.host, database.user, database.passwd, database.database)
    cursor = mydb.cursor(buffered=True)

    cursor.execute(f""" 
            INSERT INTO plyerIdsAndNames(playerID, playerName)
            VALUES('{playerId}' , '{thePlayerName}');
    """)
    mydb.commit()
    return thePlayerName