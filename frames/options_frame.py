import sys
import customtkinter
import res.font_constants as fonts

class OptionsFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        self.frame_label = customtkinter.CTkLabel(self, text="Options", font=fonts.ARIAL_H1)
        self.frame_label.grid(row=0, column=0, padx=10, pady=10, sticky="nwe")
        
        self.theme_btn = customtkinter.CTkButton(self, text="Change theme", command=self.change_theme, font=fonts.ARIAL_DEFAULT)
        self.theme_btn.grid(row=1, column=0, padx=30, pady=0, sticky="nwe")
        self.exit_btn = customtkinter.CTkButton(self, text="Exit", command=self.exit_app, font=fonts.ARIAL_DEFAULT)
        self.exit_btn.grid(row=2, column=0, padx=30, pady=(0,10), sticky="nwe")
        
    def change_theme(self):
        if customtkinter.AppearanceModeTracker.appearance_mode:
            customtkinter.set_appearance_mode("Light")
        else:
            customtkinter.set_appearance_mode("Dark")
    
    
    def exit_app(self):
        sys.exit()