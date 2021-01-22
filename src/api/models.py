from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = dbColumn(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = db.Column(db.DateTime) 
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(120), unique=True)
    village =  db.Column(db.String(120))
    age = dbColumn(db.Integer, nullable=False)

    # diseases = db.relationship("Diseases")
    # posts = db.relationship("Posts")
    # # donations = db.relationship("Donations")


    # def __str__(self):
    #     return '{} <{}>' .format(self.username, self.email)
    

    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "created_at": self.created_at,
    #         "updated_at": self.updated_at,
    #         "deleted_at": self.deleted_at,
    #         "first_name": self.first_name,
    #         "last_name": self.last_name,
    #         "email": self.email,
    #         "username": self.username,
    #         "avatar": self.avatar, 
    #         # "password": self.password 
    #         # al probar en insomnia me daba error porque es campo nullable = False
    #     }


class Conection(db.Model):
    id = dbColumn(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = db.Column(db.DateTime) 
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    village_supplier = (db.Column(db.String(120), unique=True, nullable=False))