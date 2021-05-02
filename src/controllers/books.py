from flask import Flask
from flask_restplus import Api, Resource

from src.server.instance import server
from src.models.books import book

app, api = server.app, server.api

# request no DB
books_db = [
    {'id': 0, 'title': 'War and Peace'},
    {'id': 1, 'title': 'Clean Code'}
]

@api.route("/books")
class BookList(Resource):
    @api.marshal_list_with(book)
    def get(self, ):
        return books_db

    @api.expect(book, valitade=True)
    def post(self, ):
        response = api.payload
        books_db.append(response)
        return response, 200