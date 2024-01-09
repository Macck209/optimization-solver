import customtkinter
import res.font_constants as fonts

class InputFrame(customtkinter.CTkFrame):
    maximize=True
    target_func = "-(a+3)^2 + 5"
    conditions = []
    condition_var_names = []
    positive_condition, integer_condition = False, False
    generations_num, mutation_factor = 1000, 5.0
    
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0, 1, 3, 11, 12, 13), weight=10)
        self.grid_rowconfigure((2, 4, 5, 6, 7, 8, 9, 10), weight=5)
        
        self.frame_label = customtkinter.CTkLabel(self, text="Config", font=fonts.ARIAL_H1)
        self.frame_label.grid(row=0, column=0, padx=10, pady=10, sticky="nwe", columnspan=2)

        self.direction_opt_menu = customtkinter.CTkOptionMenu(self, values=["Maximize", "Minimize"], font=fonts.ARIAL_DEFAULT, dropdown_font=fonts.ARIAL_DEFAULT)
        self.direction_opt_menu.grid(row=1, column=0, padx=10, pady=0, sticky="nwe", columnspan=2)
        
        self.target_label = customtkinter.CTkLabel(self, text="Target function:", font=fonts.ARIAL_DEFAULT)
        self.target_label.grid(row=2, column=0, padx=10, pady=0, sticky="sw", columnspan=2)
        self.target_func_entry = customtkinter.CTkEntry(self, placeholder_text="e.g. -(a+3)^2 + 5 (default)")
        self.target_func_entry.grid(row=3, column=0, padx=10, pady=0, sticky="nwe", columnspan=2)
        
        self.conditions_label = customtkinter.CTkLabel(self, text="Conditions:", font=fonts.ARIAL_DEFAULT)
        self.conditions_label.grid(row=4, column=0, padx=10, pady=0, sticky="sw")
        for i in range(0,8):
            var_name = f"cond_entry_{i}"
            
            self.condition_var_names.append(var_name)
            
            setattr(self, var_name, customtkinter.CTkEntry(self, placeholder_text="-"))
            getattr(self, var_name).grid(row=i+5 if i<4 else i+1, column=0 if i<4 else 1, padx=10, pady=0, sticky="nwe")
    
            if var_name == "cond_entry_0":
                getattr(self, var_name).configure(placeholder_text="e.g. a >= -2")
            
        self.variables_positive_checkbox = customtkinter.CTkCheckBox(self, text="Positive variables condition", font=fonts.ARIAL_DEFAULT_16, checkbox_height=16, checkbox_width=16, border_width=2)
        self.variables_positive_checkbox.grid(row=9, column=0, padx=10, pady=0, sticky="nw", columnspan=2)
        
        self.variables_integers_checkbox = customtkinter.CTkCheckBox(self, text="Integer condition", font=fonts.ARIAL_DEFAULT_16, checkbox_height=16, checkbox_width=16, border_width=2)
        self.variables_integers_checkbox.grid(row=10, column=0, padx=10, pady=0, sticky="nw", columnspan=2)
        self.variables_integers_checkbox.select()
        
        self.generation_num_label = customtkinter.CTkLabel(self, text="Max generations:", font=fonts.ARIAL_DEFAULT)
        self.generation_num_label.grid(row=11, column=0, padx=10, pady=0, sticky="w")
        self.generation_num_entry = customtkinter.CTkEntry(self, placeholder_text="Default: 500, Min: 100")
        self.generation_num_entry.grid(row=11, column=1, padx=10, pady=0, sticky="we")
        
        self.mutation_factor_label = customtkinter.CTkLabel(self, text="Mutation factor:", font=fonts.ARIAL_DEFAULT)
        self.mutation_factor_label.grid(row=12, column=0, padx=10, pady=0, sticky="w")
        self.mutation_factor_entry = customtkinter.CTkEntry(self, placeholder_text="Default: 5")
        self.mutation_factor_entry.grid(row=12, column=1, padx=10, pady=0, sticky="we")
        
        self.start_btn = customtkinter.CTkButton(self, text="Solve", command=self.pass_input, font=fonts.ARIAL_DEFAULT, border_spacing=8)
        self.start_btn.grid(row=13, column=0, padx=10, pady=10, sticky="swe", columnspan=2)
        
    def pass_input(self):
        self.start_btn.configure(state="disabled")
        self.maximize = True if self.direction_opt_menu.get() == "Maximize" else False
        # TODO clearing entry doesnt revert to default func
        self.target_func = self.target_func_entry.get() if self.target_func_entry.get() != "" else self.target_func
        
        self.conditions.clear()
        for cond_var_name in self.condition_var_names:
            entry_val = getattr(self, cond_var_name).get()
            if entry_val is not None and entry_val != '':
                self.conditions.append(entry_val)
                
        self.positive_condition = self.variables_positive_checkbox.get()
        self.integer_condition = self.variables_integers_checkbox.get()
        
        try:
            self.generations_num = int(self.generation_num_entry.get())
        except ValueError:
            self.generations_num = 500
            
        try:
            self.mutation_factor = float(self.mutation_factor_entry.get())
        except ValueError:
            self.mutation_factor = 5
        
        self.master.run_solver(self.maximize, self.target_func, self.conditions, self.positive_condition, self.integer_condition, self.generations_num, self.mutation_factor)