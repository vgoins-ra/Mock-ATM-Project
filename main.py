# Project 1 - Mock ATM
import datetime as dt
import random

userBalance = 0
curBalance = 0
response = False
userAcct = ""

# Create dictionary
acct_dict = {'Jane': ['passJane', "250987", 1000, 'jane@gmail.com'], 'John': ['passJohn', "987567", 1000,'john@gmail.com'], 'Paul': ['passPaul','987602', 1000, 'paul@gmail.com']}
#Get user balance
userName = input("Enter your name: ")
Password = input("Please enter your password: ")

#Login function using bank_dict
def Login():
    do_exist = False
    userBalance = 0
    
    for key, value in acct_dict.items():
        if(key == userName and Password == value[0]):
          userBalance = value[2]
          #Print the date and Time and welcme user
          today = dt.datetime.now()
          print("Date:", today.strftime("%c"))
          print()
          print("Welcome %s!" % userName)
          print()
          do_exist = True
          menu()
        else:
            do_exist = False
            return do_exist
            


#define menu of options
def menu():
    print("These are the available options:")
    print("1. Withdrawal")
    print("2. Cash Deposit")
    print("3. Complaint ")
    print("4. Exit Program" )
    print() 
    Options()

def Options():
  selectedOption = 0
  while (selectedOption != 4):
    selectedOption = int(input("Please select an option: ")) 
    #while selectedOption != 4: 
    for key, value in acct_dict.items():
        if(key == userName and Password == value[0]):
          userBalance = value[2]

    curBalance = 0.0     
    if (selectedOption == 1):
        print()
        currency_string3 = "${:,.2f}".format(float(userBalance))
        print("Your current balance: %s" % currency_string3 )
        print()
      #Ask user: How much would you like to withdraw
        withdraw = input("How much would you like to withdraw? ")
        print()  
        curBalance = float(userBalance) - float(withdraw) 
        acct_dict[2] = str(curBalance)  
                
        currency_string1 = "${:,.2f}".format(float(withdraw))
        currency_string2 = "${:,.2f}".format(float(curBalance))
        
        print("Withdrawing: %s" % currency_string1)
        print("Your new balance: %s" % currency_string2 )
        print()
        print("Please take your cash.")
        print()
        
      #Return to main menu
        selectedOption = 0
        menu()
      #selectedOption = int(input("Please select an option: "))
    elif (selectedOption == 2):
          #ask how much to deposit
          print()     
          currency_string4 = "${:,.2f}".format(float(userBalance))
          print("Your current balance: %s" % currency_string4 )
          print()
          deposit = input("How much would you like to deposit? ")
          currency_string5 = "${:,.2f}".format(float(deposit))
          print("Depositing: %s" %currency_string5)
          print()   

          curBalance = float(userBalance) + float(deposit)
          currency_string6 = "${:,.2f}".format(float(curBalance))
          print("Your new balance:%s" % currency_string6)
          print()
          menu()
          #selectedOption = int(input("Please select an option: "))

    elif(selectedOption == 3):
          #What issue will you like to report? 
          complaint = input("What issue will you like to report?")
          # output "Thank you for contacting us"
          print()
          print( "Thank you for contacting us")
          print("Customer Service will be contact you within 3 working days.")
          print()
          menu()
          

    elif(selectedOption == 4):
          print()
          print("**** Thanks for banking with us. ****")
          print()
          #selectedOption = 0
          break
          
    else:
          print()
          print("Invalid option selected, please try again")
          menu()

def newAccount():
  random_number = random.randint(1000000, 9999999)
  return (random_number)

 # Append multiple values for a new key 'here'

# Append multiple value to a key in dictionary
def add_values_in_dict(sample_dict, key, list_of_values):
    """Append multiple values to a key in the given dictionary"""
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict

def Register():
  #acct_dict = {'Jane': ['passJane', "250987", 1000, 'jane@gmail,classmethod'], '
  userName = input("Please enter your name: \n")
  Password = input("Please create your password: \n")
  myAcct = str(newAccount())
  userEmail = input("What is your email address: \n")
# Append multiple values for a new key 'here'
  add_values_in_dict(acct_dict, userName + ":", [Password, myAcct, userEmail])
  print()
  print('Contents of the dictionary: ')
  print(acct_dict)
   
 
response = Login()

if(response == True):
  menu()
  Options()
else:
  print()
  choice = ""
  choice = input("Would you like to set up an account?" "1 = yes 2 = no  " )
  print()
  if(choice == "1"):
    Register()
  
  #print(acct_dict)
  
  