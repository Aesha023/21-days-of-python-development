# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")


#Functions with more than 1 input

def greet_with(name,location):
    print(f"Hey, {name}")
    print(f"What it is like in {location}?")

greet_with("Angelena","USA")
greet_with("USA" , "Angelena") #it's called positional arguments

greet_with(location="USA" , name= "Angelena") #It's called keyword arguments

#quiz
def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(score)


calculate_love_score("Aesha Patel", "Kim Taeyung")