import string
import random
 
# Getting password length
length = int(input("Enter password length: "))
 
print('''Choose character set for password from these : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')
 
characterList = ""
 
# Getting character set for password
while(True):
    option = int(input("Pick a number "))
    if(option == 1):
         
        # Adding letters to possible characters
        characterList += string.ascii_letters
    elif(option == 2):
         
        # Adding digits to possible characters
        characterList += string.digits
    elif(option == 3):
         
        # Adding special characters to possible characters
        characterList += string.punctuation
    elif(option == 4):
        break

    else:
        print("Invalid input!")
 
password = []
 
for i in range(length):
   
    # Picking a random character from our character list
    randchar = random.choice(characterList)
    password.append(randchar)
 
# printing password as a string
print("The random password is " + "".join(password))