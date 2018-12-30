#frontend
from tkinter import *
import backend

#event is the object which th ebind method expects the fucntion to have
def get_selected_item(event):
    global selected_item
    cmd_clear()
    try:
        index=lb.curselection()
        print(lb.get(index))
        selected_item=lb.get(index)
    #display sttributes in respective entries
        tb1.insert(END,selected_item[1])
        tb2.insert(END,selected_item[2])
        tb3.insert(END,selected_item[3])
        tb4.insert(END,selected_item[4])
        return selected_item
    except:
        pass

def cmd_add():
    try:
        backend.add(title=scan_title.get(),author=scan_author.get(),year=int(scan_year.get()),isbn=int(scan_isbn.get()))
        cmd_view()
    except:
        pass
def cmd_view():
    lb.delete(0,END)
    #print(backend.view())
    for record in backend.view():
        lb.insert(END,record)

def cmd_delete():
    backend.del_id(selected_item[0])
    cmd_view()

def cmd_update():
    backend.update(id=selected_item[0],title=scan_title.get(),author=scan_author.get(),year=int(scan_year.get()),isbn=int(scan_isbn.get()))
    cmd_view()

def cmd_search():
    lb.delete(0,END)
    #print((backend.search(title=tb1.get(),author=tb2.get(),year=tb3.get(),isbn=tb4.get())))
#we need to iterate throygh the list of tuples return ,so that we can insert it inot a Listbox
#the scan_object is not a simple string .therfore if we use get()on it.it will be coverted to string
    for item in backend.search(title=scan_title.get(),author=scan_author.get(),year=scan_year.get(),isbn=scan_isbn.get()):
        lb.insert(END,item)

def cmd_clear():
    tb1.delete(0,END)
    tb2.delete(0,END)
    tb3.delete(0,END)
    tb4.delete(0,END)
    #lb.delete(0,END)
win=Tk()

l1=Label(win,text="title")
l1.grid(row=0,column=0)

scan_title=StringVar()
tb1=Entry(win,textvariable=scan_title)
tb1.grid(row=0,column=1)

l2=Label(win,text="author")
l2.grid(row=0,column=2)

scan_author=StringVar()
tb2=Entry(win,textvariable=scan_author)
tb2.grid(row=0,column=3)

l3=Label(win,text="year")
l3.grid(row=1,column=0)

scan_year=StringVar()
tb3=Entry(win,textvariable=scan_year)
tb3.grid(row=1,column=1)

l4=Label(win,text="isbn")
l4.grid(row=1,column=2)

scan_isbn=StringVar()
tb4=Entry(win,textvariable=scan_isbn)
tb4.grid(row=1,column=3)


sb=Scrollbar(win)
sb.grid(row=2,column=2,rowspan=5)
lb=Listbox(height=8,width=40)
lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)
lb.grid(row=2,rowspan=5,columnspan=2)
#bind selected list item
lb.bind('<<ListboxSelect>>',get_selected_item)

#buttons
b=Button(win,text="clear fields",command=cmd_clear)
b.grid(row=0,column=4)

#win.destroy will exit th eapplication
b1=Button(win,text="close",width=7,command=win.destroy)
b1.grid(row=1,column=4)

b2=Button(win,text="view all",width=25,justify=CENTER,command=cmd_view)
b2.grid(row=2,columnspan=2,column=3)

b3=Button(win,text="search",width=25,justify=CENTER,command=cmd_search)
b3.grid(row=3,columnspan=2,column=3)

b4=Button(win,text="add a book",width=25,justify=CENTER,command=cmd_add)
b4.grid(row=4,columnspan=2,column=3)

b5=Button(win,text="update selected ",width=25,justify=CENTER,command=cmd_update)
b5.grid(row=5,columnspan=2,column=3)

b6=Button(win,text="delete selected",width=25,justify=CENTER,command=cmd_delete)
b6.grid(row=6,columnspan=2,column=3)


win.mainloop()
