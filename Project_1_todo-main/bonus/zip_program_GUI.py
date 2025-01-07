import FreeSimpleGUI as sg
from zip_creater import make_archive

label1 = sg.Text("Select File to compress:")
input1 = sg.Input()
chosse_button1 = sg.FileBrowse('Select',key='files')


label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
chosse_button2 = sg.FolderBrowse('Select',key='folder')

compress_button = sg.Button("Compress")
output_label = sg.Text(key='output', text_color='green')

window = sg.Window('File Compressor', layout=[[label1,input1,chosse_button1],
                                              [label2,input2,chosse_button2],
                                              [compress_button, output_label]
                                              ])

while True:
    event, values = window.read()
    print(event,values)
    filepath = values['files'].split(';')
    folder = values['folder']
    make_archive(filepath,folder)
    window['output'].update(value="Compresson completed")



window.close()


