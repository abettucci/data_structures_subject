userData= {}
userData["name"]=input("Insert your name and last name: ")

# start infinite loop until correct role will be entered
while True:
    role=input("What is your role? \nA) Professor \nB) Student\n").upper()
    if role == 'A':
        userData["role"] = "Professor"
        break
    elif role == 'B':
        userData["role"] = "Student"
        break
    else:
        print(f"{role} is incorrect role. Please enter correct role A or B")
        continue

print(userData)