# import the app
from flask_app import app
# import our controllers here or they will not be recognized by the app
from flask_app.controllers import users, books

# run the application
if __name__ == "__main__":
    app.run(debug=True)