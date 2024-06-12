import customtkinter

from application import Application

class GUIApplication(Application, customtkinter.CTk):

    def __init__(self):
        self.app_launch()
    
    def app_launch(self):
        super().__init__()
        self.geometry("1000x800")
        self.title("Python Application")

        self.option_windows = None
        
        self.button_options = customtkinter.CTkButton(self,text = "Options", command =self.button_app_options)
        self.button_options.grid(row=0, column = 0, padx=15, pady=15)

        self.button_quit = customtkinter.CTkButton(self,text = "Quit Application", command =self.button_app_options)
        self.button_quit.grid(row=0, column=1, padx=10, pady=35)

        self.combobox_characters = customtkinter.CTkComboBox(self,values = ["Haven","Jonesy","Peely"], command =self.button_select_char)
        self.combobox_characters.grid(row=0, column=2)

    def app_main_menu(self): ...

    def app_option (self):
        if self.option_window is None or not self.option_windows.winfo_exists():
            self.option_windows = self.GUIOptionWindow()
            self.option_windows.focus()
        else:
            self.option_windows.focus()

    def app_quit(self):
        exit()

    def button_app_quit(self):
        self.app_quit()

    def button_app_options(self):
        self.app_options()

    def button_select_char(self):
        pass

    class GUIOptionWindow (customtkinter.CTkToplevel):

        def __init__(self):
            super().__init__()
            self.geometry("400x400")
            self.title("Python App Options")

            self.label = customtkinter.CTkLabel(self, text = "Top level window")
            self.label.grid(row=0,column =15)



if __name__=="__main__":
    guiapp_test_instance = GUIApplication()
    guiapp_test_instance.mainloop()
