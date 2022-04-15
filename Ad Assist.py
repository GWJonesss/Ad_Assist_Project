
from curses import window
from distutils import command
from tkinter import *
import tkinter
import pyperclip as pc
from PIL import ImageTk, Image
from tkinter import ttk
import os

frame = Tk()
frame.iconbitmap("theicon.ico") 
frame.title("Ad Assist")
frame.geometry('400x500')

is_on = True

bg = ImageTk.PhotoImage(Image.open("Your_img.jpg"))
 
canvas2 = Canvas(frame)
canvas2.pack(fill = "both", expand = True) 

canvas1 = Canvas(canvas2)     
  
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")

    
def _on_mousewheel(event):
    canvas1.yview_scroll(int(-1*(event.delta/120)), "units")
canvas1.bind_all("<MouseWheel>", _on_mousewheel)

canvas1.pack(fill = "both", expand = True)

my_scrollbar = ttk.Scrollbar(canvas1, orient=VERTICAL, command= canvas1.yview)

my_scrollbar.pack(side=RIGHT, fill=Y)

canvas1.config(yscrollcommand=my_scrollbar.set)
canvas1.bind('<Configure>', lambda e: canvas1.config(scrollregion = canvas1.bbox("all")))








variable = "G1"
def makeSomething(value):
    global variable
    variable = value



g2button = tkinter.Button(canvas2, bd= 7, text="G2",command=lambda *args: makeSomething("G2"))

g2button_canvas1 = canvas2.create_window( 80, 160,
                                       anchor = "nw",
                                       window = g2button)


g1button = tkinter.Button(canvas2, bd= 7, text="G1",command=lambda *args: makeSomething("G1"))

g1button_canvas1 = canvas2.create_window( 80, 200,
                                       anchor = "nw",
                                       window = g1button)




##########################
    #COPY BUTTONS DEF
##########################  

#list1    
def copy_button1():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("SJ SPK " + str(variable) + " " + nputtxt1.get(1.0, "end-1c")  )
def copy_button2():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TR SPK " + str(variable) + " "  + nputtxt1.get(1.0, "end-1c") )
def copy_button3():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TGWSA SPK " + str(variable) + " "  + nputtxt1.get(1.0, "end-1c"))
#list2
def copy_button4():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("SJ SPK " + str(variable) + " "  + nputtxt2.get(1.0, "end-1c"))
def copy_button5():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TR SPK " + str(variable) + " "  + nputtxt2.get(1.0, "end-1c"))
def copy_button6():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TGWSA SPK " + str(variable) + " "  + nputtxt2.get(1.0, "end-1c"))
#list3    
def copy_button7():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("SJ SPK " + str(variable) + " "  + nputtxt3.get(1.0, "end-1c"))
def copy_button8():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TR SPK " + str(variable) + " "  + nputtxt3.get(1.0, "end-1c"))
def copy_button9():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TGWSA SPK " + str(variable) + " "  + nputtxt3.get(1.0, "end-1c"))
#list4
def copy_button10():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("SJ SPK " + str(variable) + " "  + nputtxt4.get(1.0, "end-1c"))
def copy_button11():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TR SPK " +  str(variable) + " "  + nputtxt4.get(1.0, "end-1c"))
def copy_button12():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TGWSA SPK " + str(variable) + " "  + nputtxt4.get(1.0, "end-1c"))
#list5    
def copy_button13():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("SJ SPK " + str(variable) + " "  + nputtxt5.get(1.0, "end-1c"))
def copy_button14():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TR SPK " + str(variable) + " "  + nputtxt5.get(1.0, "end-1c"))
def copy_button15():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TGWSA SPK " + str(variable) + " "  + nputtxt5.get(1.0, "end-1c"))
#list6
def copy_button16():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("SJ SPK " + str(variable) + " "  + nputtxt6.get(1.0, "end-1c"))
def copy_button17():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TR SPK " + str(variable) + " "  + nputtxt6.get(1.0, "end-1c"))
def copy_button18():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TGWSA SPK " + str(variable) + " "  + nputtxt6.get(1.0, "end-1c"))
#list7    
def copy_button19():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("SJ SPK " + str(variable) + " "  + nputtxt7.get(1.0, "end-1c"))
def copy_button20():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TR SPK " + str(variable) + " "  + nputtxt7.get(1.0, "end-1c"))
def copy_button21():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TGWSA SPK " +  str(variable) + " "  + nputtxt7.get(1.0, "end-1c"))
#list8
def copy_button22():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("SJ SPK " +  str(variable) + " "  + nputtxt8.get(1.0, "end-1c"))
def copy_button23():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TR SPK " +  str(variable) + " "  + nputtxt8.get(1.0, "end-1c"))
def copy_button24():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TGWSA SPK " +  str(variable) + " "  + nputtxt8.get(1.0, "end-1c"))
#list9    
def copy_button25():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("SJ SPK " +  str(variable) + " "  + nputtxt9.get(1.0, "end-1c"))
def copy_button26():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TR SPK " +  str(variable) + " "  + nputtxt9.get(1.0, "end-1c"))
def copy_button27():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TGWSA SPK " + str(variable) + " "  + nputtxt9.get(1.0, "end-1c"))
#list10
def copy_button28():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("SJ SPK " + str(variable) + " "  + nputtxt10.get(1.0, "end-1c"))
def copy_button29():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TR SPK " + str(variable) + " "  + nputtxt10.get(1.0, "end-1c"))
def copy_button30():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("TGWSA SPK " +str(variable) + " "  + nputtxt10.get(1.0, "end-1c"))

