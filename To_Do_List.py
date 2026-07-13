print("Welcome to your to do list")

all_task = []
right_options = ["1","2","3","4","5"]


while True:

    print("1: Add task")
    print("2: Show task")
    print("3: Delete task")
    print("4: Exit")

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
                print(f"Task {all_task} added successfully")

            # Show all task

        elif user_selection == "2":
            if not all_task:

                print("Your To-Do List is completely empty")
            
            else:
                for index,task in enumerate (all_task, 1):
                    print(f"{index}. {task}")
                   
            
        elif user_selection == "3":
            remove_task = input("Please select the Task that you want to delete: ")

            for inde,task in enumerate (all_task,1):
                all_task.pop()

                

        
        elif user_selection == "4":
            break
    else:
        print("Invalid option")