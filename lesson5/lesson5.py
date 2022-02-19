import psycopg2


def dump_to_csv(conn_string, tables):
    with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
        for table in tables:
            query = f"COPY {table} TO STDOUT WITH DELIMITER ',' CSV HEADER;"
            with open(f'./resultsfile/{table}.scv', 'w') as csv_file:
                cursor.copy_expert(query, csv_file)


def load_from_csv(conn_string, tables):
    with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
        for table in tables:
            query = f"COPY {table} from STDIN WITH DELIMITER ',' SCV HEADER;"
            with open(f'./resultsfile/{table}.scv', 'r') as csv_file:
                cursor.copy_expert(query, csv_file)


conn_string1 = "host='localhost' port=54320 dbname='my_database' user='root' password='postgres'"
conn_string2 = "host='localhost' port=5433 dbname='my_database' user='root' password='postgres'"
tables = ['nation', 'region', 'part', 'supplier', 'partsupp', 'customer', 'orders', 'lineitem']

dump_to_csv(conn_string1, tables)
load_from_csv(conn_string2, tables)