##########################
     #SKU BUTTONS DEF
##########################

def SJ_sku_button():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("B00D8KZH0M")
def TR_sku_button():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("B00BNPFXK8")
def TGWSA_sku_button():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("B08NGRJ278")

#####################
    #CHECK BOXES#
#####################  
A = 260
B = 50
C = 30

#list 1
var1 = IntVar()
C1 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var1)
C1_canvas1 = canvas1.create_window( A, B + C*1,anchor = "nw",window = C1)

var2 = IntVar()
C2 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var2)
C1_canvas1 = canvas1.create_window( A, B + C*2,anchor = "nw",window = C2)

var3 = IntVar()
C3 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var3)
C1_canvas1 = canvas1.create_window( A, B + C*3,anchor = "nw",window = C3)

#list 2
var4 = IntVar()
C4 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var4)
C4_canvas1 = canvas1.create_window( A, B + C*5,anchor = "nw",window = C4)

var5 = IntVar()
C5 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var5)
C1_canvas1 = canvas1.create_window( A, B + C*6,anchor = "nw",window = C5)

var6 = IntVar()
C6 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var6)
C1_canvas1 = canvas1.create_window( A, B + C*7,anchor = "nw",window = C6)

#list 3
var7 = IntVar()
C7 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var7)
C1_canvas1 = canvas1.create_window( A, B + C*9,anchor = "nw",window = C7)

var8 = IntVar()
C8 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var8)
C2_canvas1 = canvas1.create_window( A, B + C*10,anchor = "nw",window = C8)

var9 = IntVar()
C9 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var9)
C1_canvas1 = canvas1.create_window( A, B + C*11,anchor = "nw",window = C9)

#list 4
var10 = IntVar()
C10 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var10)
C2_canvas1 = canvas1.create_window( A, B + C*13,anchor = "nw",window = C10)

var11 = IntVar()
C11 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var11)
C1_canvas1 = canvas1.create_window( A, B + C*14,anchor = "nw",window = C11)

var12 = IntVar()
C12 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var12)
C2_canvas1 = canvas1.create_window( A, B + C*15,anchor = "nw",window = C12)

