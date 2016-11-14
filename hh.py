from flask import Flask
from flask import url_for, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def form():
  #  if request.args:
    name = request.args['name']
    age = request.args['age']
    L1 = request.args['L1']
    L2 = request.args['L2']
    return render_template('anketa.html', name=name, age=age, L1=L1, L2=L2)
#    return redirect(url_for('thanku'))
        
#@app.route('/thanku')
#def thanku():
#    return render_template('thanku.html')
    
if __name__ == '__main__':
    app.run(debug=True)
