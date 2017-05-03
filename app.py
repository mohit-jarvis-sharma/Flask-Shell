from flask import Flask,render_template,request,redirect,url_for
from models import *
from shell import *
import shlex
import os

def push_db(cmd):
    temp_query = My_Shell.create(my_cmd = '>> ' + cmd, result_of_cmd = shell_result(cmd))
#Flask part
app = Flask('__name__')
@app.route('/',methods = ['POST' , 'GET'])
def index():
    """
    if request.method == 'POST':
        push_db(request.form['cmd'])
        return render_template('index.html' , temp = My_Shell.select())
    return render_template('index.html')"""
    if request.method == 'POST':
        if request.form['submit'] == 'Execute':
            push_db(request.form['cmd'])
            return render_template('index.html' , temp = My_Shell.select())
        elif request.form['submit'] == 'Restart Session':
            temp_query = My_Shell.delete()
            temp_query.execute()
            return render_template('index.html' , temp = None)
    return render_template('index.html' , temp = None)

if __name__ == "__main__":
    app.run(debug = True)
