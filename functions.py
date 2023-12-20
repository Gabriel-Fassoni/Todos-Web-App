import PySimpleGUI as sg

FILEPATH = r"C:\Users\T-GAMER\Desktop\Python\Todo_list\list_todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

def create_window():
    edit_label = sg.Text('Type in the To-Do edited: ')
    edit_input_box = sg.InputText(tooltip='Enter a To-do', key='todo')
    edit_button_2 = sg.Button('Edit')

    layout = [[edit_label],[edit_input_box,edit_button_2]]
    return sg.Window('Edit Tab',layout)