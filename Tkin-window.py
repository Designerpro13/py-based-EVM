from tkinter import *
#import logpg1


root=Tk()
screen_resol=str(root.winfo_screenheight()) +'x'+str(root.winfo_screenwidth())
root.title('Chunav Yantre')
root['bg']='#a9ebf4'
root.geometry(screen_resol)
label=Label(root,text='WELCOME TO CHUNAV YANTRE', bg='cyan').pack()
label=Label(root,text='Poll running...', bg='cyan').pack()

root.mainloop()
