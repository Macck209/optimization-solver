import customtkinter
import res.font_constants as fonts
from report_animation import DataGraph
import threading

class ResultFrame(customtkinter.CTkFrame):
    graph_data = []
    
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=2)
        self.grid_rowconfigure(2, weight=1)
        
        self.frame_label = customtkinter.CTkLabel(self, text="Results", font=fonts.ARIAL_H1)
        self.frame_label.grid(row=0, column=0, padx=10, pady=10, sticky="nwe")
        
        self.result_textbox = customtkinter.CTkTextbox(self, font=fonts.ARIAL_DEFAULT_16, wrap="word")
        self.result_textbox.grid(row=1, column=0, padx=10, pady=0, sticky="nswe")
        self.result_textbox.insert("0.0", "Click 'Solve' to generate results")
        self.result_textbox.configure(state="disabled")
        
        self.generate_report_btn = customtkinter.CTkButton(self, text="Generate report", command=self.render_report, font=fonts.ARIAL_DEFAULT, border_spacing=8)
        self.generate_report_btn.grid(row=2, column=0, padx=10, pady=10, sticky="swe")
        self.generate_report_btn.configure(state="disabled")
    
    def set_results(self, result, graph_data):
        self.show_results(result)
        self.graph_data = graph_data
        self.generate_report_btn.configure(state="normal")
    
    def show_results(self, result):
        self.result_textbox.configure(state="normal")
        self.result_textbox.delete("0.0", "end")
        self.result_textbox.insert("0.0", result)
        self.result_textbox.configure(state="disabled")
    
    def render_report(self):
        if len(self.graph_data) < 0: # TODO check for data len = 1
            self.result_textbox.configure(state="normal")
            self.result_textbox.insert("end", "\nNot enough data for the report")
            self.result_textbox.configure(state="disabled")
        else:
            self.generate_report_btn.configure(state="disabled")

            render_thread = threading.Thread(target=self.render_report_async)
            render_thread.start()
    
    def render_report_async(self):
        scene = DataGraph(self, self.graph_data)
        scene.render(True)
        
        self.generate_report_btn.configure(state="normal")
        
    def show_report_error(self):
        self.result_textbox.configure(state="normal")
        self.result_textbox.insert("end", "\nError while generating report")
        self.result_textbox.configure(state="disabled")
        self.generate_report_btn.configure(state="normal")