FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()  # here we assign variable because we need data in list format
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
# Here we don't assign variable because no use, and we simply want to write method not like above


