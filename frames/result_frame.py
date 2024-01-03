import customtkinter
import res.font_constants as fonts

class ResultFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        self.frame_label = customtkinter.CTkLabel(self, text="Result", font=fonts.ARIAL_H1)
        self.frame_label.grid(row=0, column=0, padx=10, pady=10, sticky="nwe")
        
        self.temp_label = customtkinter.CTkLabel(self, text="Click 'Solve' to generate results", font=fonts.ARIAL_DEFAULT)
        self.temp_label.grid(row=1, column=0, padx=10, pady=10, sticky="nwe")
        
    def show_results(self, result):
        self.temp_label.configure(text=result)