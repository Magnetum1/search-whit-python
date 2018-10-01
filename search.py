#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.16
# In conjunction with Tcl version 8.6
#    Sep 22, 2018 11:59:53 PM -0300  platform: Windows NT

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.frame = BrowqShop(self)
        self.frame.pack()

    def change(self, frame):
        self.frame.pack_forget()
        self.frame = frame(self)
        self.frame.pack()



class BrowqShop(Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
#Search 
        def busca():
            client = self.Entry1.get()
            if client == "Kurium":
                self.master.change(kurium)
                self.Label1.destroy()
                self.Label1_1.destroy()
                self.Entry1.destroy()
                self.Label2.destroy()
               	self.Label3.destroy()
               	self.Button1.destroy()
            elif client == "kurium":
                self.master.change(kurium)
                self.Label1.destroy()
                self.Label1_1.destroy()
                self.Entry1.destroy()
                self.Label2.destroy()
               	self.Label3.destroy()
               	self.Button1.destroy()
            elif client == "bape":
                self.master.change(bape)
                self.Label1.destroy()
                self.Label1_1.destroy()
                self.Entry1.destroy()
                self.Label2.destroy()
               	self.Label3.destroy()
               	self.Button1.destroy()
            elif client == "Bape":
                self.master.change(bape)
                self.Label1.destroy()
                self.Label1_1.destroy()
                self.Entry1.destroy()
                self.Label2.destroy()
               	self.Label3.destroy()
               	self.Button1.destroy()
            else:
               print("error")
            
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Trebuchet MS} -size 12 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        master.resizable(0,0)
        master.geometry("421x337+514+171")
        master.title("Browq Shop")
        master.configure(background="#161616")
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="#000000")



        self.Label1 = Label(master)
        self.Label1.place(relx=0.1, rely=0.12, height=41, width=334)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#191991")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Welcome to Browq Store''')

        self.Label1_1 = Label(master)
        self.Label1_1.place(relx=0.1, rely=0.33, height=41, width=334)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="#000000")
        self.Label1_1.configure(background="#191991")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font=font9)
        self.Label1_1.configure(foreground="#ffffff")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''What do you seek?''')

        self.Entry1 = Entry(master)
        self.Entry1.place(relx=0.19, rely=0.56,height=20, relwidth=0.63)
        self.Entry1.configure(background="#bfbfbf")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="black")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Button1 = Button(master)
        self.Button1.place(relx=0.19, rely=0.74, height=24, width=267)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#4a64ba")
        self.Button1.configure(command=busca)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Buscar Strings''')

        self.Label2 = Label(master)
        self.Label2.place(relx=0.02, rely=0.47, height=121, width=64)
        self.Label2.configure(background="#161616")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self._img1 = PhotoImage(file="./icons8-livre-de-spyware-filled-50.png")
        self.Label2.configure(image=self._img1)
        self.Label2.configure(text='''Label''')
        self.Label2.configure(width=64)

        self.menubar = Menu(master,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        master.configure(menu = self.menubar)



        self.Label3 = Label(master)
        self.Label3.place(relx=0.86, rely=0.5, height=101, width=54)
        self.Label3.configure(background="#161616")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self._img2 = PhotoImage(file="./icons8-hacker-50.png")
        self.Label3.configure(image=self._img2)
        self.Label3.configure(text='''Label''')
        self.Label3.configure(width=54)


class bape(Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        def voltar():
            self.master.change(BrowqShop)
            self.Listbox1.destroy()
            self.voltar.destroy()
            sys.stdout.flush()    	

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font11 = "-family {Viner Hand ITC} -size 12 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"

        master.geometry("470x441+460+157")
        master.title("Result")
        master.configure(background="#111111")
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="black")

        self.Listbox1 = Listbox(master)
        self.Listbox1.insert(0,"trumpclientftw_bape_ggM")
        self.Listbox1.insert(1,"trumpclientftw_bape_ggF")
        self.Listbox1.insert(2,"trumpclientftw_bape_gg`J")
        self.Listbox1.insert(3,"trumpclientftw_bape_ggP")
        self.Listbox1.insert(4,"trumpclientftw_bape_ggT")
        self.Listbox1.insert(5,"trumpclientftw_bape_ggw")
        self.Listbox1.insert(6,"trumpclientftw_bape_ggcK")
        self.Listbox1.insert(7,"trumpclientftw_bape_gga0")
        self.Listbox1.insert(8,"trumpclientftw_bape_gga1")
        self.Listbox1.insert(9,"trumpclientftw_bape_ggd6")
        self.Listbox1.insert(10,"trumpclientftw_bape_gga3")
        self.Listbox1.insert(11,"trumpclientftw_bape_ggay")
        self.Listbox1.insert(12,"trumpclientftw_bape_ggco")
        self.Listbox1.insert(13,"trumpclientftw_bape_ggm")
        self.Listbox1.insert(14,"trumpclientftw_bape_ggn")
        self.Listbox1.insert(15,"trumpclientftw_bape_ggl")
        self.Listbox1.insert(16,"trumpclientftw_bape_gg8")  
        self.Listbox1.insert(0,"trumpclientftw_bape_ggdw")
        self.Listbox1.insert(1,"trumpclientftw_bape_ggax")
        self.Listbox1.insert(2,"trumpclientftw_bape_ggbD")
        self.Listbox1.insert(3,"trumpclientftw_bape_ggcM")
        self.Listbox1.insert(4,"trumpclientftw_bape_ggbY")
        self.Listbox1.insert(5,"trumpclientftw_bape_ggdf")
        self.Listbox1.insert(6,"trumpclientftw_bape_ggbr")
        self.Listbox1.insert(7,"trumpclientftw_bape_ggr")
        self.Listbox1.insert(8,"trumpclientftw_bape_gge")
        self.Listbox1.insert(9,"trumpclientftw_bape_ggu")
        self.Listbox1.insert(10,"trumpclientftw_bape_ggbs")

        self.Listbox1.place(relx=0.13, rely=0.07, relheight=0.62, relwidth=0.73)
        self.Listbox1.configure(background="#1867a3")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.configure(width=344)

        self.voltar = Button(master)
        self.voltar.place(relx=0.21, rely=0.82, height=44, width=267)
        self.voltar.configure(activebackground="#1867a3")
        self.voltar.configure(activeforeground="white")
        self.voltar.configure(activeforeground="#000000")
        self.voltar.configure(background="#1867a3")
        self.voltar.configure(command=voltar)
        self.voltar.configure(disabledforeground="#a3a3a3")
        self.voltar.configure(font=font11)
        self.voltar.configure(foreground="#000000")
        self.voltar.configure(highlightbackground="#d9d9d9")
        self.voltar.configure(highlightcolor="black")
        self.voltar.configure(pady="0")
        self.voltar.configure(text='''Back''')
        self.voltar.configure(width=267)








#Kurium

class kurium(Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        def voltar():
            self.master.change(BrowqShop)
            self.Listbox1.destroy()
            self.voltar.destroy()
            sys.stdout.flush()    	

        Frame.__init__(self, master, **kwargs)
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font11 = "-family {Viner Hand ITC} -size 12 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"

        master.geometry("470x441+460+157")
        master.title("Result")
        master.configure(background="#111111")
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="black")

        self.Listbox1 = Listbox(master)
        self.Listbox1.insert(0,"10.10.10.40")
        self.Listbox1.insert(1,"memememememem ")
        self.Listbox1.insert(2,"10.10.80")
        self.Listbox1.insert(3,"10.10.10.30")
        self.Listbox1.insert(3,"10.10.10.80.60")
        self.Listbox1.insert(3,"10.10.10.80.0")
        self.Listbox1.insert(3,"10.10.10.80.40")
        self.Listbox1.insert(3,"10.10.10.10")
        self.Listbox1.insert(3,"10.10.2.10")
        self.Listbox1.insert(3,"10.10.80.40")
        self.Listbox1.insert(3,"10.10.80.0")
        self.Listbox1.insert(3,"array2")

        self.Listbox1.place(relx=0.13, rely=0.07, relheight=0.62, relwidth=0.73)
        self.Listbox1.configure(background="#1867a3")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.configure(width=344)

        self.voltar = Button(master)
        self.voltar.place(relx=0.21, rely=0.82, height=44, width=267)
        self.voltar.configure(activebackground="#1867a3")
        self.voltar.configure(activeforeground="white")
        self.voltar.configure(activeforeground="#000000")
        self.voltar.configure(background="#1867a3")
        self.voltar.configure(command=voltar)
        self.voltar.configure(disabledforeground="#a3a3a3")
        self.voltar.configure(font=font11)
        self.voltar.configure(foreground="#000000")
        self.voltar.configure(highlightbackground="#d9d9d9")
        self.voltar.configure(highlightcolor="black")
        self.voltar.configure(pady="0")
        self.voltar.configure(text='''Back''')
        self.voltar.configure(width=267)


        


app=Application()
app.mainloop()