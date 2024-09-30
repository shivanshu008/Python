# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 09:16:01 2024

@author: shivanshu gaurav
"""

from flask import Flask, render_template, request

app = Flask(__name__)

student_data = {}  # This will hold student records

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    student_id = request.form['student_id']
    scores = {
        'Math': float(request.form['math']),
        'Science': float(request.form['science']),
        'English': float(request.form['english'])
    }
    total_score = sum(scores.values())
    average_score = total_score / len(scores)

    if average_score >= 90:
        grade = 'A'
    elif average_score >= 80:
        grade = 'B'
    elif average_score >= 70:
        grade = 'C'
    elif average_score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    student_data[student_id] = {
        'name': name,
        'scores': scores,
        'total_score': total_score,
        'grade': grade
    }

    return render_template('index.html', message="Student added successfully!")

if __name__ == '__main__':
    app.run(debug=True)
