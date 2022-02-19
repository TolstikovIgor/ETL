import psycopg2

conn_string = "host='localhost' port=5433 dbname='my_database' user='root' password='postgres'"
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    q = "COPY nation from STDIN WITH DELIMITER ',' CSV HEADER;"
    with open('resultsNation.csv', 'r') as f:
        cursor.copy_expert(q, f)
