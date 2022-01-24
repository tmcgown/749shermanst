from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Thomas Mcgown',
        'title': 'Best Rental Ever',
        'content': '749 Sherman is the best rental house i have been to',
        'date_posted': 'June 6, 2021'
    }        
]

# Make sure to save all before making any changes or they won't work
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/gallery")
def gallery():
    return render_template('gallery.html', title='Gallery')


@app.route("/reviews")
def reviews():
    return render_template('reviews.html', posts=posts)


@app.route("/contacts")
def contacts():
    return render_template('contacts.html')


@app.route("/rentaloptions")
def rentaloptions():
    return render_template('rentaloptions.html', title='Rent')

if __name__ == '__main__':
    app.run(debug=True)