from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! Your Python app is running."

if __name__ == '__main__':
    # Run the app on the local development server
    app.run(debug=True)
