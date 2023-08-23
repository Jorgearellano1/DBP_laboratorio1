from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista inicial de animes
animes = [
    {"id": 1, "name": "One punch man "},
    {"id": 2, "name": "One Piece"},
    {"id": 3, "name": "JoJo's Bizarre Adventure"},
    {"id": 4, "name": "Attack on Titan"},
    {"id": 5, "name": "Gintama"},
    {"id": 6, "name": "Dragon Ball"},
    {"id": 7, "name": "Death Note"},
    {"id": 8, "name": "Fullmetal Alchemist"},
    {"id": 9, "name": "Sword Art Online"},
    {"id": 10, "name": "Tokyo Ghoul"}
]

# GET:
@app.route('/animes', methods=['GET'])
def get_animes():
    return jsonify(animes)

# GET:
@app.route('/animes/<int:id>', methods=['GET'])
def get_anime(id):
    anime = next((anime for anime in animes if anime["id"] == id), None)
    if anime:
        return jsonify(anime)
    return jsonify({"message": "Anime not found"}), 404

# POST:
@app.route('/animes', methods=['POST'])
def create_anime():
    new_anime = request.json
    animes.append(new_anime)
    return jsonify(new_anime), 201

# PUT:
@app.route('/animes/<int:id>', methods=['PUT'])
def update_anime(id):
    anime = next((anime for anime in animes if anime["id"] == id), None)
    if anime:
        anime["name"] = request.json["name"]
        return jsonify(anime)
    return jsonify({"message": "Anime not found"}), 404

# PATCH:
@app.route('/animes/<int:id>', methods=['PATCH'])
def partial_update_anime(id):
    anime = next((anime for anime in animes if anime["id"] == id), None)
    if anime and "name" in request.json:
        anime["name"] = request.json["name"]
        return jsonify(anime)
    return jsonify({"message": "Anime not found or missing data"}), 404

# DELETE:
@app.route('/animes/<int:id>', methods=['DELETE'])
def delete_anime(id):
    global animes
    animes = [anime for anime in animes if anime["id"] != id]
    return jsonify({"message": "Anime deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
