from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo

# Initialize Flask App
app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/Thursday"  # Replace with your MongoDB URI
mongo = PyMongo(app)

# Route to Render Registration Form
@app.route("/")
def registration_form():
    return render_template("registration.html")  # Serve the form

# Route to Handle Form Submission
@app.route("/submit", methods=["POST"])
def submit_form():
    # Extract form data
    full_name = request.form.get("Full_name")
    email = request.form.get("Email")
    password = request.form.get("Password")
    username = request.form.get("Username")
    phonenumber = request.form.get("Phonenumber")
    gender = request.form.get("gender")

    # Insert data into MongoDB
    mongo.db.registrationpage.insert_one({
        "full_name": full_name,
        "email": email,
        "password": password,
        "username": username,
        "phonenumber": phonenumber,
        "gender": gender
    })

    # Confirmation message
    return "Registration successful! Your data has been saved."

# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
