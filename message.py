import socket
import tkinter as tk
import tkinter.font as tkFont
import string
#import ipaddress 
from tkinter import *
from tkinter import ttk
from threading import Thread

#varibles 
contacts = ["new contact","smuble","dave"]
paddingSize = 5
FontSize = 11
username = "default_user"
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
client = [socket.socket(),socket.socket(),socket.socket()]
server = [socket.socket(),socket.socket(),socket.socket()]

port = 80 



#functions

#def IPToUID(IP):
#    IP =str(int(ipaddress.ip_address(IP)))
#    print(IP)
#    UID = []
letters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","M","1","2","3","4","5","6","7","8","9","0"]
#    converted = False
#    UID = []
#    while converted == False:
#        digits = int(IP[:2])
#        print(str(digits))
#        if digits > 36:
#            digits = int(IP[:1])
#        UID.append(letters[digits])
#        IP = IP[1:]
#        if IP == "":
#            converted = True
#        print(str(UID))
#    return(UID)




def receveText():
        while True:
            RecevedMessage = client[0].recv(1024).decode()
            outputText.insert(END,RecevedMessage)           
def sendtext(event=None):
    outputText.insert(END,username+": "+ inputVarible.get())
    data = inputVarible.get()
    client[0].send((username+": "+data).encode())
    outputText.yview(END)
    inputText.delete(0,END)

def joinIP(clientIP):
    client[0].connect((clientIP,80))
    receveThread = Thread(target=receveText)
    receveThread.start()
def hostIP():
    server[0].bind(("",port))
    server[0].listen(5)
    clientConnected = False
    while clientConnected == False:
        print("wating")
        client[0], addr = server[0].accept() 
        #clientConnected = True
        receveThread = Thread(target=receveText)
        receveThread.start()

#def selectedContact(event=None):
    currentSelected = contactSelector.get()
    if currentSelected == "new contact":
        addContact()

def addContact():
    addContactUI = tk.Tk()
    addContactUI.title("new contact")
    addContactUI.attributes('-topmost', True)
    addContactUI.resizable(False,False)
    def ipClicked(event=None):
        clientIP = inputIP.get()
        inputIP.delete(0,END)
        addContactUI.destroy()
        joinIP(clientIP)
    def hostButton():
        hostIP()
        addContactUI.destroy()
        


    addContactUITOP = PanedWindow(addContactUI)
    TkIP = tk.StringVar(addContactUITOP)
    inputIP = Entry(addContactUITOP,textvariable=TkIP,font=defaultFont)
    buttonIP = Button(addContactUITOP,text="add user",command=ipClicked, font=defaultFont)

    inputIP.bind("<Return>",ipClicked)

    inputIP.pack(side=LEFT,fill=BOTH,expand=True,padx=(paddingSize,0),pady=(paddingSize,0))
    buttonIP.pack(side=RIGHT,padx=(paddingSize,paddingSize),pady=(paddingSize,0))

    ButtonHost = Button(addContactUI,text="host",font=defaultFont,command=hostButton)

    addContactUITOP.pack(side=TOP,pady=(0,paddingSize))
    #ButtonHost.pack(side=BOTTOM,fill=X,expand=True, padx=(paddingSize,paddingSize),pady=(paddingSize,paddingSize))
