from flask import Flask
app = Flask(__name__)
import os
import glob
import shutil
from flask import request
@app.route('/generate')
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    username = request.args.get('user')
    if not username.isalpha():
        return "You need to enter a username that is all letters."
    if len(username)<2:
        return "Your username is too short"
    newdir = "ipython/user_" + username
    if os.path.exists(newdir):
        return "This username already exists"

    source_ipython = "source_ipython"
    os.makedirs(newdir)
    for filename in glob.glob(os.path.join(source_ipython, '*')):
        shutil.copy(filename, newdir)

    return "Thanks. There is now a folder for user %s. Press back!" % username
    
if __name__ == "__main__":
    app.run(host= '0.0.0.0')
