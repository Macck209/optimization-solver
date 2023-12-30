import sys
import customtkinter
import res.font_constants as fonts

class OptionsFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.theme_btn = customtkinter.CTkButton(self, text="Change theme", command=self.change_theme, font=fonts.ARIAL_DEFAULT, border_spacing=8)
        self.theme_btn.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.exit_btn = customtkinter.CTkButton(self, text="Exit", command=self.exit_app, font=fonts.ARIAL_DEFAULT, border_spacing=8)
        self.exit_btn.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
    def change_theme(self):
        if customtkinter.AppearanceModeTracker.appearance_mode:
            customtkinter.set_appearance_mode("Light")
        else:
            customtkinter.set_appearance_mode("Dark")
    
    
    def exit_app(self):
        sys.exit()