import users,owner
from pwinput import pwinput as take_pass

def owner_login():
    _pass_w = "Rest@123" 
    pwd = take_pass(prompt = "\n---->> Enter Password :- ")
    while pwd != _pass_w:
        print("\nIncorrect Password !!!\n")
        pwd = take_pass(prompt = "\n---->> Enter Password :- ")
        
    print("\n-------------------/// LOGGED IN SUCCESSFULLY ///------------------------\n")

print("\n","-"*52,"\U0001F600 WELCOME TO PARADISE RESTAURANT \U0001F600","-"*52)
print('\n1. Press 1 for Organisational User. \U0001F9D1')
print('2. Press 2 for Customer User. \U0001F9D1')
inp = int(input("\nYour Choice -->> "))
while inp != 1 and inp != 2:
    print("\nPlease Enter Correct Reference !!!")
    inp = int(input("Your Choice -->> "))
    
if inp == 1:
    owner_login()
    owner.task()
    print("\n\nExiting The Window ...............")
elif inp == 2:
    users.customer()
    print("\n{}>> THANK YOU VISIT AGAIN !! <<{}\n".format("-"*32,"-"*32))