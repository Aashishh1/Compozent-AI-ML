from flask import Flask, jsonify, request

app = Flask(__name__)

movie_reviews = [
    {"id": 1, "movie_name": "Inception", "review": "Amazing movie with a complex plot!", "rating": 5},
    {"id": 2, "movie_name": "Titanic", "review": "A heart-wrenching love story.", "rating": 4}
]

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/reviews', methods=['GET'])
def get_reviews():
    return jsonify(movie_reviews)

@app.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    new_review = {
        "id": len(movie_reviews) + 1,
        "movie_name": data["movie_name"],
        "review": data["review"],
        "rating": data["rating"]
    }
    movie_reviews.append(new_review)
    return jsonify(new_review), 201

@app.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    review = next((rev for rev in movie_reviews if rev['id'] == review_id), None)
    if review:
        data = request.get_json()
        review["movie_name"] = data.get("movie_name", review["movie_name"])
        review["review"] = data.get("review", review["review"])
        review["rating"] = data.get("rating", review["rating"])
        return jsonify(review)
    return jsonify({"message": "Review not found"}), 404


@app.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    global movie_reviews
    movie_reviews = [rev for rev in movie_reviews if rev["id"] != review_id]
    return jsonify({"message": "Review deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
