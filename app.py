from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)

# db tables create karne ke liye function
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            time TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# main index page call karne ke liye
@app.route('/')
def home():
    return render_template('index.html')

# user data save karne aur message check karne ke liye api (POST)
@app.route('/api/appointments', methods=['POST'])
def add_appointment():
    try:
        data = request.json
        name = data.get('name')
        phone = data.get('phone')
        appointment_time = data.get('time') # Format: YYYY-MM-DDTHH:MM
        
        # validation checking
        if not name or not phone or not appointment_time:
            return jsonify({"error": "Fields empty hai"}), 400

        # database entry logic
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO appointments (name, phone, time, status) VALUES (?, ?, ?, ?)",
            (name, phone, appointment_time, 'Confirmed')
        )
        conn.commit()
        conn.close()
        
        # --- BONUS TASK LOGIC (1 Hour Reminder Check) ---
        app_dt = datetime.strptime(appointment_time, "%Y-%m-%dT%H:%M")
        now = datetime.now()
        
        is_urgent = False
        if now <= app_dt <= (now + timedelta(hours=1)):
            is_urgent = True
        
        # Whatsapp API Simulation logging
        print("\n--- WhatsApp Reminder Simulated ---")
        print(f"Sending message to: {phone}")
        print(f"Message Text: Hello {name}, your appointment at {appointment_time} is confirmed.")
        
        if is_urgent:
            print(f"⚠️ ALERT: Appointment is within 1 hour! Sending Urgent Reminder to {phone}...")
        
        print("-------------------------------------\n")
        
        return jsonify({"status": "success", "message": "Saved successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# dashboard table data get route (GET)
@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        # Yahan 'id' ko bhi select kiya taaki frontend use delete kar sake
        cursor.execute("SELECT id, name, phone, time, status FROM appointments ORDER BY id DESC")
        rows = cursor.fetchall()
        conn.close()
        
        # loop chala kar json list banana
        appointments = []
        for row in rows:
            appointments.append({
                "id": row[0],
                "name": row[1],
                "phone": row[2],
                "time": row[3],
                "status": row[4]
            })
        return jsonify(appointments)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# record delete karne ke liye api route (DELETE)
@app.route('/api/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM appointments WHERE id = ?", (appointment_id,))
        conn.commit()
        conn.close()
        return jsonify({"status": "success", "message": "Deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    init_db()
    print("Server started on port 5000...")
    app.run(debug=True, port=5000)