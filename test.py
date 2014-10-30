from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return render_template('form.html')

@app.route('/form', methods=['POST'])
def fn():
    print request.form['firstname']
    print request.form['lastname']
    return str(request.form)

if __name__ == '__main__':
    app.debug = True
    app.run()

