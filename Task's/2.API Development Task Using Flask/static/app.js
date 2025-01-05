document.getElementById("review-form").addEventListener("submit", function (e) {
    e.preventDefault();

    const movieName = document.getElementById("movie-name").value;
    const reviewText = document.getElementById("review-text").value;
    const rating = document.getElementById("rating").value;


    fetch("/reviews", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            movie_name: movieName,
            review: reviewText,
            rating: rating
        })
    })
        .then(response => response.json())
        .then(data => {
            alert("Review added!");
            loadReviews();
            document.getElementById("review-form").reset();
        });
});

function loadReviews() {

    fetch("/reviews")
        .then(response => response.json())
        .then(reviews => {
            const reviewsList = document.getElementById("reviews-list");
            reviewsList.innerHTML = "";

            reviews.forEach((review, index) => {
                const reviewItem = document.createElement("div");
                reviewItem.classList.add("review-item");
                reviewItem.innerHTML = `
                    <strong>${review.movie_name}</strong>
                    <p>${review.review}</p>
                    <p>Rating: ${review.rating} / 5</p>
                    <button onclick="deleteReview(${review.id})">Delete</button>
                `;
                reviewsList.appendChild(reviewItem);
            });
        });
}

function deleteReview(reviewId) {
    fetch(`/reviews/${reviewId}`, { method: "DELETE" })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            loadReviews();
        });
}

window.onload = loadReviews;
