import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.contacts = []

        self.root.title("Contact Book")
        self.root.geometry("800x400")

        self.create_widgets()

    def create_widgets(self):
        # Main Frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)

        # Contact Information
        contact_frame = tk.Frame(main_frame)
        contact_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        self.name_label = tk.Label(contact_frame, text="Name:", font=("Arial", 14))
        self.name_label.pack()
        self.name_entry = tk.Entry(contact_frame, font=("Arial", 14))
        self.name_entry.pack()

        self.phone_label = tk.Label(contact_frame, text="Phone Number:", font=("Arial", 14))
        self.phone_label.pack()
        self.phone_entry = tk.Entry(contact_frame, font=("Arial", 14))
        self.phone_entry.pack()

        self.email_label = tk.Label(contact_frame, text="Email:", font=("Arial", 14))
        self.email_label.pack()
        self.email_entry = tk.Entry(contact_frame, font=("Arial", 14))
        self.email_entry.pack()

        self.address_label = tk.Label(contact_frame, text="Address:", font=("Arial", 14))
        self.address_label.pack()
        self.address_entry = tk.Text(contact_frame, height=5, width=30, font=("Arial", 14))
        self.address_entry.pack()

        # Panel
        self.panel = tk.Frame(main_frame, bg='gray', width=200)
        self.panel.pack(side="left", fill="both")

        # Buttons
        self.add_button = tk.Button(self.panel, text="Add Contact", command=self.add_contact, font=("Arial", 14))
        self.add_button.pack(pady=10)

        self.view_button = tk.Button(self.panel, text="View Contact List", command=self.view_contacts, font=("Arial", 14))
        self.view_button.pack(pady=10)

        self.search_button = tk.Button(self.panel, text="Search Contact", command=self.search_contact, font=("Arial", 14))
        self.search_button.pack(pady=10)

        self.update_button = tk.Button(self.panel, text="Update Contact", command=self.update_contact, font=("Arial", 14))
        self.update_button.pack(pady=10)

        self.delete_button = tk.Button(self.panel, text="Delete Contact", command=self.delete_contact, font=("Arial", 14))
        self.delete_button.pack(pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get("1.0", "end-1c")

        if name and phone and email and address:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            self.name_entry.delete(0, "end")
            self.phone_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.address_entry.delete("1.0", "end")
        else:
            messagebox.showerror("Error", "Please enter all contact details")

    def view_contacts(self):
        contact_list = tk.Toplevel(self.root)
        contact_list.title("Contact List")

        for i, contact in enumerate(self.contacts):
            tk.Label(contact_list, text=f"{i+1}. {contact['name']} - {contact['phone']}").pack()

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number to search")
        if search_term:
            for contact in self.contacts:
                if search_term.lower() in contact["name"].lower() or search_term.lower() in contact["phone"].lower():
                    messagebox.showinfo("Contact Found", f"{contact['name']} - {contact['phone']}")
                    break
            else:
                messagebox.showinfo("Contact Not Found", "No contact found with the given name or phone number")

    def update_contact(self):
        search_term = simpledialog.askstring("Update Contact", "Enter name or phone number to update")
        if search_term:
            for contact in self.contacts:
                if search_term.lower() in contact["name"].lower() or search_term.lower() in contact["phone"].lower():
                    self.update_contact_details(contact)
                    break
            else:
                messagebox.showinfo("Contact Not Found", "No contact found with the given name or phone number")

    def update_contact_details(self, contact):
        new_name = simpledialog.askstring("Update Contact", "Enter new name")
        new_phone = simpledialog.askstring("Update Contact", "Enter new phone number")
        new_email = simpledialog.askstring("Update Contact", "Enter new email")
        new_address = simpledialog.askstring("Update Contact", "Enter new address")

        if new_name and new_phone and new_email and new_address:
            contact["name"] = new_name
            contact["phone"] = new_phone
            contact["email"] = new_email
            contact["address"] = new_address
            messagebox.showinfo("Contact Updated", "Contact details updated successfully")
        else:
            messagebox.showerror("Error", "Please enter all contact details")

    def delete_contact(self):
        search_term = simpledialog.askstring("Delete Contact", "Enter name or phone number to delete")
        if search_term:
            for contact in self.contacts:
                if search_term.lower() in contact["name"].lower() or search_term.lower() in contact["phone"].lower():
                    self.contacts.remove(contact)
                    messagebox.showinfo("Contact Deleted", "Contact deleted successfully")
                    break
            else:
                messagebox.showinfo("Contact Not Found", "No contact found with the given name or phone number")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()