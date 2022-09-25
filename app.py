# config                    
from flask import Flask
app = Flask(__name__)

# index route
@app.route('/')
def index(): 
    return 'Hello, this is PetFax Jenni style!'

# pets index route
@app.route('/jpets')
def jpets():
    return 'These are our pets available for adoption! Cuz Jenni said so'

 
