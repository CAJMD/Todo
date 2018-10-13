TodoList = {}

def PrintTodoList():
    for Priority, Todo in sorted(TodoList.items()):
        print (Todo, Priority)


def GetTodoTask():
    Todo = input ("What do you want to do now? ")
    return Todo

def GetTodoTaskPriority():
    Priority = input ("Rank this task by importance:")
    return Priority


def AddTodoTaskToList():
    TodoList[Priority] = Todo

while True:
    PrintTodoList()
    Todo = GetTodoTask()
    if Todo == 'stop':
        break
    else:
        Priority = GetTodoTaskPriority()
        AddTodoTaskToList() 
        