#list 5
var13 = IntVar()
C13 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var13)
C1_canvas1 = canvas1.create_window( A, B + C*17,anchor = "nw",window = C13)

var14 = IntVar()
C14 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var14)
C2_canvas1 = canvas1.create_window( A, B + C*18,anchor = "nw",window = C14)

var15 = IntVar()
C15 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var15)
C1_canvas1 = canvas1.create_window( A, B + C*19,anchor = "nw",window = C15)

#list 6
var16 = IntVar()
C16 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var16)
C2_canvas1 = canvas1.create_window( A, B + C*21,anchor = "nw",window = C16)

var17 = IntVar()
C17 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var17)
C1_canvas1 = canvas1.create_window( A, B + C*22,anchor = "nw",window = C17)

var18 = IntVar()
C18 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var18)
C2_canvas1 = canvas1.create_window( A, B + C*23,anchor = "nw",window = C18)

#list 7
var19 = IntVar()
C19 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var19)
C1_canvas1 = canvas1.create_window( A, B + C*25,anchor = "nw",window = C19)

var20 = IntVar()
C20 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var20)
C2_canvas1 = canvas1.create_window( A, B + C*26,anchor = "nw",window = C20)

var21 = IntVar()
C21 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var21)
C1_canvas1 = canvas1.create_window( A, B + C*27,anchor = "nw",window = C21)

#list 8
var22 = IntVar()
C22 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var22)
C2_canvas1 = canvas1.create_window( A, B + C*29,anchor = "nw",window = C22)

var23 = IntVar()
C23 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var23)
C1_canvas1 = canvas1.create_window( A, B + C*30,anchor = "nw",window = C23)

var24 = IntVar()
C24 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var24)
C2_canvas1 = canvas1.create_window( A, B + C*31,anchor = "nw",window = C24)

#list 9
var25 = IntVar()
C25 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var25)
C1_canvas1 = canvas1.create_window( A, B + C*33,anchor = "nw",window = C25)

var26 = IntVar()
C26 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var26)
C2_canvas1 = canvas1.create_window( A, B + C*34,anchor = "nw",window = C26)

var27 = IntVar()
C27 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var27)
C1_canvas1 = canvas1.create_window( A, B + C*35,anchor = "nw",window = C27)

#list 10
var28 = IntVar()
C28 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var28)
C2_canvas1 = canvas1.create_window( A, B + C*37,anchor = "nw",window = C28)

var29 = IntVar()
C29 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var29)
C1_canvas1 = canvas1.create_window( A, B + C*38,anchor = "nw",window = C29)

var30 = IntVar()
C30 = Checkbutton(canvas1, text="G2", bg= 'cyan', variable=var30)
C2_canvas1 = canvas1.create_window( A, B + C*39,anchor = "nw",window = C30)









###################
    #LIST NAME#
###################
A = 150
G = 50
H = 120
J = 44

list_name =  tkinter.Label     
nputtxt1 = tkinter.Text(canvas1,bd=3, width=20, height=-20)
canvas1.create_text(A, J + H*0, text="List Name", fill="black", font=('Helvetica 7 bold'))
inputtxt_canvas = canvas1.create_window( A, G + H*0,
                                       anchor = "nw",
                                       window = nputtxt1)

nputtxt2 = tkinter.Text(canvas1,bd=3, width=20, height=-20)
canvas1.create_text(A, J + H*1, text="List Name", fill="black", font=('Helvetica 7 bold'))
inputtxt_canvas = canvas1.create_window( A, G + H*1,
                                       anchor = "nw",
                                       window = nputtxt2)
nputtxt3 = tkinter.Text(canvas1,bd=3, width=20, height=-20)
canvas1.create_text(A, J + H*2, text="List Name", fill="black", font=('Helvetica 7 bold'))
inputtxt_canvas = canvas1.create_window( A, G + H*2,
                                       anchor = "nw",
                                       window = nputtxt3)
           
