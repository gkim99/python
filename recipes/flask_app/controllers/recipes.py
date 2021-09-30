from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    logged_in = User.get_by_id({'id': session['user_id']})
    recipes = Recipe.get_all()
    return render_template("dashboard.html", user_name = logged_in.first_name, recipes=recipes)

@app.route('/recipes/<int:id>')
def show_recipe(id):
    if 'user_id' not in session:
        return redirect('/')

    logged_in = User.get_by_id({'id': session['user_id']})
    recipe = Recipe.get_one({"id": id})
    if not recipe:
        return redirect('/dashboard')
    return render_template("show_recipe.html", user_name = logged_in.first_name, recipe=recipe)

@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("new_recipe.html")

@app.route('/create', methods = ['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/')
    
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')

    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "date_made_on": request.form['date_made_on'],
        "under_30_mins": request.form['under_30_mins'],
        "user_id": session['user_id']
    }

    Recipe.save(data)
    return redirect('/dashboard')

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    
    recipe_to_edit = Recipe.get_one({"id": id})

    if not recipe_to_edit:
        return redirect('/dashboard')

    return render_template("edit_recipe.html", recipe = recipe_to_edit)

@app.route('/recipes/update/<int:id>', methods=['POST'])
def update_recipe(id):
    if 'user_id' not in session:
        return redirect('/')

    if not Recipe.validate_recipe(request.form):
        return redirect(f'/recipes/edit/{id}')

    data = {
        "id": id,
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "date_made_on": request.form['date_made_on'],
        "under_30_mins": request.form['under_30_mins'],
    }

    Recipe.update_one(data)
    return redirect('/dashboard')

@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect('/')

    Recipe.delete({"id": id})
    return redirect('/dashboard')