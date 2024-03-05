import os

while True:
    command = input()

    if command == "End":
        break

    action, file_name, *args = command.split("-")

    if action == "Create":
        open(file_name, "w").close()

    elif action == "Add":
        content = args[0]
        with open(file_name, "a") as f:
            f.write(f"{content}\n")

    elif action == "Replace":
        old_string = args[0]
        new_string = args[1]
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                content = f.read()
            with open(file_name, "w") as f:
                content = content.replace(old_string, new_string)
                f.write(content)
        else:
            print("An error occurred")

    elif action == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")
