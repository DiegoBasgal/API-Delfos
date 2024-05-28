import psycopg2
import random
from datetime import datetime, timedelta

def generate_random_data(start_time, end_time):
    current_time = start_time
    while current_time < end_time:
        yield {
            'timestamp': current_time.strftime('%Y-%m-%d %H:%M:%S'),
            'wind_speed': round(random.uniform(0, 30), 2),
            'power': round(random.uniform(0, 100), 2),
            'ambient_temperature': round(random.uniform(10, 30), 2)
        }
        current_time += timedelta(minutes=1)

def insert_data_to_db(data):
    conn = psycopg2.connect(
        dbname="fonte",
        user="admin",
        password="admin",
        host="localhost",
        port="5433"
    )
    cursor = conn.cursor()
    
    for row in data:
        cursor.execute("INSERT INTO data (timestamp, wind_speed, power, ambient_temperature) VALUES (%s, %s, %s, %s)",
                       (row['timestamp'], row['wind_speed'], row['power'], row['ambient_temperature']))
    
    conn.commit()
    cursor.close()
    conn.close()

def main():
    start_time = datetime.now()
    end_time = start_time + timedelta(days=10)

    data = list(generate_random_data(start_time, end_time))
    insert_data_to_db(data)

if __name__ == "__main__":
    main()