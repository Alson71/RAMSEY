from tkinter import *
import customtkinter


class RAMSEY:
    global tkWindow,parameters,dropdowns
    global cuisines,cuisines2,brooklynAreas,manhattanAreas,queensAreas,bronxAreas,statenAreas
    global labels, options
    
    customtkinter.set_appearance_mode("dark")
    tkWindow = customtkinter.CTk()
    tkWindow.geometry("1000x600")
    tkWindow.title("RAMSEY")
    tkWindow.resizable("False","False")
    
    parameters = [None] * 3
    parameters[0] = ["American","Indian","Chinese","Japanese","Greek","Mexican","French","Peruvian","Korean","Thai""Cuban", "Dominican", "Vietnamese", "Spain", "Brazilian", "Colombian", "Filippino", "Jamaican", "Russian", "Italian"]
    parameters[1] = ["Manhattan","Queens","Staten Island","Bronx","Brooklyn"]
    parameters[2] = ["None","None","None","None","None"]
    options = ["Cuisine", "Borough", "Area"]
    
    
   
    vars = [None] * 3
    labels = [None] * 3
    dropdowns = [None] * 3
    increment = 230
    for i in range(3):
        vars[i] = StringVar()
        vars[i].set("Select")
        
        labels[i] = customtkinter.CTkLabel(tkWindow,fg_color = "transparent", height = 30, width = 100,text = options[i])
        dropdowns[i] = customtkinter.CTkOptionMenu(tkWindow,variable = vars[i],values = parameters[i],height = 30, width = 100)
        
        labels[i].place(x = increment, y = 75)
        dropdowns[i].place(x = increment, y = 100)
        increment += 200
        
   
if __name__ == "__main__":
    tkWindow.mainloop()
    
