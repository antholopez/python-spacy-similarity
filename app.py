from flask import Flask, jsonify, make_response
import spacy;
nlp = spacy.load('es_core_news_md');

app = Flask(__name__)


@app.route("/")
def hello_from_root():
    print("Hello from root acaaaaaaaaaaaaaa")
    doc1 = nlp('Cuales son los tipos de inteligencia artificial')
    doc2 = nlp('que tipos de inteligencia artificial existe')
    doc3 = nlp('que es la inteligencia artificial')
    doc4 = nlp('la inteligencia artificial que tipos existen')
    doc5 = nlp('¿Cuales son los tipos de inteligencia artificial?')

    print(doc1.similarity(doc2)) 
    print(doc1.similarity(doc3))
    print(doc1.similarity(doc4))
    print(doc1.similarity(doc5))
    return jsonify(message=doc1.similarity(doc2))


@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
