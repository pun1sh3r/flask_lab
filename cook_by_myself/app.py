from flask import Flask, render_template, request, url_for, redirect
from helper import recipes, descriptions, ingredients, instructions, add_instructions, add_ingredients, comments, types
from forms import RecipeForm, CommentForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"


@app.route('/', methods=["GET", "POST"])
def index():
    '''
    new_id = len(recipes) + 1
    if len(request.form) > 0:
        print(request.form)
        #### Add the recipe name to recipes[new_id]
        recipes[new_id] = request.form['recipe']
        #### Add the recipe description to descriptions[new_id]
        descriptions[new_id] = request.form['description']
        #### Add the values to new_ingredients and new_instructions
        new_ingredients = request.form['ingredients']
        new_instructions = request.form['instructions']
        add_ingredients(new_id,new_ingredients)
        add_instructions(new_id,new_instructions)
    '''
    recipe_form = RecipeForm(csrf_enabled=False)
    if recipe_form.validate_on_submit():
        new_id = len(recipes) + 1
        recipes[new_id] = recipe_form.recipe.data
        descriptions[new_id] = recipe_form.description.data
        new_ingredients = recipe_form.ingredients.data
        new_instructions = recipe_form.instructions.data
        add_ingredients(new_id, new_ingredients)
        add_instructions(new_id, new_instructions)
        comments[new_id] = []
        types[new_id] = recipe_form.recipe_type.data
        return redirect(url_for('recipe',id=new_id,_scheme='http',_external=True))
    #### Return a rendered index.html file
    return render_template('index.html',template_recipes=recipes, template_form=recipe_form)


@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe(id):
    #### Return a rendered fried_egg.html file
    test = recipes
    test_ = instructions

    comment_form = CommentForm(csrf_enabled=False)
    if comment_form.validate_on_submit():
        new_comment = comment_form.comment.data
        comments[id].append(new_comment)
    return render_template('recipe.html',template_recipe=recipes[id],template_description=descriptions[id],template_ingredients=ingredients[id], template_instructions=instructions[id], template_form=comment_form)


@app.route("/about")
def about():
    return render_template("about.html")