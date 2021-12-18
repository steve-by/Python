# typical function

# def my_function(str1, str2):
#     print(str1)
#     print(str2)

# my_function("This is str1", "This is str2")

# does not need conversion of number to text ie. str(age)
# def print_something(name, age): 
#     print("My name is", name, "and my age is", age)

# print_something("Steve", 57)

# function withdefault arguement

# will print Steve with unknown : if name and age are here
# then these will override "person" and "Unknown"
# No arguements will print "Person" and "Unknown"
# def print_something(name = "person", age = "unknown"): 
#     print("My name is", name, "and my age is", age)

# print_something("Steve") 

# function with keyword arguemets 
# Will override "person" and "unknown" the order in
# call is reversed, but is printed as in the function order
# def print_something(name = "person", age = "unknown"): 
#     print("My name is", name, "and my age is", age)

# print_something(age = 27, name = "Steve") 

# flexable arguments
# adds a number of people from a list of people - 5, 10, 50 people etc.
def print_people(*people):
    for person in people:
        print("This person is", person)

print_people("Steve", "Tom", "Abdul", "Kerion", "Asad")
