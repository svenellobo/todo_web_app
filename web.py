import streamlit as st
import functions

todos = functions.get_todos()

def clear_output():
    if "clear" not in st.session_state:
        st.session_state.clear = False

    if st.session_state.clear:
        st.session_state.clear = False
        st.write("")
    else:
        st.write(f"You entered: {st.session_state.input}")
        st.session_state.clear = True

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



st.title("Bok")
st.subheader("This is my todo app!")
st.write("This app is for increasing your productivity!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

