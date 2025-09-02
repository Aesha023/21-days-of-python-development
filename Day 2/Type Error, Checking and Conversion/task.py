len("Hello")

print(type("Helllo"))
print(type(1234))
print(type(123.456))
print(type(True))

print( int("123") + int("456"))

#Make this line of code run without errors
#print("Number of letters in your name: " + len(input("Enter your name")))

name_of_the_user = input("Enter your name:")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: "))#str
print(type(length_of_name))#int

print("Number of letters in your name: " + str(length_of_name) )
#we convrted int into str by using str()
