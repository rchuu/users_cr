from flask import Flask, render_template, redirect, request, session
# import the class from friend.py
from users import User  # imports the user class
app = Flask(__name__)


@app.route("/")
def index():
    return redirect('/users')


# @app.route("/users")
# def users():
#     users = User.get_all()
#     # print(users)
#     return render_template("users.html", all_users=users)

@app.route('/users')
def users():
    return render_template("users.html", users=User.get_all())


@app.route('/user/new')
def new():
    return render_template("new_user.html")


@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')


@app.route('/user/edit/<int:id>')
def edit(id):  # bring in id
    data = {  # create the data object
        "id": id
    }
    # render the form with all the info
    return render_template("edit_user.html", user=User.get_one(data))


@app.route('/user/show/<int:id>')
def show(id):  # bring in id
    data = {  # create the data object
        "id": id
    }
    # render the form with all the info
    return render_template("show_user.html", user=User.get_one(data))


@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)  # pass in the request.form
    return redirect('/users')


@app.route('/user/destroy/<int:id>')  # delete is a reversed keyword
def destroy(id):
    data = {
        'id': id
    }
    User.destroy(data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)
