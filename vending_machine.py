def Restock(available_sodas): #available_sodas is synonymous with the soda_list array
    valid_name=False
    restocking=True
    stop_options=['n','no']
    affirm_options=['y','yes']
    while 
        restocking==True:
        quit_status1=""
        quit_status2=""
        name_quit_status=False
        restocking_quit_status=False
        while valid_name==False and name_quit_status==False:
            restock_name=input('Please select the soda you would like to restock.: ')
            for name_options in range(len(available_sodas)):
                updated_quantity=available_sodas[name_options][3] #index of the available quantity
                if restock_name.lower()==available_sodas[name_options][0]:
                    valid_name=True

            if not valid_name==True:    
                print('The soda you have named is not available to be restocked. Select another option.')
                quit_status1=input("Or, press 'Q' to quit.")
                if quit_status1.lower()=='q':
                    name_quit_status=True
                    restocking=False
                    break
        while restocking_quit_status == False:            
            restock=input('Please enter the quantity of sodas that are being added for the '+restock_name+' soda.: ')
            if type(restock) == int and restock > 0 and restock <= 100: # must be a reasonable integer value being restocked
                    updated_quantity=updated_quantity+restock
                    print('The '+restock_name+' soda has been restocked by '+restock+'. Thank you.')
                    valid_response=False
                    while valid_response==False:
                        still_stocking=input("Would you like to restock another soda? Y/N: ")
                        if still_stocking.lower() in stop_options:
                            valid_response=True
                            restocking_quit_status=True
                            restocking=False
                            print('Have a nice day!')
                            break
                        elif still_stocking.lower() in affirm_options:
                            valid_response=True
                            valid_name=False
                            restocking_quit_status=True
                        else:
                            print('Please make a valid selection.')

                else:
                    print('The number you have selected is not in range. Please try again.')
                    quit_status2=input("Or, press 'Q' to quit. ")
                    if quit_status2.lower()=='q':
                        restocking_quit_status=True
                        restocking=False
                        break

        else:    
            print("Please enter a valid quantity for restock.")
            
        
    return available_sodas

        

#assuming that each object instantiated within the Soda Class has a type as follows (forgot how JSON goes kinda):
class "Soda": { 
    "name": str,
    "desc": str,
    "cost": float,
    "quant_available": int
 } 

#soda_list is the array containing all of the JSON objects
soda_list = [['Fizz', 'An effervescent fruity experience with hints of grape and coriander.',1.00,100],
['Pop', 'An explosion of flavor that will knock your socks off!', 1.00, 100],
['Cola', 'A basic no nonsense cola that is the perfect pick me up for any occasion.', 1.00, 200],
['MegaPop','Not for the faint of heart. So flavorful and so invigorating, it should probably be illegal.',1.00, 50]

#accept user input
available = False
while available == False:
    quit_status=""
    #assuming the front-end will have the names of the sodas, so I'm not putting them in the input string
    choice = input('Please make a selection from the available options.')
    for soda_name in range(len(soda_list)):
        if choice == soda_list[soda_name][0]:
            stock = soda_list[soda_name][3] #quantity available
            if not stock==0:
                price = soda_list[soda_name][2] #cost
                available = True
                more_info_choice = False
                affirm_array = ['y','yes']
                decline_array = ['n','no']
                while more_info_choice == False:
                read_desc=input('You have selected '+choice+'. Would you like to see its description? Y/N: ')
                    if read_desc.lower() in affirm_array:
                        more_info_choice=True
                        desc_declined=False
                        print(soda_list[soda_name][1])
                    elif read_desc.lower() in decline_array:
                        more_info_choice=True
                        desc_declined=True
                        
                    else:
                        print('You have not selected a valid option. Try again.')
                confirmed=False
                if desc_declined==True:
                    confirmed=True
                else:  #some people might not want to proceed when they hear that coriander is in that Fizz one lol
                    proceed=input('Would you like to proceed with the transaction? Y/N: ')
                while confirmed==False:
                    if proceed.lower() in affirm_array:
                        confirmed=True
                        print('Please deposit the required amount of '+price+' dollar US.')
                        stock-=1 #decrement of available quantity  
                        break #should break out of the original for loop when the transaction has been completed  
                    elif proceed.lower() in decline_array:
                        confirmed=True
                        print('Have a nice day!')
                        break #should break out of the original for loop when the transaction has been completed
                    else:
                        print('Confirmation to continue has not been received.')

            else:
                print('The soda you have chosen is not in stock at the moment. Please choose another.')
                    
    if not available == True:
        acceptable_response=False
        while acceptable_response==False:
            print('You have chosen an invalid option. Please make a different selection.')
            perform_restocking=False
            maintenance=input('Or, if you have sufficient admin privileges, you may restock selected items. Y/N :')
            if maintenance.lower() in stop_options:
                acceptable_response=True
            elif maintenance.lower() in affirm_options:
                acceptable_response=True
                bad_creds=True
                while bad_creds==True:
                    uname=input('Enter the admin username.: ')
                    password=input('Enter the admin password.: ')
                    if uname = 'admin' and password='pass':
                        bad_creds=False
                        Restock(soda_list)
                    else:
                        print('You have entered either the username or password incorrectly. Please try again.')
                        quit_status=input("Or, press 'Q' to cancel. ")
                        if quit_status.lower()=='q':
                            break
                    
            else:
                print('Please make a valid selection.')

    