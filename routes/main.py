from flask import Blueprint



main = Blueprint('test', __name__)

print(__name__)


@main.route("/ho")
def accountList():

    print(main)
   
    return "list of accounts"