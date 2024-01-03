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
        
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0, 1, 3, 10, 11, 12), weight=10)
        self.grid_rowconfigure((2, 4, 5, 6, 7, 8, 9), weight=5)
        
        self.frame_label = customtkinter.CTkLabel(self, text="Config", font=fonts.ARIAL_H1)
        self.frame_label.grid(row=0, column=0, padx=10, pady=10, sticky="nwe", columnspan=2)

        self.direction_opt_menu = customtkinter.CTkOptionMenu(self, values=["Maximize", "Minimize"], font=fonts.ARIAL_DEFAULT, dropdown_font=fonts.ARIAL_DEFAULT)
        self.direction_opt_menu.grid(row=1, column=0, padx=10, pady=0, sticky="nwe", columnspan=2)
        
        self.target_label = customtkinter.CTkLabel(self, text="Target function:", font=fonts.ARIAL_DEFAULT)
        self.target_label.grid(row=2, column=0, padx=10, pady=0, sticky="sw", columnspan=2)
        self.target_func_entry = customtkinter.CTkEntry(self, placeholder_text="e.g. -(a+3)^2 + 5")
        self.target_func_entry.grid(row=3, column=0, padx=10, pady=0, sticky="nwe", columnspan=2)
        
        self.conditions_label = customtkinter.CTkLabel(self, text="Conditions:", font=fonts.ARIAL_DEFAULT)
        self.conditions_label.grid(row=4, column=0, padx=10, pady=0, sticky="sw")
        self.cond_entry_1 = customtkinter.CTkEntry(self, placeholder_text="e.g. a >= -2")
        self.cond_entry_1.grid(row=5, column=0, padx=10, pady=0, sticky="nwe")
        for i in range(2,9):
            var_name = f"cond_entry_{i}"
            exec(f"{var_name} = customtkinter.CTkEntry(self, placeholder_text=\"-\")")
            exec(f"{var_name}.grid(row={i+4 if i<5 else i}, column={0 if i<5 else 1}, padx=10, pady=0, sticky=\"nwe\")")
            
        self.variables_positive_checkbox = customtkinter.CTkCheckBox(self, text="Positive variables condition", font=fonts.ARIAL_DEFAULT_16, checkbox_height=16, checkbox_width=16, border_width=2)
        self.variables_positive_checkbox.grid(row=9, column=0, padx=10, pady=0, sticky="nw", columnspan=2)
        
        self.generation_count_label = customtkinter.CTkLabel(self, text="Max generations:", font=fonts.ARIAL_DEFAULT)
        self.generation_count_label.grid(row=10, column=0, padx=10, pady=0, sticky="w")
        self.generation_count_entry = customtkinter.CTkEntry(self, placeholder_text="Default: 1000")
        self.generation_count_entry.grid(row=10, column=1, padx=10, pady=0, sticky="we")
        
        self.mutation_factor_label = customtkinter.CTkLabel(self, text="Mutation factor:", font=fonts.ARIAL_DEFAULT)
        self.mutation_factor_label.grid(row=11, column=0, padx=10, pady=0, sticky="w")
        self.mutation_factor_entry = customtkinter.CTkEntry(self, placeholder_text="Default: 5")
        self.mutation_factor_entry.grid(row=11, column=1, padx=10, pady=0, sticky="we")
        
        self.start_btn = customtkinter.CTkButton(self, text="Solve", command=self.pass_input, font=fonts.ARIAL_DEFAULT, border_spacing=8)
        self.start_btn.grid(row=12, column=0, padx=10, pady=10, sticky="swe", columnspan=2)
        
    def pass_input(self):
        self.maximize = True if self.direction_opt_menu.get() == "Maximize" else False
        self.target_func = self.target_func_entry.get() if self.target_func_entry.get() != "" else self.target_func
        self.condition_1 = self.cond_entry_1.get() if self.cond_entry_1.get() != "" else self.condition_1
        
        self.master.run_solver(self.maximize, self.target_func, self.condition_1)