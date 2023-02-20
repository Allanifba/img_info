import PySimpleGUI as sg
import os


layout = [
    [sg.Text('                                                                                ',font='Times 14 bold'),
     sg.Button('Selecionar', bind_return_key=True,font='Times 16 bold'),
     sg.Text('                                                              ',font='Times 14 bold'),
     sg.Button('Limpar', bind_return_key=True,font='Times 16 bold')],
    [sg.Input(key='entrada0', do_not_clear=True,size=(18,1),font='Times 14 bold'),
     sg.Input(key='entrada1', do_not_clear=True,size=(18,1),font='Times 14 bold'),
     sg.Input(key='entrada2', do_not_clear=True, size=(18,1), font='Times 14 bold'),
     sg.Input(key='entrada3', do_not_clear=True, size=(18,1), font='Times 14 bold'),
     sg.Input(key='entrada4', do_not_clear=True, size=(18,1), font='Times 14 bold')],
    [sg.Button(image_filename='ini.png',key='im0',visible=True),
     sg.Button(image_filename='ini.png',key='im1',visible=True),
     sg.Button(image_filename='ini.png',key='im2',visible=True),
     sg.Button(image_filename='ini.png',key='im3',visible=True),
     sg.Button(image_filename='ini.png',key='im4',visible=True)],
    [sg.Input(key='entrada5', do_not_clear=True,size=(18,1),font='Times 14 bold'),
     sg.Input(key='entrada6', do_not_clear=True,size=(18,1),font='Times 14 bold'),
     sg.Input(key='entrada7', do_not_clear=True, size=(18,1), font='Times 14 bold'),
     sg.Input(key='entrada8', do_not_clear=True, size=(18,1), font='Times 14 bold'),
     sg.Input(key='entrada9', do_not_clear=True, size=(18,1), font='Times 14 bold')],
    [sg.Button(image_filename='ini.png',key='im5',visible=True),
     sg.Button(image_filename='ini.png',key='im6',visible=True),
     sg.Button(image_filename='ini.png',key='im7',visible=True),
     sg.Button(image_filename='ini.png',key='im8',visible=True),
     sg.Button(image_filename='ini.png',key='im9',visible=True)]
]


window = sg.Window('Sorteador by Allan', layout)


# função para ler o arquivo de informações de uma imagem
def read_info_file(image_filename):
    filename, _ = os.path.splitext(image_filename)
    txt_filename = f'{filename}.txt'
    if os.path.isfile(txt_filename):
        with open(txt_filename, 'r') as f:
            return f.read()
    else:
        return 'Nenhuma informação disponível.'


while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    entradas = [values[f'entrada{i}'] for i in range(0, 10)]
    imagens = [window[f'im{i}'] for i in range(0,10)]


    if event == 'Selecionar':
        for entrada, imagem in zip(entradas, imagens):
            if entrada:
                filename = f'{entrada}.png'
                if os.path.isfile(filename):
                    imagem.Update(image_filename=filename, visible=True)
                else:
                    sg.Popup(f'O arquivo {filename} não foi encontrado na pasta.')

    if event in ('im0','im1', 'im2', 'im3', 'im4', 'im5', 'im6', 'im7', 'im8', 'im9'):
        button_num = int(event[-1])-1
        entrada = values[f'entrada{button_num+1}']
        print(entrada)
        filename = f'{entrada}.png'
        if os.path.isfile(filename):
            # atualiza a variável global com o nome da imagem
            current_image_name = entrada
            info = read_info_file(filename)
            popup_layout = [
                [sg.Multiline(info, size=(100, 28), font='Arial 12', key='info', disabled=True)],
                [sg.Button('OK', size=(10, 1), pad=((250, 0), (20, 30)))]
            ]
            popup_window = sg.Window('Informações', popup_layout, size=(800, 600))
            while True:
                event, values = popup_window.read()
                if event == sg.WIN_CLOSED or event == 'OK':
                    break
            popup_window.close()
        else:
            sg.Popup(f'O arquivo {filename} não foi encontrado na pasta. Não há informações.')

    if event == 'Limpar':
        for imagem in imagens:
            imagem.Update(image_filename='ini.png', visible=True)
        for i in range(0, 10):
            window[f'entrada{i}'].Update('')

window.close()
