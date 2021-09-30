#!/usr/bin/python3

import tkinter as tk
from tkinter import filedialog
import imghdr
from PIL import Image, ImageTk



root = tk.Tk()
root.title("GUI test")
root.geometry('300x250')
top_frame = tk.Frame(root)
top_frame.pack()
#######
middle_frame=tk.Frame(root)
middle_frame.pack()
main_frame=tk.Frame(root)
main_frame.pack()
bottom_frame = tk.Frame(root)
bottom_frame.pack()


#######
word_var=tk.StringVar()
display_var=tk.StringVar()

Choice=None

colourMenu = tk.StringVar()
colourMenu.set('black')
w = tk.Label(main_frame,textvariable = display_var, font=8,fg=colourMenu.get())

####### reset frame
def destroyall():
    global w
    global middle_frame
    global main_frame
    global store_w
    global bottom_frame

    display_var.set("")
    middle_frame.destroy()
    main_frame.destroy()
    bottom_frame.destroy()
    middle_frame = tk.Frame(root)
    middle_frame.pack(side=tk.TOP)
    main_frame = tk.Frame(root)
    main_frame.pack(side=tk.TOP)
    bottom_frame = tk.Frame(root)
    bottom_frame.pack(side=tk.BOTTOM)
    store_w= None
    w = tk.Label(main_frame, textvariable=display_var, font=8, fg=colourMenu.get())

canvas_width = root.winfo_width()
canvas_height = root.winfo_height()
def paint(event):

    python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    draw_w.create_oval(x1, y1, x2, y2, fill=python_green)



def draw():
    destroyall()
    global draw_w
    global canvas_width
    global canvas_height
    draw_w = tk.Canvas(middle_frame,
        width=200,
        height=100)
    draw_w.pack(expand=tk.YES, fill=tk.BOTH)
    draw_w.bind("<B1-Motion>", paint)

    message = tk.Label(middle_frame, text="Press and Drag the mouse to draw")
    message.pack(side=tk.BOTTOM)

    print("draw def")
    root.mainloop()

def submitform():
    global w
    global store_w
    store_w=w.cget('text')

    w.configure(fg=colourMenu.get())
    word = word_var.get()

    print("{}:{}".format(colourMenu.get(), word))
    display_var.set(word)
    #print("display: {}, type:{}".format(store_w,display_var.get()))
    if not store_w:
        if store_w!=display_var.get():
            w.pack(side=tk.TOP,pady=10)



def newform():
    destroyall()
    global M_colour
    M_colour = tk.OptionMenu(middle_frame, colourMenu, 'black', 'blue', 'red', 'yellow', 'green')
    M_colour.pack(side=tk.LEFT, anchor=tk.NW,padx=10)

    height_label=tk.Entry(middle_frame,text='HEIGHT',textvariable = word_var,bd=3)
    height_label.pack(side=tk.LEFT, anchor=tk.N,pady=5,padx=5,ipadx=20)

    # bottom
    b_button = tk.Button(bottom_frame, text='Submit', fg='black', command=submitform, width=10, height=1)
    b_button.pack(side=tk.BOTTOM, pady=5)



################################## upload function
def uploadAction():
    global display_var
    filename=filedialog.askopenfilename()
    print('Selected',filename)
    image_type = imghdr.what(filename)
    print(image_type)
    if not image_type:
        print(filename.format)
        display_var.set('Not an image')
        w.configure(fg="black")
        w.pack()

    else:
        display_var.set('')
        #print("ok")
        imgupload= Image.open(filename)

        width, height = imgupload.size

        img_width = root.winfo_width()
        img_height= int(round(height/width*img_width))
        print(img_height,img_width)
        imgupload=imgupload.resize((img_width,img_height))

        photo=ImageTk.PhotoImage(imgupload)
        #display_var.set('is image')
        w.configure(image=photo)
        w.pack()
        root.mainloop()




def uploadfunction():
    destroyall()
    message = tk.Label(middle_frame, text="Upload an image", font=8)
    upload_button=tk.Button(middle_frame,text='HERE!!',command=uploadAction)
    message.pack(side=tk.LEFT)
    upload_button.pack(side=tk.LEFT,padx=10)



#top

l_button = tk.Button(top_frame,text='Typing',fg='red',command=newform, width=10, height=3)
m_button = tk.Button(top_frame,text='Image',fg='green', command=uploadfunction,width=10, height=3)
r_button = tk.Button(top_frame,text='Draw',fg='blue', command=draw,width=10, height=3)

l_button.pack(side=tk.LEFT, padx=10, pady=20)  #auto assign
m_button.pack(side=tk.LEFT, padx=10, pady=20)
r_button.pack(side=tk.LEFT, padx=10, pady=20)








root.mainloop()
