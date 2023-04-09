# Import necessary libraries
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector

# Create a tkinter window
window = tk.Tk()
window.title("Blood Donation App")
window.geometry("600x350")
p1 = PhotoImage(file='bd.png')

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="life2life"
)

# Create a cursor object to interact with the database
mycursor = mydb.cursor()

# Define a function to add a new donor to the database
def add_donor():
    global name_input, bld_opt, gen_opt, age_input, phone_input, email_input, address_input, city_input, state_input, pincode_input, ctr_opt
    # Get the values from the input fields
    name = name_input.get()
    blood_type = bld_opt.get()
    gen = gen_opt.get()
    age = age_input.get()
    phone = phone_input.get()
    email = email_input.get()
    address = address_input.get()
    city = city_input.get()
    state = state_input.get()
    pincode = pincode_input.get()
    country = ctr_opt.get()
    
    # Insert the new donor into the database
    if name != "" and blood_type != "" and gen != "" and age != "" and phone != "" and email != "" and address != "" and city != "" and state != "" and pincode != "" and country != "":
        sql = "INSERT INTO donors (name, blood_type, gen, age, phone, email, address, city, state, pincode, country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (name, blood_type, gen, age, phone, email, address, city, state, pincode, country)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Success", "Donor added successfully.")
    else:
        messagebox.showinfo("Error", "All the fields are required")

    # Clear the input fields
    name_input.delete(0, tk.END)
    age_input.delete(0, tk.END)
    phone_input.delete(0, tk.END)
    email_input.delete(0, tk.END)
    address_input.delete(0, tk.END)
    city_input.delete(0, tk.END)
    state_input.delete(0, tk.END)
    pincode_input.delete(0, tk.END)

#Showing the listed requests window
def show_requests():
    # Retrieve all blood donation requests from the database
    mycursor.execute("SELECT * FROM requests")
    requests = mycursor.fetchall()
    
    # Create a new window to display the list of requests
    requests_window = tk.Toplevel(window)
    requests_window.title("Blood Donation Requests")
    requests_window.geometry("1051x550")
    
    # Create a tkinter listbox to display the requests
    requests_listbox = tk.Listbox(requests_window)
    requests_listbox.insert(tk.END, "Name       -       Gender - Age - Blood Group - Blood Quantity - Phone Number - Email Address - Address")
    
    # Loop through each request and add it to the listbox
    for request in requests:
        requests_listbox.insert(tk.END, f"{request[1]} - {request[11]} - {request[12]} - {request[2]} - {request[3]} - {request[4]} - {request[5]} - {request[6]}, {request[7]}, {request[9]}-{request[10]}")
    
    # Pack the listbox and start the new tkinter event loop
    requests_listbox.pack(side=LEFT, fill=BOTH, expand=True)
    requests_listbox.configure(background="skyblue4", foreground="white", font=('Poppins 13'), width=0)

    requests_window.iconphoto(False, p1)
    requests_window.mainloop()

