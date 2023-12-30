import customtkinter
import res.font_constants as fonts

class InputFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 7), weight=10)
        self.grid_rowconfigure((4, 5, 6), weight=5)
        
        self.frame_label = customtkinter.CTkLabel(self, text="Config", font=fonts.ARIAL_H1)
        self.frame_label.grid(row=0, column=0, padx=10, pady=5, sticky="nw")

        self.direction_opt_menu = customtkinter.CTkOptionMenu(self, values=["Maximize", "Minimize"], command=self.test, font=fonts.ARIAL_DEFAULT)
        self.direction_opt_menu.grid(row=1, column=0, padx=10, pady=5, sticky="we")
        
        self.target_func_entry = customtkinter.CTkEntry(self, placeholder_text="placeholder")
        self.target_func_entry.grid(row=2, column=0, padx=10, pady=5, sticky="we")
        
        self.conditions_label = customtkinter.CTkLabel(self, text="Conditions:", font=fonts.ARIAL_DEFAULT)
        self.conditions_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.cond_entry_1 = customtkinter.CTkEntry(self, placeholder_text="option 1")
        self.cond_entry_1.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.cond_entry_2 = customtkinter.CTkEntry(self, placeholder_text="option 2")
        self.cond_entry_2.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.cond_entry_3 = customtkinter.CTkEntry(self, placeholder_text="option 3")
        self.cond_entry_3.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        
        self.start_btn = customtkinter.CTkButton(self, text="Solve", command=self.test, font=fonts.ARIAL_DEFAULT)
        self.start_btn.grid(row=7, column=0, padx=10, pady=10, sticky="we")
        
    def test(self):
        print('test')