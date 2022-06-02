import tkinter
import subprocess

top = Tk()
top.geometry("100x100")
def helloCallBack():
   camera = subprocess.call(r'C:\Users\jfra\ZBar\bin\zbarcam.bat')

B = Button(top, text = "Open Camera", command = helloCallBack)
B.place(x = 50,y = 50)
top.mainloop()
