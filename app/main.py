from flask import Flask, render_template, request, redirect, url_for

from index import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lender = request.form['lender']
        amount = request.form['amount']
        borrower = request.form['borrower']

        write_block(lender, amount, borrower)
        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/checking', methods=['GET'])
def check():
    results = check_hash_block()
    return render_template('index.html', results=results)
    

if __name__ == '__main__':
    app.run(debug=True)