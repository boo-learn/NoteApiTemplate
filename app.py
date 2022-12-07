from api import app
from config import Config
from api.handlers import auth, note, user

# CRUD

# Create --> POST
# Read --> GET
# Update --> PUT
# Delete --> DELETE

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)
