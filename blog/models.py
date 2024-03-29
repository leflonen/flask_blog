from flask_blog import db
from datetime import datetime

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    admin = db.Column(db.Integer, db.ForeignKey('author.id'))
    posts = db.relationship('Post', backref='blog', lazy='dynamic')

    def __init__(self, name, admin):
        self.name = name
        self.admin = admin

    def __repr__(self):
        return '<Blog %r>' % self.name

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    slug = db.Column(db.String(256), unique=True)
    publish_date = db.Column(db.DateTime)
    live = db.Column(db.Boolean)
    #TODO: Add category.id database
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __init__(self, blog, author, title, body, category, slug=None, publish_date=None, live=True):
        self.blog_id = blog.id
        self.author_id = author.id
        self.title = title
        self.body = body
        self.slug = slug
        self.category = category
        if publish_date is None:
            self.publish_date = datetime.utcnow()
        else:
            self.publish_date = publish_date
        self.live = live

    def __repr__(self):
        return '<Post %r>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' %self.name
