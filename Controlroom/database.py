import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="juno",
        passwd="wnsgh0924",
        database="temp"
    )

def save_data_to_database(data):
    db = connect_to_database()
    cursor = db.cursor()
    query = "insert into DHT22 values(%s,%s,%s)"
    cursor.executemany(query, [data])
    db.commit()
    cursor.close()
    db.close()

def fetch_latest_data():
    db = connect_to_database()
    cursor = db.cursor(dictionary=True)
    query = "select time, temp AS temperature, hum AS humidity from DHT22 order by time desc limit 1"
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result

def fetch_all_data():
    db = connect_to_database()
    cursor = db.cursor(dictionary=True)
    query = "select time, temp AS temperature, hum AS humidity from DHT22 order by time desc"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result
