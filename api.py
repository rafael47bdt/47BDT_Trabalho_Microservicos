import flask
from flask import request, jsonify
import mysql.connector

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''Bem vindo a API! para testar digite o caminho /api/testeConsulta'''


@app.route('/api/testeConsulta', methods=['GET'])
def api_all():


    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="fiap47bdt",
      database="rm338145"
    )
    cursor = mydb.cursor()

    query = ("SELECT * FROM tableFiap;")
    #query = ("show databases;")
    
    cursor.execute(query)
    #for (name) in cursor:
     #  print("{}, {} ".format(
      #  id, name))
    r = cursor.fetchall()
    return str(r)
    
    cursor.close()

    mydb.close()
    



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404



app.run()
