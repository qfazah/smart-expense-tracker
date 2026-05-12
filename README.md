# smart-expense-tracker
Smart Python Tkinter-based expense tracker that saves data in CSV and sends email alerts when high spending is detected.
# 💰 Smart Expense Tracker (Python + Tkinter)

A simple yet powerful desktop-based expense tracking system built using Python Tkinter.  
It allows users to add daily expenses, store them in a CSV file, and automatically sends an email alert when high spending is detected in a category.

---

## 🚀 Features

- 🧾 Add expenses with email, category, and amount  
- 📊 Stores all data in CSV file (`user_data.csv`)  
- 🔍 Detects highest spending in each category  
- 📧 Sends email alert when unusual/high spending occurs  
- 🎨 Clean and modern Tkinter GUI  
- ⚡ Lightweight and easy to run  

---

## 🛠️ Technologies Used

- Python 🐍  
- Tkinter (GUI)  
- CSV module (data storage)  
- SMTP (email sending)  
- datetime module  

---

## 📂 Project Structure
ui_app.py → Main GUI application (Tkinter)
snd_email.py → Email sending functionality
main.py → Entry point of project
user_data.csv → Stores expense data


---

## ⚙️ How to Run

### 1. Clone repository
```bash
git clone https://github.com/your-username/smart-expense-tracker.git
cd smart-expense-tracker
python main.py
📧 Email System Setup

This project uses Gmail SMTP.

Important setup steps:
Enable 2-Step Verification in Google Account
Generate an App Password
Use that password in snd_email.py

⚠️ Normal Gmail password will NOT work.
How It Works
User enters expense data in GUI
Data is saved into CSV file
System checks category-wise spending
Finds highest expense
If highest expense is from today → email is sent
tell me what you give me above all copy and paste ?
also givew me description 
