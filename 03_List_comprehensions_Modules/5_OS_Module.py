import os

os.mkdir("os_exercises")

x = input("Write something: ")
with open("exercise.py", "w") as f:
    f.write(x)

x = input("Write something: ")
with open("exercise.py", "w") as f:
    f.write(x)

with open('exercise.py', 'r') as f1:
    with open('exercise2.py', 'r' ) as f2:
        print(f1.read() + f2.read())