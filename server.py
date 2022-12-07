from flask import Flask, render_template, request, redirect

import csv
app = Flask(__name__)


@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/<path>')
def page(path):
    return render_template(path)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        database.write(
            f"\n{data['email']},{data['subject']},{data['message']}")


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        csv_writer = csv.writer(database, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writeheader()
        csv_writer.writerow(data['email'], data['subject'], data['message'])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
        except:
            return 'something went wrong'
    return redirect('/thankyou.html')
# export FLASK_APP=server.py
# export FLASK_ENV=development
# FLASK_DEBUG=true
# source venv/bin/activate
# flask run -p 5001


if __name__ == '__main__':
    app.run(port=5001)
