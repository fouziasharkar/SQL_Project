import mysql.connector
from mysql.connector import Error

class DB:
    def __init__(self):
        print("Initializing connection...")
        try:
            self.con_obj = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='Fsc@@2112##',
                database='Flight'
            )
            if self.con_obj.is_connected():
                print('Connection Successful')
                self.mycursor = self.con_obj.cursor()  # this gives the connection object

        except Error as e:
            print(f"Error: {e}")


    #city list
    def fetch_city_names(self):

        self.mycursor.execute("""

        SELECT DISTINCT(Source) FROM flight.`flights_cleaned - flights_cleaned`
        UNION
        SELECT DISTINCT(Destination) FROM flight.`flights_cleaned - flights_cleaned`

        """)

        city = []
        data = self.mycursor.fetchall()

        for i in data:
            city.append(i[0])

        print(city)
        return city


    def fetch_all_flights(self,start,destination):
        self.mycursor.execute("""
        SELECT Airline, Dep_Time, Route, Price FROM flight.`flights_cleaned - flights_cleaned`
        WHERE source= '{}' AND Destination = '{}'       
        """.format(start,destination))
        data = self.mycursor.fetchall()
        print(data)

        return data


    def daily_flight_frequency(self):

        self.mycursor.execute("""
        SELECT Airline, Count(*) From flight.`flights_cleaned - flights_cleaned`
        GROUP BY Airline       
        """)

        data = self.mycursor.fetchall()

        airline = []
        freq = []
        #print(data)

        for i in data:
            airline.append(i[0])
            freq.append(i[1])

        return airline, freq


    def busy_airport(self):

        self.mycursor.execute("""
        
        SELECT Source,COUNT(*) FROM (SELECT Source FROM flight.`flights_cleaned - flights_cleaned`
							UNION ALL
							SELECT Destination FROM flight.`flights_cleaned - flights_cleaned`) t
        GROUP BY t.Source
        ORDER BY COUNT(*) DESC
               
        """)

        city = []
        freq = []

        data = self.mycursor.fetchall()
        #print(data)
        for i in data:
            city.append(i[0])
            freq.append(i[1])

        return city, freq


    def expensive_airline(self):

        self.mycursor.execute("""
        
        SELECT 
        Airline, 
        Round(AVG(price)) AS price
        FROM 
        flight.`flights_cleaned - flights_cleaned`
        GROUP BY 
        Airline
        ORDER BY 
        price DESC Limit 5;
        
        """)

        data = self.mycursor.fetchall()
        print(data)

        return data





db = DB()
db.expensive_airline()
