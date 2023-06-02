from mongoengine import Document, StringField, EmailField, ReferenceField, ListField


class User(Document):
    nom = StringField(required=True)
    prenom = StringField(required=True)
    email = EmailField(required=True, unique=True)
    mdp = StringField(required=True)
    role = StringField(required=False, default='user')
    username = StringField(required=True, unique=True)
    bookIds = ListField(ReferenceField('Book'))
