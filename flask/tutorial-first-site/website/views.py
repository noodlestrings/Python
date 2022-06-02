# storing the standard pages/roots for the site
from flask import Blueprint

views = Blueprint('views', __name__)


# whenever we go to root (slash page), this function will run
@views.route('/')
def home():
    return "<h1>Test</h1>"
