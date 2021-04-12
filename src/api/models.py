from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func

db = SQLAlchemy()
# será que esto da error en el vs code? Digo.. porque "se supone" que es posgressSQL

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = db.Column(db.DateTime) 
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    age= db.Column(db.Integer(), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    #tengo dudas si hacemos el FK de villages, todo por leer documentación
    villages_id =  db.Column(db.Integer(), ForeignKey('villages.id'))
   
    villages = db.relationship('Villages')

    def __str__(self):
        return '{} <{}>' .format(self.email, self.dni)
    
    def serialize(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "age": self.age,
            "village": self.villages_id
        }
    

class Villages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = db.Column(db.DateTime) 
    village_name = db.Column(db.String(125), unique=True, nullable = False)
    volunteer_first_name = db.Column(db.String(80), nullable = False)
    volunteer_last_name = db.Column(db.String(120), nullable = False)
    volunteer_email = db.Column(db.String(120), unique=True, nullable=False)
    volunteer_phone = db.Column(db.String(120), nullable=False)

    users = db.relationship('Users')

    def __str__(self):
        return '{} <{}>' .format(self.village_name, self.volunteer_phone)
    

    def serialize(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
            "village_name": self.village_name,
            "volunteer": self.volunteer_first_name,
            "email": self.volunteer_email,
            "phone": self.volunteer_phone
        }
    

class Packages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = db.Column(db.DateTime) 
    books_id = db.Column(db.Integer, ForeignKey('books.id'))
    # user_id = db.Column(db.Integer, ForeignKey('users.id')) no estoy segura de que haya que ponerlo puesto que ya existe la tabla intermedia "Reservations"
    suitable_ages =  db.Column(db.String(3))
    package_tittle = db.Column(db.String(120), unique=True)
    package_description = db.Column(db.Text, nullable=False)
    reserved_status = db.Column(db.Boolean(), nullable=False)
    date_reservation = db.Column(db.String(120))
    # reserved_status y date_reservation no sé si irían en reservations directamente
    

    # users = db.relationship("Users")
    books = db.relationship("Books")
    reservations = db.relationship("Reservations")

    def __str__(self):
        return '{} <{}>' .format(self.package_tittle, self.package_description)
    

    def serialize(self):
        # reviews = []

        # for review in self.reviews:
        #     reviews.append(review.serialize())

        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
            "books": self.books_id, #si quiero todos los books, lista de books no habrá que hacer lo mismo de reviews? 
            "suitable_ages": self.suitable_ages,
            "package_tittle": self.package_tittle
        }
 

class Reservations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = db.Column(db.DateTime) 
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    package_id = db.Column(db.Integer, ForeignKey('packages.id')) 
    returning_date = db.Column(db.DateTime)

    users = db.relationship("Users")
    packages = db.relationship("Packages")
   

    def __str__(self):
        return '{} <{}>' .format(self.returning_date, self.package_id)
    


    def serialize(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
            "returning_date": self.returning_date,
            # "user": self.user_id, 
            "package": self.package_id,
        }


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = db.Column(db.DateTime) 
    writer_reviews_id = db.Column(db.Integer, ForeignKey('users.id')) 
    package_reviewed_id = db.Column(db.Integer, ForeignKey('packages.id'))
    text_review = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    users = db.relationship("Users") 
    packages = db.relationship("Packages") 


    def __str__(self):
        return '{} <{}>' .format(self.package_reviewed_id, self.writer_reviews_id) 
    

    def serialize(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
            "writer_reviews": self.user_id,
            "package_reviewed": self.packages_id,
            "text_review": self.text_review
        }
    
    # def serialize_required(self):
    #     return{
    #         "writer_revies_id": int,
    #         "package_reviewed_id": int,
    #         # "text_review": text?
    #     }

    # def serialize_all_types(self):
    #     return{
    #         "writer_revies_id": int,
    #         "package_reviewed_id": int,
    #         # "text_review": text?
    #     }


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = db.Column(db.DateTime)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    suitable_ages = db.Column(db.String(120), nullable=False)
    pages = db.Column(db.String(100))
    book_description = db.Column(db.String(500), nullable=False)

    packages = db.relationship("Packages")
    

    def __str__(self):
        return '{} <{}>' .format(self.created_at, self.title, self.author)
    

    def serialize(self):
        
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
            "title": self.title,
            "author": self.author,
            "suitable_ages": self.suitable_ages,
            "pages": self.pages,
            "book_description": self.book_description,
        }

    # def serialize_required(self):
    #     return{
    #         "title": str,
    #         "author": str,
    #         "suitable_ages": str,
    #         "pages": str,
    #         "book_description": str
    #     }

    # def serialize_all_types(self):
    #     return{
    #         "title": str,
    #         "author": str,
    #         "suitable_ages": str,
    #         "pages": str,
    #         "book_description": str
    #     }

