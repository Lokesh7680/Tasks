import PySimpleGUI as sg

# Define the layout of the GUI
layout = [
    [sg.Input(size=(20, 1), key='-DISPLAY-', justification='right')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('/')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('*')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('-')],
    [sg.Button('0'), sg.Button('.'), sg.Button('+'), sg.Button('=')],
    [sg.Button('C')]
]

# Create the window
window = sg.Window('Simple Calculator', layout, return_keyboard_events=True)

# Event loop
expression = ''
while True:
    event, values = window.read()

    if event in ('C', 'Escape:27'):
        expression = ''
    elif event == '=':
        try:
            result = eval(expression)
            expression = str(result)
        except:
            expression = 'Error'
    elif event != sg.WIN_CLOSED:
        expression += event

    window['-DISPLAY-'].update(expression)

    if event == sg.WIN_CLOSED:
        break

# Close the window
window.close()
