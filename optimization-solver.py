import customtkinter
from frames.input_frame import InputFrame
from frames.result_frame import ResultFrame
from frames.options_frame import OptionsFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.geometry("700x500")
        self.title("Optimal Solver")
        
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
            
        self.config_frame = InputFrame(self)
        self.config_frame.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="nswe", rowspan=3)
        self.result_frame = ResultFrame(self)
        self.result_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nswe", rowspan=2)
        self.options_frame = OptionsFrame(self)
        self.options_frame.grid(row=2, column=1, padx=10, pady=(0, 10), sticky="nswe", rowspan=1)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()