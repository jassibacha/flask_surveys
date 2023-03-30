from flask import Flask, request, render_template, redirect, flash,  jsonify, session
# from random import randint,  choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)

app.config['SECRET_KEY'] = "dfsa87dfsdkj3k4389s7d"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


survey = satisfaction_survey


# Responses list
responses = []

@app.route('/')
def home_page():
    """Shows home page"""
    # session['fav_number'] = 42
    return render_template('home.html', survey=survey)

@app.route('/questions/<int:question_id>')
def questions_page(question_id):
    """Build the question page"""
    return render_template('question.html', survey=survey, question_id=question_id)


@app.route('/answer/<int:question_id>', methods=["POST"])
def answer_page(question_id):
    
    answer = request.form['answer'] #how can I do this with radio buttons ?
    print(answer)
    responses.append(answer)
    print(responses)
    if question_id == len(survey.questions) - 1:
        return redirect('/thanks')
    else:
        question_id += 1 # increment question_id
        return redirect(f"/questions/{question_id}")