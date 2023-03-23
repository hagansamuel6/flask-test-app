import requests
from bs4 import BeautifulSoup

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# sqlite db setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/usd-exchange-rate')
def usd_exchange_rate():
    # Your code to retrieve the exchange rate goes here
    

    # Send HTTP request to Google.com's search results page for the Ghana cedi exchange rate
    url = 'https://www.google.com/search?q=usd+exchange+rate'
    response = requests.get(url)

    # Parse the HTML response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the element containing the exchange rate information
    exchange_rate_element = soup.find('div', {'class': 'BNeawe iBp4i AP7Wnd'}).get_text()

    # Extract the exchange rate from the element
    exchange_rate = exchange_rate_element.split(' ')[0]

    # print('Ghana cedi exchange rate:', exchange_rate)

    return {'usd_exchange_rate': exchange_rate}



if __name__ == '__main__':
    app.run(debug=True)
