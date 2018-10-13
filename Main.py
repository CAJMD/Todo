TodoList = {}

def PrintTodoList():
    for Priority, Todo in sorted(TodoList.items()):
        print (Todo, Priority)


def GetTodoTask():
    Todo = input ("What do you want to do now? ")
    Priority = input ("Rank this task by importance:")
    return Todo, Priority


def AddTodoTaskToList():
    TodoList[Priority] = Todo

while True:
    PrintTodoList()
    Todo, Priority = GetTodoTask()
    if Todo == 'stop':
        break
    else:
        AddTodoTaskToList() 
        
