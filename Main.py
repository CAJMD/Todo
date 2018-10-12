TodoList = []
while True:
    for Todo in TodoList:
        print (Todo)
    Todo = input ('What do you want to do now? ')
    print('Todo List', Todo)
    if Todo == 'stop':
        break
    else:
        TodoList.append(Todo)    