import pathlib
import zipfile
import os
import time
import streamlit as st

TASKS_FILE = "/Users/Bhavan_1/Pycharm-Proj2/Webapp-1/tasks-list.txt"
COMPLETED_TASKS = "/Users/Bhavan_1/Pycharm-Proj2/Webapp-1/completed-tasks.txt"
timestamp = time.strftime('%b %d %Y')


def my_clock():
    while True:
        current_time = time.strftime('%b %m %Y %H:%M:%S')
        st.text(current_time)
        time.sleep(1)


if not os.path.exists('tasks-list.txt'):
    with open('tasks-list.txt', 'w') as file:
        pass

if not os.path.exists('completed-tasks.txt'):
    with open('tasks-list.txt', 'w') as file:
        pass


def get_todos(filename=TASKS_FILE):
    """ function will read the file and return the data as list """
    try:
        with open(filename, 'r') as rfile:
            data = rfile.readlines()
        return data
    except FileNotFoundError:
        print(f"FILE: {TASKS_FILE} Not Found")
        return []


def get_ctodos(filename=COMPLETED_TASKS):
    """ function will read the file and return the data as list """
    try:
        with open(filename, 'r') as cfile:
            data = cfile.readlines()
        return data
    except FileNotFoundError:
        print(f"FILE: {COMPLETED_TASKS} Not Found")
        return []


# improve the above function to validate file error before enumerating in the main.py


def write_todos(data_to_write, filename_to_write=TASKS_FILE):
    """ function will write/updates the data in the specified file """
    with open(filename_to_write, 'w') as wfile:
        wfile.writelines(data_to_write)


def complete_todos(data_to_write, filename_to_write=COMPLETED_TASKS):
    with open(filename_to_write, 'a') as filew:
        filew.writelines(data_to_write)


def color_txt(color, txt):
    if color == 'red':
        print("\033[91m {}\033[00m".format(txt))
    elif color == 'cyan':
        print("\033[96m {}\033[00m".format(txt))
    elif color == 'green':
        print("\033[92m {}\033[00m".format(txt))
    elif color == 'yellow':
        print("\033[93m {}\033[00m".format(txt))
    elif color == 'purple':
        print("\033[94m {}\033[00m".format(txt))
    elif color == 'blue':
        print("\033[34m {}\033[00m".format(txt))
    elif color == 'orange':
        print("\033[33m {}\033[00m".format(txt))
    else:
        pass


def make_archive(source_files, dest_dir):
    dest_path = pathlib.Path(dest_dir, 'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for sfile in source_files:
            sfile = pathlib.Path(sfile)
            archive.write(sfile, arcname=file.name)


def archive_extractor(source, dest):
    with zipfile.ZipFile(source, 'r') as arfile:
        if len(source) and len(dest) > 0:
            arfile.extractall(dest)
        else:
            return 'Error'


if __name__ == "__main__":
    print('Hello, I am:', __name__)
    print('Hi There, I can only print when program executed local to this module')
    print('I am testing GIT VC..')
