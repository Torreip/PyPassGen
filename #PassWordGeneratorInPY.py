#Import Section 
from os import sep, system, name, fsync
import os
import time
import sys
import random
import pyperclip

#Global Variable
global email

#Clear Fonction
def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


#Options Function
def options():
    pass

#Generation Function And Subordinate
def gen():
    clear()
    dataRead()
    global email
    sName = input("What's the service name ? ")
    email_choice = -1
    if len(email) > 1:
        for x in range(len(email)):
            print(x+1,")",email[x])
        print("what email should be used for the ",sName, "site or app ?")
        while email_choice > len(email) or email_choice < 0:
            try:
                email_choice = int(input("Please enter the number associeted with the desired email."))-1
            except ValueError:
                print("invalid input ")
    chars = "#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~';"#MAIN charslist.
    chartest = list(chars)
    pwd = "".join(random.choices(chartest, k=16)) #change lenght of pass here
    print(pwd)
    pyperclip.copy(pwd)
    pwd_data = open("pwd.txt", "a+")
    pwd_data.write("--- "+sName+" ---\n")  #MODIFY HERE THE FILE STRUCTURE
    pwd_data.write("\nemail : "+email[1+email_choice]+"\n")
    pwd_data.write("password : "+pwd+"\n")
    pwd_data.write("\n")

#File Functions:
def dataRead():
    global email
    try:
        data_email = open("data.dbeml", "r")
        email = data_email.readlines()
        email = [x[:-1] for x in email]
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
    data_email.flush()
    os.fsync(data_email.fileno())
    email = data_email.readlines()
    data_email.close

def dataFill():
    clear()
    global email
    if email == 0:
        print("Let's populate that file with it's first data !")
        print("The email should be writed as such : user@example.com")
        emailAdd()
        menu()
    else:
        data_email = open("data.dbeml", "r")
        email = data_email.readlines()
        data_email.close
        print("Welcome to the Data Filling Utility (DFU)")
        print("You curently have", len(email), "Registered in your file")
        print(email)
        try: 
            c2 = input("Make your choice (Y or n) ")
            c2 = c2.lower()

        except ValueError:
            print("invalid input")
        else:
            while c2 == "y" or c2 == "ye" or c2 == "yes":
                emailAdd()
                c2 = input("Do you want to continue (Yes or no) ? ")
                c2 = c2.lower()
            else:
                menu()

#Menu Fonction And Subordinate
def menu():
    clear()
    print("\n\n     [1] Generate a Password")
    print("     [2] Populate The email file")
    print("     [3] Manipulate The email file")
    print("     [4] Options")
    print("     [5] Info")
    print("     [6] Quit")
    print("\33[1;31;31m     [9] Delete The email data file \33[0m\n\n")
    #WIP Thinking about adding a 5th an 6th menu opytion (Delete a file and manipulate the file itself changing order delete ect)

    while True:
        try: 
            c1 = int(input("Please type the number associated with your choice. "))
        except ValueError:
            print("invalid input, please select a valid option from the above menu. ")
        else:
            if c1 == 1:
                gen()
            elif c1 == 2:
                dataFill()
            elif c1 == 3:
                pass
            elif c1 == 4:
                options()#
            elif c1 == 5:
                print("This python script as for utility to automaticly create and store password into a text file\nIt use the storing method the creator use tho you can modify this script as much as you want to better fit you.")
                print("Signed Torreip 2022")
                input("Press enter to return to the menu ")
                menu()
            elif c1 == 6:
                exit()
            elif c1 == 9:
                print("\33[1;31;31mThis Action Will Delete every bit of data in the data.dbeml file. This can't be reversed\33[0m")
                try: 
                    c3 = input("Make your choice (Yes or no) ")
                except ValueError:
                    print("invalid input")
                else:
                    c3 = c3.lower()
                    if c3 == "y" or c3 == "ye" or c3 == "yes":
                        if os.path.exists("data.dbeml"):
                            print("\33[1;31;31mNUKE PROCEDURE ENGAGED\33[0m")
                            os.remove("data.dbeml")
                            exit()
                        else:
                            print("An error occured the program will now close please restart it and select the 9th option again.")
                            time.sleep(5)
                            sys.exit
                    else:
                        menu()
            elif c1 == 507444126:
                print("Even tho the option wasn't presented you found it !")
                print("I congratulate you, you found this easter egg.")
                print("Torreip")
                time.sleep(5)
                menu()

def exit():
    print("\33[94mThank's for using my script ! (V0.6)")
    time.sleep(2)
    sys.exit()





#TODO:

#TO IMPROVE REDABILITY ==> Switch menu to case statement.
#Finish Every WIP feature
#Order the code!
#V1.0 release ??

#General Code

dataRead()
menu()
