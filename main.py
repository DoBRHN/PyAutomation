import PySimpleGUI as sg
import os

from pathlib import Path
from var import SAVE_DIR, DATA_DIR
from function import pysave

sg.theme('Material2')

layout = [
    [sg.Text('Login', border_width=13), sg.Input(size=(15,1), key='-LOGIN-'), 
    sg.Text('Password'), sg.Input(size=(15,1), password_char="*", key='-PASSWORD-')],
    [sg.Button('SAUVEGARDE', expand_x=True)],
    [sg.Text('Output', key='-OUTPUT-')],
    [sg.Output(size=(40,5), expand_x=True)],
]

window = sg.Window("PyAutomation").Layout(layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'EXIT'):
        break

    if event == 'SAUVEGARDE':

        if Path(DATA_DIR).is_dir() == False:
            os.makedirs(DATA_DIR)
            os.makedirs(SAVE_DIR)
            
        pysave(values['-LOGIN-'], values['-PASSWORD-'])

window.close()
