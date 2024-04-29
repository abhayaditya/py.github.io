# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 09:25:37 2024

@author: abhay
"""

from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def show_students():
    students=[
        {
            "name":"Alice","age":20},
        {
        "name":"Bob","age":21},
        {
            "name":"Charlie","age":22},
        {
            "name":"Babu","age":22},
        ]
    return render_template('info.html',students=students)
app.run(port=5000)