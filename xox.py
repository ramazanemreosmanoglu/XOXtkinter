import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo, showerror


class Symbol:
    def __init__(self, _type):
        assert _type == "X" or _type == "O" or _type == "", "TypeError"

        self.type = _type
    
    def __str__(self):
        if self.type == "":
            return "   _   "
        
        else:
            return f"   {self.type}   "
    
    


class Game(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("XOX Oyunu")
        self.geometry("400x400")

        _n = Symbol
        self.table = [
            [_n(""), _n(""), _n("")],
            [_n(""), _n(""), _n("")],
            [_n(""), _n(""), _n("")],
        ]

        self.sira = 0

        self.create_widgets()


    def create_widgets(self):
        table = tk.Frame(self)

        for l in self.table:
            for i in l:
                ix = self.get_index(i)
                x = tk.Label(table, text=str(i), font=("Helvetica", "30", "bold"))
                x.bind("<Button-1>", self.element_click)
                x.grid(row=ix["row"], column=ix["column"])
        table.pack()

        self.siralabel = tk.Label(self, text="Sıra: X")
        self.siralabel.pack(side="bottom")
        
    
    def get_index(self, obj):
        res = {
            "row": None,
            "column": None,
        }

        for row in self.table:
            for col in row:
                if col == obj:
                    res["column"] = row.index(col)
                    res["row"] = self.table.index(row)

                    return res

        return False
    
    def element_click(self, event):
        rc = event.widget.grid_info()
        row = rc["row"]
        column = rc["column"]

        if (self.sira % 2) == 0:
            
            if self.table[row][column].type == "X" or self.table[row][column].type == "O":
                showerror("Hata", "Orası dolu, sıranı kaybettin :(")
                self.siralabel["text"] = "Sıra: O"
            else:
                self.table[row][column] = Symbol("X")
                self.siralabel["text"] = "Sıra: O"

                self.check_win("X")
        else:
            if self.table[row][column].type == "X" or self.table[row][column].type == "O":
                showerror("Hata", "Orası dolu, sıranı kaybettin :(")
                self.siralabel["text"] = "Sıra: X"
            else:
                self.table[row][column] = Symbol("O")
                self.siralabel["text"] = "Sıra: X"

                self.check_win("O")
        



        event.widget["text"] = self.table[row][column]

        self.sira += 1



    def check_win(self, s):
        def win():
            showinfo("Kazanan", f"{s} oyunu kazandı!")
            self.destroy()

        # Aynı satırda var mı?
        for row in self.table:
            if (row[0].type == s) and (row[1].type == s) and (row[2].type == s):
                win()
                return
        
        # Aynı Sütunuda var mı?
        if (self.table[0][0].type == s) and (self.table[1][0].type == s) and (self.table[2][0].type == s):
            win()
            return
        
        if (self.table[0][1].type == s) and (self.table[1][1].type == s) and (self.table[2][1].type == s):
            win()
            return
        
        if (self.table[0][2].type == s) and (self.table[1][2].type == s) and (self.table[2][2].type == s):
            win(); return
        
        # Çaprazda var mı?
        if (self.table[0][0].type == s) and (self.table[1][1].type == s) and (self.table[2][2].type == s):
            win(); return
        
        if (self.table[0][2].type == s) and (self.table[1][1].type == s) and (self.table[2][0].type == s):
            win(); return
    
    

Game().mainloop()
