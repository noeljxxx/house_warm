from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/call_contact1')
def call_contact1():
    phone_number = '9645951639'  # Phone number for Contact 1
    return f'<script>window.location.href = "tel:{phone_number}";</script>'

@app.route('/call_contact2')
def call_contact2():
    phone_number = '9447354934'  # Phone number for Contact 2
    return f'<script>window.location.href = "tel:{phone_number}";</script>'

if __name__ == '__main__':
    app.run(debug=True)
