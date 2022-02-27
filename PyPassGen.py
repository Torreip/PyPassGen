#Import Section 
from os import sep, system, name, fsync
import os
import time
import sys
import random
import pyperclip

#Global Variable
global email
global emailstr

#Clear Fonction
def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

#Menu Fonction And Subordinate
def menu():
    clear()
    print("\n\n     [1] Generate a Password")
    print("     [2] Populate The email file")
    print("     [3] Info")
    print("     [4] Quit")
    print("\33[1;31;31m     [9] Delete The email data file \33[0m\n\n")

    try: 
        c1 = int(input("Please type the number associated with your choice. "))
    except ValueError:
        print("invalid input, please select a valid option from the above menu. ")

    menuChoice = {
        1: gen,
        2: dataFill,
        3: info,
        4: exit,
        9: nuke,
    }

    menuChoice[c1]()

def info():
    print("What started as a little personnal week-end project, to speed up password generation and storage.")
    print("Got a lil bit out of hand, to a point I think my litle tool may help some people out there.")
    print("Torreip // 2022")
        
def exit():
    print("\33[94mThank's for using my program ! (V1.0)")
    time.sleep(3)
    sys.exit()

def nuke():
    global email
    print("\33[1;31;31mThis Action Will Delete every bit of data in the data.dbeml file. This can't be reversed ! \33[0m")
    try: 
        c2 = input("Do you want to proceed ? (Y/n) ")
    except ValueError:
        print("invalid input ")
    else:
        c2 = c2.lower()
        if c2 == "y" or c2 == "ye" or c2 == "yes":
            print("\33[1;31;31mNUKE PROCEDURE ENGAGED\33[0m")
            email = 0
            os.remove("data.dbeml")
            exit()
        else:
            menu()

#Generation Function And Subordinate
def gen():
    clear()
    dataRead()
    global email
    global emailstr
    sName = input("What's the service name ? ")
    email_choice = -1
    if len(email) > 1:
        for x in range(len(email)):
            print(x+1,")",emailstr[x])
        print("what email should be used for the ",sName, "site or app ?")
        while email_choice > len(email) or email_choice < 0:
            try:
                email_choice = int(input("Please enter the number associeted with the desired email. "))-1
            except ValueError:
                print("invalid input ")
    chars = "#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~';"#MAIN charslist.
    chartest = list(chars)
    pwd = "".join(random.choices(chartest, k=16)) #change lenght of pass here
    print(pwd)
    pyperclip.copy(pwd)
    pwd_data = open("pwd.txt", "a+")
    pwd_data.write("--- "+sName+" ---\n")  #MODIFY HERE THE PASSWORD FILE STRUCTURE
    pwd_data.write("\nemail : "+email[email_choice]+"\n")
    pwd_data.write("password : "+pwd+"\n\n")

#File Functions:
def dataRead():
    global email
    global emailstr
    try:
        data_email = open("data.dbeml", "r")
        email = data_email.readlines()
        emailstr = [x[:-1] for x in email]
        data_email.close
        if email:
            pass#may do something here to tell the user ^^
        else:
            print("An Email data file was found but is empty. To resolve the issue the DFU will now lunch")
            print("Welcome to the Data Filling Utility (DFU)")
            email = 0
            dataFill()
    except FileNotFoundError:
        print("The email list file dosen't exit. The DFU will help you configure the program for your first use !")
        print("Welcome to the Data Filling Utility (DFU)")
        email = 0
        dataFill()

def emailAdd():
    global email
    data_email = open("data.dbeml", "a+")
    userEmail = input("What email should be added ? ")
    data_email.write(userEmail+"\n")
    data_email.flush()
    os.fsync(data_email.fileno())
    email = data_email.readlines()
    data_email.close

def dataFill():
    clear()
    global email
    global emailstr
    if email == 0:
        print("Let's populate that file with it's first data !")
        print("The email should be writed as such : user@example.com")
        emailAdd()
        menu()
    else:
        print("Welcome to the Data Filling Utility (DFU)")
        print("You curently have", len(email), "Email address registered in your file")
        for x in range(len(email)):
            print(x+1,")",emailstr[x])
        try: 
            c3 = input("Do you want to add an email to the file ? (Y/n) ")
            c3 = c3.lower()
        except ValueError:
            print("invalid input ")
        else:
            while c3 == "y" or c3 == "ye" or c3 == "yes":
                emailAdd()
                c3 = input("Do you want to add another email ? (Y/n) ")
                c3 = c3.lower()
            else:
                menu()

#General Code

dataRead()
menu()
