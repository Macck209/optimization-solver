import customtkinter
import res.font_constants as fonts

class InputFrame(customtkinter.CTkFrame):
    maximize=True
    target_func = "-(a+3)^2 + 5"
    condition_1 = "a>=-2"
    condition_2 = ''
    condition_3 = ''
    condition_4 = ''
    
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0, 1, 3, 9), weight=10)
        self.grid_rowconfigure((2, 4, 5, 6, 7, 8), weight=5)
        
        self.frame_label = customtkinter.CTkLabel(self, text="Config", font=fonts.ARIAL_H1)
        self.frame_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.direction_opt_menu = customtkinter.CTkOptionMenu(self, values=["Maximize", "Minimize"], font=fonts.ARIAL_DEFAULT, dropdown_font=fonts.ARIAL_DEFAULT)
        self.direction_opt_menu.grid(row=1, column=0, padx=10, pady=0, sticky="nwe")
        
        self.frame_label2 = customtkinter.CTkLabel(self, text="Target function:", font=fonts.ARIAL_DEFAULT)
        self.frame_label2.grid(row=2, column=0, padx=10, pady=0, sticky="sw")
        self.target_func_entry = customtkinter.CTkEntry(self, placeholder_text="e.g. -(a+3)^2 + 5")
        self.target_func_entry.grid(row=3, column=0, padx=10, pady=0, sticky="nwe")
        
        self.conditions_label = customtkinter.CTkLabel(self, text="Conditions:", font=fonts.ARIAL_DEFAULT)
        self.conditions_label.grid(row=4, column=0, padx=10, pady=0, sticky="sw")
        self.cond_entry_1 = customtkinter.CTkEntry(self, placeholder_text="e.g. a>=-2")
        self.cond_entry_1.grid(row=5, column=0, padx=10, pady=0, sticky="nw")
        self.cond_entry_2 = customtkinter.CTkEntry(self, placeholder_text="-")
        self.cond_entry_2.grid(row=6, column=0, padx=10, pady=0, sticky="nw")
        self.cond_entry_3 = customtkinter.CTkEntry(self, placeholder_text="-")
        self.cond_entry_3.grid(row=7, column=0, padx=10, pady=0, sticky="nw")
        self.cond_entry_4 = customtkinter.CTkEntry(self, placeholder_text="-")
        self.cond_entry_4.grid(row=8, column=0, padx=10, pady=0, sticky="nw")
        
        self.start_btn = customtkinter.CTkButton(self, text="Solve", command=self.pass_input, font=fonts.ARIAL_DEFAULT, border_spacing=8)
        self.start_btn.grid(row=9, column=0, padx=10, pady=10, sticky="swe")
        
    def pass_input(self):
        self.maximize = True if self.direction_opt_menu.get() == "Maximize" else False
        self.target_func = self.target_func_entry.get() if self.target_func_entry.get() != "" else self.target_func
        self.condition_1 = self.cond_entry_1.get() if self.cond_entry_1.get() != "" else self.condition_1
        
        self.master.run_solver(self.maximize, self.target_func, self.condition_1)