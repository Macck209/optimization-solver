import customtkinter
import res.font_constants as fonts

class ResultFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.frame_label = customtkinter.CTkLabel(self, text="Result", font=fonts.ARIAL_H1)
        self.frame_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        
        self.temp_label = customtkinter.CTkLabel(self, text="Nothing here yet", font=fonts.ARIAL_DEFAULT)
        self.temp_label.grid(row=1, column=0, padx=10, pady=10, sticky="nw")
        
    def show_results(self, result):
        self.temp_label.configure(text=result)