my_tasks = []
while True:
    print("\n====================")
    print("      To-Do List")
    print("====================")
    print('Choose your operation')
    print('1. Add task')
    print('2. View tasks')
    print('3. Exit')
    print("====================")
    choose = input('Enter operation number: ')
    if choose == '1':
        task = input('Enter task details: ')
        if task.strip() == '':
                print('Empty task can not be create.')
        my_tasks.append(task)
        print('Task created successfully...')
        
    elif choose == '2':
        if len(my_tasks) == 0:
            print('No tasks found...')
        else:
            print('Your tasks')
            print("====================")
            for index,  task in enumerate(my_tasks, start=1):
                print(f"{index}. {task.capitalize()}")
        
    elif choose == '3':
        print('Thank you for choosing the To-Do list')
        break
    else:
        print('Invalid operation. Choose 1, 2 or 3')
   
    
    
    