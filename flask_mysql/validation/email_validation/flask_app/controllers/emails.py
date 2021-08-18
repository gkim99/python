from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    if not Email.validate_email(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    Email.save(request.form)
    return redirect('/success')

@app.route('/success')
def success():
    return render_template("success.html", emails=Email.get_all())

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    Email.delete(data)
    return redirect ('/success')