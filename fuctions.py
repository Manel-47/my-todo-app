FILEPATH = "todo.txt"

def get_todos(filepath=FILEPATH):
    """Read to do list in the file
    and return the full list."""

    with open(filepath, "r") as file:
       todos = file.readlines()
    return todos


def write_todos(todos, filepath= FILEPATH):
    """Write to do list in the txt file"""

    with open(filepath, "w") as file:
        file.writelines(todos)



if __name__ == "__main__":
    print("Hello")