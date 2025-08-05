import os
todolist=[]
print("Welcome to the To-Do List App!")
def display_tasks():
    if not todolist:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, task in enumerate(todolist, start=1):
            print(f"{index}. {task}")           
def add_task():
    task = input("Enter a new task: ")
    todolist.append(task)
    print(f"Task '{task}' added to your to-do list.")
def remove_task():
    display_tasks()
    if todolist:
        try:
            task_number = int(input("Enter the task number to remove: "))       
            if 1 <= task_number <= len(todolist):
                removed_task = todolist.pop(task_number - 1)
                print(f"Task '{removed_task}' removed from your to-do list.")   
            else:
                print("Invalid task number. Please try again.") 
        except ValueError:
            print("Invalid input. Please enter a number.")
def save_tasks():
    with open("todolist.txt", "w") as file:
        for task in todolist:
            file.write(task + "\n") 
    print("Your to-do list has been saved to 'todolist.txt'.")
print("what would you like to do?")
print("1.display tasks \n 2.add task \n 3.remove task \n4. save tasks \n5.exit")
while True:
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        display_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        save_tasks()
    elif choice == '5':
        print("Exiting the To-Do List App. Goodbye!")
        break
    
