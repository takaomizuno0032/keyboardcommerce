from datetime import datetime
from . import db


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(500), nullable=False)
    keyboards = db.relationship(
        'Keyboard', backref='Category', cascade="save-update, merge")

    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}\n"
        str = str.format(self.id, self.name, self.description)
        return str


orderdetails = db.Table('orderdetails',
                        db.Column('order_id', db.Integer, db.ForeignKey(
                            'orders.id'), nullable=False),
                        db.Column('keyboard_id', db.Integer, db.ForeignKey(
                            'keyboards.id'), nullable=False),
                        db.PrimaryKeyConstraint('order_id', 'keyboard_id'))


class Keyboard(db.Model):
    __tablename__ = 'keyboards'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    price = db.Column(db.Float, nullable=False)
    brand = db.Column(db.String(64), nullable=False)
    conective = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __repr__(self):
        str = "Id: {}, Name: {}, Price: {}, Brand: {}, Conective: {}, Description: {}, Image: {}, Category: {} \n"
        str = str.format(self.id, self.name, self.price, self.brand,
                         self.conective, self.description, self.image, self.category_id)
        return str


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    address = db.Column(db.String(500))
    date = db.Column(db.DateTime)
    totalcost = db.Column(db.Float)
    keyboards = db.relationship(
        "Keyboard", secondary=orderdetails, backref="orders")

    def __repr__(self):
        str = "Id: {}, Status: {}, FirstName: {}, LastName: {}, Email: {}, Address: {}, Dates: {}, TotalCost: {} \n"
        str = str.format(self.id, self.status, self.firstname, self.lastname, self.totalcost, self.email, self.address, self.date,
                         self.totalcost)
        return str
