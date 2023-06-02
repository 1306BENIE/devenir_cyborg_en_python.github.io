from flask import Flask, jsonify, request
from models.user import User
from models.book import Book
from mongoengine import connect
from utils.format_id import from_objectId_to_json
import certifi


app = Flask(__name__)

connect(host="mongodb+srv://lebigbg:8hPW0fRJFuV4VVOR@cluster0.xyntwm2.mongodb.net/test",
        tlsCAFile=certifi.where())


@app.post('/api/user/')
def create_user():
    try:
        user_info = request.get_json()
        del user_info['role']
        new_user = User(**user_info)
        new_user.save()
        return from_objectId_to_json(new_user)
    except Exception as e:
        print("erreur", e)
        return "Y'a eu une erreur"


@app.get('/api/user/<id>')
def get_user(id):
    try:
        user = User.objects.get(id=id)
        return from_objectId_to_json(user)
    except Exception as e:
        print("erreur", e)
        return "Y'a eu une erreur"


@app.get('/api/users')
def get_all_users():
    try:
        users = User.objects.all()
        return [from_objectId_to_json(user) for user in users]

    except Exception as e:
        print(e.with_traceback())
        return jsonify([])


@app.put('/api/user/<id>')
def update_user(id: str):
    try:
        user = User.objects.get(id=id)
        user_info = request.get_json()
        if (user_info['mdp'] == from_objectId_to_json(user)["mdp"]):
            print("c'est le bon utilisateur")
            user.update(**user_info)
            user.save()
            return from_objectId_to_json(user)

        raise PermissionError("vous n'êtes pas authorisé")

    except Exception as e:
        print(e)
        return e.__str__()


@app.delete('/api/user/<id>')
def delete_user(id: str):
    try:
        user = User.objects.get(id=id)
        mdp = request.get_json()['mdp']
        userinfo = from_objectId_to_json(user)
        if userinfo['mdp'] == mdp or userinfo['role'] == 'admin':
            user.delete()
            return 'supprimer avec succès'

        raise PermissionError('Action non authorisé')

    except Exception as e:
        print('error : ', e)
        return 'Une erreur est survenue'

# ======================   BOOK ROUTES   ======================


@app.post('/api/book')
def create_book():
    try:
        infos = request.get_json()
        user = User.objects.get(id=infos['userId'])
        new_book = Book(**infos)
        new_book.save()
        user.update(push__bookIds=new_book.to_dbref())
        return from_objectId_to_json(new_book)

    except Exception as e:
        error_message = e.__str__()
        print("error : ", error_message)
        if ('User matching query' in error_message):
            return "L'utilisateur n'existe pas"

        if ('duplicate key error' in error_message):
            return "Ce livre existe déjà"

        return 'une erreur est survenue ...'


@app.get('/api/book/<id>')
def get_book(id):
    try:
        book = Book.objects.get(id=id)
        return from_objectId_to_json(book)
    except:
        return 'Aucun livre trouvé'


@app.get('/api/books')
def get_all_books():
    try:
        books = Book.objects.all()
        return [from_objectId_to_json(book) for book in books]
    except:
        return "Une erreur est survénue ..."


@app.get('/api/books/<userId>')
def get_my_books(userId: str):
    try:
        books = Book.objects(userId=userId)
        return [from_objectId_to_json(book) for book in books]
    except Exception as e:
        print(e)
        return "Une erreur est survenue ..."


@app.delete('/api/book/<id>')
def delete_book(id: str):
    try:
        request_info = request.get_json()
        user = User.objects.get(id=request_info['userId'])
        inter_user = from_objectId_to_json(user)
        book = Book.objects.get(id=id)
        book_json = from_objectId_to_json(book)

        print(user['mdp'], request_info['mdp'],
              book_json['userId'], request_info['userId'])

        # assert the user is an admin or user is the owner of the book
        if (inter_user['mdp'] == request_info['mdp'] and (book_json['userId']['$oid'] == request_info['userId']) or inter_user['role'] == 'admin'):
            book.delete()
            # remove the book from the user's bookIds
            user['bookIds'].remove(book.to_dbref())
            return 'supprimer avec succès'

        raise PermissionError('Action non authorisé')

    except Exception as e:
        print(e)
        return 'Une erreur est survenue'
