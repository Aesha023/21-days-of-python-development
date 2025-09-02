def greet():
    print("Hello!!")
    print("It's your Assistant.")
    print("Nice to meet you!!")
greet()

#Functions that allows for inputs

def greet_with_name(name):
    print(f"Hello!! {name}.")
    print(f"What are you doing,{name}?")
greet_with_name("Aniyaa")

#quiz
def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")


life_in_weeks(56)