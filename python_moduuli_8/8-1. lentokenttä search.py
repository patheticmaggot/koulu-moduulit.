import mysql.connector


def lentokenttahakija(yhteys, ICAO):
    kursori = yhteys.cursor()
    kursori.execute(f"SELECT name, municipality FROM airport WHERE ident = '{ICAO}';")
    return kursori.fetchone()

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='a1234xd',
         autocommit=True
         )

ICAO = input("Anna ICAO-koodi : ")
tulos = lentokenttahakija(yhteys, ICAO)
print(tulos)
