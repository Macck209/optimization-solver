import customtkinter
import res.font_constants as fonts

class ResultFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=2)
        
        self.frame_label = customtkinter.CTkLabel(self, text="Results", font=fonts.ARIAL_H1)
        self.frame_label.grid(row=0, column=0, padx=10, pady=10, sticky="nwe")
        
        self.result_textbox = customtkinter.CTkTextbox(self, font=fonts.ARIAL_DEFAULT_16, wrap="word")
        self.result_textbox.grid(row=1, column=0, padx=10, pady=0, sticky="nswe")
        self.result_textbox.insert("0.0", "Click 'Solve' to generate results")
        self.result_textbox.configure(state="disabled")
        
    def show_results(self, result):
        self.result_textbox.configure(state="normal")
        self.result_textbox.delete("0.0", "end")
        self.result_textbox.insert("0.0", result)
        self.result_textbox.configure(state="disabled")