nputtxt4 = tkinter.Text(canvas1,bd=3, width=20, height=-20)
canvas1.create_text(A, J + H*3, text="List Name", fill="black", font=('Helvetica 7 bold'))
inputtxt_canvas = canvas1.create_window( A, G + H*3,
                                       anchor = "nw",
                                       window = nputtxt4)

nputtxt5 = tkinter.Text(canvas1,bd=3, width=20, height=-20)
canvas1.create_text(A, J + H*4, text="List Name", fill="black", font=('Helvetica 7 bold'))
inputtxt_canvas = canvas1.create_window( A, G + H*4,
                                       anchor = "nw",
                                       window = nputtxt5)
nputtxt6 = tkinter.Text(canvas1,bd=3, width=20, height=-20)
canvas1.create_text(A, J + H*5, text="List Name", fill="black", font=('Helvetica 7 bold'))
inputtxt_canvas = canvas1.create_window( A, G + H*5,
                                       anchor = "nw",
                                       window = nputtxt6)
           
nputtxt7 = tkinter.Text(canvas1,bd=3, width=20, height=-20)
canvas1.create_text(A, J + H*6, text="List Name", fill="black", font=('Helvetica 7 bold'))
inputtxt_canvas = canvas1.create_window( A, G + H*6,
                                       anchor = "nw",
                                       window = nputtxt7)

nputtxt8 = tkinter.Text(canvas1,bd=3, width=20, height=-20)
canvas1.create_text(A, J + H*7, text="List Name", fill="black", font=('Helvetica 7 bold'))
inputtxt_canvas = canvas1.create_window( A, G + H*7,
                                       anchor = "nw",
                                       window = nputtxt8)
nputtxt9 = tkinter.Text(canvas1,bd=3, width=20, height=-20)
canvas1.create_text(A, J + H*8, text="List Name", fill="black", font=('Helvetica 7 bold'))
inputtxt_canvas = canvas1.create_window( A, G + H*8,
                                       anchor = "nw",
                                       window = nputtxt9)
          
nputtxt10 = tkinter.Text(canvas1,bd=3, width=20, height=-20)
canvas1.create_text(A, J + H*9, text="List Name", fill="black", font=('Helvetica 7 bold'))
inputtxt_canvas = canvas1.create_window( A, G + H*9,
                                       anchor = "nw",
                                       window = nputtxt10)





#####################
    #COPY BUTTONS
##################### 
D = 320

#list1
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button1)
copyButton_canvas = canvas1.create_window( D, B + C*1, 
                                       anchor = "nw",
                                       window = copyButton)  
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button2)
copyButton_canvas2 = canvas1.create_window( D, B + C*2, 
                                       anchor = "nw",
                                       window = copyButton)
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button3)
copyButton_canvas3 = canvas1.create_window( D, B + C*3, 
                                       anchor = "nw",
                                       window = copyButton)
#list2
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button4)
copyButton_canvas = canvas1.create_window( D, B + C*5,
                                       anchor = "nw",
                                       window = copyButton)  
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button5)
copyButton_canvas2 = canvas1.create_window( D, B + C*6, 
                                       anchor = "nw",
                                       window = copyButton)
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button6)
copyButton_canvas3 = canvas1.create_window( D, B + C*7, 
                                       anchor = "nw",
                                       window = copyButton)
#list3
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button7)
copyButton_canvas = canvas1.create_window( D, B + C*9, 
                                       anchor = "nw",
                                       window = copyButton)  
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button8)
copyButton_canvas2 = canvas1.create_window( D, B + C*10,
                                       anchor = "nw",
                                       window = copyButton)
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button9)
copyButton_canvas3 = canvas1.create_window( D, B + C*11,
                                       anchor = "nw",
                                       window = copyButton)
