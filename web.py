import streamlit as st
import functions
todos = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    functions.write_todos(todos)
    print(todos)



st.title('My To-do List')

todos = functions.get_todos()

for index, todo in enumerate(todos):
   checkbox=st.checkbox(todo, key=todo)
   if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
    



st.text_input(label='Enter a todo',placeholder='Enter a todo...',
                     on_change=add_todo, key='new_todo')


