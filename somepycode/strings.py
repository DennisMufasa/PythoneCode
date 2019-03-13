"""introducing python strings"""
name = " dennis"
# strings are mutable
print(name[1])
print('J'+name[2:])
print(name[2:5])
print(name[-1])  # last item on the list

# arranging strings
age = 10
career = "ps 4 gamer"
print("""Name    :       {}\nAge     :       {}\nCareer  :       {}
    """.format(name,age,career))

# string methods
print(name)
print(name.strip())  # removes white spaces before a string
print(name.lower())
print(name.upper())
print(name.replace('e', 'a'))
greeting = "Hello, World!"
print(greeting.split(','))
name2 = name.strip()
print(name2.capitalize())
print(name2.count('n'))

# capture strings from user
# username = input("Choose a username!")
# print("Hello, {}".format(username))



