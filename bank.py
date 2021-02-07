import os
import pathlib
from tabulate import tabulate
import pickle


class Account :
    accNo = 0
    name = ''
    deposit = 0
    type = ''
  
    def createAccount(self):
        self.accNo = int(input("\nEnter the account no : "))
        self.name = input("Enter the account holder's name : ")
        self.type = input("Enter account type <Current(C) / Savings(S)> : ")
        self.deposit = int(input("Enter initial amount --> Savings (>=500) and Current (>=1000) : "))

        print("\n--> Account Created...")


def intro():
    print("\n")
    print("*****************************************************************")
    print("||                                                             ||")
    print("||                                                             ||")
    print("||                                                             ||")
    print("||                R  O  Y  A  L     B  A  N  K                 ||")
    print("||               ------------------------------                ||")
    print("||                                                             ||")
    print("||                                                             ||")
    print("||                                                             ||")
    print("*****************************************************************")

    input()


def create_new_account():
    account = Account()
    account.createAccount()
    create_new_accountsFile(account)
    

def balance_enquiry(num): 
    file = pathlib.Path("accounts.data")
    found = False

    if file.exists():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
    
        for item in mylist :
            if item.accNo == num : 
                print(f"\n--> Account Number : {item.accNo}\t\tName : {item.name}\t\tAccount Type : {item.type}\tAccount Balance : {item.deposit}")
                found = True
    else :
        print("--> No Records Found")
    if not found :
        print("--> No Existing Account.")


def update_account(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accNo == num :
                item.name = input("Enter Account holder's name : ")
                item.type = input("Enter the Account Type : ")
                item.deposit = int(input("Enter the Amount : "))

        print(f"\n--> Account of {item.name} with Account Number : {item.accNo} updated.")

        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


def deposit_withdraw(num1, num2): 
    file = pathlib.Path("accounts.data")
    
    if file.exists():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        
        for item in mylist :
            if item.accNo == num1 :
                
                if num2 == 1 :
                    amount = int(input("Enter depositing amount : "))
                    item.deposit += amount
                    print(f"\n--> Amount Deposited in {item.name}'s account with Account Number : {item.accNo}")
                
                elif num2 == 2 :
                    amount = int(input("Enter withdrawing amount : "))
                    if amount <= item.deposit :
                        item.deposit -= amount
                        print(f"\n--> {item.name}'s remaining amount : {item.deposit}.")
                    else :
                        print(f"\n--> You can only withdraw {item.deposit} amount.")
            
    else:
        print("\n--> No Records Found.")

    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


def display_all_accounts():

    list_all_records = []

    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            list_all_records.append([item.accNo, item.name, item.type, item.deposit])

        print("\n")
        print(tabulate(list_all_records, headers = ["Account", "Name", "Type", "Deposit"]))
        infile.close()
        
    else :
        print("\n--> No Records Found.")
        
    
def delete_account(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accNo != num :
                newlist.append(item)
        
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
        print(f"\n--> Account Number : {item.accNo}, deleted.")
      

def create_new_accountsFile(account) :   
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    

ch = ''
num = 0
intro()
    
while ch != 8:
    print("\n\n------ MAIN MENU ------\n")
    print("1. Create New Account")
    print("2. Balance Enquiry")
    print("3. Update Account")
    print("4. Deposit Amount")
    print("5. Withdraw Amount")
    print("6. List All Accounts")
    print("7. Close Account")
    print("8. EXIT\n")
    print("--> Please Select (1-8) : ", end = "")
    ch = input()
    
    if ch == '1':
        create_new_account()

    elif ch == '2':
        num = int(input("\nEnter Account No. : "))
        balance_enquiry(num)

    elif ch == '3':
        num = int(input("\nEnter Account No. : "))
        update_account(num)

    elif ch =='4':
        num = int(input("\nEnter Account No. : "))
        deposit_withdraw(num, 1)
    
    elif ch == '5':
        num = int(input("\nEnter Account No. : "))
        deposit_withdraw(num, 2)
    
    elif ch == '6':
        display_all_accounts()
    
    elif ch == '7':
        num =int(input("\nEnter Account No. : "))
        delete_account(num)
    
    elif ch == '8':
        print("--> T H A N K  Y O U ")
        exit()
    
    else :
        print("--> Invalid choice")




    
    
    
    
    
    
    
    
    
    
