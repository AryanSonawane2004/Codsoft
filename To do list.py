# programming logic:

# 1) create options for to do list like:
# add
# view 
# delete
# quit
# 2) define addTasks method
# 3) define listTasks method
# 4) define deleteTasks method
# 5) implement

tasks = []

def addTasks():

    task = input("Enter your Task:")
    tasks.append(task)
    print(f" Task {task} is successfully added !!")

def listTasks():

    if not tasks:
        print("your tasks is currently not present")
    else:
        print("Current Tasks:")
        for i, task in enumerate(tasks):
            print(f"Task #{i}. {task}")

def deleteTasks():

    taskToDelete = int(input("Please enter your choice"))
    if taskToDelete >= 0 and taskToDelete < len(tasks):
        print(f"Task #{taskToDelete} is deleted successfully")
    else:
        print("Invalid input !!")


while True:
    print("\n")
    print("Welcome to the to do list python project ")
    print("Please select among following:")
    print("1.Add")
    print("2.View")
    print("3.Delete")
    print("4.Quit")
    
    choice = int(input("Enter your Choice:"))

    if choice == 1:
        addTasks()
    elif choice == 2:
        listTasks()
    elif choice == 3:
        deleteTasks()
    elif choice == 4:
        print("Goodbye!!")
    else:
        print("Invalid Input!!")
