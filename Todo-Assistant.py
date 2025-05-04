#World's best todo-list assistant by LB23! 2025

todos = []
mainerror = "Invalid entry. Please try again!"
error = "Invalid entry, please type Y or N."
exit = "You may now exit the program."
save_msg = "File successfully saved as: "
no_todos = "No todos yet! Try adding or load existing list!"

def val_error():
    print("Please enter a valid number.")

def show_todos():
    if not todos:
        print(no_todos)
    else:
        for i, task in enumerate(todos):
            status = "✅" if task["done"] else "❌"
            print(f"{i + 1} - {task['task']} [{status}]")

def update_history(filename):
    try:
        with open(".history.txt", "r") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        lines = []

    #adds file to the top of list.
    if filename in lines:
        lines.remove(filename)
    lines.insert(0, filename)

    #limits file to 5 lines.
    lines = lines[:5]

    with open(".history.txt", "w") as f:
        for line in lines:
            f.write(line + "\n")

#mainmenu
while True:
     print("\n--- LB23 TODO MENU ---")
     print("[1] Add new item todo.")   
     print("[2] Delete existing item todo.")
     print("[3] Show what todo.")
     print("[4] Save Todo-list.")
     print("[5] Load Todo-list.")
     print("[6] Edit Todo status")
     print("[7] Exit.")

     main_sel = input("What do you want to do now?: ")

     if main_sel == "1": #Add new item todo.
        while True:
            item = input("What do you want to add to your todo list? (Type 'done' to finish): ")
            if item.lower() == "done":
                break
            todos.append({"task": item, "done": False}) 
            print(f'"{item}" added to your todo list! ✔️')
   
     elif main_sel == "2": #Delete existing item todo.
        for i, task in enumerate(todos):
            status = "✅" if task["done"] else "❌"
            print(f"{i + 1} - {task['task']} [{status}]")
        try:
            number = int(input("What number do you want to delete?: "))
            if 0 < number <= len(todos):   
                deleted_task = todos[number - 1]
                del todos[number - 1]
                print(f"Task '{deleted_task}' has been deleted.")
            else:
                print("Invalid number. No task deleted.")
        except ValueError:
            val_error()

     elif main_sel == "3": #Show what todo.
        show_todos()

     elif main_sel == "4": #Save todo-list.
        print("OK, let's save!")
        save_filename = input("Enter filename to save as: ")
        if not save_filename.endswith(".txt"):
            save_filename += ".txt"
        with open(save_filename, "w") as file:
             for task in todos:
                  file.write(task["task"] + "\t" + str(task["done"]) + "\n")
        print(save_msg + save_filename)
     
     elif main_sel == "5": #Load todo-list.
        history = []
        print("Recent files: ")
        try:
            with open(".history.txt", "r") as f:
                history = f.read().splitlines()
                if not history:
                    print("(No recent files)")
        except FileNotFoundError:
            pass

        for idx, file in enumerate(history):
            print(f"{idx+1} - {file}")

        choice = input("Choose a file number or enter filename to load: ")
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(history):
                load_filename = history[index]
            else:
                print(mainerror)
                continue
        else:
            load_filename = choice
            if not load_filename.endswith(".txt"):
                load_filename += ".txt"
             
        try:
            todos.clear()
            with open(load_filename, "r") as file:
                    for line in file:
                        task, done = line.strip().split("\t")
                        todos.append({"task": task, "done": done == "True"})
            print("Todo list loaded!")
            show_todos()

            update_history(load_filename)
        except FileNotFoundError:
            print("File not found. Please check the name and try again.")

     elif main_sel == "6": #Status editing.
          print("\nWhich task status do you want to toggle?")
          show_todos()
          try:
              number = int(input("Enter the task number to toggle status: "))
              if 0 < number <= len(todos):
                  todos[number - 1]["done"] = not todos[number - 1]["done"]
                  print(f"Status updater for: {todos[number - 1]['task']}")
              else:
                  print(mainerror)
          except ValueError:
              val_error()
              
     elif main_sel == "7": #Exit.
          print(exit)
          break
     else:
          print(mainerror)

