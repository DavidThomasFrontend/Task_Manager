import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'task_manager'
app.config['MONGO_URI'] = 'mongodb+srv://dthomas86:r00tuser@myfirstcluster-pf6q6.mongodb.net/task_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_tasks')

def get_tasks():
    return render_template('tasks.html', tasks=mongo.db.tasks.find()) ##going to redirect to an existing template ie task.html - supply tasks collection returned making call to mongo##

@app.route('/add_task')
def add_task():
    return render_template('addtask.html',
    categories=mongo.db.categories.find())


if __name__ == '__main__':
    app.run(host = os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug = True)    ##this allows changes to be picked up by browser, will also producr bug reports in the event of a bug##

            