import httpx
from dagster import job, op

@op
def extract_data():
    return httpx.get('http://localhost:8080/signal/list')

@op
def transform_data():
    pass

@op
def load_data():
    pass

@job
def etl_pipeline():
    extract_data()
    transform_data()
    load_data()