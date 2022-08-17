from flask import Flask, jsonify, make_response, request
import spacy;
nlp = spacy.load('es_core_news_md');

app = Flask(__name__)


@app.route("/")
def hello_from_root():
    return jsonify(message="Hello from root")

@app.route("/similarity", methods=['POST'])
def get_similarity():
    text1 = request.json['text1']
    text2 = request.json['text2']
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    similarity=round(doc1.similarity(doc2), 2)

    return jsonify({'similarity': similarity})

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
