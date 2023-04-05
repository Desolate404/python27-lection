from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# driveurl//user:
db_url = 'postgresql://Xexe:1@127.0.0.1:5432/sqlalchemy_test'
engine =  create_engine(db_url)
# подключение к БД

Base = declarative_base()
# базовый класс для таблиц

# создаем таблицу
class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Integer)

    def __repr__(self):
        return f"({self.id} -> {self.title})"

Base.metadata.create_all(bind=engine)
# записываем таблицу в БД


SessionLocal = sessionmaker(bind=engine)
# создаем класс для сессий (один обьект от данного класса - одна сессия)

session = SessionLocal()
# создаем сессию

# new_product = Product(title='product1', price=120)
# # создаем продукт (запись в таблицу)
# # для орм создаем запрос на запись в таблицу

# session.add(new_product)
# # добавляем наш запрос в сессию

# session.commit()
# # отрпавляем набор запросов в БД

products = session.query(Product).all()
# получаем все записи из таблицы products
print(products)

res = session.query(Product).filter(Product.price > 100).all()
print(res)

product3 = session.query(Product).get(3)
# получаем продукт под id 3
print(product3)

product4 = session.query(Product).get(4)
# #получаем продукт под id 4
# session.delete(product4)
# #удаляем продукт
# session.commit()
# #сохраняем изменения в бд

product3.title = 'new title'
product3.price = 100
# изменяем продукт
session.commit()
# сохраняем изменения в бд