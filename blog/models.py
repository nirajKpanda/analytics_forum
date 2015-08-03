from blog.helpers.ext import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))
    email = db.Column(db.String, unique=True)
    about_me = db.Column(db.String)
    posts = db.relationship('Post', backref='writer', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<user: {}>".format(self.username)


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.String(140))
    author = db.Column(db.Integer, db.ForeignKey(User.id))
    upvotes = db.Column(db.Integer, default=0)
    downvotes  = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime)

    def __repr__(self):
        return "<{} by {}>".format(self.title, self.author)


class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    commented_by = db.Column(db.Integer, db.ForeignKey(User.id))
    postid = db.Column(db.Integer, db.ForeignKey(Post.id))
    text = db.Column(db.String)
    posts = db.relationship('Post', backref="comment", lazy="dynamic", uselist=True)

    def __repr__(self):
        return "@{} commented: {}".format(self.commented_by, self.text) 

