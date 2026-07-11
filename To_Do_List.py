print("Welcome to your to do list")

all_task = []
right_options = ["1","2","3","4","5"]


while True:

    print("1: Add task")
    print("2: Show task")
    print("3: Mark as completed")
    print("4: Delete task")
    print("5: Exit")

    user_selection = input("Choose an option: ")

    if user_selection in right_options:
        if user_selection == "1":
            add_task = input("Add a task: ")
            add_date =input("Add deadline date: ")
            if add_task !="" and add_date != "":
                all_task.append({"Task":add_task,
                                 "Date":add_date,
                                 "Completed":False
                                 })

        elif user_selection == "2":
            print(all_task)
        
        elif user_selection == "3":
            ...
        elif user_selection == "4":
            ...
        elif user_selection == "5":
            break
    else:
        print("Choose a right option")