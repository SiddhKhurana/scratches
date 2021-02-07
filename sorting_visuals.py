import PySimpleGUI as sg 
from random import randint 
from time import sleep
sg.theme('Dark')
def sort():
    global initiated
    initiated = True
    n = len(array) 
    for j in range(0, n-1): 
        if array[j] > array[j+1] : 
            array[j], array[j+1] = array[j+1], array[j]
            canvas.erase()
            for idx,v in enumerate(array):
                canvas.draw_line((idx+5,0),(idx+5,v))
    window.refresh()
hlayout1 = [[sg.In(default_text='Enter number of colums',size=(20,12),k='--[NUMROWS]--',)],
            [sg.Button('Generate\nrandom\nArray',size=(6,4),pad=(0,20),k='--[RANDOM]--')],
            [sg.Graph(canvas_size=(400,300),graph_bottom_left=(0,300),graph_top_right=(300,0),
                      background_color='white',k='--[CANVAS]--')]]
window = sg.Window('Sort Visualizer',hlayout1)
while True:
    event,value = window.read(timeout=50)
    if event == sg.WINDOW_CLOSED:
        break
    if event == '--[RANDOM]--':
        canvas = window.FindElement('--[CANVAS]--')
        canvas.erase()
        array = [randint(5,200) for i in range(int(value.get('--[NUMROWS]--')))]
        Ids=[]
        for idx,i in enumerate(array):
            Ids.append(canvas.draw_line((idx+5,0),(idx+5,i)))
    if event == sg.TIMEOUT_KEY:
        try:
            sort()
        except:
            pass
window.close()
