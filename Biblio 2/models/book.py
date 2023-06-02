from mongoengine import Document, StringField, ReferenceField, CASCADE


class Book(Document):
    categorie = StringField(required=True)
    nom = StringField(required=True)
    description = StringField(required=True)
    auteur = StringField(required=True)
    userId = ReferenceField('User', required=True,
                            reverse_delete_rule=CASCADE)

    meta = {
        "indexes": [
           {"fields": ("nom", "auteur"), "unique": True}
        ],
    }
