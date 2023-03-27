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