#Showing the form window to submit request
class req_form:
    def __init__(self):
        global window
        req_window = tk.Toplevel(window)
        req_window.title("Request for Blood")
        req_window.geometry("600x350")

        screen_label = tk.Label(req_window, text="Request for Blood", justify=CENTER, font=('Poppins 17 bold'))
        screen_label.grid(row=2, column=2)
        name_label = tk.Label(req_window, text="Name:")
        name_label.grid(row=3, column=1)
        self.name_input = tk.Entry(req_window, width=25, background="skyblue3", foreground="white")
        self.name_input.grid(row=4, column=1)
        blood_type_label = tk.Label(req_window, text="Blood Type:")
        blood_type_label.grid(row=3, column=2)
        # blood_type_input = tk.Entry(req_window)
        options = [
            "O+",
            "B+",
            "A+",
            "AB+",
            "O-",
            "B-",
            "A-",
            "AB-"
        ]

        # datatype of menu text
        self.bld_opt = tk.StringVar()
        # initial menu text
        self.bld_opt.set("O+")
        # Create Dropdown menu
        self.blood_type_input = tk.OptionMenu(req_window, self.bld_opt, *options)
        self.blood_type_input.grid(row=4, column=2)
        blood_qty_label = tk.Label(req_window, text="Blood Quantity:")
        blood_qty_label.grid(row=3, column=3)
        self.blood_qty_input = tk.Entry(req_window, width=25, background="skyblue3", foreground="white")
        self.blood_qty_input.grid(row=4, column=3)
        gen_label = tk.Label(req_window, text="Gender:")
        gen_label.grid(row=9, column=3)
        options = [
            "Male",
            "Female",
            "Other"
        ]

        # datatype of menu text
        self.gen_opt = tk.StringVar()
        # initial menu text
        self.gen_opt.set("Male")
        # Create Dropdown menu
        self.gen_input = tk.OptionMenu(req_window, self.gen_opt, *options)
        self.gen_input.grid(row=10, column=3)
        age_label = tk.Label(req_window, text="Age:")
        age_label.grid(row=5, column=1)
        self.age_input = tk.Entry(req_window, width=25, background="skyblue3", foreground="white")
        self.age_input.grid(row=6, column=1)
        phone_label = tk.Label(req_window, text="Phone with Country Code:")
        phone_label.grid(row=5, column=2)
        self.phone_input = tk.Entry(req_window, width=25, background="skyblue3", foreground="white")
        self.phone_input.grid(row=6, column=2)
        email_label = tk.Label(req_window, text="Email:")
        email_label.grid(row=5, column=3)
        self.email_input = tk.Entry(req_window, width=25, background="skyblue3", foreground="white")
        self.email_input.grid(row=6, column=3)
        address_label = tk.Label(req_window, text="Address:")
        address_label.grid(row=7, column=1)
        self.address_input = tk.Entry(req_window, width=25, background="skyblue3", foreground="white")
        self.address_input.grid(row=8, column=1)
        city_label = tk.Label(req_window, text="City:")
        city_label.grid(row=7, column=2)
        self.city_input = tk.Entry(req_window, width=25, background="skyblue3", foreground="white")
        self.city_input.grid(row=8, column=2)
        state_label = tk.Label(req_window, text="State:")
        state_label.grid(row=7, column=3)
        self.state_input = tk.Entry(req_window, width=25, background="skyblue3", foreground="white")
        self.state_input.grid(row=8, column=3)
        pincode_label = tk.Label(req_window, text="Pincode:")
        pincode_label.grid(row=9, column=1)
        self.pincode_input = tk.Entry(req_window, width=25, background="skyblue3", foreground="white")
        self.pincode_input.grid(row=10, column=1)
        country_label = tk.Label(req_window, text="Country:")
        country_label.grid(row=9, column=2)
        options = [
            "Bangladesh",
            "India",
            "Srilanka"
        ]

        # datatype of menu text
        self.ctr_opt = tk.StringVar()
        # initial menu text
        self.ctr_opt.set("India")
        # Create Dropdown menu
        self.country_input = tk.OptionMenu(req_window, self.ctr_opt, *options)
        self.country_input.grid(row=10, column=2)

        add_button = tk.Button(req_window, text="Request Blood", command=self.add_request, width=35, border="2", relief="groove")
        add_button.grid(row=13, column=2)
        requests_button = tk.Button(req_window, text="View Blood Donation Requests", command=show_requests)
        requests_button.grid(row=1, column=1)
        donors_button = tk.Button(req_window, text="View Donors List", command=show_donors)
        donors_button.grid(row=1, column=2)

        req_window.iconphoto(False, p1)
        req_window.mainloop()

    def add_request(self):
        # Get the values from the input fields
        name = self.name_input.get()
        blood_type = self.bld_opt.get()
        blood_qty = self.blood_qty_input.get()
        gen = self.gen_opt.get()
        age = self.age_input.get()
        phone = self.phone_input.get()
        email = self.email_input.get()
        address = self.address_input.get()
        city = self.city_input.get()
        state = self.state_input.get()
        pincode = self.pincode_input.get()
        country = self.ctr_opt.get()
        
        # Insert the new donor into the database
        if name != "" and blood_type != "" and gen != "" and age != "" and phone != "" and email != "" and address != "" and city != "" and state != "" and pincode != "" and country != "":
            sql = "INSERT INTO requests (name, blood_type, blood_qty, gen, age, phone, email, address, city, state, pincode, country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (name, blood_type, blood_qty, gen, age, phone, email, address, city, state, pincode, country)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Success", "Request added successfully.")
        else:
            messagebox.showinfo("Error", "All the fields are required")

        # Clear the input fields
        self.name_input.delete(0, tk.END)
        self.age_input.delete(0, tk.END)
        self.phone_input.delete(0, tk.END)
        self.email_input.delete(0, tk.END)
        self.address_input.delete(0, tk.END)
        self.city_input.delete(0, tk.END)
        self.state_input.delete(0, tk.END)
        self.pincode_input.delete(0, tk.END)
    

