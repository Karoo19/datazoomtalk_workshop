#!/usr/bin/env python
# coding: utf-8



import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm




df = pd .read_csv(url)



df.head()



len(df)


df['tpep_pickup_datetime']


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates
)


df.head()


df['tpep_pickup_datetime']


df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])


print(df['tpep_pickup_datetime'].dtype)


df['tpep_pickup_datetime']



get_ipython().system('uv add sqlalchemy')



get_ipython().system('uv add psycopg2-binary')


print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))




engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

def run():


    pg_user = 'root'
    pg_pass = 'root'
    pg_host = 'localhost'
    pg_port = 5432
    pg_db = 'ny_taxi'

    year = 2021
    month = 1


df.head(0).to_sql()



df.head(0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')


from sqlalchemy.types import DateTime, Float, Integer, String

dtype_dict = {
    'tpep_pickup_datetime': DateTime(),
    'tpep_dropoff_datetime': DateTime(),
    'passenger_count': Integer(),
    'trip_distance': Float(),
    'payment_type': String()
    # Add all columns you want
}

print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine, dtype=dtype_dict))


psql -h localhost -U root -d ny_taxi



len(df)


# Define data types for columns
dtype = {
    'passenger_count': 'Int64',
    'trip_distance': 'float',
    'payment_type': 'string'
    # Add other columns as needed
}

# Define which columns should be parsed as dates
parse_dates = ['tpep_pickup_datetime', 'tpep_dropoff_datetime']



def run():


    pg_user = 'root'
    pg_pass = 'root'
    pg_host = 'localhost'
    pg_port = 5432
    pg_db = 'ny_taxi'

    year = 2021
    month = 1

    target_table= 'yellow_taxi_data'

    chunksize = 100000

prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow'
url = f'{prefix}/yellow_tripdata_{year}-{month:02d}.csv.gz'

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

df_iter = pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates,  # <-- COMMA added here
    iterator=True,
    chunksize=chunksize,
)




get_ipython().system('uv add tqdm')



    first = True
for df_chunk in tqdm(df_iter):
    if first:
        df_chunk.head(0).to_sql(
            name='yellow_taxi_data',
            con=engine,
            if_exists='replace'
        )
        first = False

    df_chunk.to_sql(
        name=target_table,
        con=engine,
        if_exists='append'
    )


if __name__== '__main__':
    run()


df = next(df_iter)






