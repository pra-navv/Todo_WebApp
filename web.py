import streamlit as st
import functions

st.set_page_config(layout="wide")

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("MY TODO APP")
st.subheader("made by Pranav")
st.write("This app is to increase your <b>PRODUCTIVITY</b>."
         , unsafe_allow_html=True)
st.text_input(label=" ", placeholder="Add new Todo..."
              , on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

print("HELLO")