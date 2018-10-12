TodoList = []

def PrintTodoList():
    for Todo in TodoList:
        print (Todo)


def GetTodoTask():
    Todo = input ('What do you want to do now? ')
    return Todo


def AddTodoTaskToList():
    TodoList.append(Todo) 

while True:
    PrintTodoList()
    Todo = GetTodoTask()
    if Todo == 'stop':
        break
    else:
        AddTodoTaskToList() 
        
