import gspread
from oauth2client.service_account import ServiceAccountCredentials
    
def setup():
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    #creates an instance of the setupList object that takes care of interactions with the google cloud platform 

    ######### stuff that I actually wrote ... ##########

    setupList = [scope,creds,client]

    return setupList
#dont rlly need to worry about this one 
def sheetValFunc():
    sheetVal = 3 #the index of the spreadsheet you want to edit
        #another bigly important value-- this index starts at 0 
        #0 = clinton 
        #1 = centre 
        #2 - mifflin
        #3 - Juniata 
        #4 - perry
        #5 - rawdata (DO NOT EDIT!)

    return sheetVal 
#which sheet are you editing?
def whichColVal():
    print("hey! which column do you want to edit?")
    while True:
        colName = input()
        if colName == "Precinct":
            colVal = 2
            break
        elif colName == "DW":
            colVal = 3
            break
        elif colName == "Committeeman":
            colVal = 4
            break
        elif colName == "Phone":
            colVal = 5
            break
        elif colName == "Email":
            colVal == 6
            break
        elif colName == "Address":
            colVal = 7
            break
        elif colName == "Notes":
            colVal = 8
            break
        elif colName == "Polling Place":
            colVal = 9
            break
        elif colName == "Map":
            colVal = 10
            break
        else:
            print("Not a valid column name! try again")

    #colVal = 9 #the value of the column you want to edit ...this index starts at 1 
        #bigly important value
        #1 - empty 
        #2 - precinct name 
        #3 - DW 
        #4 - Committeman name 
        #5 - phone# 
        #6 = Email 
        #7 -- addresses of committeman 
        #8 notes 
        #9 -- polling places 
        #10 - Map 

    return colVal
#which column in the sheet are you editing?
def whichFile():
    addrFileName = "juniata_cty_addresses.txt" 

    return addrFileName 
#which text file has the data you're filling in?

def filler(setupList):
    
    scope = setupList[0]
    creds = setupList[1]
    client = setupList[2]
    
    sheet = client.open("Copy of Precincts")
    # -- LIVE! sheet = client.open("Precincts")
    #opens the spreadsheet by its title

    sheetVal = sheetValFunc()
    colVal = whichColVal()

    worksheet = sheet.get_worksheet(sheetVal)
    colValList = worksheet.col_values(colVal) #fetches the values of the chosen column in the chosen spreadsheet 
    #print(colValList) -- making sure that the list contains everything (output validation) 

    addrFileName = whichFile()
    addrFile = open(addrFileName, "r") #opens the file containing all of the addresses

    table = str.maketrans(dict.fromkeys("\n")) #translation table for removing the newline statements 

    addrList = addrFile.readlines() #creates a list of all the values from addresses.txt 

    gfList = [] #empty list for just the addresses --"Good Format List" 

    for x in range(len(addrList)):
        plcHolder = addrList[x] #holds the value of the current index to be brought to the new list gfList
        plcHolder = plcHolder.translate(table)
    
        gfList.append(plcHolder)
        
            #this for loop gets rid of all of the newline statements in the string

    #print(gfList) #output validation oWo
    
    addrFile.close()
    #row where to begin filling; 8

    editRowVal = 8

    for z in range(len(gfList)):
        newCellVal = gfList[z]
        print(newCellVal)
        worksheet.update_cell((editRowVal + z ), colVal, newCellVal)

        #this for loop updates the values in the spreadsheet, using the list with the new values! 

    print("all done -- your spreadsheet has been filled!")

setupList = setup()
filler(setupList)