#list4
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button10)
copyButton_canvas = canvas1.create_window( D, B + C*13,
                                       anchor = "nw",
                                       window = copyButton)  
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button11)
copyButton_canvas2 = canvas1.create_window( D, B + C*14,
                                       anchor = "nw",
                                       window = copyButton)
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button12)
copyButton_canvas3 = canvas1.create_window( D, B + C*15,
                                       anchor = "nw",
                                       window = copyButton)
#list5
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button13)
copyButton_canvas = canvas1.create_window( D, B + C*17, 
                                       anchor = "nw",
                                       window = copyButton)  
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button14)
copyButton_canvas2 = canvas1.create_window( D, B + C*18, 
                                       anchor = "nw",
                                       window = copyButton)
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button15)
copyButton_canvas3 = canvas1.create_window( D, B + C*19,
                                       anchor = "nw",
                                       window = copyButton)
#list6
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button16)
copyButton_canvas = canvas1.create_window( D, B + C*21, 
                                       anchor = "nw",
                                       window = copyButton)  
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button17)
copyButton_canvas2 = canvas1.create_window( D, B + C*22, 
                                       anchor = "nw",
                                       window = copyButton)
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button18)
copyButton_canvas3 = canvas1.create_window( D, B + C*23,
                                       anchor = "nw",
                                       window = copyButton)
#list7
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button19)
copyButton_canvas = canvas1.create_window( D, B + C*25,
                                       anchor = "nw",
                                       window = copyButton)  
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button20)
copyButton_canvas2 = canvas1.create_window( D, B + C*26, 
                                       anchor = "nw",
                                       window = copyButton)
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button21)
copyButton_canvas3 = canvas1.create_window( D, B + C*27,
                                       anchor = "nw",
                                       window = copyButton)
#list8
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button22)
copyButton_canvas = canvas1.create_window( D, B + C*29, 
                                       anchor = "nw",
                                       window = copyButton)  
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button23)
copyButton_canvas2 = canvas1.create_window( D, B + C*30, 
                                       anchor = "nw",
                                       window = copyButton)
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button24)
copyButton_canvas3 = canvas1.create_window( D, B + C*31,
                                       anchor = "nw",
                                       window = copyButton)
#list9
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button25)
copyButton_canvas = canvas1.create_window( D, B + C*33, 
                                       anchor = "nw",
                                       window = copyButton)  
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button26)
copyButton_canvas2 = canvas1.create_window( D, B + C*34, 
                                       anchor = "nw",
                                       window = copyButton)
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button27)
copyButton_canvas3 = canvas1.create_window( D, B + C*35, 
                                       anchor = "nw",
                                       window = copyButton)
#list10
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button28)
copyButton_canvas = canvas1.create_window( D, B + C*37, 
                                       anchor = "nw",
                                       window = copyButton)  
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button29)
copyButton_canvas2 = canvas1.create_window( D, B + C*38,
                                       anchor = "nw",
                                       window = copyButton)
copyButton = tkinter.Button(canvas1,
                        text = "Copy", 
                        command = copy_button30)
copyButton_canvas3 = canvas1.create_window( D, B + C*39,
                                       anchor = "nw",
                                       window = copyButton)



####################
    #SKU BUTTONS
#################### 

SKU_Button = tkinter.Button(canvas2,bd=3,
                        text = "SJ SKU", 
                        command = SJ_sku_button)
SKU_Button_canvas = canvas2.create_window( 120, 20, 
                                       anchor = "ne",
                                       window = SKU_Button)  
SKU_Button = tkinter.Button(canvas2,bd=3,
                        text = "TR SKU", 
                        command = TR_sku_button)
SKU_Button_canvas2 = canvas2.create_window( 120, 50, 
                                       anchor = "ne",
                                       window = SKU_Button)
SKU_Button = tkinter.Button(canvas2,bd=3,
                        text = "TGWSA SKU", 
                        command = TGWSA_sku_button)
SKU_Button_canvas3 = canvas2.create_window( 120, 80, 
                                       anchor = "ne",
                                       window = SKU_Button)  




 
frame.mainloop()

