#Import Section 
from os import sep, system, name, fsync
import os
import time
import sys

#Global Variable
global email

#Clear Fonction
def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


#Generation Fonction And Subordinate
def gen():
    print("the generation fonction as been called")#placeholder

def dataRead():
    global email
    try:
        data_email = open("data.dbeml", "r")
        email = data_email.readlines()
        data_email.close
        if email:
            pass#may do something here to tell the user ^^
        else:
            print("An Email data file was found but is empty. To resolve the issue the DFU will now lunch")
            print("Welcome to the Data Filling Utility (DFU)")
            email = 0
            dataFill()
    except FileNotFoundError:
        print("The email list file dosen't exit. The DFU will help you configure the script for your first use !")
        print("Welcome to the Data Filling Utility (DFU)")
        email = 0
        dataFill()

def emailAdd():
    global email
    data_email = open("data.dbeml", "a+")
    userEmail = input("What email should be added ? ")
    data_email.write(userEmail+"\n")
    email = data_email.readlines()
    data_email.flush()
    os.fsync(data_email.fileno())
    data_email.close

def dataFill():
    global email
    data_email = open("data.dbeml", "r")
    email = data_email.readlines()
    data_email.close
    if email == 0:
        print("Let's populate that file with it's first data !")
        print("The email should be writed as such : user@example.com")
        emailAdd()
    else:
        print("Welcome to the Data Filling Utility (DFU)")
        print("You curently have", len(email), "Registered in your file")
        print(email)
        try: 
            c2 = input("Make your choice (Y or n) ")
        except ValueError:
            print("invalid input")
        else:
            while c2 == "y" or c2 == "ye" or c2 == "yes":
                emailAdd()
                c2 = input("Do you want to continue (Y or n) ? ")
            else:
                clear()
                menu()
    data_email.close

#Menu Fonction And Subordinate
def menu():
    print("     [1] Generate a Password")
    print("     [2] Populate The email file")
    print("     [3] Info")
    print("     [4] Quit")
    #WIP Thinking about adding a 5th an 6th menu opytion (Delete a file and manipulate the file itself changing order delete ect)

    while True:
        try: 
            c1 = int(input("Make your choice (between 1 and 4) "))
        except ValueError:
            print("invalid input, please select a number between 1 and 4. ")
        else:
            if c1 == 1:
                gen()
            elif c1 == 2:
                print("Welcome to the Data Filling Utility (DFU)")
                dataFill()
            elif c1 == 3:
                print("This python script as for utility to automaticly create and store password into a text file\nIt use the storing method the creator use tho you can modify this script as much as you want to better fit you.")
                print("Signed Torreip 2022")
                time.sleep(7.5)
                clear()
                menu()
            elif c1 == 4:
                print("Thank's for using my script !")
                time.sleep(2)
                sys.exit()
            elif c1 == 507444126:
                print("Even tho the option wasen't presented you found it !")
                print("I congratulate you, you found this easter egg.")
                print("Torreip")



#General Code

dataRead()
menu()
