import Main
import tkinter as tk

class GUI:
    
    manager = False
    employee = False
    
    def __init__(self):
        
        
        
        def click():
            self.menu.login(t1.get())
        def click2():
            self.menu.employeeLogin(t2.get())
        
        self.menu = Main
        self.window = tk.Tk()
        self.window.title("KWALITY KLOTHING")
        self.frame = tk.Frame(self.window)
        
        l1 = tk.Label(self.frame, text="Admin login", fg="black", font="none 12 bold").grid(row=1, column=0)
        l2 = tk.Label(self.frame, text="Normal login", fg="black", font="none 12 bold").grid(row=2, column=0)
        t1 = tk.Entry(self.frame, width=20, bg="white").grid(row=1, column=1)
        t2 = tk.Entry(self.frame, width=20, bg="white").grid(row=2, column=1)
        b1 = tk.Button(self.frame, text="-->", width=6, command=click).grid(row=1, column=2)
        b2 = tk.Button(self.frame, text="-->", width=6, command=click2).grid(row=2, column=2)
        
        self.frame.pack()
        
        self.window.mainloop()
        
        
    def nextMenu(self):
        if GUI.manager == True:
            self.frame.destroy()
            self.window.mainloop()
        elif GUI.employee == True:
            self.frame.destroy()
            self.window.mainloop()
        else:
            self.window.kill()
    
        
        


def main():
    gui = GUI()
    
if __name__ == "__main__":
    main()