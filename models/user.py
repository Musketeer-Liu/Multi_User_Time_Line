from google.appengine.ext import db
from utility import make_pw_hash, valid_pw, user_key

class User(db.Model):
    name = db.StringProperty(required=True)
    pw_hash = db.StringProperty(required=True)
    email = db.StringProperty()

    @classmethod
    def by_id(cls, uid):
        return User.get_by_id(uid, parent=user_key())


    @classmethod
    def by_name(cls, name):
        return User.all().filter('name =', name).get()

    @classmethod
    def signup(cls, name, pw, email=None):
        pw_hash = make_pw_hash(name, pw)
        return User(parent=user_key(),
                    name=name,
                    pw_hash=pw_hash,
                    email=email)

    @classmethod
    def login(cls, name, pw):
        user = cls.by_name(name)
        if user and valid_pw(name, pw, u.pw_hash):
            return user
        return None