import time
print("Please insert Your CARD")
time.sleep(5)
password = 852
pin=int(input("enter your atm pin"))
balance = 100

if pin==password:
    while True:
    
        print("""
        1 == balance
        2 == withdraw balance
        3 == deposite balance
        4 == exit
        """
        )
        try:
            option=int(input("Please Enter Your Choise"))
        except:
         print("Please Enter Valid Option")
        
        if option==1:
            print(f"Your current balance is {balance}")
        
        if option==2:
            withdraw_amount = int(input("please enter withdraw_amount"))
            balance = balance - withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"your current balance is {balance}")
        
        if option==3:
            deposite_amount = int(input("please enter your deposite_amount"))
            balance = balance + deposite_amount
            print(f"{deposite_amount} is credited to your account")
            print(f"your current balance is {balance}")

        if option==4:
            break
    else:
        print("wrong pin please try again")