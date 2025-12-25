from flask import Flask

# 1. Initialize the Flask application
# __name__ helps Flask locate resources like templates and static files
app = Flask(__name__)

# 2. Define the Index Route
# This maps the root URL ('/') to the index function
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

# 3. Define a Variable Route
# This captures part of the URL as a variable named 'username'
# The <string:username> converter ensures the input is treated as a string
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# 4. Run the Application
# This block ensures the server only runs if the script is executed directly
if __name__ == '__main__':
    app.run(port=5555, debug=True)