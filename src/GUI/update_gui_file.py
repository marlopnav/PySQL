"""
Script to update correctly the main GUI (.py) file from the Qt design (.ui) file
"""
from subprocess import call

import sys

python_path = r'C:\Users\Lopez-m\Documents\Python\Python39\Scripts'

sys.path.insert(0, python_path)

if __name__ == '__main__':
    # pyrcc5 icons.qrc -o icons_rc.py
    # pyuic5 -x MainWindow.ui -o MainWindow.py

    filename = 'gui.py'
    filename_ui = 'gui.ui'

    # update icon/images resources
    call([python_path + '\pyside2-rcc', 'icons.qrc', '-o', 'icons_rc.py'],shell=True)

    # update ui handler file
    call([python_path + '\pyside2-uic', filename_ui, '-o', filename])

    # replace annoying text import
    # Read in the file
    with open(filename, 'r') as file:
        file_data = file.read()

    # Replace the target string
    file_data = file_data.replace('import icons_rc', 'from .icons_rc import *')

    # Write the file out again
    with open(filename, 'w') as file:
        file.write(file_data)
