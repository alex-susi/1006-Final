# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template
import requests
import pandas as pd
import bs4

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/1006")
def test():
    return render_template("1006.html")

@app.route("/columbia")
def columbia():
    return "Columbia"

@app.route("/Assignments")
def assignments():
    return render_template("Assignments.html")

@app.route("/NBA")
def advancedstats():
    return scrape("https://www.basketball-reference.com/leagues/NBA_2020_advanced.html")


def scrape(website):
    bs = bs4.BeautifulSoup(requests.get(website).content, 'lxml')
    tables = bs.find_all('table')
    stats = pd.read_html(str(tables[0]))[0]
    return stats
    

#start the server
if __name__ == "__main__":
    app.run()