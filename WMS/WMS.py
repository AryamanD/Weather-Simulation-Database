from tkinter import *
from tkinter import ttk
import ctypes
from PIL import ImageTk,Image
import mysql.connector
ctypes.windll.shcore.SetProcessDpiAwareness(1)
Combo = None
attribute = None
attribute1 = None
attribute2 = None
warning  = None
entry = None
entry1 = None
entry2 = None
flag = 0
s = 0
c = 0
p = 0
e = 0
u = 0
q = 0
VB1 = None
counts = None
procedure = None
frame = None
pframe = None
insert = None
delete = None
update = None
m_ide = None
m_namee = None
m_typee = None
launch_datee = None
done_datee = None
coste = None
t_ide = None
t_namee = None
deg_celsiuse = None
s_ide = None
s_namee = None
s_locatione = None
team_ide = None
a_id1e = None
a_name1e = None
a_id2e = None
a_name2e = None
a_id3e = None
a_name3e = None
codee = None
namee = None
Classe = None
def Update():
    global myDB, attribute1, attribute2, entry1, entry2, e, u
    Choice = attribute1.get()
    Choice1 = attribute2.get()
    value = entry1.get()
    value1 = entry2.get()
    table = "missions"
    if Choice1 == "s_name" or Choice1 == "s_location":
        table = "satellites"
    elif Choice1 == "a_id1" or Choice1 == "a_name1" or Choice1 == "a_id2" or Choice1 == "a_name2" or Choice1 == "a_id3" or Choice1 == "a_name3":
        table = "teams"
    elif Choice1 == "name" or Choice1 == "class":
        table = "spacecrafts"
    try:
        myDB = mysql.connector.connect(host = "localhost", username = "root", password = "mysequel",database = "project")
        cursor = myDB.cursor()
        if value1.isdigit() and value.isdigit():
            cursor.execute(f"update {table} set {Choice1} = %s where {Choice} = %s",(int(value1),int(value)))
            myDB.commit()
        elif value1.isdigit():
            cursor.execute(f"update {table} set {Choice1} = %s where {Choice} = %s",(int(value1),value))
            myDB.commit()
        elif value.isdigit():
            cursor.execute(f"update {table} set {Choice1} = %s where {Choice} = %s",(value1,int(value)))
            myDB.commit()
        else:
            cursor.execute(f"update {table} set {Choice1} = %s where {Choice} = %s",(value1, value))
            myDB.commit()
    except:
        i = 0
        for widget in root.winfo_children():
            if i!=3:
                i=i+1
                continue
            widget.destroy()
        UpdateData(1)
    if cursor.rowcount > 0:
        Display(4)
    else:
        UpdateData(1)
def UpdateData(plag):
    global insert, delete, update, VB1, attribute1, attribute2, entry1, entry2, pframe, u, q, warning
    insert.destroy()
    delete.destroy()
    update.destroy()
    if u == 1:
        u=0
        warning.destroy()
    if plag == 1:
        u = 1
        pframe.destroy()
        warning = Label(root, text = "Entries not Valid! Try again", font = ("",12,""))
        warning.pack()
    if plag == 2:
        u = 1
        pframe.destroy()
        warning = Label(root, text = "Record(s) found and Updated Successfully!", font = ("",12,""))
        warning.pack()
    pframe = Frame(root)
    pframe.pack(pady = 3)
    frame = Frame(pframe)
    frame.pack(side = LEFT)
    frame1 = Frame(pframe)
    frame1.pack(side = RIGHT)
    if q == 1:
        VB1.destroy()
        q = 0
    select = Label(frame, text = "Search by:", font = ("",12,""))
    select.pack()
    attribute1 = ttk.Combobox(frame, values = ["m_id","m_name","m_type","launch_date","done_date","cost","s_id","team_id","code"])
    attribute1.pack(pady = 15)
    attribute1.set("m_id")
    sel = Label(frame, text = "Enter Value", font = ("",12,""))
    sel.pack()
    entry1 = Entry(frame, width = 23)
    entry1.pack(padx = 20, pady = 15)
    select = Label(frame1, text = "Update:", font = ("",12,""))
    select.pack()
    attribute2 = ttk.Combobox(frame1, values = ["m_id","m_name","m_type","launch_date","done_date","cost","s_name","s_location","a_id1","a_name1","a_id2","a_name2","a_id3","a_name3","name","class"])
    attribute2.pack(pady = 15)
    attribute2.set("m_id")
    sel = Label(frame1, text = "Enter New Value", font = ("",12,""))
    sel.pack()
    entry2 = Entry(frame1, width = 23)
    entry2.pack(padx = 20, pady = 15)
    update = Button(root, text = "Update", width = 10, font = ("",12,""), command = Update)
    update.pack(pady = 10)
    VB1 = Button(root, text = "Back", width = 10, font = ("",12,""),command = lambda: Display(1))
    VB1.pack(pady = 5)
