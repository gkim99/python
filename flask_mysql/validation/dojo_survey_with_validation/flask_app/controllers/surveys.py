from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.survey import Survey

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
    if not Survey.validate_survey(request.form):
        return redirect('/')
    Survey.save(request.form)
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html', survey = Survey.get_survey())