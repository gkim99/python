from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)

@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("read_all.html", users = users)

@app.route('/user/new')
def create():
    return render_template("create.html")

@app.route('/user/create', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)