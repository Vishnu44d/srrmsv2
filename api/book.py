from flask import Blueprint

bookBP = Blueprint('TestAPI', __name__)

@bookBP.route('/', methods=['GET', 'POST'])
def get_status():
    return 'xyz'