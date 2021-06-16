# Terminal Run

# cd /Users/manuglez/MacDocuments/Python/Web\:Mobile\ Dev/web\ server
# export FLASK_ENV=development
# export FLASK_APP=server.py
# flask run

from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route("/<username>/<int:post_id>")
def hello_world(username=None, post_id=None):
    url = url_for('static', filename='favicon.ico')
    print(url)
    return render_template('./index.html', name=username, post_id=post_id)


@app.route("/")
def my_home():
    return render_template('./index.html')


""" @app.route("/blog")
def blog():
    return "<h1>This are my thoughts on the blog</h1>"


@app.route("/blog/2020/dogs")
def blog2():
    return "<h1>This is dog</h1>"


@app.route("/about.html")
def about():
    return render_template('about.html')


@app.route("/components.html")
def components():
    return render_template('components.html')


@app.route("/project.html")
def project():
    return render_template('project.html')


@app.route("/favicon.ico")
def favicon():
    return render_template('favicon.ico') """


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', newline='', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database_csv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database_csv, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_csv(data)
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    # return render_template('login.html', error=error)
        return redirect('/thankyou.html')
    else:
        return "Something went wrong!"
