import streamlit as st
import functions as func
import time

timestamp = time.strftime('%b %d %Y')
timestamp2 = time.strftime('%b %d %Y %H:%M:%S %p')

st.set_page_config(layout="wide")
st.write(timestamp2)
st.caption(':eye: Copyright to BCM')

st.title(':sun_with_face: :blue[_To-Do Task Organizer_] :writing_hand:')

st.subheader('**:red[This is daily task organizer]**')
st.write(":green[This app is to increase <b> productivity </b>]", unsafe_allow_html=True)

tasks = func.get_todos()


def add_task():
    web_task = st.session_state['new task'] + "\n"
    tasks.append(web_task)
    func.write_todos(tasks)


st.text_input(label=" ", placeholder='Add a new task', on_change=add_task, key='new task')

for index, task in enumerate(tasks):
    task_selected = st.checkbox(task, key=task)
    if task_selected:
        func.complete_todos(task.strip() + ' ' + timestamp + '\n')
        tasks.pop(index)
        func.write_todos(tasks)
        del st.session_state[task]
        st.experimental_rerun()

st.divider()
st.title(':white_check_mark: :green[Completed Tasks] :trophy:')
st.divider()

ctasks = func.get_ctodos()
for index, ctask in enumerate(ctasks):
    st.text(ctask)
