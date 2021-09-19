# comment


"""
multi
line
comment
"""


print("Hello World!!!")


# variables

name = "Cameron"
age = 99
total = 123.21
found = False
names = []

print(age * 2)
print(total / 10)

if (age < 100):
    print("you aren't all that old")
    print("just kidding")
elif(age == 100):
    print("you're riding the line, pal")
else:
    print("you're old as dirt!")


def hello():
    print("Hello There")
    print("I'm a function")


def play(num):
    print("Your number:")
    print(num)

    if(num < 5):
        print("not quite pal")


hello()
hello()

play(5)
