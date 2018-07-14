from tkinter import *
import webbrowser    
def getusername():
    text=TextEntry.get()
    password=TextEntry2.get()
    #text=text.upper()
    if  text=="PETER" and password=="MWAKUGHU":
        
#define all functions

        def openFile():
#open the file in notepad
            webbrowser.open("sample.txt")

        def readFile():
            textFile=open("sample.txt","r")
            print(textFile.read())
            textFile.close()

        def writeToFile():
            diaryEntry=textbox.get()
            diaryEntry=diaryEntry+"\n"
            textbox.delete(0, END)
            textFile=open("sample.txt", "a")
            textFile.write(diaryEntry)
            textFile.close()

        def close():
            window.destroy


#Make a GUI object
        window=Tk()
        window.geometry("400x400")
        window.title("My Diary")
        #set window colour to light blue
        window.configure (background='#DEEFF5')

        #Menu bar object
        menubar=Menu(window)
        #Drop down list
        filemenu1=Menu(menubar,tearoff= 0)


        filemenu1.add_command(label="Open in Idle",command=readFile)
        filemenu1.add_command(label="Open in Notepad",command=openFile)
        filemenu1.add_command(label="Quit",command=close)

        #add the menu to the menu bar
        menubar.add_cascade(label="File", menu=filemenu1)
        #make the dropdown visible
        window.config(menu=menubar)




        #Add the label, input box and submit button
        diary=Label(window,text="Write your diary entry below")
        diary.configure(background='#DEEFF5')
        diary.pack()
        textbox=Entry(window,bd=5,width=68)
        textbox.pack()
        button=Button(window,text="submit",command=writeToFile)
        button.pack()

        #start the GUI loop
        window.mainloop()




        
  #      from subprocess import call
  #      call(["python","MyDiary.py"])
  #      import os
  #      os.system('MyDiary.py')
  #      lbl2.config(text="access granted")
    else:
        lbl2.config(text="access denied")

window=Tk()
window.geometry("200x150")
window.title("My GUI")
#set window colour to light blue.
window.configure (background='#DEEFF5')

lbl=Label(window,text="Enter your username")
#set label colour  to light blue
lbl.configure(background='#DEEFF5')
lbl.pack()

#bd = border depth
TextEntry=Entry(window, bd =5)
TextEntry.pack()

lbl3=Label(window, text="Enter your password")
lbl3.configure(background='#DEEFF5')
lbl3.pack()
#Text entry for password
TextEntry2=Entry(window,bd=5)
TextEntry2.pack()

button=Button(window,text="submit",command=getusername)
button.pack()

lbl2=Label(window,text="")
#set window  colour to blue
lbl2.configure(background='#DEEFF5')
lbl2.pack()

window.mainloop()
