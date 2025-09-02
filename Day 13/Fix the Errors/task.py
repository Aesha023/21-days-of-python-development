try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed wrong input.Try in numerical way.")
    age = int(input("How old are you?"))


if age > 18:
    print(f"You can drive at age {age}.")
else:
    print(f"You can't drive because you are not old enough to drive.You are just {age} years old.")


# try:
#     print(6 > "five")
# except TypeError:
#     print("You can't mix integers and strings in a comparison")