def Delete():
    global myDB, attribute, entry, e
    Choice = attribute.get()
    value = entry.get()
    myDC = mysql.connector.connect(host = "localhost", username = "root", password = "mysequel",database = "project")
    cursor = myDC.cursor()
    cursor.execute("call record_count()")
    result = cursor.fetchall()
    for i in result:
        num = i[0]
    try:
        cursor = myDB.cursor()
        if value.isdigit():
            cursor.execute(f"delete from missions where {Choice} = %s",(int(value),))
            myDB.commit()
        else:
            cursor.execute(f"delete from missions where {Choice} = %s",(value,))
            myDB.commit()
    except:
        i = 0
        for widget in root.winfo_children():
            if i!=3:
                i=i+1
                continue
            widget.destroy()
        DeleteData(1)
    myDD = mysql.connector.connect(host = "localhost", username = "root", password = "mysequel",database = "project")
    cursor = myDD.cursor()
    cursor.execute("call record_count()")
    result = cursor.fetchall()
    for i in result:
        num1 = i[0]
    if num == num1:
        i = 0
        for widget in root.winfo_children():
            if i!=3:
                i=i+1
                continue
            widget.destroy()
        DeleteData(1)    
    else:
        Display(3)    
def DeleteData(clag):
    global delete, VB1, q, attribute, entry, update
    insert.destroy()
    delete.destroy()
    update.destroy()
    if q == 1:
        VB1.destroy()
        q = 0
    if clag == 1:
        warning = Label(root, text = "Entries not Valid! Try again", font = ("",12,""))
        warning.pack(pady = 5)
    if clag == 2:
        warning = Label(root, text = "Record(s) found and Deleted Successfully!", font = ("",12,""))
        warning.pack(pady = 5)
    select = Label(root, text = "Search by:", font = ("",12,""))
    select.pack()
    attribute = ttk.Combobox(root, values = ["m_id","m_name","m_type","launch_date","done_date","cost","t_id","s_id","team_id","code"])
    attribute.pack(pady = 15)
    attribute.set("m_id")
    sel = Label(root, text = "Enter Value", font = ("",12,""))
    sel.pack()
    entry = Entry(root, width = 23)
    entry.pack(pady = 15)
    delete = Button(root, text = "Delete", width = 10, font = ("",12,""), command = Delete)
    delete.pack()
    VB1 = Button(root, text = "Back", width = 10, font = ("",12,""),command = lambda: Display(1))
    VB1.pack(pady = 15)
def count(Choice):
    global c, myDB, counts, VB1
    i=0
    for widget in root.winfo_children():
        if i!=4:
            i=i+1
            continue
        widget.destroy()
    c = 1
    if Choice == "temperatures":
        num = 7
    else:
        cursor = myDB.cursor()
        cursor.execute("call record_count()")
        Result = cursor.fetchall()
        for i in Result:
            num = i[0]
    counts = Label(root, text = "The total number of records are: " + str(num), font = ("",12,""))
    counts.pack()  
    VB1 = Button(root, text = "Back", width = 10, font = ("",12,""),command = Home)
    VB1.pack(pady = 15)
