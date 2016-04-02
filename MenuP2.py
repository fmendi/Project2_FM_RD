import os
import random
i


def get_random():
    return random.randint(0,63)
def get_random_char():
    return chr(97 + random.randint(0,25))


def clear():
    os.system('cls')
    os.system('clear')    

def main_menu():
    print("Project 2 Main Menu")
    print("Enter 1: Create and populate a database")
    print("Enter 2: Retrieve records with a given key")
    print("Enter 3: Retrieve records with a given data")
    print("Enter 4: Retrieve records with a given range of key values")
    print("Enter 5: Destroy the database")
    print("Enter 0: Quit (Please Destroy database before quitting) ")
    
    selection = int(input("What would you like to do?"))
    return selection

def selection():
    print("Please enter 6 to go back to main menu to do a task")
    selection = int(input("What would you like to do?"))
    return selection


while ((structuretype != "btree") || (structuretype != "hash") || (structuretype != "indexfile")) {
    clear()
    print("Please input 'btree', 'hash', or 'indexfile'")
    structuretype = input("Please input what structure type u would like to make & test: ")    

    }

select = main_menu()
while select!=0:
    if select==1:
        clear()
        print('Create and populate a database')
        select=selection()
        while select!=6:
            clear()
            print('Have to be in the Main Menu to choose different application.\
')
            select=selection()
    elif select==2:
        clear()
        print('Retrieve records with key')
        searchkey()
        select=selection()
        while select!=6:
            clear()
            print('Have to be in the Main Menu to choose different application.\
')
            select=selection()
    elif select==3:
        clear()
        print('Retrieve records with data')
        select=selection()
        while select!=6:
            clear()
            print('Have to be in the Main Menu to choose different application.\
')
            select=selection()
    elif select==4:
        clear()
        print('Retrieve records with range of key values')
        select=selection()
        while select!=6:
            clear()
            print('Have to be in the Main Menu to choose different application.\
')
            select=selection()    
            
    elif select ==5:
        clear()
        print("Destroy database")
        select = selection()
        while select !=6:
            clear()
            print('Have to be in the main menu to choose different application.')
            select = selection()
    
    elif select==6:
        clear()
        select=main_menu()
                    
    elif select>6:
        clear()
        print('You have selected an invalid option. Please try again')
        select=main_menu()