def settings():
    global paddingSize
    def setUsername(event=NONE):
        global username
        username = TKusername.get()
        inputUsername.delete(0,END)
    def setPadding(event=NONE):
        global paddingSize
        print(paddingSize)
        paddingSize = TKpadding.get()
        paddingInput.delete(0,END)

    settingsUI = tk.Tk()
    settingsUI.title("settings")
    settingsUI.attributes('-topmost', True)

    usernameUI = PanedWindow(settingsUI)
    TKusername = tk.StringVar(usernameUI)
    inputUsername = Entry(usernameUI,textvariable=TKusername,font=defaultFont)
    usernameButton = Button(usernameUI,text="set",font=defaultFont,command=setUsername)
    usernameLable = Label(usernameUI,text="username:",font=defaultFont)
    inputUsername.bind("<Return>",setUsername)
    usernameLable.pack(side=LEFT,padx=(paddingSize,0),pady=(paddingSize,paddingSize))
    inputUsername.pack(side=LEFT,fill=BOTH,expand=True,padx=(paddingSize,0),pady=(paddingSize,paddingSize))
    usernameButton.pack(side=RIGHT,padx=(paddingSize,paddingSize),pady=(paddingSize,paddingSize))

    paddingUI = PanedWindow(settingsUI)
    TKpadding= tk.StringVar(paddingUI)
    paddingInput = Entry(paddingUI,textvariable=TKpadding)
    paddingButton = Button(paddingUI,text="set",font=defaultFont,command=setPadding)
    paddingLable = Label(paddingUI,text="padding size",font=defaultFont)
    paddingInput.bind("<Return>",setPadding)
    paddingLable.pack(side=LEFT,padx=(paddingSize,0),pady=(0,paddingSize))
    paddingInput.pack(side=LEFT,fill=BOTH,expand=TRUE,padx=(paddingSize,0),pady=(0,paddingSize))
    paddingButton.pack(side=RIGHT,fill=Y,padx=(paddingSize,paddingSize),pady=(0,paddingSize))
    

    usernameUI.pack(side=TOP,fill=X)
    #paddingUI.pack(side=TOP,fill=X)
    




hostThread = Thread(target=hostIP)
hostThread.start()
#create ui 
mainUI = tk.Tk()
mainUI.title("shmuble chat")
mainUI.minsize(400,310)
mainUI.geometry("600x500")
defaultFont = tkFont.Font(size=FontSize)

#controll bar
controllPanell = PanedWindow(mainUI)
contactText = Label(controllPanell, text="message:",font=defaultFont)
#contactSelector = ttk.Combobox(controllPanell,values=contacts)
contactSelector = Button(controllPanell,text="new user",font=defaultFont,command=addContact)
ipText = Label(controllPanell,text="ip:"+IPAddr,font=defaultFont)
settingsButton = Button(controllPanell,text="settings",font=defaultFont,command=settings)

#contactSelector.bind("<<ComboboxSelected>>",selectedContact)

contactText.pack(side = LEFT)
contactSelector.pack(side=LEFT,fill=BOTH, expand=True)
ipText.pack(side=LEFT,padx=(paddingSize,0))
settingsButton.pack(side=RIGHT,fill=Y, padx=(paddingSize,0))

#text output
outputPanell = PanedWindow(mainUI)
outputText = Listbox(outputPanell,font=defaultFont)
outputScrollbar = Scrollbar(outputPanell, command= outputText.yview)

outputText.config(yscrollcommand=outputScrollbar.set)   

outputText.pack(side=LEFT,fill=BOTH,expand=True)
outputScrollbar.pack(side=RIGHT,fill=Y)

#input box
inputPanell = PanedWindow(mainUI)
inputVarible = tk.StringVar(inputPanell)
inputText = Entry(inputPanell,textvariable=inputVarible,font=defaultFont)
inputButton = Button(inputPanell,text="send", command=sendtext,font=defaultFont)

inputText.bind("<Return>",sendtext)

inputText.pack(side=LEFT,fill=BOTH,expand=True)
inputButton.pack(side=RIGHT,padx=(paddingSize,0),fill=Y)



#final layout
controllPanell.pack(side=TOP,fill=X,padx=(paddingSize,paddingSize),pady=(paddingSize,paddingSize))
outputPanell.pack(side=TOP,fill=BOTH,expand=True,padx=(paddingSize,paddingSize))
inputPanell.pack(side=BOTTOM,fill=X,padx=(paddingSize,paddingSize),pady=(paddingSize,paddingSize))
mainUI.mainloop()