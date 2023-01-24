from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "postgresql+psycopg2://postgres:1234567@localhost:5432/batch2db"
db = create_engine(db_string)

base = declarative_base()

class FilmORM(base):
    __tablename__ = 'filmORM'
    
    title = Column(String, primary_key=True)
    director = Column(String, nullable=False)
    year = Column(String, nullable=False)
    
Session = sessionmaker(db)
sess = Session()

base.metadata.create_all(db)

# create
doctor_strange = FilmORM(
    title = "Doctor Strange Multivers",
    director = "Director",
    year = "2021"
)

sess.add(doctor_strange)
sess.commit()

# Read
films = sess.query(FilmORM)
for film in films:
    print(film.title)
    
# Update
doctor_strange.title = "Some2016Film"
sess.commit()

# Delete
sess.delete(doctor_strange)
sess.commit()