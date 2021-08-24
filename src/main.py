from flask import Flask, render_template
from flask_restful import Resource, Api

# This example uses Python 2.7 and the python-request library.
# from requests import Request, Session
# from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
# import json

# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# parameters = {
#   'start':'1',
#   'limit':'5000',
#   'convert':'USD'
# }
# headers = {
#   'Accepts': 'application/json',
#   'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
# }

# session = Session()
# session.headers.update(headers)

# try:
#   response = session.get(url, params=parameters)
#   data = json.loads(response.text)
#   print(data)
# except (ConnectionError, Timeout, TooManyRedirects) as e:
#   print(e)


# class HelloWorld(Resource):
#     def get(self):
#         return 'Hello World'

# api.add_resource(HelloWorld, '/')

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
