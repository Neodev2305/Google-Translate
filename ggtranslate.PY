from tkinter import*
from PIL import Image,ImageTk       #GIÚP CHÈN ẢNH 
from googletrans import Translator   #ĐỂ DỊCH
 
#tạo window
root=Tk()
root.title("GOOGLE DỊCH")
root.geometry("1280x720")
root.iconbitmap('logo.ico') # CHÈN LOGO

load=Image.open('background.jpg')
render=ImageTk.PhotoImage(load)    #XUẤT HÌNH 
lb1=Label(root,image=render)       # HIỂN THỊ HÌNH ẢNH VÀ VĂN BẢN
lb1.place(x=10,y=10)                 # ĐẶT LÊN MÀN HÌNH
lb1=Label(root,text="translator",fg="#FFFFFF",bd=0,bg="#190566")
lb1.config(font=("Transformers Movie",30))
lb1 .pack(pady=20)

box=Text(root,width=28,height=8,font=("ROBOTO",16))
box.pack(pady=20)

button_frame=Frame(root).pack(side=BOTTOM)
 
def clear():
    box.delete (1.0, END)
    box1.delete(1.0, END)
def translate():
    INPUT = box.get(1.0, END)
    print(INPUT)
    t=Translator ()
    a=t.translate (INPUT, src="vi", dest="en")
    b=a.text
    box1.insert (END,b)
clear_button=Button (button_frame, text="Clear text", font=(("Transformers Movie"),10, 'bold'),bg='#303030', fg="#FFFFFF",command=clear)
clear_button.place(x=540, y=330)
trans_button=Button (button_frame, text="Translate", font=(("Transformers Movie"),10, 'bold'),bg='#303030', fg="#FFFFFF",command=translate)
trans_button.place(x=650, y=330)
box1=Text (root,width=28,height=8,font=("ROBOTO",16))
box1.pack(pady=50)

root.mainloop()