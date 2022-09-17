import mysql.connector
from geopy import distance


def lentokenttahakija(yhteys, ident):
    sql = f'SELECT latitude_deg, longitude_deg, name FROM airport WHERE ident = "{ident}";'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return kursori.fetchall()[0]


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='a1234xd',
         autocommit=True
         )

icao1 = input('anna ensimmäisen lentokentän ICAO-koodi:')
icao2 = input('anna toisen lentokentän ICAO-koodi:')

koord1 = lentokenttahakija(yhteys, icao1)
koord2 = lentokenttahakija(yhteys, icao2)

print(f'lentokenttien {koord1[2]} ja {koord2[2]}\n'
      f'etäisyys toisistaan on: {distance.distance(koord1[0:2], koord2[0:2]).km:.0f} km')
