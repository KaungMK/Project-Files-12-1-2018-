from flask import Flask, render_template, request
from wtforms import Form, StringField, validators

import AddGoalProcess

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/views')
def views():
    return render_template('views.html')

@app.route('/graph')
def graph():
    return render_template('Graph.html')

@app.route('/details')
def details():
    return render_template('Details.html')

@app.route('/rewards')
def rewards():
    return render_template('Rewards.html')

#for AddGoal.html
class RegisterUser(Form):
    Name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    Goal = StringField('Goal', [validators.Length(min=1, max=150), validators.DataRequired()])
    Duration = StringField('Duration', [validators.Length(min=1, max=150), validators.DataRequired()])

@app.route('/AddGoal',methods=['GET', 'POST'])
def AddGoal():
    form = RegisterUser(request.form)
    if request.method == 'POST' and form.validate():
        AddGoalProcess.registerNewUser(form.Name.data, form.Goal.data, form.Duration.data)
        print("Your goal has been successfully added!")
    return render_template('AddGoals.html')

@app.route('/EditGoal')
def EditGoal():
    return render_template('EditGoal.html')

@app.route('/EditingGoal')
def EditingGoal():
    return render_template('EditingGoal.html')
@app.route('/DeleteGoal')

def DeleteGoal():
    return render_template('DeleteGoal.html')

if __name__ == '__main__':
    app.run()
