from flask import Flask, render_template, request, redirect
import user_db  # This module handles user login and registration
from pymongo import MongoClient  # To connect and query MongoDB

# Initialize the Flask app and set the templates folder
app = Flask(__name__, template_folder='Pages')

# Connect to MongoDB database
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["Lap6"]# Use database
restaurants_col = mongo_db["resturants"] # Use collection for restaurants

# Homepage,shows login page
@app.route('/')
def index():
    return render_template('login.html', message='')

# Login processing
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('username')
    password = request.form.get('password')

    # Check if user exists and password is correct
    if user_db.check_user(email, password):
        return render_template('search.html')  # Go to search page if login is successful
    return render_template('login.html', message="Invalid login")  # Otherwise show error

# Register page and processing
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('username')
        password = request.form.get('password')

        # Try to register user
        if user_db.register_user(email, password):
            return render_template('login.html', message="You have been registered successfully. Please log in.")
        return render_template('register.html', message="The email is already associated with an existing account.")

    return render_template('register.html', message='')  # Show registration page

# Restaurant search page
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = {}  # Build a MongoDB search query

        # Add filters based on user input
        if request.form.get('name'):
            query["name"] = request.form['name']
        if request.form.get('borough'):
            query["borough"] = request.form['borough']
        if request.form.get('cuisine'):
            query["cuisine"] = request.form['cuisine']
        if request.form.get('grade'):
            query["grades.grade"] = request.form['grade']
        if request.form.get('street'):
            query["address.street"] = request.form['street']

        # Search the MongoDB collection
        results = list(restaurants_col.find(query))
        if results:
            return render_template('search.html', results=results)  # Show results
        else:
            return render_template('search.html', message="No results found.")  # No match found
    
    return render_template('search.html')  # Show search page (GET request)

# View all users (used for debugging or admin)
@app.route('/users')
def show_users():
    users = user_db.get_all_users()
    return str(users)

# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)