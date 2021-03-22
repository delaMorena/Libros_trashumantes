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
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(120), unique=True)
    dni = db.Column(db.Integer, unique=True, nullable=False)
    village =  db.Column(db.Integer, ForeignKey('villages.id'))
    volunteer_id = db.Column(db.Integer, ForeignKey('volunteers.id'))
    # avatar = db.Column(db.String(255))

    volunteers = db.relationship("Volunteers")
    villages = db.relationship("Villages")
    # reviews = db.relationship("Reviews")
   
    # packages = db.relationship("Packages")
    # reservations = db.relationship("Reservations")
    


    def __str__(self):
        return '{} <{}>' .format(self.username, self.email)
    

    def serialize(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "username": self.username,
            "village": self.village
            # "avatar": self.avatar
        }
    
    # def serialize_required(self):
    #     return{
    #         "first_name": str,
    #         "last_name": str,
    #         "email": str,
    #         "username": str,
    #         "avatar": str,
    #         "password": str
    #     }

    # def serialize_all_types(self):
    #     return{
    #         "first_name": str,
    #         "last_name": str,
    #         "email": str,
    #         "username": str,
    #         "avatar": str
    #     }

class Villages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = db.Column(db.DateTime) 
    village_name = db.Column(db.String(125), unique=True, nullable = False)
    

    # citizens = db.relationship("Users")
    # designated_volunteer = db.relationship("Volunteers")

    def __str__(self):
        return '{} <{}>' .format(self.village_name)
    

    def serialize(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
            "village_name": self.village_name
        }

    # def serialize_required(self):
    #     return{
    #         'village_name': str
    #     }

    # def serialize_all_types(self):
    #     return{
    #         'village_name': str
    #     }
    

class Packages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = db.Column(db.DateTime) 
    books_id = db.Column(db.Integer, ForeignKey('books.id'))
    # user_id = db.Column(db.Integer, ForeignKey('users.id')) no estoy segura de que haya que ponerlo puesto que ya existe la tabla intermedia "Reservations"
    package_tittle = db.Column(db.String(120), unique=True)
    suitable_ages =  db.Column(db.String(120))
    subject = db.Column(db.String(120))
    package_description = db.Column(db.Text, nullable=False)
    reserved_status = db.Column(db.Boolean(), nullable=False)
    date_reservation = db.Column(db.String(120))
    # reserved_status y date_reservation no sé si irían en reservations directamente
    

    # users = db.relationship("Users")
    books = db.relationship("Books")
    # reservations = db.relationship("Reservations")

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
            "books": self.books_id,
            "suitable_ages": self.suitable_ages,
            "package_tittle": self.package_tittle
        }
    # def serialize_required(self):
    #     return{
    #         "books_id": int,
    #         "user_id": int,
    #         "package_tittle": str,
    #         "suitable_ages": str,
    #         "subject": str,
    #         "reserved_status": bool,
    #         "date_reservation": str,
    #         # "package_description": ?
    #     }

    # def serialize_all_types(self):
    #     return{
    #         "books_id": int,
    #         "user_id": int,
    #         "package_tittle": str,
    #         "suitable_ages": str,
    #         "subject": str,
    #         "reserved_status": bool,
    #         "date_reservation": str,
    #         # "package_description": ?
    #     }


class Volunteers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = db.Column(db.DateTime) 
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    village_supplier = db.Column(db.Integer, ForeignKey('villages.id'))
    info_reservation = db.Column(db.Integer, ForeignKey('reservations.id'))

    # users = db.relationship("Users") pruebo a quitarlo para buscar el error
    villages = db.relationship("Villages")
    info = db.relationship("Reservations")
    


    def __str__(self):
        return '{} <{}>' .format(self.info_reservation, self.email, self.phone)
    

    def serialize(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            # "village_supplier": self.village_supplier
        }

    # def serialize_required(self):
    #         return{
    #             "first_name": str,
    #             "last_name": str,
    #             "email": str,
    #             "phone": str,
    #             "village_supplier": str,
    #             "info_reservation": int
    #         }

    # def serialize_all_types(self):
    #     return{
    #         "first_name": str,
    #         "last_name": str,
    #         "email": str,
    #         "phone": str,
    #         "village_supplier": str,
    #         "info_reservation": int
    #     }

class Reservations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = db.Column(db.DateTime) 
    # user_id = db.Column(db.Integer, ForeignKey('users.id')) OJO !!!!!!!!!!
    package_id = db.Column(db.Integer, ForeignKey('packages.id')) 
    returning_date = db.Column(db.DateTime)

    # users = db.relationship("Users") OJO !!!!!!!!!!
    packages = db.relationship("Packages")
    volunteers = db.relationship("Volunteers")


    def __str__(self):
        return '{} <{}>' .format(self.returning_date, self.package_id)
    

    def serialize(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
            "returning_date": self.returning_date,
            # "user": self.user_id, OJO !!!!!!!!!!
            "package": self.package_id,
        }
    
    # def serialize_required(self):
    #     return{
    #         "user_id": int,
    #         "package_id": int,
    #         "returning_date": str
    #     }

    # def serialize_all_types(self):
    #     return{
    #         "user_id": int,
    #         "package_id": int,
    #         "returning_date": str
    #     }

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

