from flask import Flask, request, render_template, redirect, flash,  jsonify, session
# from random import randint,  choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)

app.config['SECRET_KEY'] = "dfsa87dfsdkj3k4389s7d"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

#SESSION_RESPONSES = "responses"

# Pass survey to a variable
survey = satisfaction_survey
# Responses list
responses = []
# Current Question
# question_count = 0

@app.route('/')
def home_page():
    """Shows home page"""
    # session['fav_number'] = 42
    return render_template('home.html', survey=survey)

@app.route('/start')
def start_survey():
    """BEGIN THE SURVEY"""
    return redirect('/questions/0')

@app.route('/questions/<int:question_id>')
def questions_page(question_id):
    """Build the question page"""

    print('QUESTION ID:', question_id, 'RESPONSES LENGTH:', len(responses))
    # If the question id matches the length of responses, we're on the right question
    if question_id == len(responses):
        print('ID & COUNT MATCH, GO AHEAD.')
        return render_template('question.html', survey=survey, question_id=question_id)
    else:
        flash(f"ERROR: Please follow the survey from start to finish, redirecting you to the next question in order.", 'error')
        return redirect(f"/questions/{len(responses)}")


@app.route('/answer/<int:question_id>', methods=["POST"])
def answer_page(question_id):
    """Answer POST to store answer in global responses list"""
    answer = request.form['answer'] #how can I do this with radio buttons ?
    #print(answer)
    responses.append(answer)
    print('Current Responses List:', responses)
    # Is there another question?
    if question_id == len(survey.questions) - 1:
        return redirect('/thanks') # no more, head to thank you page
    else:
        question_id += 1 # increment question_id
        return redirect(f"/questions/{question_id}") # go to next question

@app.route('/thanks')
def thanks_page():
    """Thank you page"""
    return render_template('thanks.html')