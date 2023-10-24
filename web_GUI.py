import streamlit as st
import functions


todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]+'\n'
    # session_state is  a dict
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
# it gives u a title
st.subheader("This is my todo app.")
# it gives u subheading
st.write("This app is to increase your productivity.")
# for simple text


for index, todo in enumerate(todos):
    # now create todos with checkbox
    checkbox = st.checkbox(todo, key=todo)
    # the key should be unique to every todo so key should be dynamic
    # perhaps put todo as key so every time new key will appear
    if checkbox:
        # here we implement complete function
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        # deletes todo in command line
        st.rerun()

st.text_input(label="Add todo", placeholder="Add new todo here...",
              on_change=add_todo, key="new_todo")
# it creates input area, it needs at least label with empty str argument

print("Hello")

st.session_state