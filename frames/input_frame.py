import customtkinter
import font_constants

class InputFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label = customtkinter.CTkLabel(self, text="Config", font=font_constants.ARIAL_H1)
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="we")

        self.startBtn = customtkinter.CTkButton(self, text="Solve", command=self.test, font=font_constants.ARIAL_DEFAULT)
        self.startBtn.grid(row=1, column=0, padx=10, pady=10, sticky="we")
        self.exitBtn = customtkinter.CTkButton(self, text="Exit", command=self.test, font=font_constants.ARIAL_DEFAULT)
        self.exitBtn.grid(row=2, column=0, padx=10, pady=10, sticky="we")
        self.themeBtn = customtkinter.CTkButton(self, text="Change theme", command=self.test, font=font_constants.ARIAL_DEFAULT)
        self.themeBtn.grid(row=3, column=0, padx=10, pady=10, sticky="we")
        
    def test(self):
        print('test')