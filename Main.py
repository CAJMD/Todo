TodoList = {}

def TopThreeItems ():
    for Priority in range (1,4,1):
        # print (Todo,Priority)
        print (TodoList.get(Priority))


def PrintTodoList():
    for Priority, Todo in sorted(TodoList.items()):
        print (Todo, Priority)


def GetTodoTask():
    Todo = input ("What do you want to do now? ")
    return Todo

def GetTodoTaskPriority():
    Priority = input ("Rank this task by importance:")
    return int(Priority)

def AddTodoTaskToList():
    TodoList[Priority] = Todo

while True:
    PrintTodoList()
    Todo = GetTodoTask()
    if Todo == 'stop':
        print ("This is your top three thing you MUST do!\n")  
        TopThreeItems()
        break
    else:
        Priority = GetTodoTaskPriority()
        AddTodoTaskToList() 
        