def Insert():
    global insert, delete, s, VB1,Classe,namee,codee,a_name3e,a_id3e,a_name2e,a_id2e,a_name1e,a_id1e,team_ide,s_locatione,s_namee,s_ide,deg_celsiuse,t_namee,t_ide,coste,done_datee,launch_datee,m_typee,m_namee,m_ide
    try:
        cursor = myDB.cursor()
        cursor.execute("insert into missions values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(int(m_ide.get()),m_namee.get(),m_typee.get(),launch_datee.get(),done_datee.get(),int(coste.get()),int(t_ide.get()),int(s_ide.get()),int(team_ide.get()),int(codee.get())))
        myDB.commit()
    except:
        i = 0
        for widget in root.winfo_children():
            if i!=3:
                i=i+1
                continue
            widget.destroy()
        InsertData(1)
    try:
        cursor = myDB.cursor()
        cursor.execute("insert into satellites values(%s,%s,%s)",(int(s_ide.get()),s_namee.get(),s_locatione.get()))
        myDB.commit()
    except:
        i = 0
        for widget in root.winfo_children():
            if i!=3:
                i=i+1
                continue
            widget.destroy()
        InsertData(1)
    try:
        cursor = myDB.cursor()
        cursor.execute("insert into spacecrafts values(%s,%s,%s)",(int(codee.get()),namee.get(),Classe.get()))
        myDB.commit()
    except:
        i = 0
        for widget in root.winfo_children():
            if i!=3:
                i=i+1
                continue
            widget.destroy()
        InsertData(1)
    try:
        cursor = myDB.cursor()
        cursor.execute("insert into teams values(%s,%s,%s,%s,%s,%s,%s)",(int(team_ide.get()),int(a_id1e.get()),a_name1e.get(),int(a_id2e.get()),a_name2e.get(),int(a_id3e.get()),a_name3e.get()))
        myDB.commit()
        s = 1
    except:
        i = 0
        for widget in root.winfo_children():
            if i!=3:
                i=i+1
                continue
            widget.destroy()
        InsertData(1) 
    if s==1:
        s=0
        Display(2)
def InsertData(slag):
    global insert, q, delete, update, VB1,Classe,namee,codee,a_name3e,a_id3e,a_name2e,a_id2e,a_name1e,a_id1e,team_ide,s_locatione,s_namee,s_ide,deg_celsiuse,t_namee,t_ide,coste,done_datee,launch_datee,m_typee,m_namee,m_ide, pframe
    insert.destroy()
    delete.destroy()
    update.destroy()
    if q==1:
        VB1.destroy()
        q=0
    pppframe = Frame(root)
    pppframe.pack()
    ppframe = Frame(pppframe)
    ppframe.pack(side=LEFT)
    pframe = Frame(ppframe)
    pframe.pack(side=LEFT)
    pframe1 = Frame(ppframe)
    pframe1.pack(side=RIGHT)
    pframe2= Frame(pppframe)
    pframe2.pack(side=RIGHT)
    frame=Frame(pframe)
    frame.pack(side=LEFT)
    frame1 = Frame(pframe)
    frame1.pack(side=RIGHT)
    frame2=Frame(pframe1)
    frame2.pack(side=LEFT)
    frame3 = Frame(pframe1)
    frame3.pack(side=RIGHT)
    frame4=Frame(pframe2)
    frame4.pack(side=LEFT)
    frame5 = Frame(pframe2)
    frame5.pack(side=RIGHT)
    m_id = Label(frame, text = "Mission Id", font = ("",10,""))
    m_id.pack()
    m_ide = Entry(frame, width = 15)
    m_ide.pack(padx = 25, pady = 5)
    m_name = Label(frame, text = "Mission Name", font = ("",10,""))
    m_name.pack(pady = 5)
    m_namee = Entry(frame, width = 15)
    m_namee.pack(pady = 5)
    m_type = Label(frame, text = "Mission Type", font = ("",10,""))
    m_type.pack(pady = 5)
    m_typee = Entry(frame, width = 15)
    m_typee.pack(pady = 5)
    launch_date = Label(frame, text = "Launch Date", font = ("",10,""))
    launch_date.pack(pady = 5)
    launch_datee = Entry(frame, width = 15)
    launch_datee.pack(pady = 5)
    done_date = Label(frame1, text = "Done Date", font = ("",10,""))
    done_date.pack()
    done_datee = Entry(frame1, width = 15)
    done_datee.pack(padx = 25, pady = 5)
    cost = Label(frame1, text = "Cost", font = ("",10,""))
    cost.pack(pady = 5)
    coste = Entry(frame1, width = 15)
    coste.pack(pady = 5)
    t_id = Label(frame1, text = "Temperature Id", font = ("",10,""))
    t_id.pack(pady = 5)
    t_ide = Entry(frame1, width = 15)
    t_ide.pack(pady = 5)
    #t_name = Label(frame1, text = "Temperature Name", font = ("",10,""))
    #t_name.pack(pady = 5)
    #t_namee = Entry(frame1, width = 15)
    #t_namee.pack(pady = 5)
    #deg_celsius = Label(frame1, text = "Degrees Celsius", font = ("",10,""))
    #deg_celsius.pack()
    #deg_celsiuse = Entry(frame1, width = 15)
    #deg_celsiuse.pack(padx = 25, pady = 5)
    s_id = Label(frame1, text = "Satellite Id", font = ("",10,""))
    s_id.pack(pady = 5)
    s_ide = Entry(frame1, width = 15)
    s_ide.pack(pady = 5)
    s_name = Label(frame2, text = "Satellite Name", font = ("",10,""))
    s_name.pack()
    s_namee = Entry(frame2, width = 15)
    s_namee.pack(pady = 5)
    s_location = Label(frame2, text = "Satellite Location", font = ("",10,""))
    s_location.pack(pady = 5)
    s_locatione = Entry(frame2, width = 15)
    s_locatione.pack(pady = 5)
    team_id = Label(frame2, text = "Team Id", font = ("",10,""))
    team_id.pack(pady = 5)
    team_ide = Entry(frame2, width = 15)
    team_ide.pack(padx = 25, pady = 5)
    a_id1 = Label(frame2, text = "Astronaut1 Id", font = ("",10,""))
    a_id1.pack(pady = 5)
    a_id1e = Entry(frame2, width = 15)
    a_id1e.pack(pady = 5)
    a_name1 = Label(frame3, text = "Astronaut1 Name", font = ("",10,""))
    a_name1.pack()
    a_name1e = Entry(frame3, width = 15)
    a_name1e.pack(pady = 5)
    a_id2 = Label(frame3, text = "Astronaut2 Id", font = ("",10,""))
    a_id2.pack(pady = 5)
    a_id2e = Entry(frame3, width = 15)
    a_id2e.pack(pady = 5)
    a_name2 = Label(frame3, text = "Astronaut2 Name", font = ("",10,""))
    a_name2.pack(pady = 5)
    a_name2e = Entry(frame3, width = 15)
    a_name2e.pack(padx = 25,pady = 5)
    a_id3 = Label(frame3, text = "Astronaut3 Id", font = ("",10,""))
    a_id3.pack(pady = 5)
    a_id3e = Entry(frame3, width = 15)
    a_id3e.pack(pady = 5)
    a_name3 = Label(frame4, text = "Astronaut3 Name", font = ("",10,""))
    a_name3.pack()
    a_name3e = Entry(frame4, width = 15)
    a_name3e.pack(pady = 5)
    code = Label(frame4, text = "Spacecraft Code", font = ("",10,""))
    code.pack(pady = 5)
    codee = Entry(frame4, width = 15)
    codee.pack(pady = 5)
    name = Label(frame4, text = "Spacecraft Name", font = ("",10,""))
    name.pack(pady = 5)
    namee = Entry(frame4, width = 15)
    namee.pack(padx = 25, pady = 5)
    Class = Label(frame4, text = "Spacecraft Class", font = ("",10,""))
    Class.pack(pady = 5)
    Classe = Entry(frame4, width = 15)
    Classe.pack(pady = 5)
    if slag == 1:
        Error = Label(frame5, text = "Incorrect Data!\nPlease Retry!",font = ("",10,""))
        Error.pack()
    if slag == 2:
        Success = Label(frame5, text = "Data Inserted!\nSuccessfully!",font = ("",10,""))
        Success.pack()
    insertdata = Button(frame5, text = "Insert", width = 10, font = ("",12,""),command = Insert)
    insertdata.pack(pady = 15)
    VB2 = Button(frame5, text = "Back", width = 10, font = ("",12,""),command = lambda: Display(1))
    VB2.pack()
def Display(glag):
    global Combo, flag, VB1, frame, insert, delete, update, myDB, c, counts, procedure, p, q
    if glag == 0:
        Choice = Combo.get()
        if c == 1:
            counts.destroy()
            VB1.destroy()
            c=0
    else:
        Choice = "All Data"
        for widget in root.winfo_children():
            widget.destroy()
        DL0 = Label(root, image = Bg)  
        DL0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        DL1 = Label(root, text = "Edit Data", font = ("",18,"bold"))
        DL1.pack()
    myDB = mysql.connector.connect(host = "localhost", username = "root", password = "mysequel",database = "project")
    Cursor = myDB.cursor()
    if glag == 0:
        VB1.destroy()
    if flag == 1:
        frame.destroy()
        if p==1:
            p=0
            procedure.destroy()
    flag = 1
    if Choice != "All Data":
        Cursor.execute(f"select * from {Choice}")
    else:
        Cursor.execute("select m.m_id, m.m_name, m.m_type, m.launch_date, m.done_date, m.cost, m.t_id, y.t_name, y.deg_celsius, m.s_id, s.s_name, s.s_location, m.team_id, t.a_id1, t.a_name1, t.a_id2, t.a_name2, t.a_id3, t.a_name3, m.code, c.name, c.class from missions m, temperatures y, satellites s, teams t, spacecrafts c where m.t_id = y.t_id and m.s_id = s.s_id and m.team_id = t.team_id and m.code = c.code order by m_id")
    Result = Cursor.fetchall()
    style = ttk.Style()
    style.configure("Treeview", background = "white", foreground = "black", rowheight = 30)
    frame = Frame(root)
    frame.pack(pady=20)
    scrollx = Scrollbar(frame, orient = HORIZONTAL)
    scroll = Scrollbar(frame)
    scroll.pack(side = RIGHT, fill = Y)
    scrollx.pack(side = BOTTOM, fill = X)
    my_tree = ttk.Treeview(frame, yscrollcommand = scroll.set, xscrollcommand = scrollx.set)
    scroll.config(command = my_tree.yview)
    scrollx.config(command = my_tree.xview)
    my_tree.tag_configure("oddrow", background = "white")
    my_tree.tag_configure("evenrow", background = "lightblue")
    if Choice == "satellites":
        my_tree['columns'] = ("Satellite Id","Satellite Name","Satellite Location")
        my_tree.column("#0",width = 0, stretch = NO)
        my_tree.column("Satellite Id", anchor = W, width = 200)
        my_tree.column("Satellite Name", anchor = W, width = 200)
        my_tree.column("Satellite Location", anchor = W, width = 200)
        my_tree.heading("#0", text = "", anchor = W)
        my_tree.heading("Satellite Id", text = "Satellite Id", anchor = W)
        my_tree.heading("Satellite Name", text = "Satellite Name", anchor = W)
        my_tree.heading("Satellite Location", text = "Satellite Location", anchor = W)
    if Choice == "teams":
        my_tree['columns'] = ("Team Id","Astronaut1 Id","Astronaut1 Name","Astronaut2 Id","Astronaut2 Name","Astronaut3 Id","Astronaut3 Name")
        my_tree.column("#0",width = 0, stretch = NO)
        my_tree.column("Team Id", anchor = W, width = 150)
        my_tree.column("Astronaut1 Id", anchor = W, width = 150)
        my_tree.column("Astronaut1 Name", anchor = W, width = 150)
        my_tree.column("Astronaut2 Id", anchor = W, width = 150)
        my_tree.column("Astronaut2 Name", anchor = W, width = 150)
        my_tree.column("Astronaut3 Id", anchor = W, width = 150)
        my_tree.column("Astronaut3 Name", anchor = W, width = 150)
        my_tree.heading("#0", text = "", anchor = W)
        my_tree.heading("Team Id", text = "Team Id", anchor = W)
        my_tree.heading("Astronaut1 Id", text = "Astronaut1 Id", anchor = W)
        my_tree.heading("Astronaut1 Name", text = "Astronaut1 Name", anchor = W)
        my_tree.heading("Astronaut2 Id", text = "Astronaut2 Id", anchor = W)
        my_tree.heading("Astronaut2 Name", text = "Astronaut2 Name", anchor = W)
        my_tree.heading("Astronaut3 Id", text = "Astronaut3 Id", anchor = W)
        my_tree.heading("Astronaut3 Name", text = "Astronaut3 Name", anchor = W)
    if Choice == "spacecrafts":
        my_tree['columns'] = ("Spacecraft Code","Spacecraft Name","Spacecraft Class")
        my_tree.column("#0",width = 0, stretch = NO)
        my_tree.column("Spacecraft Code", anchor = W, width = 200)
        my_tree.column("Spacecraft Name", anchor = W, width = 200)
        my_tree.column("Spacecraft Class", anchor = W, width = 200)
        my_tree.heading("#0", text = "", anchor = W)
        my_tree.heading("Spacecraft Code", text = "Spacecraft Code", anchor = W)
        my_tree.heading("Spacecraft Name", text = "Spacecraft Name", anchor = W)
        my_tree.heading("Spacecraft Class", text = "Spacecraft Class", anchor = W) 
    if Choice == "temperatures":  
        my_tree['columns'] = ("Temperature Id","Temperature Name","Degrees Celsius")
        my_tree.column("#0",width = 0, stretch = NO)
        my_tree.column("Temperature Id", anchor = W, width = 200)
        my_tree.column("Temperature Name", anchor = W, width = 200)
        my_tree.column("Degrees Celsius", anchor = W, width = 200)
        my_tree.heading("#0", text = "", anchor = W)
        my_tree.heading("Temperature Id", text = "Temperature Id", anchor = W)
        my_tree.heading("Temperature Name", text = "Temperature Name", anchor = W)
        my_tree.heading("Degrees Celsius", text = "Degrees Celsius", anchor = W)  
    if Choice == "missions":
        my_tree['columns'] = ("Mission Id","Mission Name","Mission Type","Launch Date","Done Date","Cost","Temperature Id","Satellite Id","Team Id","Spacecraft Code")
        my_tree.column("#0",width = 0, stretch = NO)
        my_tree.column("Mission Id", anchor = W, width = 90)
        my_tree.column("Mission Name", anchor = W, width = 130)
        my_tree.column("Mission Type", anchor = W, width = 155)
        my_tree.column("Launch Date", anchor = W, width = 110)
        my_tree.column("Done Date", anchor = W, width = 110)
        my_tree.column("Cost", anchor = W, width = 75)
        my_tree.column("Temperature Id", anchor = W, width = 130)
        my_tree.column("Satellite Id", anchor = W, width = 90)
        my_tree.column("Team Id", anchor = W, width = 75)
        my_tree.column("Spacecraft Code", anchor = W, width = 140)
        my_tree.heading("#0", text = "", anchor = W)
        my_tree.heading("Mission Id", text = "Mission Id", anchor = W)
        my_tree.heading("Mission Name", text = "Mission Name", anchor = W)
        my_tree.heading("Mission Type", text = "Mission Type", anchor = W)
        my_tree.heading("Launch Date", text = "Launch Date", anchor = W)
        my_tree.heading("Done Date", text = "Done Date", anchor = W)
        my_tree.heading("Cost", text = "Cost", anchor = W)
        my_tree.heading("Temperature Id", text = "Temperature Id", anchor = W)   
        my_tree.heading("Satellite Id", text = "Satellite Id", anchor = W)
        my_tree.heading("Team Id", text = "Team Id", anchor = W) 
        my_tree.heading("Spacecraft Code", text = "Spacecraft Code", anchor = W)  
    if Choice == "All Data":
        my_tree['columns'] = ("Mission Id","Mission Name","Mission Type","Launch Date","Done Date","Cost","Temperature Id","Temperature Name","Degrees Celsius","Satellite Id","Satellite Name","Satellite Location","Team Id","Astronaut1 Id","Astronaut1 Name","Astronaut2 Id","Astronaut2 Name","Astronaut3 Id","Astronaut3 Name","Spacecraft Code","Spacecraft Name","Spacecraft Class")
        my_tree.column("#0",width = 0, stretch = NO)
        my_tree.column("Mission Id", anchor = W, width = 90)
        my_tree.column("Mission Name", anchor = W, width = 130)
        my_tree.column("Mission Type", anchor = W, width = 155)
        my_tree.column("Launch Date", anchor = W, width = 110)
        my_tree.column("Done Date", anchor = W, width = 110)
        my_tree.column("Cost", anchor = W, width = 75)
        my_tree.column("Temperature Id", anchor = W, width = 130)
        my_tree.column("Temperature Name", anchor = W, width = 165)
        my_tree.column("Degrees Celsius", anchor = W, width = 140)
        my_tree.column("Satellite Id", anchor = W, width = 90)
        my_tree.column("Satellite Name", anchor = W, width = 130)
        my_tree.column("Satellite Location", anchor = W, width = 150)
        my_tree.column("Team Id", anchor = W, width = 75)
        my_tree.column("Astronaut1 Id", anchor = W, width = 125)
        my_tree.column("Astronaut1 Name", anchor = W, width = 150)
        my_tree.column("Astronaut2 Id", anchor = W, width = 125)
        my_tree.column("Astronaut2 Name", anchor = W, width = 150)
        my_tree.column("Astronaut3 Id", anchor = W, width = 125)
        my_tree.column("Astronaut3 Name", anchor = W, width = 150)
        my_tree.column("Spacecraft Code", anchor = W, width = 140)
        my_tree.column("Spacecraft Name", anchor = W, width = 150)
        my_tree.column("Spacecraft Class", anchor = W, width = 150)
        my_tree.heading("#0", text = "", anchor = W)
        my_tree.heading("Mission Id", text = "Mission Id", anchor = W)
        my_tree.heading("Mission Name", text = "Mission Name", anchor = W)
        my_tree.heading("Mission Type", text = "Mission Type", anchor = W)
        my_tree.heading("Launch Date", text = "Launch Date", anchor = W)
        my_tree.heading("Done Date", text = "Done Date", anchor = W)
        my_tree.heading("Cost", text = "Cost", anchor = W)
        my_tree.heading("Temperature Id", text = "Temperature Id", anchor = W) 
        my_tree.heading("Temperature Name", text = "Temperature Name", anchor = W)
        my_tree.heading("Degrees Celsius", text = "Degrees Celsius", anchor = W)   
        my_tree.heading("Satellite Id", text = "Satellite Id", anchor = W)
        my_tree.heading("Satellite Name", text = "Satellite Name", anchor = W)
        my_tree.heading("Satellite Location", text = "Satellite Location", anchor = W)
        my_tree.heading("Team Id", text = "Team Id", anchor = W) 
        my_tree.heading("Astronaut1 Id", text = "Astronaut1 Id", anchor = W)
        my_tree.heading("Astronaut1 Name", text = "Astronaut1 Name", anchor = W)
        my_tree.heading("Astronaut2 Id", text = "Astronaut2 Id", anchor = W)
        my_tree.heading("Astronaut2 Name", text = "Astronaut2 Name", anchor = W)
        my_tree.heading("Astronaut3 Id", text = "Astronaut3 Id", anchor = W)
        my_tree.heading("Astronaut3 Name", text = "Astronaut3 Name", anchor = W)
        my_tree.heading("Spacecraft Code", text = "Spacecraft Code", anchor = W) 
        my_tree.heading("Spacecraft Name", text = "Spacecraft Name", anchor = W)
        my_tree.heading("Spacecraft Class", text = "Spacecraft Class", anchor = W)            
    j = 0
    for i in Result:
        if j%2 == 0:
            my_tree.insert(parent = "",index = "end", iid = j, text = "", values = i, tag = "evenrow") 
        else:
            my_tree.insert(parent = "",index = "end", iid = j, text = "", values = i, tag = "oddrow")        
        j = j + 1
    my_tree.pack()
    if glag == 0:
        p = 1
        procedure = Button(root, text = "Count Records", font = ("",12,""), width = 15,command = lambda: count(Choice))
        procedure.pack()
    elif glag == 1:
        insert = Button(root, text = "Insert Mission", font = ("",12,""), width = 15,command = lambda: InsertData(0))
        insert.pack(pady = 15)
        update = Button(root, text = "Update Mission", font = ("",12,""), width = 15,command = lambda: UpdateData(0))
        update.pack(pady = 15)
        delete = Button(root, text = "Delete Mission", font = ("",12,""), width = 15, command = lambda: DeleteData(0))
        delete.pack(pady = 15)
    elif glag == 2:
        InsertData(2)
    elif glag == 3:
        DeleteData(2)
    else:
        UpdateData(2)
    if glag == 1 or glag == 0:
        q = 1
        VB1 = Button(root, text = "Back", width = 15, font = ("",12,""),command = Home)
        VB1.pack(pady = 15)
def ViewData():
    global Combo, VB1
    for widget in root.winfo_children():
        widget.destroy()
    VL0 = Label(root, image = Bg)  
    VL0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    VL1 = Label(root, text = "View Database", font = ("",18,"bold"))
    VL1.pack()
    vlist = ["satellites","spacecrafts","temperatures","teams","missions","All Data"]
    frame = Frame(root)
    frame.pack(pady = 15)
    Combo = ttk.Combobox(frame, values = vlist)
    Combo.set("satellites")
    Combo.pack(side = LEFT)
    VB2 = Button(frame, text = "Select", font = ("",12,""), command = lambda: Display(0))
    VB2.pack(side = RIGHT)
    VB1 = Button(root, text = "Back", width = 10, font = ("",12,""),command = Home)
    VB1.pack(pady = 15)
def Home():
    global myDB, c
    if c == 1:
        c = 0
        myDB = mysql.connector.connect(host = "localhost", username = "root", password = "mysequel",database = "project")
    for widget in root.winfo_children():
        widget.destroy()
    rL0 = Label(root, image = Bg)
    rL0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    rL1 = Label(root, text = "Welcome to Weather Manipulator and Simulation Database", font = ("",17,"bold"))
    rL1.pack(pady = 25)
    frame = Frame(root)
    frame.pack(pady = 10)
    rB1 = Button(frame, image = View, command = ViewData)
    rB1.pack()
    rL3 = Label(frame, text = "View Data", font = ("",11,""))
    rL3.pack()
    frame1 = Frame(root)
    frame1.pack(pady = 10)
    rB2 = Button(frame1, image = Edit, command = lambda: Display(1))
    rB2.pack()
    rL4 = Label(frame1, text = "Edit Data", font = ("",11,""))
    rL4.pack()
    frame2 = Frame(root)
    frame2.pack(pady = 10)
    rB3 = Button(frame2, image = Scenario, command = Story)
    rB3.pack()
    rL5 = Label(frame2, text = "Scenario", font = ("",11,""))
    rL5.pack()
    frame3 = Frame(root)
    frame3.pack(pady = 10)
    rB4 = Button(frame3, image = Credits, command = Credit)
    rB4.pack()
    rL6 = Label(frame3, text = "Credits", font = ("",11,""))
    rL6.pack()
def Story():
    for widget in root.winfo_children():
        widget.destroy()
    SL0 = Label(root, image = Bg)
    SL0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    SL2 = Label(root, text = "Scenario",font = ("",18,"bold"))
    SL2.pack(pady = 15)
    SL1 = Label(root, text = "The Weather Simulation Database is the Database of a Company\n that Launches specialized satellites into orbit that are able to \nmanipulate the climatic conditions of a desired location. The Company is based\n sometime in the imaginary future wherein climates around the globe\n have gone haywire due to global warming. Thus, the weather \nneeds to be artificially simulated. The database contains the data \nof the ongoing missions of the company to launch, repair or dismantle satellites", font = ("",14,""))
    SL1.pack(pady = 50)
    SB1 = Button(root, text = "Back", width = 10, font = ("",12,""),command = Home)
    SB1.pack(pady = 15)
def Credit():
    for widget in root.winfo_children():
        widget.destroy()
    CL0 = Label(root, image = Bg)
    CL0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    CL2 = Label(root, text = "Credits",font = ("",18,"bold"))
    CL2.pack(pady = 15)
    CL1 = Label(root, text = "Team Members - Aryaman Datta, Hajira Zuha\n USN - 1AT20CS011, 1AT20CS036\nDBMS Mini Project\nAtria Institute of Technology\n2022-2023",font = ("",12,"bold"))
    CL1.pack(pady = 50)
    CB1 = Button(root, text = "Back", width = 10, font = ("",12,""),command = Home)
    CB1.pack(pady = 15)  
root = Tk()
root.title("Weather Simulation Database")
root.geometry("1201x800")
root.iconbitmap("C:/WMS/Weather.ico")
root.resizable(0,0)
myDB = mysql.connector.connect(host = "localhost", username = "root", password = "mysequel",database = "project")
Bg = ImageTk.PhotoImage(Image.open("C:/WMS/Space9.jpg").resize((1201,800)))
View = ImageTk.PhotoImage(Image.open("C:/WMS/View.png").resize((110,110)))
Edit = ImageTk.PhotoImage(Image.open("C:/WMS/Edit2.png").resize((110,103)))
Scenario = ImageTk.PhotoImage(Image.open("C:/WMS/Scenario.png").resize((110,110)))
Credits = ImageTk.PhotoImage(Image.open("C:/WMS/Credits.png").resize((127,110)))
Home()
root.mainloop()