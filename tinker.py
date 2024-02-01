from customtkinter import *

app = CTk()
app.geometry("400x400")

dropbox = CTkComboBox(master=app, values=["Option 1", "Option 2", "Option 3"], fg_color="black", bg_color="white", dropdown_fg_color="red")


dropbox.place(x=100, y=100, anchor="center")

app.mainloop()
