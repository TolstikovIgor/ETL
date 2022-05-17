### Курсовой проект
Создать:
- dag который пересоздает (drop if exists) в целевой базе нужные таблицы (копирует схему из source), выполняется однократно.

В целевой базе таблицы создавать следует в отдельной схеме (stage)

Запуск большого кол-ва операторов sql можно вынести в отдельный файл и вызвать:<br>
>    create_tables_step = PostgresOperator(<br>
>      task_id="create_tables",<br>
>      postgres_conn_id="pg_target",<br>
>      sql="sql/my_file.sql"<br>
>      )

- dag который пересоздает в целевой базе таблицы для хранения данных в модели data vault, однократно

Продумайте структуру хранения для данных в терминах хабов, линков и их саттелитов. Подсказка - должно быть 3 хаба и 2 линка.
Сформируйте файл sql который создаст такую структуру.

Для хранения данных после преобразования используйте отдельную схему для таблиц (core)
- dag который копирует данные из исходной\source бд в целевую в stage, сохраняя формат
- dag который копирует данные из stage схемы в core схему (все манипуляции происходят на целевой\target БД)

Хабы будут иметь вид:

>     create table core.h_orders ( 
>        h_order_rk SERIAL PRIMARY KEY,
>        order_id int,
>        source_system string,
>        processed_dttm datetime
>        UNIQUE(order_bk)
>      );

Таким образом мы поддерживаем уникальность сурогатного и бизнес ключа.

Сателлиты будут иметь вид:
>     create table core.s_orders (
>         h_order_rk int,
>         name text,
>         source_system string,
>         valid_from_dttm datetime,
>         valid_to_dttm datetime,
>         processed_dttm datetime
>         (ключ FK для провеки корректности работы рекомендуется)
>     );

[lesson8_v2.ipynb](https://drive.google.com/file/d/1OMKHY6mBkkf3BZok7Rsc1iUPxH3G-A_l/view?usp=sharing)
