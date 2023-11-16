import time as t
print("   FEDERAL BANK ATM   ")

user_balance = 100000
user_pin = 1234
while True:
    name = str(input("Enter Your Name :  "))
    print("Welcome ",name)
    pin = int(input("Enter User Pin : > "))
    if pin == user_pin:
          print("AUTHENTICATING.....")
          t.sleep(1)
          print("USER VERIFIED")
          break
        
    elif pin != user_pin:
        print("INVALID PIN!!\n Re-enter username and pin  ") 
       
  
    

while True:
        print("\n        1.CHECK BALANCE\n        2.WITHDRAW\n        3.DEPOSIT\n        4.EXIT")
        option = int(input("Select Option >>> "))

        if option == 4:
            
            print("Exiting.....")
            break
        elif option == 1:
            print("Your Bank Balance is ",user_balance)
            bblnce_optn = str(input("Do you Wish to continue (y/n) "))
            if bblnce_optn == 'y' or bblnce_optn == 'Y':
                print("")
                
            elif bblnce_optn == 'n' or bblnce_optn == 'N':
                print("Thank you")
                break
                
           
      

  
        elif option == 2:
         print("Your Bank Balance is ",user_balance)
         while True:
          w_draw = int(input("Enter Withdraw Amount : "))
         
          if w_draw > user_balance:
             print("no balance")
             
          else:
            cnfrm = str(input("Confirm(y/n)"))
            if cnfrm == 'y' or cnfrm == 'Y':
                user_balance = user_balance - w_draw
               
                
                print("Bank Balance is ",user_balance)
                wdrw_optn = str(input("DO you wish to withdraw again(Y/N)  "))
                if wdrw_optn == 'y' or wdrw_optn == 'Y':
                    print("")
                else:
                   
                    break
              
           
   
        elif option == 3:
            while True:
             deposit = int(input("Enter Deposit Amount : "))
             user_balance = user_balance + deposit
             
             print("Bank Balance is ",user_balance)
             dp_option = str(input("Do you wish to Deposit again..(y/n)"))
             if dp_option == 'y' or dp_option == 'Y':
                
                print("")
             else:
                break
    
    
        
    
