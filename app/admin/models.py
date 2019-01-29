from app import db 
from datetime import datetime 
from werkzeug.security import generate_password_hash,check_password_hash

label_post = db.Table(
    'label_post',
    db.Column('label_id',db.Integer,db.ForeignKey('label.id')),
    db.Column('post_id',db.Integer,db.ForeignKey('post.id'))
)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post',backref='post',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError("password is not readable attribute")
    
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),index=True,unique=True)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id")) 
    body = db.Column(db.Text)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    create_time = db.Column(db.DateTime,default=datetime.now)
    last_modify = db.Column(db.DateTime,default=datetime.now)
    comments = db.relationship('Comment',backref='comment',lazy='dynamic')


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),index=True,unique=True)
    posts = db.relationship('Post',backref='post',lazy='dynamic')

class Label(db.Model):
    __tablename__ = 'label'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),index=True,unique=True)
    posts = db.relationship('Post',secondary=label_post,backref=db.backref('labels',lazy='dynamic'),lazy='dynamic')


class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),index=True)
    email = db.Column(db.String(50))
    body = db.Column(db.String(500))
    post_id = db.Column(db.Integer,db.ForeignKey('post.id'))


