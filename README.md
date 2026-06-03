# whatsapp-appointment-system
# 📅 AI WhatsApp Appointment Reminder System

A lightweight, real-time Appointment Management System built with **Python (Flask)**, **SQLite**, and **Vanilla HTML/JavaScript**.

---

## 🛠️ Tech Stack Used
- **Backend:** Python (Flask Framework)
- **Database:** SQLite3 (Local file-based system)
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)

---

## 🚀 Key Features Implemented
1. **Live Dashboard:** Save and display records instantly without reloading the page.
2. **WhatsApp Notification Simulation:** Simulated notification payload prints directly in the terminal logs upon submission.
3. **Bonus Task (1-Hour Urgent Reminder):** Automatically checks system time. If the appointment is within **1 hour**, it triggers a highlighted `⚠️ ALERT` in the console.
4. **Extra Feature (Delete Record):** Functional **Delete** button next to each row to manage and clean up database entries dynamically.

---

## 🏃‍♂️ How to Run and Operate

### Step 1: Start the Server
Open your terminal inside the project folder and run:
```bash
python app.py

Step 2: Test the Live Actions
Add Record: Fill the form with a future date and submit. It will show in the table live.

Delete Record: Click the red Delete button to remove any entry instantly from the UI and database.

Test 1-Hour Alert (Bonus): Submit an entry with today's date and set the time just 15-20 minutes ahead of your current computer time. Check your terminal console to see the ⚠️ ALERT log live.
