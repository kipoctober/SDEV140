# program: final project: interior detailing estimator
# author: kristen p
# created 2024-03-09
# purpose: have user select services and output the total 

# import the gui interface 
import tkinter as tk
# import the messagebox feature to display the output at the end of the code 
from tkinter import messagebox
# create class for parent window 
class DetailingEstimator(tk.Tk):
    def __init__(self):
        super().__init__()
        # title 
        self.title("Car Detailing Price Estimator")
        self.geometry("1000x400")
        # image with resizing
        self.photo= tk.PhotoImage(file="car_detailing_image.gif", width=200, height=200)
        self.image_label= tk.Label(self, image=self.photo)
        self.image_label.pack(pady=20)
        # first label 
        self.label = tk.Label(self, text="Car Detailing Price Estimator")
        self.label.pack(pady=10)
        # two buttons, for users to choose which category of detailing 
        self.button_interior = tk.Button(self, text="Interior Detailing", command=self.open_interior_window)
        self.button_interior.pack(pady=5)
        
        self.button_exterior = tk.Button(self, text="Exterior Detailing", command=self.open_exterior_window)
        self.button_exterior.pack(pady=5)
        # exit button 
        self.button_exit = tk.Button(self, text="Exit", command=self.exit_program)
        self.button_exit.pack(pady=5)
        # open the interior detailing window when clicked 
    def open_interior_window(self):
        self.withdraw()
        interior_window = InteriorDetailingWindow(self)
        # open the exterior detailing window when clicked 
    def open_exterior_window(self):
        self.withdraw()
        exterior_window = ExteriorDetailingWindow(self)
       # exit button instructions  
    def exit_program(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            self.destroy()
# second window 
class InteriorDetailingWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Interior Detailing Services")
        self.geometry("400x400")
        
        self.label = tk.Label(self, text="Please select the interior detailing services you require:")
        self.label.pack(pady=10)
        # check boxes for each service 
        self.interior_var1 = tk.IntVar()
        self.checkbox_carpet = tk.Checkbutton(self, text="Carpet Cleaning", variable=self.interior_var1)
        self.checkbox_carpet.pack(pady=5)
        
        self.interior_var2 = tk.IntVar()
        self.checkbox_seat = tk.Checkbutton(self, text="Seat Cleaning", variable=self.interior_var2)
        self.checkbox_seat.pack(pady=5)
        
        self.interior_var3 = tk.IntVar()
        self.checkbox_steam = tk.Checkbutton(self, text="Steam Cleaning", variable=self.interior_var3)
        self.checkbox_steam.pack(pady=5)
        
        self.interior_var4 = tk.IntVar()
        self.checkbox_tinting = tk.Checkbutton(self, text="Window Tinting", variable=self.interior_var4)
        self.checkbox_tinting.pack(pady=5)
        
        self.calculate_button = tk.Button(self, text="Calculate Total", command=self.calculate_total_price)
        self.calculate_button.pack(pady=5)
        # back to main window 
        self.button_back = tk.Button(self, text="Back", command=self.go_back)
        self.button_back.pack(pady=5)
        # calculating total price based on which checkboxes are selected 
    def calculate_total_price(self):
        total_price = 0
        if self.interior_var1.get() == 1:
            total_price += 40
        if self.interior_var2.get() == 1:
            total_price += 30
        if self.interior_var3.get() == 1:
            total_price += 50
        if self.interior_var4.get() == 1:
            total_price += 80
            # output 
        messagebox.showinfo("Total Price", f"The total price for selected services is ${total_price}.")
       # close second window if back button is selected  
    def go_back(self):
        self.destroy()
        master = self.master
        master.deiconify()
# second window if exterior is selected from mai 
class ExteriorDetailingWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Exterior Detailing Services")
        self.geometry("400x400")
        
        self.label = tk.Label(self, text="Please select the exterior detailing services you require:")
        self.label.pack(pady=10)
        # checkboxes for exterior detail choices 
        self.exterior_var1 = tk.IntVar()
        self.checkbox_wash = tk.Checkbutton(self, text="Car Wash", variable=self.exterior_var1)
        self.checkbox_wash.pack(pady=5)
        
        self.exterior_var2 = tk.IntVar()
        self.checkbox_wax = tk.Checkbutton(self, text="Car Wax", variable=self.exterior_var2)
        self.checkbox_wax.pack(pady=5)
        
        self.exterior_var3 = tk.IntVar()
        self.checkbox_polish = tk.Checkbutton(self, text="Car Polish", variable=self.exterior_var3)
        self.checkbox_polish.pack(pady=5)
        
        self.calculate_button = tk.Button(self, text="Calculate Total", command=self.calculate_total_price)
        self.calculate_button.pack(pady=5)
        
        self.button_back = tk.Button(self, text="Back", command=self.go_back)
        self.button_back.pack(pady=5)
        # calculate total price of services selected 
    def calculate_total_price(self):
        total_price = 0
        if self.exterior_var1.get() == 1:
            total_price += 20
        if self.exterior_var2.get() == 1:
            total_price += 30
        if self.exterior_var3.get() == 1:
            total_price += 40
            # output 
        messagebox.showinfo("Total Price", f"The total price for selected services is ${total_price}.")
        # back to main window if selected 
    def go_back(self):
        self.destroy()
        master = self.master
        master.deiconify()

if __name__ == "__main__":
    app = DetailingEstimator()
    app.mainloop()