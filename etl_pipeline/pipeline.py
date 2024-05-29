import json
import httpx
import pandas
import psycopg2
from datetime import datetime
from dagster import job, op

@op
def extract_data():
    conn = psycopg2.connect(
        dbname="fonte",
        user="admin",
        password="admin",
        host="localhost",
        port="5433"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM data")
    rows = cursor.fetchall()

    raw_data_df = pandas.DataFrame(rows, columns=['timestamp', 'wind_speed', 'power', 'ambient_temperature'])

    return raw_data_df

@op
def transform_data(raw_data: pandas.DataFrame):

    raw_data["wind_speed"] = raw_data["wind_speed"].apply(float)
    raw_data["power"] = raw_data["power"].apply(float)
    raw_data["ambient_temperature"] = raw_data["ambient_temperature"].apply(float)
    mean = [raw_data["wind_speed"].mean(), raw_data["power"].mean(), raw_data["ambient_temperature"].mean()]
    max = [raw_data["wind_speed"].max(), raw_data["power"].max(), raw_data["ambient_temperature"].max()]
    min = [raw_data["wind_speed"].min(), raw_data["power"].min(), raw_data["ambient_temperature"].min()]
    std = [raw_data["wind_speed"].std(), raw_data["power"].std(), raw_data["ambient_temperature"].std()]

    transformed_data_df = pandas.DataFrame([mean, max, min, std], index=['mean', 'max', 'min', 'std'], columns=['wind_speed', 'power', 'ambient_temperature'])

    return transformed_data_df

@op
def load_data(transformed_data: pandas.DataFrame):

    id = 0
    for row in transformed_data.itertuples():
        items = ['wind_speed', 'power', 'ambient_temperature']
        for index, item in enumerate(items):
            id += 1
            dct = {"id": id, "name": row.Index +'_'+ item, "value":row[1:].__getitem__(index)}
            httpx.post("http://localhost:8080/signal/create", json={"name": dct["name"]})
            httpx.post("http://localhost:8080/signal/data/add", json={"timestamp": str(datetime.now()), "value": dct["value"], "signal_id": dct["id"]})

@job
def etl_pipeline():
    raw_data = extract_data()
    transformed_data = transform_data(raw_data)
    load_data(transformed_data)