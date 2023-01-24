from sqlalchemy import create_engine

db_string = "postgresql+psycopg2://postgres:1234567@localhost:5432/batch2db"

db = create_engine(db_string)

db.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")
db.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Derrickson', '2016')")

# result = db.execute("SELECT * FROM films")
# print(result)
# for r in result:
#     print(r)

result_set = db.execute("SELECT * FROM films")
for r in result_set:
    print(r)
    
    
db.execute("UPDATE films SET title='Some2016Film' WHERE year='2016'")
db.execute("DELETE FROM films WHERE year='2016'")