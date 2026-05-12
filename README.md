# smart-expense-tracker
Smart Python Tkinter-based expense tracker that saves data in CSV and sends email alerts when high spending is detected.
# 💰 Smart Expense Tracker

A Python-based desktop application built with Tkinter that helps users track daily expenses and receive email alerts when spending becomes unusually high.

---

## 🚀 Features

- Add expenses with category, amount, and email
- Store expense records in CSV files
- Detect high spending in categories
- Send automatic email alerts
- Simple and clean Tkinter GUI
- Beginner-friendly Python project

---

## 🛠️ Technologies Used

- Python
- Tkinter
- CSV
- SMTP (Email Sending)
- datetime module

---

## 📂 Project Structure

```text
main.py          -> Main project logic
ui_app.py        -> Tkinter user interface
snd_email.py     -> Email sending functionality
user_data.csv    -> Expense data storage
⚙️ How to Run
1. Clone Repository
git clone https://github.com/qfazah/smart-expense-tracker.git
2. Open Project Folder
cd smart-expense-tracker
3. Run Application
python main.py

📧 Email Alert System
The application sends email alerts when a user's spending becomes unusually high in a category.
To use this feature:


Enable 2-Step Verification in Gmail


Generate Gmail App Password


Use the App Password inside snd_email.py



📊 Example CSV Data
email,category,price,dateexample@gmail.com,Food,250,2026-05-12

🎯 Future Improvements


Monthly budget system


Expense charts and graphs


Database integration


Mobile version


User authentication



👨‍💻 Author
Fazah Qamar

⭐ Support
If you like this project:


Give it a star ⭐


Fork the repository


Improve the project 🚀


