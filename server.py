from flask import Flask, redirect, request, render_template
from user import User

app = Flask(__name__)

@app.route('/')
@app.route('/Read(all)')
def index():
    all_users = User.get_all()
    return render_template("index.html", all_users)

@app.route('/create')
def user_creation():
    return render_template("ucreate.html")

@app.route('/created', methods=['POST'])
def create_user():
    # creating the data to be passed into the class method
    # data will be passed into .save() and query will update db
    data = {
        "fname": request.form["fname"],
        "lname": request.form['lname'],
        "email": request.form['email']
    }
    User.save(data)
    return redirect('/Read(all)')

if __name__ == "__main__":
    app.run(debug=True)