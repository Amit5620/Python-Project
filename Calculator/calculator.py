import PySimpleGUI as gui
import math

gui.theme("Topanga")

layout = [
    [gui.B("Sin", size= (8, 1)), gui.B("Cos", size= (8, 1)), gui.B("Tan", size= (8, 1))],
    [gui.B("Sqrt", size= (8, 1)), gui.B("Pow2", size= (8, 1)), gui.B("lg2", size= (8, 1))],
    [gui.Text(key = "InPut", size = (32, 1),  background_color='#2D4245', font=("Verdana", 20))],
    [gui.B("AC", size = (5, 2)), gui.B("=", size = (14, 1)), gui.B("C", size = (5, 2))],
    [gui.B(str(i), size = (4, 2)) for i in range(5)],
    [gui.B(str(i), size = (4, 2)) for i in range(5, 10)],
    [gui.B(i, size = (4, 2)) for i in ["+", "-", "*", "/", "%"] ]
]

window  = gui.Window("Calculator", layout, size= (260, 290))

result = ""
result1 = ""

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED:
        break
    elif event in ["+", "-", "*", "/", "%"]:
        result = result + event
        result1 = ""
        window["InPut"].update("")
    elif event in  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        result = result + event
        result1 = result1 + event
        window["InPut"].update(result1)
    elif event == "=" and result != "":
        if result[0] == "r":
            if  ("sin" in result or "cos" in result or "tan" in result):
                result = result + "/180*math.pi), 2)"
            elif "pow" in result or "log" in result:
                result = result + ", 2), 2)"
        result1 = eval(result)
        window["InPut"].update(result1)
        result = ""
        result1 = ""
    elif event == "Sin":
        result = "round(math.sin("
        window["InPut"].update("sin")
    elif event == "Cos":
        result = "round(math.cos("
        window["InPut"].update("cos")
    elif event == "Tan":
        result = "round(math.tan("
        window["InPut"].update("tan")
    elif event == "Sqrt":
        result = "round(math.sqrt("
        window["inPut"].update("sqrt")
    elif event == "Pow2":
        result = "round(pow("
        window["InPut"].update("pow2 ")
    elif event == "lg2":
        result = "round(math.log("
        window["InPut"].update("log2 ")
    elif event == "C":
        if len(result) > 0 and result[-1] not in ["+", "-", "*", "/", "%"]:
            result = result[:-1]
        if len(result1) > 0:
            result1 = result1[:-1]
        window["InPut"].update(result1)
    elif event == "AC":
        result = result1 = ""
        window["InPut"].update(result)
