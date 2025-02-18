import streamlit as st
import fuctions  # Assuming 'fuctions' is the correct name of your module

todos = fuctions.get_todos()
# Initialize session state for 'new_todo'
if 'new_todo' not in st.session_state:
    st.session_state['new_todo'] = ""
if 'todos' not in st.session_state:
    st.session_state['todos'] = fuctions.get_todos()
if 'rerun' not in st.session_state:
    st.session_state['rerun'] = False

todos = st.session_state['todos']

print(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")


# Define function to add a new todo
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fuctions.write_todos(todos)
    st.session_state['new_todo'] = ""  # Clear the input field after adding
    st.write("Todos written to the file successfully!")
    st.session_state['rerun'] = not st.session_state['rerun']  # Toggle the rerun flag


# Text input for adding new todos
st.text_input(label=" ", placeholder="add new todo...",
              on_change=add_todo, key="new_todo")

# Display todos with checkboxes
for i, todo in enumerate(todos):
    if st.checkbox(todo, key=f"todo_{i}"):
        st.session_state['todos'].pop(i)
        fuctions.write_todos(st.session_state['todos'])
        st.session_state['rerun'] = not st.session_state['rerun']  # Toggle the rerun flag



print("Hello")
