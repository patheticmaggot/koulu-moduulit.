import json
from flask import Flask, Response


app = Flask(__name__)


@app.route('/alkuluku/<luku>')
def summa(luku):
    luku = int(luku)
    if luku == 1:
        tulos = False
    else:
        for k in range(2, luku):
            if luku % k == 0:
                tulos = False
                break
        else:
            tulos = True

    vastaus = {
        "Number": luku,
        "isPrime": tulos
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=200, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
