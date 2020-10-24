from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class User(UserMixin,db.Model):

    'User model schema'

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):

    'Pitch model schema'
    
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch_title = db.Column(db.String)
    pitch_body = db.Column(db.String)
    pitch_category = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    pitch_comments_count = db.Column(db.Integer, default=0)
    pitch_upvotes = db.Column(db.Integer, default=0)
    pitch_downvotes = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref = 'pitch',lazy = "dynamic")


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_all_pitches(cls):
        pitches = Pitch.query.order_by(Pitch.posted.desc()).all()
        return pitches

    @classmethod
    def get_user_pitches(cls,id):
        pitches = Pitch.query.filter_by(user_id=id).order_by(Pitch.posted.desc()).all()
        return pitches          


class Comment(db.Model):

    'Comment model schema'
    
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
  

         