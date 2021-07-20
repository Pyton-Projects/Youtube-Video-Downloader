
from  tkinter import*
from tkinter import messagebox
import pafy
from tkinter.ttk import Progressbar,Combobox
from tkinter import filedialog
import threading
import os
root=Tk()
total_12=0
value=StringVar()
value.set('')
def saveas():
    global saveas
    saveas = filedialog.asksaveasfile(filetype=(("mp4","*.mp4"),('mp4','*.mp4')),title='Save Mp4 File')
def call(total, recvd, ratio, rate, eta):
    global total12
    r=('{0:.2f}'.format(ratio*100))
    r1=('{0:.2f}'.format(total/1e+6))
    try:
        value.set(ratio*100)
        percentage_dowload.config(text=f"Percentage Downloaded:{r}%")
        time_left_lab.config(text=f'Time Left: {eta} Sec')
        file_size_lab.config(text=f'File Size: {r1} MB')
        total12 = float('{:.5}'.format(total/(1024*1024)))
        l.configure(maximum=total12)
        l['value'] = recvd/(1024*1024)
        if ratio*100==100.00:
            l.stop()
            time_left_lab.config(text=f'')
            percentage_dowload.config(text=f"")
            leree.config(text=f'')
            file_size_lab.config(text=f'')
    except ValueError:
        pass
times_called=0
def down_Video():
    url=input_entry.get()
    try:
        dir=filedialog.askdirectory()
        os.chdir(str(dir))

        p = pafy.new(url)
        leree.config(text=f'Video:-{p.title}')
        ba = p.getbest()
        filename = ba.download(quiet=True, callback=call)
        start['state']=ACTIVE
        messagebox.showinfo('Info',f'{p.title} Video Downloaded At {dir}.')
        input_entry.delete(0,END)
    except ValueError:
        start['state']=ACTIVE
        messagebox.showinfo('Info','Please Enter A Valid Url!! Or Check The Net Work Connection.')
def audio():
    url=input_entry.get()
    try:
        dir=filedialog.askdirectory()
        os.chdir(str(dir))
        p = pafy.new(url)
        leree.config(text=f'Video:-{p.title}')
        ba = p.getbestaudio()
        filename = ba.download(quiet=True, callback=call)
        start['state']=ACTIVE
        messagebox.showinfo('Info',f'{p.title} Audio Downloaded At {dir}')
        input_entry.delete(0,END)
    except ValueError:
        start['state']=ACTIVE
        messagebox.showinfo('Info','Please Enter A Valid Url!! Or Check The Net Work Connection.')
def download_procees():
    if data_of_qual.get()=='Audio Only':
        start['state']='disabled'
        threading.Thread(target=audio).start()
    else:
        start['state']='disabled'
        threading.Thread(target=down_Video).start()
menus.add_cascade(label='File',menu=m1,)
root.geometry('700x400')
Heading=Label(root,text='''Youtube Video Downloader''',font=('Arial Rounded MT bold',25,'bold'),fg='red')
Heading.pack()
put_here=Label(root,text='Enter The Video URL:',font=('Arial Rounded MT bold',20,'bold'),fg='darkblue')
put_here.place(y=50)
data=StringVar()
input_entry=Entry(root,width=35,textvariable=data,fg='grey',font=('Arial',15,'bold'))
input_entry.place(y=100)
start=Button(root,text='Start Download',bg='black',fg='white',activebackground='black',activeforeground='white',font=('Algerian',15),command=download_procees)
start.place(x=116+50+30,y=150)
qualites=('144p','240p','360p','480p','720p','Audio Only')
data_of_qual=StringVar()
data_of_qual.set('360p')
g=Combobox(root,textvariable=data_of_qual,values=qualites,state='readonly',font=('Arial',13)).place(y=101,x=400)
quality=Label(root,text='Quality:',font=('Arial',15,'bold'),fg='darkblue').place(x=450,y=65)
root.title('YouTube Video Downloader')
percentage_dowload=Label(root,text='',font=('Font',15),fg='darkblue')
percentage_dowload.place(y=250+45,x=180)
leree=Label(root,text='',font=('Font',15),fg='darkblue')
leree.place(y=210,x=1)
l=Progressbar(root,mode='determinate',length=300,maximum=total_12)
l.place(y=250,x=165)
time_left_lab=Label(root,text='343',font=('Font',15),fg='darkblue')
time_left_lab.place(y=250+45+45,x=150)#
file_size_lab=Label(root,text='',font=('Font',15),fg='darkblue')
file_size_lab.place(x=375,y=250+45+45)
mainloop()
