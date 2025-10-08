# Optional script to insert seed data into the database.
from db import SessionLocal, engine, Base
from models import Category, Product
Base.metadata.create_all(bind=engine)
db = SessionLocal()

cats = [
    {'name':'Almacen'}, {'name':'Carnes'}, {'name':'Lacteos'}
]
for c in cats:
    db.add(Category(name=c['name']))
db.commit()

# small product sample
db.add(Product(name='Arroz Largo Fino', price=5800.0, supermarket='D1'))
db.add(Product(name='Leche Entera 1L', price=4200.0, supermarket='Olimpica'))
db.commit()
print('Seed inserted.')

