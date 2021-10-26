from app import Reader,Book, Review
from app import db
b1 = Book(id = 123, title = 'Demian', author_name = "Hermann", author_surname = 'Hesse', month = "February", year = 2020)

r1 = Reader(id = 342, name = 'Ann', surname = 'Adams', email = 'ann.adams@example.com')

db.session.add(b1)
db.session.commit()