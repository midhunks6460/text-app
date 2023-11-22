from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    user_text = request.form['user_text']
    return render_template('result.html', user_text=user_text)

if __name__ == '__main__':
    app.run(debug=True)
