# assuming this is a database engine connected to a server
import email

from numpy import save


DBEngine = None

def validate_user_data(user):
    if not user.age or not user.password or not user.first_name or not user.last_name:
        raise ValueError("Invalid user data")
    
    validate_email(user.email)

def validate_email(email):
    if not email or "@" not in email:
        raise ValueError(
            "Invalid user data: email is required and must be a valid email address"
        )
    
def create_new_user(user):
    validate_user_data(user)

    save_user_data_to_database(user)


def save_user_data_to_database(user):
    name = user.first_name + " " + user.last_name
    query = {
        "text": "INSERT INTO users (email, password, name, age) VALUES ($1, $2, $3, $4)",
        "values": [user.email, user.password, name, user.age],
    }
    DBEngine.query(query)

    print("Saving user data to the database:")
    send_confirmation_email(user.email)


def send_confirmation_email(email):
    validate_email(email)
    # Simulate sending a confirmation email
    print("Sending confirmation email to:", email)



user = {
    "first_name": "Ahmed",
    "last_name": "Mohamed",
    "email": "ahmed@gmail.com",
    "password": "182983983",
    "age": 12
}

create_new_user(user)
