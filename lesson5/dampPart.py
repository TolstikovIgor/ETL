import psycopg2

conn_string = "host='localhost' port=54320 dbname='my_database' user='root' password='postgres'"
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    q = "COPY part TO STDOUT WITH DELIMITER ',' CSV HEADER;"
    with open('resultsPart.csv', 'w') as f:
        cursor.copy_expert(q, f)
