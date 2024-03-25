import PySimpleGUI as sg
def open_game():
    
    choices = sorted([elem.__name__ for elem in sg.Element.__subclasses__()])
    
    input_width = 20
    num_items_to_show = 6
    
    layout = [
        [sg.Text(text='From the given actors, guess the movie.', font=('Arial Bold', 30), size=(25,2),justification='center')],
        [sg.CB('Ignore Case', k='-IGNORE CASE-')],
        [sg.Text(text='Actor:', font=('Arial Bold', 20))],
        [sg.Text(text='Actor:', font=('Arial Bold', 20))],
        [sg.Text('Actor:', font=('Arial Bold', 20))],
        [sg.Text('Actor:', font=('Arial Bold', 20))],
        [sg.Text('Movie: ',font=('Arial Bold', 25))],
        [sg.Input(size=(input_width, 1), enable_events=True, key='-IN-')],
        [sg.pin(sg.Col([[sg.Listbox(values=[], size=(input_width, num_items_to_show), enable_events=True, key='-BOX-',
                                    select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, no_scrollbar=True)]],
                       key='-BOX-CONTAINER-', pad=(0, 0), visible=False))],
        #[sg.Button('Enter Answer',font=('Arial Bold', 15))]
        [sg.Button('Close',font=('Arial Bold', 10))]
             ]


    
    window = sg.Window('Game', layout, element_justification='c', return_keyboard_events=True, finalize=True)
            


    list_element:sg.Listbox = window.Element('-BOX-')           # store listbox element for easier access and to get to docstrings
    prediction_list, input_text, sel_item = [], "", 0

    while True: 
        event, values = window.read()
        # print(event, values)
        if event == sg.WINDOW_CLOSED or event == 'Close':
            break
        # pressing down arrow will trigger event -IN- then aftewards event Down:40
        elif event.startswith('Down') and len(prediction_list):
            sel_item = (sel_item + 1) % len(prediction_list)
            list_element.update(set_to_index=sel_item, scroll_to_index=sel_item)
        elif event.startswith('Up') and len(prediction_list):
            sel_item = (sel_item + (len(prediction_list) - 1)) % len(prediction_list)
            list_element.update(set_to_index=sel_item, scroll_to_index=sel_item)
        elif event == '\r':
            if len(values['-BOX-']) > 0:
                window['-IN-'].update(value=values['-BOX-'])
                window['-BOX-CONTAINER-'].update(visible=False)
        elif event == '-IN-':
            text = values['-IN-'] if not values['-IGNORE CASE-'] else values['-IN-'].lower()
            if text == input_text:
                continue
            else:
                input_text = text
            prediction_list = []
            if text:
                if values['-IGNORE CASE-']:
                    prediction_list = [item for item in choices if item.lower().startswith(text)]
                else:
                    prediction_list = [item for item in choices if item.startswith(text)]

            list_element.update(values=prediction_list)
            sel_item = 0
            list_element.update(set_to_index=sel_item)

            if len(prediction_list) > 0:
                window['-BOX-CONTAINER-'].update(visible=True)
            else:
                window['-BOX-CONTAINER-'].update(visible=False)
        elif event == '-BOX-':
            window['-IN-'].update(value=values['-BOX-'])
            window['-BOX-CONTAINER-'].update(visible=False)
    
    window.close()




layout = [[sg.Text(text='Movie Guessing Game',font=('Arial Bold', 40),size=(20,5),justification='center')],
          [sg.Button('Play',font=('Arial Bold', 30))],
          [sg.Button('Close',font=('Arial Bold', 30))]]

window = sg.Window('Intro', layout, element_justification='c')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Close':
        break
    elif event == 'Play':
        open_game()

window.close()

if __name__ == '__main__':
    open_game()
