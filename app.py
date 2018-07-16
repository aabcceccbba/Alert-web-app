from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
from flask_table import Table, Col
from google.cloud import bigquery

# # Or, equivalently, some dicts

# # Or, more likely, load items from your database with something like
# items = ItemModel.query.all()

# Populate the table

# Print the html
def get_data_from_bigquery():
    """query bigquery to get data to import to PSQL"""
    bq = bigquery.Client(project="datalab-205719")
    query = """SELECT DATE_TIME, dr3 FROM `water.cor`
    LIMIT 10"""
    query_job = bq.query(query)
    data = query_job.result()
    rows = list(data)
    return rows

app = Flask(__name__)
 
@app.route("/")
def index():
  # rows = Units.query.all()
  # rows = [dict(a='Name1', b='Description1'),
  #        dict(a='Name2', b='Description2'),
  #        dict(a='Name3', b='Description3')]
  rows = get_data_from_bigquery()
  return render_template('table.html',
                            title='Overview',
                            rows=rows)
 
#@app.route("/hello/<string:name>")
@app.route("/hello/<string:name>/")
def hello(name):
#    return name
    quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
               "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
               "'To understand recursion you must first understand recursion..' -- Unknown",
               "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
               "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
               "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
    randomNumber = randint(0,len(quotes)-1) 
    quote = quotes[randomNumber] 
    gg = "jintianzhendeshichaojiganga"
    return render_template(
        'test.html',**locals())
 
if __name__ == "__main__":
    app.run()
