import requests
import json
import os
import urllib.request
import sys
import shutil
import codecs
from fdaencrypt import *
#
# from Crypto.Cipher import AES

global websiteUrl

def connectToDB(username, password):
#    resp = requests.post('http://127.0.0.1:8000/remote_login/', data = {'username': username, 'password': password})
    resp = requests.post(websiteUrl + '/fdalogin/', data = {'username': username, 'password': password})

    # print(resp.status_code)
    # print(resp.content)

    if(resp.status_code == 200):
        print("Welcome to the File Download Application, " + username + "!")
        print("-------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------")
        return 1;
    else:
        print("Incorrect Username or Password")
        return 0;

def getReports():
    #resp = requests.post('http://127.0.0.1:8000/remote_reports/')
    resp = requests.post(websiteUrl + '/remote_reports_view/')

    if resp.status_code == 200:
        print("-------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------")
        print("Available Reports:")
        print("")
        decoded = resp.content.decode("utf-8")
        dictObj = json.loads(decoded)
        reportList = dictObj["list_of_report_names"]

        for name in reportList:
            print(name)
        print("")
        print("-------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------")





        return reportList
    else:
        print(resp.status_code)
        print("Connection Error")
        sys.exit()



def getInfo(company_name):
    # curDir = os.getcwd()
#    resp = requests.post('http://127.0.0.1:8000/report_info/', data={"report" : report_name})
    #print("getInfo method reached")
    resp = requests.post(websiteUrl + '/report_info/', data={'company_name' : company_name})
    #print("request method reached")
    if resp.status_code == 200:
    #     print("request method 2 reached")
        decoded = resp.content.decode("utf-8")
        dictObj = json.loads(decoded)
        reportInfo = dictObj["report_info"]
        files = dictObj["report_files"]


        compName = reportInfo[0]
        compPhone = reportInfo[1]
        compLoc = reportInfo[2]
        compCountry = reportInfo[3]
        # compSector = reportInfo[5]
        # compIndustry = reportInfo[6]
        curProj = reportInfo[4]
        # repName = reportInfo[8]

        print("-------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------")




        print("Report Info:")
        print("")
        print("Company Name: " + compName)
        print("Company Phone: " + compPhone)
        print("Company Location: " + compLoc)
        print("Company Country: " + compCountry)
        # print("Company Sector: " + compSector)
        # print("Company Industry: " + compIndustry)
        print("Current Project: " + curProj)
        print("Report Files: ")
        count = 1
        for key,value in files.items():
            print("  " + str(count) + ") " + key)
            count += 1
            # value = "http://127.0.0.1:8000" + value


        print("-------------------------------------------------------------------------")

        #Form a dict mapping filename to URL


        downloadLoop(files)
        # while (1):
        #     cont = input("Enter 'c' to view another report or 'quit' exit the program: ")
        #     if cont == "continue":
        #         return 1
        #     elif cont == "quit":
        #         print("Exiting Program...")
        #         sys.exit()
        #     else:
        #         print("Please Enter either 'continue' or 'quit' ")



    else:
        print("Connection Error")
        sys.exit()




# def download(fileUrl, filename, isEncrypted):

def download(fileUrl, filename, isEncrypted):
    # #get filename and extension
    #fileUrl = "http://127.0.0.1:8000" + fileUrl
    fileUrl = websiteUrl[:-1] + fileUrl
    print(fileUrl)
    # print(fileUrl)
    suffix = fileUrl.split(".")[-1]


    with urllib.request.urlopen(fileUrl) as response, open(filename, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

    if (suffix == "enc"):
        print("Decrypting File...")
        decrypt_file(filename, '0123456789abcdef')


#Input control functions

def logIn():
    logged = 0
    while (not logged):
        username = input("Enter username: ")
        password = input("Enter password: ")
        logged = connectToDB(username, password)
        # logged = connectToDB("team29", "team29")

def chooseTask():
    validResponse = 0
    while (not validResponse):
        task = input("Enter 'reports' to view reports or 'encrypt' to encrypt a file or 'terminate' to terminate program: ")
        if task == "reports":
            list = getReports()
            EnterReportName(list)

        elif task == "encrypt":
            encryptLoop()
        elif task == "terminate":
            print("Exiting Program...")
            sys.exit()
        else:
            print("Error: Enter valid response or 'terminate' ")



def downloadLoop(urlDict):
    doneDownloading = 0
    while (not doneDownloading):
        print (websiteUrl)
        file = input("Enter name of file to download or type 'quit' to go back: ")
        if file == "quit":
            doneDownloading = 1
        elif file in urlDict:
            download(urlDict[file], file, 0)
            print("Downloading " + file + "...")
            download(urlDict[file], file, 0)
            print("Download complete, file saved to current directory.")
            doneDownloading = continueLoop()
        else:
            print("Please enter a valid filename or 'quit' ")




def EnterReportName(list):
    notFirstTime = 0
    enteringReport = 1
    while (enteringReport):
        if(notFirstTime):
            getReports()
        report = input("Type the name of the report you wish to view or type 'quit' to go back: ")
        if report == 'quit':
            return
        elif report in list:
            notFirstTime = getInfo(report)
        else:
            print("Please Enter a Valid Report Name.")

# def fileLoop(urlDict):
#     downloading = 1
#     while (downloading):
#         file = input("Type the name of the file you wish to download or type 'quit' to exit: ")
#         if file == 'quit':
#             return
#         elif file in urlDict:
#             download(urlDict[file], file, 0)
#             print("Downloading " + file + "...")
#             print("Download complete, file saved to current directory.")
#             downloading = continueLoop()
#
#         else:
#             print("Please Enter a Valid File Name.")

def continueLoop():
    while (1):
        continueDownload = input("Download another file? (yes/no): ")
        if continueDownload == 'yes':
            return 0
        elif continueDownload == 'no':
            return 1
        else:
            print("Invalid Input.")

def encryptLoop():
    #Get all files in user's cwd
    curDir = os.getcwd()
    myListDir = os.listdir(curDir)
    nonDir = []
    for file in myListDir:
        if not os.path.isdir(file):
            nonDir.append(file)

    while (1):
        file = input("Enter the name of file to encrypt or 'quit' to go back: ")
        if file in nonDir:
            encrypt_file(file,'0123456789abcdef')
            print("Encrytping " + file + "...")
            return 1
        elif file == 'quit':
            return 0
        else:
            print("Invalid input, make sure file is in your current directory.")


if __name__ == "__main__":
    websiteUrl = input("Input website URL: ")
    logIn()
    chooseTask()

#
# key = "Nader_is_awesome"
#
# def decrypt_file(filename_input, symmetric_key):
#     init_vec = b"1234567890123456"
#     AES_key = AES.new(symmetric_key, AES.MODE_CFB, init_vec)
#     output_filename = filename_input[:-4]
#     with open(filename_input, 'rb') as f:
#         raw_file = f.read()
#         data_dec = AES_key.decrypt(raw_file)
#     with open(output_filename, 'wb') as o:
#         o.write(data_dec)
#         print('Decrypted File Name:' + output_filename)
#     return True
