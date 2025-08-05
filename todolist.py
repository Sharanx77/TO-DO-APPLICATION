import os
print("TO DO LIST APPLICATION")
f=open("todolist.txt",'w')
todolist=[]
def add_task(task):
    todolist.append(task)
    print(f'Task {task} added to the list')
print("Welcome to the 'TO DO APPLICATION'")
op='yes'
while op=='yes':
    n=1
    task=input("Enter the task to be added to the list:")
    add_task(task)
    op=input("Do you want to add any task to the list? (yes/no):").lower()
for i in todolist:
    f.write(f"{n}.{i}\n")
    n+=1
n=1
f.close()
print("your tasks have been saved to todolist.txt file")
print("You can check the tasks in the todolist.txt file")
print("Thank you for using the 'TO DO APPLICATION'")