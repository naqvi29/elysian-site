from flask import Flask, render_template, request, url_for, redirect, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/how-to-avail-bank-discounts")
def how_to_avail_bank_discounts():
    return render_template("how-to-avail-bank-discounts.html")

@app.route("/all-books")
def all_books():
    return render_template("books_all.html")

@app.route("/book-details")
def book_details():
    return render_template("book_details.html")

if __name__ == "__main__":
    app.run(debug=True)