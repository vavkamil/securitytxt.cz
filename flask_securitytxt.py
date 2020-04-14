#!/usr/bin/python

from flask import Flask, render_template
import pymysql

app = Flask(__name__)

class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "localhost"
        db = "securitytxt"

        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def list_domains(self):
        self.cur.execute("SELECT domain, rank, txt, encryption, hiring, acknowledgments, policy FROM domains ORDER BY rank DESC")
        result = self.cur.fetchall()

        return result

    def count_domains(self):
        self.cur.execute("SELECT count(id) FROM domains")
        result = self.cur.fetchone()

        return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pridat-odkaz')
def pridat_odkaz():
    return render_template('pridat-odkaz.html')

@app.route('/generator')
def generator():
    return render_template('generator.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/statistiky')
def statistiky():

    def db_query():
        db = Database()
        emps = db.list_domains()

        return emps

    res = db_query()
    #print(res)

    def db_query2():
        db = Database()
        emps = db.count_domains()

        return emps

    res2 = db_query2()
    #print(res)
    return render_template('statistiky.html', result=res, count=res2, content_type='application/json')