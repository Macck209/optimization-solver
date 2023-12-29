import sys
import customtkinter
import font_constants

class OptionsFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.themeBtn = customtkinter.CTkButton(self, text="Change theme", command=self.change_theme, font=font_constants.ARIAL_DEFAULT, border_spacing=8)
        self.themeBtn.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.exitBtn = customtkinter.CTkButton(self, text="Exit", command=self.exit_app, font=font_constants.ARIAL_DEFAULT, border_spacing=8)
        self.exitBtn.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
    def change_theme(self):
        customtkinter.set_appearance_mode("light")
    
    def exit_app(self):
        sys.exit()