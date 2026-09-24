### logical operator = evaluate multiple conditions (or. and, not)
#                 or = at least one condition must be true
#                and = both conditions must be true
#                not = inverts the condition (not False, not True)

# use or
# yaum = input("enter the day: ")
# wakt = input("enter the time(morning, noon, afternoom, night): ")

# if yaum in ('friday', 'saturday', 'sunday') or wakt == "afternoon":
#     print("this is a rest/recovery time")
# elif wakt == 'morning':
#     print("this time is obligated to learn")
# else: 
#     print("do all you're jobs")


# use and
# day = input('enter a day: ').lower()
# time = input("what's time now (breakfaast, lunch, dinner): ").lower()

# if day == 'friday' or time == 'breakfast':
#     print("the special menu now is Fried Rice")
# elif day == 'monday' and time == 'dinner':
#     print("the special menu now is chicken opor")
# elif day == 'thursday' and time == 'dinner':
#     print("the special menu now is pecel lele")
# else:
#     print("all menus as usual")

# use not
student = True
member = False

if student and member:
    print("please, u able to enter this room")
elif student and not member:
    print("u must pay for it!")
elif not student or not member:
    print("you can't join this club")
else:
    pass
    