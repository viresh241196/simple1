from tkinter import *
from tkinter import messagebox
cartlist=[]

#--------function Call--------------------------------------------
def AddCake():
    data = txt_type.get()+","+txt_price.get()+","+txt_quant.get()
    list1.insert(END,data)
    clearData()

def SelectCake():
    global index
    clearData()
    index = list1.curselection()[0]
    data = list1.get(ACTIVE)
    data = data.split(",")
    txt_type.insert(0,data[0])
    txt_price.insert(0,data[1])
    txt_quant.insert(0,data[2])

def DeleteCake():
    list1.delete(ACTIVE)
   
def Remove():
    list1.insert(END,list2.get(ACTIVE))
    if list2.get(ACTIVE) in cartlist:
        cartlist.remove(list2.get(ACTIVE))
    list2.delete(ACTIVE)
    print(cartlist)
    

def EditCake():
    data = txt_type.get()+","+txt_price.get()+","+txt_quant.get()
    #Delete the selected record
    list1.delete(index)
    list1.insert(index,data)
    clearData()

def CartCake():
    data = list1.get(ACTIVE)
    list2.insert(END,data)
    list1.delete(ACTIVE)
    cartlist.append(data)
    print(cartlist)

def BillCake():
    l=len(cartlist)
    total = 0
    for item in cartlist:
        saperate = item.split(",")
        total = total + int(saperate[1])
    print(total)
    messagebox.showinfo(" Total Bill is  rs")


def clearData():
    txt_type.delete(0,END)
    txt_price.delete(0,END)
    txt_quant.delete(0,END)
    txt_type.focus()

#----------main window----------------------------------------------

if(__name__ == "__main__"):
    global txt_type, txt_price, txt_quant
    window = Tk()
    window.title("Cake Shop")
    #window.geometry("300x400")
    lbl1 = Label(window,text="Markiv's Cake Shop")
    lbl1.pack()
    frame1= Frame(window)
    frame2= Frame(window)
    frame3= Frame(window)
    frame4= Frame(window)
    frame1.pack()
    frame2.pack()
    frame3.pack()
    frame4.pack()
#----------frame1---------------------
    lbl_type=Label(frame1,text=" Cake Type")
    lbl_price=Label(frame1,text=" Cake Price")
    lbl_quant=Label(frame1,text=" Cake Quantity(kg)")
    txt_type=Entry(frame1)
    txt_price=Entry(frame1)
    txt_quant=Entry(frame1)
    lbl_type.grid(row=1,column=1)
    txt_type.grid(row=1,column=2)
    lbl_price.grid(row=2,column=1)
    txt_price.grid(row=2,column=2)
    lbl_quant.grid(row=3,column=1)
    txt_quant.grid(row=3,column=2)
#---------frame2--------------------------------
    btnAdd = Button(frame2, text="Add to list", command = AddCake)
    btnSelect = Button(frame2, text="Select from list", command = SelectCake)
    btnDelete = Button(frame2, text="Delete from list", command = DeleteCake)
    btnEdit = Button(frame2, text="Edit from list", command = EditCake)
    btnCart = Button(frame2, text="Add to Cart", command = CartCake)
    btnRemove = Button(frame2, text="Remove from Cart", command = Remove)
    btnBill = Button(frame2, text="View Total Bill", command = BillCake)
    btnAdd.grid(row=1,column=1)
    btnSelect.grid(row=1,column=2)
    btnDelete.grid(row=1,column=3)
    btnEdit.grid(row=1,column=4)
    btnCart.grid(row=2,column=1)
    btnRemove.grid(row=2,column=2)
    btnBill.grid(row=2,column=3)

#---------frame3--------------------------------

    lbl_list1 = Label(frame3,text=" List of Cake Available  ")
    lbl_list1.pack(side= LEFT)
    
    lbl_list2 = Label(frame3,text="Cake Added to Cart")
    lbl_list2.pack(side= RIGHT)
    
#---------frame4---------------------------------------------
    scrollbar1 = Scrollbar(frame4)
    
    list1 = Listbox(frame4,height=5, yscrollcommand = scrollbar1.set )
    list1.pack( side = LEFT, fill = BOTH )
    scrollbar1.pack(side = LEFT, fill = Y )
    scrollbar1.config( command = list1.yview )
    

    scrollbar2 = Scrollbar(frame4)
    scrollbar2.pack(side = RIGHT, fill = Y )

    list2 = Listbox(frame4,height=5, yscrollcommand = scrollbar2.set )
    list2.pack( side = LEFT, fill = BOTH )
    scrollbar2.config( command = list2.yview )
    
    

    window.mainloop()