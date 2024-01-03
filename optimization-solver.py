import customtkinter
from frames.input_frame import InputFrame
from frames.result_frame import ResultFrame
from frames.options_frame import OptionsFrame
import calculation_script

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("dark-blue")

        self.geometry("700x600")
        self.title("Optimal Solver")
        
        self.grid_columnconfigure(0, weight=50)
        self.grid_columnconfigure(1, weight=40)
        self.grid_rowconfigure((0, 1), weight=80)
        self.grid_rowconfigure(2, weight=20)
            
        self.config_frame = InputFrame(self)
        self.config_frame.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="nswe", rowspan=3)
        self.result_frame = ResultFrame(self)
        self.result_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nswe", rowspan=2)
        self.options_frame = OptionsFrame(self)
        self.options_frame.grid(row=2, column=1, padx=10, pady=(0, 10), sticky="nswe", rowspan=1)
        
    def run_solver(self, maximize, target_func, condition_1):
        result = calculation_script.solve(maximize, target_func, condition_1)
        
        self.show_results(result)
        
    def show_results(self, result):
        self.result_frame.show_results(result)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()