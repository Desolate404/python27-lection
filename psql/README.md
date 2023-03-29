# Slash commands
* \l - вывод всех базданных(бд)
* \c - показывает через какого юзера и к какой бд мы подключились
* \c name_of_db - подключение к какой-то бд
* \du - список всех юзеров в postgres
* \dt - список всех таблиц в текущей бд
* \d+ - более подробная информация о таблицах в текущей БД
* \d+ name_of_table - более подробная информация о таблице
* \q - выход из субд(psql)
```sql
-- СУБД - система управления базой данных
```
# Создание бд и таблиц
```sql
CREATE DATABASE name_of_db;
-- создани базы данных
```


```sql
CREATE TABLE name_of_table (
    columnl data_type1,
    columnl data_type2,
    ...
);
-- создание таблицы
```
# удаление бд и таблиц
```sql
drop DATABASE name_of_db;
--удаление бд
```

```sql
DROP TABLE name_of_table;
--удаление таблицы
```

# Заполнение таблиц
```sql
INSERT INTO name_of_db VALUES
(val1, val2),
(val1.2, val2.2);
-- запись данных в таблицу (заполнение всех полей)
```

# вывод данных из таблицы
```sql
select * from name_of_table;
-- вывод всех записей со всеми полями
```

```sql
SELECT columnl, column3 FROM name_of_table;
-- вывод конкретных полей
```

# Условие
```sql
DELETE FROM name_of_table WHERE condition;
-- удаление всех записей из таблицы соответствующих данному условию


```sql
SELECT * FROM name_of_table WHERE column = 'hello';
-- строгое равенство
```

```sql
SELECT * FROM name_of_table WHERE column LIKE '%hello%';
-- записи включающие в себя данную строку с учетом регистра
-- aaahello
-- hello world
-- hello
-- Hello world - не пройдет (потому что регистр другой)
```

```sql
SELECT * FROM name_of_table WHERE column ILIKE '%hello%';
-- записи включающие в себя данную строку без учетом регистра
-- aaahello
-- hello world
-- hello
-- Hello world
-- Hello
```

```sql
SELECT * FROM name_of_table ORDER BY column;
-- сортировка записей по данному полю в порядке возрастания
```

```sql
SELECT * FROM name_of_table ORDER BY column DESC;
-- сортировка записей по данному полю в порядке убывания
```

```sql
SELECT * FROM name_of_table LIMIT 10;
-- вывод первых 10 записей
```

```sql
SELECT * FROM name_of_table OFFSET 10;
-- пропускаем первые 10 записей, выдает записи после 10-го 
```

```sql
SELECT * FROM name_of_table LIMIT 10 OFFSET 5;
-- пропускаем первые 5 записей
-- вытаскивает 10 записей
-- порядок не важен
-- говорят, это пагинация, хмм...
```
# Обновления таблицы
```sql
ALTER TABLE name_of_table ADD COLUMN col_name col_type constraint;
-- добавляет новую колонку в таблицу
```


```sql
ALTER TABLE name_of_table DROP COLUMN col_name;
--удаляем колонку из таблицы
```

```sql
ALTER TABLE name_of_table RENAME COLUMN col_name TO new_col_name
-- переименовывание колонки
```
```sql
ALTER TABLE name_of_table ALTER COLUMN col_name SET DATA TYPE new_type;
-- изменение типа данных
```

# Ограничения (constraints)
* 'UNIQUE' - не разрешает дубликаты
* 'NOT NULL' - требует обязательного заполнения поля
* 'PRIMARY KEY' - как UNIQUE и NOT NULL + строит binary tree(бинарное дерево) для быстрого поиска
* 'FOREIGN KEY' - ссылается на PRIMARY KEY в другой таблице и проверяет существует ли такой id

# Связи
## Виды связей
> Один к одному (one to one)
> один человек - один профиль
> один автор - одна автобиография

> Один ко многим (one to many)
> один блогер - много постов
> одна марка - много моделей
> одна страна - много областей
> один продукт - много коментариев

> Многие во многих (many to many)
> один разработчик - много проектов, один проект - много разработчиков

## реализация one2many в postgres
```sql
CREATE TABLE blogger (
    id serial PRIMARY KEY,
    name varchar(50),
    age int
);

CREATE TABLE post (
    id serial PRIMARY KEY,
    title varchar(100),
    body text,blogger_id int,

    CONSTRAINT fk_post_blogger
    FOREIGN KEY (blogger_id) REFERENCES blogger (id)
);
```

# JOINS
> **JOIN** - инструкция, котораая позволяет одним SELECT, брать данные из двух таблиц ( у которых есть связанные поля)

> **INNER JOIN (JOIN)** - достаются только те записи у которых есть дданные в обоих таблицах
> **FULL JOIN** - дотсаются все записи из первой таьлицы и со второй