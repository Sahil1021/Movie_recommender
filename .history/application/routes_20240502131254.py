from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    email_or_mobile = data.get('regEmailOrMobile')
    user_id = data.get('regUserID')
    password = data.get('createPassword')
    age = data.get('age')
    gender = data.get('gender')

    # Validate data (e.g., check if user already exists)
    if any(user['userID'] == user_id for user in users):
        return jsonify({'error': 'User ID already exists'}), 400

    # Store user data
    users.append({
        'emailOrMobile': email_or_mobile,
        'userID': user_id,
        'password': password,
        'age': age,
        'gender': gender
    })

    return jsonify({'message': 'Registration successful'}), 200