def show_donors():
    # Retrieve all donors from the database
    mycursor.execute("SELECT * FROM donors")
    donors = mycursor.fetchall()
    
    # Create a new window to display the list of donors
    donors_window = tk.Toplevel(window)
    donors_window.title("Donors List")
    donors_window.geometry("990x500")
    
    # Create a tkinter listbox to display the donors
    donors_listbox = tk.Listbox(donors_window)
    
    donors_listbox.insert(tk.END, "Name       -       Gender - Age - Blood Group - Phone Number - Email Address - Address")
    # Loop through each donor and add it to the listbox
    for donor in donors:
        donors_listbox.insert(tk.END, f"{donor[1]} - {donor[10]} - {donor[11]} - {donor[2]} - {donor[3]} - {donor[4]} - {donor[5]}, {donor[6]}, {donor[7]}-{donor[8]}, {donor[9]}")
    
    # Pack the listbox and start the new tkinter event loop
    donors_listbox.pack(side=LEFT, fill=BOTH, expand=True)
    donors_listbox.configure(background="skyblue4", foreground="white", font=('Poppins 13'), width=0)

    donors_window.iconphoto(False, p1)
    donors_window.mainloop()

# Create the input fields and buttons for the "Add Donor" screen
screen_label = tk.Label(window, text="Add Donor", justify=CENTER, font=('Poppins 17 bold'))
screen_label.grid(row=2, column=2)
name_label = tk.Label(window, text="Name:")
name_label.grid(row=3, column=1)
name_input = tk.Entry(window, width=25, background="skyblue3", foreground="white")
name_input.grid(row=4, column=1)
blood_type_label = tk.Label(window, text="Blood Type:")
blood_type_label.grid(row=3, column=2)
# blood_type_input = tk.Entry(window)
options = [
    "O+",
    "B+",
    "A+",
    "AB+",
    "O-",
    "B-",
    "A-",
    "AB-"
]

# datatype of menu text
bld_opt = tk.StringVar()
# initial menu text
bld_opt.set("O+")
# Create Dropdown menu
blood_type_input = tk.OptionMenu(window, bld_opt, *options)
blood_type_input.grid(row=4, column=2)
gen_label = tk.Label(window, text="Gender:")
gen_label.grid(row=3, column=3)
# blood_type_input = tk.Entry(window)
options = [
    "Male",
    "Female",
    "Other"
]

# datatype of menu text
gen_opt = tk.StringVar()
# initial menu text
gen_opt.set("Male")
# Create Dropdown menu
gen_input = tk.OptionMenu(window, gen_opt, *options)
gen_input.grid(row=4, column=3)
age_label = tk.Label(window, text="Age:")
age_label.grid(row=5, column=1)
age_input = tk.Entry(window, width=25, background="skyblue3", foreground="white")
age_input.grid(row=6, column=1)
phone_label = tk.Label(window, text="Phone with Country Code:")
phone_label.grid(row=5, column=2)
phone_input = tk.Entry(window, width=25, background="skyblue3", foreground="white")
phone_input.grid(row=6, column=2)
email_label = tk.Label(window, text="Email:")
email_label.grid(row=5, column=3)
email_input = tk.Entry(window, width=25, background="skyblue3", foreground="white")
email_input.grid(row=6, column=3)
address_label = tk.Label(window, text="Address:")
address_label.grid(row=7, column=1)
address_input = tk.Entry(window, width=25, background="skyblue3", foreground="white")
address_input.grid(row=8, column=1)
city_label = tk.Label(window, text="City:")
city_label.grid(row=7, column=2)
city_input = tk.Entry(window, width=25, background="skyblue3", foreground="white")
city_input.grid(row=8, column=2)
state_label = tk.Label(window, text="State:")
state_label.grid(row=7, column=3)
state_input = tk.Entry(window, width=25, background="skyblue3", foreground="white")
state_input.grid(row=8, column=3)
pincode_label = tk.Label(window, text="Pincode:")
pincode_label.grid(row=9, column=1)
pincode_input = tk.Entry(window, width=25, background="skyblue3", foreground="white")
pincode_input.grid(row=10, column=1)
country_label = tk.Label(window, text="Country:")
country_label.grid(row=9, column=2)
options = [
    "Bangladesh",
    "India",
    "Srilanka"
]

# datatype of menu text
ctr_opt = tk.StringVar()
# initial menu text
ctr_opt.set("India")
# Create Dropdown menu
country_input = tk.OptionMenu(window, ctr_opt, *options)
country_input.grid(row=10, column=2)

add_button = tk.Button(window, text="Add Donor", command=add_donor, width=35, border="2", relief="groove")
add_button.grid(row=13, column=2)
requests_button = tk.Button(window, text="View Blood Donation Requests", command=show_requests)
requests_button.grid(row=1, column=1)
request_button = tk.Button(window, text="Add Donation Request", command=req_form)
request_button.grid(row=1, column=2)
donors_button = tk.Button(window, text="View Donors List", command=show_donors)
donors_button.grid(row=1, column=3)

window.iconphoto(False, p1)
# Start the tkinter event loop
window.mainloop()
