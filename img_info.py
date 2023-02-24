'''
informacao

Siga os passos para rodar o programa no PyCharm (recomendado)
(1) Crie um novo projeto no PyCharm img_info (recomendado)
(2) Copie o código do arquivo img_info.py para a janela de execução
(3) Instale o módulo PySimpleGUI
	No terminal digite: pip install PySimpleGUI
(4) Copie a pasta arq_img_info e para o mesmo diretório que o arquivo
principal do seu projeto informacao (mesma pasta que o arquivo main.py ou
img_info.py caso tenha editado)
(5) Execute o arquivo: shift+f10

Siga os passos para criar um arquivo .exe (continuando do passo 5)
(6) No terminal digite: pip install pyinstaller
(7) Novamente, no terminal: pyinstaller --onefile -w main.py
ou pyinstaller --onefile -w img_info.py
(8) O arquivo exe encontra-se na pasta dist
(9) Copie o arquivo main.exe (ou informacao.exe) para um mesmo diretório
contendo a pasta arq_img_info.
(10) Na pasta arq_img_info conter uma nomedaimagem.png referente a qual se quer
associar as informações. Neste caso, pode-se colocar um arquivo de texto
nomedaimagem.txt com informações ou criar um durante a execução do programa.
(12) Digite em um dos campos de entrada Knolan e aperte Selecionar ou Enter. Em
seguida clique sobre a foto do guerreiro que irá aprecer...
(13) IMPORTANTE: As imagens, nesta versão, apresentam um tamanho fixo de 182x250
pixels. Usar imagens de tamanho diferente pode causar distorção da interface.
Uma dica é copiar a imagem ini.png para um powerpoint e usá-la como forma para
as outras imagens salvas. Em caso de tela pequena edite a imagem ini para que as
10 imagens caibam na tela.
'''



import PySimpleGUI as sg
import os

layout = [
    [sg.Text('                                                                                   ', font='Times 14 bold'),
     sg.Button('Selecionar', bind_return_key=True, font='Times 16 bold'),
     sg.Text('                                      ', font='Times 14 bold'),
     sg.Button('Arquivos', font='Times 16 bold'),
     sg.Text(' ', font='Times 14 bold'),
     sg.Button('Limpar', bind_return_key=True, font='Times 16 bold')],
    [sg.Input(key='entrada0', do_not_clear=True, size=(18, 1), font='Times 14 bold'),
     sg.Input(key='entrada1', do_not_clear=True, size=(18, 1), font='Times 14 bold'),
     sg.Input(key='entrada2', do_not_clear=True, size=(18, 1), font='Times 14 bold'),
     sg.Input(key='entrada3', do_not_clear=True, size=(18, 1), font='Times 14 bold'),
     sg.Input(key='entrada4', do_not_clear=True, size=(18, 1), font='Times 14 bold')],
    [sg.Button(image_filename=os.path.join('arq_img_info', 'ini.png'), key='im0', visible=True),
     sg.Button(image_filename=os.path.join('arq_img_info', 'ini.png'), key='im1', visible=True),
     sg.Button(image_filename=os.path.join('arq_img_info', 'ini.png'), key='im2', visible=True),
     sg.Button(image_filename=os.path.join('arq_img_info', 'ini.png'), key='im3', visible=True),
     sg.Button(image_filename=os.path.join('arq_img_info', 'ini.png'), key='im4', visible=True)],
    [sg.Input(key='entrada5', do_not_clear=True, size=(18, 1), font='Times 14 bold'),
     sg.Input(key='entrada6', do_not_clear=True, size=(18, 1), font='Times 14 bold'),
     sg.Input(key='entrada7', do_not_clear=True, size=(18, 1), font='Times 14 bold'),
     sg.Input(key='entrada8', do_not_clear=True, size=(18, 1), font='Times 14 bold'),
     sg.Input(key='entrada9', do_not_clear=True, size=(18, 1), font='Times 14 bold')],
    [sg.Button(image_filename=os.path.join('arq_img_info', 'ini.png'), key='im5', visible=True),
     sg.Button(image_filename=os.path.join('arq_img_info', 'ini.png'), key='im6', visible=True),
     sg.Button(image_filename=os.path.join('arq_img_info', 'ini.png'), key='im7', visible=True),
     sg.Button(image_filename=os.path.join('arq_img_info', 'ini.png'), key='im8', visible=True),
     sg.Button(image_filename=os.path.join('arq_img_info', 'ini.png'), key='im9', visible=True)]
]

