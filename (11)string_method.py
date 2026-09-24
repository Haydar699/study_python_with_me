### String Methods

name =  "haydar fatah"
phone_num  = 123

# result = len(name)
# result = name.find('a')
# result = name.rfind("a")
# name = name.capitalize()
# name = name.upper()
# name = name.isalpha() # must be continued
# name = name.isdigit()
# name = name.count("a")
name = name.replace("haydar", "Muh")

# print(name)

### Exercise to validate a username
#  the username is no more than 12 characters
#  the username must not contains space
#  the username must not contains digit


# username = input("create username: ")

# username.find(" ")
# username.isalpha()

# if len(username) > 12:
#     print("your username can't be more than 12 characters")
# elif not username.find(" ") == -1:
#     print("your username can't contain the space ")
# elif not username.isalpha():
#     print("your username can't contain the number")
# else:
#     print(f"Welcome {username} to ur account")

### exercise to validate email n password
#  the email must be contain '@' and '.'
#  the min character of password is 8 char

# email = input("create your email: ")

# if '@' not in email or '.' not in email:
#     print("the email must contain '@' and '.'")
# else:
#     print(f"OK next...")
    
#     password = input('create your secure password: ')

#     if len(password) < 8:
#         print("the password must more then 8 character")
#     elif password.isdigit():
#         print("the password can't be number only")
#     else:
#         print("welcome, the account is successfully")

### validate bioskop account
#       the username character must in range(6-15) char, and must not contain space
#       the minimum age is 13 years old

try: 
    usrnm = input("create the username: ")
    
    if len(usrnm) < 6 or len(usrnm) > 15:
        print("the username character must in range(6-15) char")
    elif not usrnm.find(" ") == -1:
        print("the username must not contain space")
    else:
        print("OK next...")
        
        age = int(input("how old are u? "))
        
        if age < 13:
            print("sorry, this is for 13 years and above")
        else:
            print("welcome, your Bioskop account is created")
            
except ValueError:
    print("Error: enter the number for age!")