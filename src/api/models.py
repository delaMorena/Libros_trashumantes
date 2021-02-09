from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = db.Column(db.DateTime) 
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(120), unique=True)
    village =  db.Column(db.String(120))
    age = db.Column(db.Integer, nullable=False)
    conection_id = db.Column(db.Integer, ForeignKey('conections.id'))

    conections = db.relationship("Conections")
    # reviews = db.relationship("Reviews")
    # packages = db.relationship("Packages")
    # leandings = db.relationship("Leandings")


    def __str__(self):
        return '{} <{}>' .format(self.username, self.email, self.village)
    

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
            "avatar": self.avatar, 
            "village": self.village
            # "password": self.password 
            # al probar en insomnia me daba error porque es campo nullable = False
        }
class Packages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = db.Column(db.DateTime) 
    books_id = db.Column(db.Integer, ForeignKey('books.id'))
    last_owner_id = db.Column(db.Integer, ForeignKey('users.id'))
    package_tittle = db.Column(db.String(120), unique=True)
    suitable_age =  db.Column(db.String(120))
    package_description = db.Column(db.text, nullable=False)

    users = db.relationship("Users")
    books = db.relationship("Books")
    leandings = db.relationship("Leandings")


    def __str__(self):
        return '{} <{}>' .format(self.package_tittle, self.package_description)
    

    def serialize(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
            "books": self.books_id,
            "last_owner": self.last_owner_id,
            "suitable_age": self.suitable_age,
            "package_tittle": self.package_tittle
            # "password": self.password 
            # al probar en insomnia me daba error porque es campo nullable = False
        }


class Conections(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = db.Column(db.DateTime) 
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    village_supplier = (db.Column(db.String(120), unique=True, nullable=False))

    users = db.relationship("Users")


    def __str__(self):
        return '{} <{}>' .format(self.village_supplier, self.phone)
    

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
            "village_supplier": self.village_supplier
            # "password": self.password 
            # al probar en insomnia me daba error porque es campo nullable = False
        }

class Leandings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = db.Column(db.DateTime) 
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    package_id = db.Column(db.Integer, ForeignKey('packages.id'))

    users = db.relationship("Users")
    packages = db.relationship("Packages")


    def __str__(self):
        return '{} <{}>' .format(self.created_at, self.books_id)
    

    def serialize(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
            "user": self.user_id,
            "books": self.books_id,
            "email": self.email,
            "phone": self.phone,
            "village_supplier": self.village_supplier
            # "password": self.password 
            # al probar en insomnia me daba error porque es campo nullable = False
        }

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = db.Column(db.DateTime) 
    writer_revies_id = db.Column(db.Integer, ForeignKey('users.id'))
    book_reviewed_id = db.Column(db.Integer, ForeignKey('books.id'))

    users = db.relationship("Users")
    books = db.relationship("Books")


    def __str__(self):
        return '{} <{}>' .format(self.created_at, self.book_reviewed_id, self.writer_revies_id)
    

    def serialize(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
            "writer_revies": self.user_id,
            "book_reviewed": self.books_id
            # "password": self.password 
            # al probar en insomnia me daba error porque es campo nullable = False
        }


