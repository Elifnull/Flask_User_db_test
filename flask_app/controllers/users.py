from flask import Flask, render_template, request, redirect
from flask_app import app
from flask_app.models.user import User

@app.route('/')
@app.route('/Read(all)')
def index():
    allusers = User.get_all()
    return render_template("index.html", all_users= allusers)

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

@app.route('/show/user/<int:id>')
def show_user(id):
    data = {
        "id": id
    }
    single_user= User.get_single(data)
    return render_template("show.html", user_data=single_user)

@app.route('/edit/user/<int:id>')
def edit_user(id):
    data ={ "id": id
    }
    user=User.get_single(data)
    return render_template("edit.html", user_data=user)

@app.route('/update', methods=["POST"])
def update_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form['lname'],
        "email": request.form['email'],
        'id': request.form['id']
    }
    User.update_user(data)
    return redirect('/Read(all)')

@app.route('/delete/user/<int:id>')
def delete_users(id):
    data = {
        "id": id
    }
    User.delete_user(data)
    return redirect('/')