# Import MySQL connector library to connect to the database
import mysql.connector

# Database configuration (host, username, password, database name)
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234512345Sh@',
    'database': 'login_system'
}

# Function to create a new database connection using the config
def create_connection():
    return mysql.connector.connect(**db_config)

# Function to register a new user (email + password)
def register_user(email, password):
    try:
        # Open connection and prepare a cursor
        conn = create_connection()
        cursor = conn.cursor()
        
        # Insert new user into the 'users' table
        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
        
        # Save changes to the database
        conn.commit()
        return True

    # If email already exists, handle the error and return False
    except mysql.connector.IntegrityError:
        return False

    # Close the connection in any case
    finally:
        conn.close()

# Function to check if a user's email and password are correct
def check_user(email, password):
    conn = create_connection()
    cursor = conn.cursor()
    
    # Query to find a user with matching email and password
    cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    
    # Fetch the result
    user = cursor.fetchone()
    
    # Close the connection
    conn.close()
    
    # Return True if user exists, otherwise False
    return user is not None

# Function to retrieve all users (only ID and email)
def get_all_users():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Query to get all users
    cursor.execute("SELECT id, email FROM users")
    
    # Fetch all results
    users = cursor.fetchall()
    
    # Close the connection
    conn.close()
    
    return users
