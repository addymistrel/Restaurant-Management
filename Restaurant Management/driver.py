import users,owner

def owner_login():
    _pass_w = "Rest@123" 
    pwd = input("\n---->> Enter Password :- ")
    while pwd != _pass_w:
        print("\nIncorrect Password !!!\n")
        pwd = input("---->> Enter Correct Password :- ")
        
    print("\n**************** LOGGED IN SUCCESSFULLY *******************\n")

print("\n","-"*52,">> WELCOME TO PARADISE RESTAURANT <<","-"*52)
print('\n1. Press 1 for Organisational User.')
print('2. Press 2 for Customer User.')
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