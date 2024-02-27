import os
from brute_forcer import BruteForcer
from colorama import  Style, Fore

# Name of the User and Password lists
users_file_name = "usernames.txt"
passwords_file_name = "passwords.txt"
    
   
def menu_header():
    print(Style.BRIGHT + Fore.GREEN)
    print("*******************************************************")
    print("*                                                     *")
    print("*       Bruteforcer v1.0 by Franco Joaquin Zini       *")
    print("*     Coded to only be used on Portswigger's Lab.     *")
    print("*                                                     *")
    print("*******************************************************")
    print(Style.RESET_ALL)

def menu_body(bf):
    print("Current LOGIN URL: " + Fore.LIGHTBLUE_EX + (bf.url if bf is not None else "None") + Style.RESET_ALL)
    print("\n[1] Enter login URL")
    print("[2] Find valid user")
    print("[3] Perform brute force attack")
    print("[4] Print results")
    print("[5] Save credentials in a JSON file")
    print("[6] Exit")

def enterURL_option():
    url = input("\n>>> Please enter the login URL: ")
    return BruteForcer(url, users_file_name, passwords_file_name)
 

def find_username_option(bf):
    #Proceed only if a URL has been provided.
    if bf is not None:
        bf.find_valid_usernames()
        if len(bf.valid_usernames) > 0:
            print(Style.BRIGHT + Fore.GREEN + f"\n-> Valid usernames: {', '.join(bf.valid_usernames)}" + Style.RESET_ALL)
        else:
            print(Style.BRIGHT + Fore.RED + "\nNo username has been found." + Style.RESET_ALL)
    else:
        print(Fore.LIGHTRED_EX + "\nPlease provide the login URL first." + Style.RESET_ALL)
    input("\n>>> Press ENTER to continue...")
        
        
def brute_force_option(bf):
    #Proceed only if a URL has been provided.
    if bf is not None:
        #Proceed only if at least one user name has been found
        if len(bf.valid_usernames) > 0:
            bf.find_valid_passwords()
            print(Style.BRIGHT + Fore.GREEN + f"\n-> Passwords found: {', '.join(bf.valid_passwords)}" + Style.RESET_ALL)
        else:
            print(Style.BRIGHT + Fore.RED + "\nNo username has been found yet. Try using [2]OPTION to find one." + Style.RESET_ALL)
    else:
        print(Fore.LIGHTRED_EX + "\nPlease provide the login URL first." + Style.RESET_ALL)
    input("\n>>> Press ENTER to continue...")
    
    
def output_results(bf):
    valid_usernames = bf.valid_usernames
    valid_passwords = bf.valid_passwords
    print(f"\n-> Valid usernames: {Fore.LIGHTGREEN_EX} {', '.join(valid_usernames)} {Style.RESET_ALL}")

    if len(valid_passwords) > 0:
        print(f"-> Passwords found: {Fore.LIGHTGREEN_EX} {', '.join(valid_passwords)} {Style.RESET_ALL}")

        print("\n***********************************************************************\n\nCredentials found: ")
        credentials = [f"user: {Fore.LIGHTGREEN_EX}\'{username}\'{Style.RESET_ALL}, password: {Fore.LIGHTGREEN_EX}\'{password}\'{Style.RESET_ALL}" for username, password in zip(valid_usernames, valid_passwords)]

        for credential in credentials:
            print(f"- {credential}")
        print("\n***********************************************************************")
    else:
        print("\nNo passwords found yet")
        
            
def print_results_option(bf):
    #Proceed only if a URL has been provided.
    if bf is not None:
        output_results(bf)
    else:
        print(Fore.LIGHTRED_EX + "\nPlease provide the login URL first." + Style.RESET_ALL)
    input("\n>>> Press ENTER to continue...")  
    
    
def save_file_option(bf):
    #Proceed only if a URL has been provided.
    if bf is not None:
        # Check if there is at least one valid username and password.
        if len(bf.valid_usernames) > 0 and len(bf.valid_passwords):
            filename = input("\n>>> Please enter the file name to save the credentials that were found:")
            bf.save_credentials(filename)
            print(f"\n{Fore.GREEN}Credentials written on: {filename}.{Style.RESET_ALL}")
        else:
            print(Fore.LIGHTRED_EX + "\nNo valid credentials to save." + Style.RESET_ALL)
    else:
        print(Fore.LIGHTRED_EX + "\nPlease provide the login URL first." + Style.RESET_ALL)
    input("\n>>> Press ENTER to continue...")

    
       
def menu():
    bf = None
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # clean the terminal
        
        menu_header()
        menu_body(bf)
        
        option = input("\nPlease, select an option: ")
        #OPTION 1 - Enter login URL
        if option == '1':
            bf = enterURL_option()
        #OPTION 2 - Find valid user
        elif option == '2':
            find_username_option(bf)
        #OPTION 3 - Perform brute force attack
        elif option == '3':
            brute_force_option(bf)
        #OPTION 4 - Print results 
        elif option == '4':
            print_results_option(bf)
        #OPTION 5 - Save credentials in JSON file
        elif option == '5':
            save_file_option(bf)
        #OPTION 6 - Exit  
        elif option == '6':
            break
        #INVALID OPTION
        else:
            print(Fore.LIGHTRED_EX + "\nInvalid option. Please try again." + Style.RESET_ALL)
            input("\n>>> Press ENTER to continue...")

if __name__ == "__main__":
    menu()