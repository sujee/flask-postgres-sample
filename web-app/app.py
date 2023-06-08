# Importing required functions
import os, sys

## set log_level explicity
# os.environ["MY_DEBUG"] = 'DEBUG' # DEBUG / INFO / WARNING / ERROR

from flask import Flask, request, render_template
import json
import psycopg2



# Connect to db
DB_HOST=os.getenv('PGHOST', 'postgres')
DB_USER=os.getenv('PGUSER', 'postgres')
DB_PASSWORD=os.getenv('PGPASSWORD', 'postgres')
DB_PORT=os.getenv('PGPORT', '5432')
DB_DATABASE=os.getenv('PGDATABASE', 'happydb')
DB_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
connection = psycopg2.connect(f"dbname='{DB_DATABASE}' user='{DB_USER}' host='{DB_HOST}' port='{DB_PORT}' password='{DB_PASSWORD}'")
print("Connection url:", DB_URL)

# Flask constructor
app = Flask(__name__)


#----    index ---------------------
# Root endpoint
@app.route('/', methods=['GET'])
def index():
    ## Display the HTML form template
    return render_template('index.html', DB_URL = DB_URL)
#---- end: index ---------------------

# Main Driver Function
if __name__ == '__main__':

    # Run the application on the local development server
    app.run(host='0.0.0.0', debug=True)
    # app.run(host='0.0.0.0')
    # app.run('0.0.0.0', 8000, debug=True)