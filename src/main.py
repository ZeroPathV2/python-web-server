from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# class HelloWorld(Resource):
#     def get(self):
#         return 'Hello World'

# api.add_resource(HelloWorld, '/')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/crypto')
def cryptoPage():
    return render_template('cryptoPage.html')


@app.route('/emails')
def email():
    return render_template('emails.html')


if __name__ == '__main__':
    app.run(debug=True)
