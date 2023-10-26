from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    model = Column(String(40))
    price = Column(Integer)


Base.metadata.create_all(engine)



from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
new_product = Product(name='Lenovo', model='Aspire', price=500)
session.add(new_product)

our_product = (session.query(Product).filter_by(name='Lenovo').first())
print(our_product)