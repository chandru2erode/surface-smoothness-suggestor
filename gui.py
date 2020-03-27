import PySimpleGUI as sg      
from utils import SurfaceSmoothnessSuggestor

sg.theme('Reddit')   
sg.SetOptions(font='monserrat 11 bold')

layout = [  
            [sg.Text('Material           :', size=(25, 1), font='roboto 11 bold', pad=((30,3),3)), sg.Radio('ABS', 1), sg.Rad('PLA',1)],     
            [sg.Text('Layer Thickness    :', size=(25, 1), font='roboto 11 bold', pad=((30,13),3)), sg.InputText('0', size=(10,1))],      
            [sg.Text('Raw Value          :', size=(25, 1), font='roboto 11 bold', pad=((30,13),3)), sg.InputText('0', size=(10,1))],      
            [sg.Text('Surface Smoothness :', size=(25, 1), font='roboto 11 bold', pad=((30,13),3)), sg.InputText('0', size=(10,1))],      
            [sg.Button('Suggest', bind_return_key=True, pad=((150,3),30))],
            [sg.Text(key='-SUGGESTION_MESSAGE-', size=(40,3), text_color='#88aad9', font='helvetica 16 bold')],
            [sg.Text(key='-SANDING_TIME-', size=(45,1), text_color='#ff0000', font='roboto 11 bold')]
        ]

window = sg.Window('Surface Smoothness Suggestor', layout, size=(435,325))

while True:
    event, values = window.Read()
    print(values)
    suggestor = SurfaceSmoothnessSuggestor(float(values[2]), float(values[3]), float(values[4]))
    sanding_time, message = suggestor.extract()

    if event == 'Suggest':
        window['-SUGGESTION_MESSAGE-'].update(message)
        window['-SANDING_TIME-'].update(f'Estimated required Sanding time : {sanding_time} minutes.')

window.close()
