import PySimpleGUI as ps

ps.theme('black')

col1=[[ps.B("7",font="bold")],[ps.B("4",font="bold")],[ps.B("1",font="bold")],[ps.B("0",font="bold")]]
col2=[[ps.B("8",font="bold")],[ps.B("5",font="bold")],[ps.B("2",font="bold")],[ps.B("%",font="bold",key="%")]]
col3=[[ps.B("9",font="bold")],[ps.B("6",font="bold")],[ps.B("3",font="bold")],[ps.B(".",font="bold",key=".")]]
col4=[[ps.B("/",font="bold",key="/")],[ps.B("*",font="bold",key="*")],[ps.B("-",font="bold",key="-")],[ps.B("+",font="bold",key="+")]]
col5=[[ps.B("C",button_color="red",font="bold",key="C")],[ps.B("(",font="bold",key="()")],[ps.B(")",font="bold",key=")")],[ps.B("=",font="bold",key="equal")]]

col6=[[ps.B("sin",button_color="orange",font="bold")],[ps.B("cos",button_color="orange",font="bold")],[ps.B("tan",button_color="orange",font="bold")],[ps.B("cosc",button_color="orange",font="bold")]]

        
abc=[[ps.Col(col1),ps.Col(col2),ps.Col(col3),ps.Col(col4),ps.Col(col5),ps.Col(col6)]]

menu= [ [ps.T("Calculate")],[ps.I(font=(None,20),key="input",size=(50,10))],
       [ps.Frame('PyCalci',abc)]]



window=ps.Window("PyCalci",menu,size=(350,350),return_keyboard_events=True)

def update(event):
    print("event : "+event)
   
    input_element = window["input"]
    current_value = input_element.get()
    print("curent value :  " + current_value)
    input_element.update(current_value+event)

def calculate(event):
    input_element = window["input"]
    current_value=input_element.get()
    try:
       ans=eval(current_value)
       print(ans)
       input_element.update(ans)
    except:
        input_element.update("")

while True:
    event,values=window.read()
    if event == ps.WINDOW_CLOSED:
        break
    if event in "1234567890.+-/()%*":
        update(event)

    if event == "equal":
        calculate(event)

window.close()