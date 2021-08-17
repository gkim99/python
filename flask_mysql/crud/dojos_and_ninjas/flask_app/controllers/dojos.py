from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("dojos.html", dojos=dojos)

@app.route('/dojo/create', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"],
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_one_with_ninjas(data)
    return render_template("dojo_list.html", dojo=dojo)