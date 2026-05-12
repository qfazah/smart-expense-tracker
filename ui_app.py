from tkinter import *
from tkinter.ttk import Combobox, Style
import datetime as dt
from tkinter import messagebox
import csv
from snd_email import SndEmail


class UiApp:
    def __init__(self):
        self.window = Tk()
        self.window.minsize(600, 600)
        self.window.geometry("650x650+300+100")

        self.window.configure(bg="#eef2f7")
        self.window.title("Smart Expense Tracker")

        style = Style()
        style.theme_use("default")

        style.configure("TCombobox", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 13, "bold"))

        self.today_date = dt.datetime.now()
        self.date = self.today_date.date()

        self.user_choice = StringVar()
        self.user_choice.set("None")

    def on_select(self, event):
        user_choice = event.widget.get()
        print(f"User selected: {user_choice}")

    def add(self):
        category = self.categories.get()
        price = self.price_entry.get()
        email = self.email_entry.get()

        if not price or not email:
            messagebox.showwarning("Warning", "Please fill all fields!")
            return

        try:
            price = float(price)
            new_data = [email, category, price, self.date]

            with open("user_data.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(new_data)

            # -------------------------------
            # EMAIL CHECKING LOGIC
            # -------------------------------

            price_lst = []

            with open("user_data.csv", "r") as file:
                reader_for_standard = list(csv.reader(file))

                if reader_for_standard:

                    standard = category

                    for row in reader_for_standard:

                        if row[1] == standard:
                            # store price + row together
                            price_lst.append((float(row[2]), row))

                    if price_lst:

                        highest_price, highest_row = max(price_lst)

                        y = highest_row[3]

                        # send email only if highest spending is today
                        if str(y) == str(self.date):

                            sender = SndEmail(email)
                            sender.send_email()

                            messagebox.showinfo(
                                "Alert",
                                "High spending detected today!\nEmail sent successfully."
                            )

                        else:
                            messagebox.showinfo(
                                "Saved",
                                "Expense saved successfully!"
                            )

        except ValueError:
            messagebox.showwarning("Warning", "Enter valid number!")

        self.price_entry.delete(0, END)

    def ui_making(self):
        self.window.columnconfigure(0, weight=1)

        Label(
            text="Smart Expense Tracker",
            font=("Arial", 28, "bold"),
            bg="#eef2f7",
            fg="#1f3a5f"
        ).grid(column=0, row=0, pady=(25, 15))

        main_frame = Frame(
            self.window,
            bg="white",
            padx=30,
            pady=30,
            bd=0,
            highlightthickness=1,
            highlightbackground="#d9e2ec"
        )
        main_frame.grid(column=0, row=1, padx=25, pady=10)

        # EMAIL
        Label(
            main_frame,
            text="Email Address",
            font=("Arial", 13, "bold"),
            bg="white",
            fg="#334e68"
        ).grid(column=0, row=0, sticky=W)

        self.email_entry = Entry(
            main_frame,
            font=("Arial", 12),
            relief=FLAT,
            bg="#f1f5f9",
            width=33
        )
        self.email_entry.grid(column=0, row=1, pady=(0, 15), ipady=7)

        # CATEGORY
        Label(
            main_frame,
            text="Expense Category",
            font=("Arial", 13, "bold"),
            bg="white",
            fg="#334e68"
        ).grid(column=0, row=2, sticky=W)

        expense_choices = [
            "Food", "Transport", "Shopping", "Bills", "Entertainment",
            "Education", "Health", "Mobile", "Savings", "Travel",
            "Gym", "Subscriptions", "Family", "Gifts", "Other"
        ]

        self.categories = Combobox(
            main_frame,
            values=expense_choices,
            state="readonly",
            font=("Arial", 12),
            width=30
        )

        self.categories.set(expense_choices[0])

        self.categories.grid(column=0, row=3, pady=(0, 15), ipady=6)

        self.categories.bind("<<ComboboxSelected>>", self.on_select)

        # PRICE
        Label(
            main_frame,
            text="Amount",
            font=("Arial", 13, "bold"),
            bg="white",
            fg="#334e68"
        ).grid(column=0, row=4, sticky=W)

        self.price_entry = Entry(
            main_frame,
            font=("Arial", 12),
            relief=FLAT,
            bg="#f1f5f9",
            width=33
        )

        self.price_entry.grid(column=0, row=5, pady=(0, 15), ipady=7)

        # DATE
        Label(
            main_frame,
            text="Date",
            font=("Arial", 13, "bold"),
            bg="white",
            fg="#334e68"
        ).grid(column=0, row=6, sticky=W)

        Label(
            main_frame,
            text=f"{self.date}",
            font=("Arial", 12),
            bg="white",
            fg="#486581"
        ).grid(column=0, row=7, sticky=W)

        # BUTTON
        Button(
            main_frame,
            text="Add Expense",
            font=("Arial", 14, "bold"),
            bg="#2ecc71",
            fg="white",
            bd=0,
            padx=10,
            pady=6,
            command=self.add
        ).grid(column=0, row=8, pady=10)


if __name__ == "__main__":
    app = UiApp()
    app.ui_making()
    app.window.mainloop()