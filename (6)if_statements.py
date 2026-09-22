# if =  do something if a condition is true
#       else do something else if the condition is false


### for integers and floats
grade = float(input('enter ur grade: '))
if grade >= 100:
    print(f"u're an amazing student!!!")
elif grade >= 80:
    print(f"u're got a good grade, keep it up!")
elif grade >= 60:
    print(f"u're got a passing grade, but u can do better!") 
else:
    print(f"don't worry, u can do better next time!")


### for string   
book = input('would u like this book?(y/n): ').lower().strip()
if book == 'y' or book == 'yes':
    print(f"this book for u")
elif book == 'n' or book == 'not':
    print(f"ok, maybe next time")
else:
    print('what do u mean bro???')
    
    
### for boolean
student = False
if student:
    print(f"u're a student")
else:
    print(f"u aren't a student")
    