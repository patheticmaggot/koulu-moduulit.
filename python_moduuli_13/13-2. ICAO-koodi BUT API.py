import mysql.connector
import json
from flask import Flask, Response



def koodihakija(koodi):
    sql = f'SELECT name, municipality FROM airport WHERE ident = "{koodi}";'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return kursori.fetchall()[0]


app = Flask(__name__)
@app.route('/kenttä/<ICAO>')
def tulostus(ICAO):
    result = koodihakija(ICAO)

    vastaus = {
        "ICAO": ICAO,
        "Name": result[0],
        "Municipality": result[1]
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=200, mimetype="application/json")

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='a1234xd',
         autocommit=True
         )

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

