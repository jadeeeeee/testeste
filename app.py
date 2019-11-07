from flask import Flask, render_template
from formulario import 

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///msgs.db'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario', methods=[POST, GET])
def formulario():
    form = MsgForm()

    return render_template('formulario.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
