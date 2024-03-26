from flask import Flask
from flask import jsonify
import requests

app = Flask(__name__)

@app.route('/')
def info():
    return jsonify({
        'studentId': 200583720,
        'name': 'Ramkumar Subramanian',
    })

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route('/listCategories')
def category():

    categoryList = ["Algorithms Unlocked","Introduction to the Theory of Computation","Computer Networks: A Top-Down Approach","Clean Code: A Handbook of Agile Software Craftsmanship","Operating System Concepts","Artificial Intelligence: A Modern Approach","Database Management Systems","Computer Organization and Design: The Hardware/Software Interface","Web Development with HTML, CSS, and JavaScript","Data Structures and Algorithms in Java","Software Engineering: A Practitioner's Approach","Computer Graphics: Principles and Practice","Computer Architecture: A Quantitative Approach","Python Crash Course","Computer Networking: Principles, Protocols and Practice","Introduction to Machine Learning with Python","Head First Design Patterns","Introduction to Cyber Security","Art of Computer Programming, Volume 1: Fundamental Algorithms","Introduction to Data Mining","Computer Vision: Algorithms and Applications","The Mythical Man-Month: Essays on Software Engineering","Computer Systems: A Programmer's Perspective","Introduction to Robotics: Mechanics and Control","Code Complete: A Practical Handbook of Software Construction"
    ]
    
    categoryList.sort()
    return jsonify({
        'categories': categoryList
    })

@app.route('/listCategories2')
def category2():

    categoryList = ["Computer Networking: Principles, Protocols and Practice","Introduction to Machine Learning with Python","Head First Design Patterns","Introduction to Cyber Security","Art of Computer Programming, Volume 1: Fundamental Algorithms"
    ]
    
    categoryList.sort()
    return jsonify({
        'categories': categoryList
    })

@app.route('/webhook/getWeather/<city>')
def getWeather(city):
    if city == '':
        city = 'Barrie'

    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=e083a458742cf95bace14d3c6025cd58&units=metric')

    if response.status_code == 200:
        data = response.json()
        return jsonify({
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        })
    else:
        return jsonify({
            'error': response.json()
        })


if __name__ == '__main__':
    app.run()