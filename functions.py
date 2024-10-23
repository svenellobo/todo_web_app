FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read a text file and return
     a list of to-do items.
     """
    with open(filepath, 'r') as file:
        todos_local = file.readlines() #ovo stvori listu od svih predmeta u .txt fileu
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("hello from functions")