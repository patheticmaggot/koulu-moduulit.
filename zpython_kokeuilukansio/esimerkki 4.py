import json
from flask import Flask, Response


app = Flask(__name__)


@app.route('/summa/<luku1>/<luku2>')
def summa(luku1, luku2):
    luku1 = float(luku1)
    luku2 = float(luku2)
    summa = luku1 + luku2

    vastaus = {
        "status": 200,
        "luku1": luku1,
        "luku2": luku2,
        "summa": summa
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=200, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": 404,
        "teksti": "virheellinen paatepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=200, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