window = sg.Window('Sorteador by Allan', layout)


# função para ler o arquivo de informações de uma imagem
def read_info_file(image_filename):
    folder = 'arq_img_info'
    filename, _ = os.path.splitext(image_filename)
    txt_filename = os.path.join(folder, f'{filename}.txt')
    if os.path.isfile(txt_filename):
        with open(txt_filename, 'r') as f:
            return f.read()
    else:
        return 'Nenhuma informação disponível.'



def clear_inputs_and_images():
    # limpa os valores das entradas
    for i in range(10):
        window[f'entrada{i}'].update('')
    # redefine as imagens dos botões para a imagem inicial
    for i in range(10):
        window[f'im{i}'].update(image_filename=os.path.join('arq_img_info', 'ini.png'))

def show_files():
    folder = 'arq_img_info'
    filenames = os.listdir(folder)
    files_str = '\n'.join([os.path.splitext(f)[0] for f in filenames if f.endswith('.png')])
    popup_layout = [
        [sg.Multiline(files_str, size=(50, 20), font='Arial 12', key='files', disabled=True)],
        [sg.Button('Fechar', font='Arial 14')]]
    popup_window = sg.Window('Arquivos na pasta', popup_layout)
    while True:
        popup_event, _ = popup_window.read()
        if popup_event == sg.WIN_CLOSED or popup_event == 'Fechar':
            break
    popup_window.close()

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    entradas = [values[f'entrada{i}'] for i in range(0, 10)]
    imagens = [window[f'im{i}'] for i in range(0, 10)]
    current_dir = os.getcwd()

    if event == 'Selecionar':
        for entrada, imagem in zip(entradas, imagens):
            if entrada:
                filename = os.path.join(current_dir, 'arq_img_info', f'{entrada}.png')
                if os.path.isfile(filename):
                    imagem.Update(image_filename=filename, visible=True)
                else:
                    sg.Popup(f'O arquivo {filename} não foi encontrado na pasta.')

    if event == 'Arquivos':
        show_files()

    if event in ('im0', 'im1', 'im2', 'im3', 'im4', 'im5', 'im6', 'im7', 'im8', 'im9'):
        button_num = int(event[-1]) - 1
        entrada = values[f'entrada{button_num + 1}']
        filename = os.path.join(current_dir, 'arq_img_info', f'{entrada}.png')
        if os.path.isfile(filename):
            current_image_name = entrada
            info_filename = os.path.join(current_dir, 'arq_img_info', f'{entrada}.txt')
            if os.path.isfile(info_filename):
                with open(info_filename, 'r') as f:
                    info = f.read()
            else:
                info = 'Nenhuma informação disponível.'
            popup_layout = [
                [sg.Multiline(info, size=(100, 26), font='Arial 12', key='info', disabled=False)],
                [sg.Button('Editar', font='Arial 14'), sg.Button('Fechar', font='Arial 14')]]
            popup_window = sg.Window(current_image_name, popup_layout)
            while True:
                popup_event, popup_values = popup_window.read()
                if popup_event == sg.WIN_CLOSED or popup_event == 'Fechar':
                    break
                if popup_event == 'Editar':
                    with open(info_filename, 'w') as f:
                        f.write(popup_values['info'])
                    sg.Popup('As informações foram salvas com sucesso.')
            popup_window.close()

    if event == 'Limpar':
        clear_inputs_and_images()

window.close()



