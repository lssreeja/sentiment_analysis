from flask import Flask, render_template, request
from main_nltk import perform_sentiment_analysis

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process_text', methods=["POST"])
def process_text():
    # Get the entered text from the form submission
    text = request.form['text']

    # Write the text to read.txt
    with open('read.txt', 'w', encoding='utf-8') as file:
        file.write(text)

    # Execute nltk_main.py using subprocess
    # subprocess.run(['python', 'static/nltk_main.py'])
    perform_sentiment_analysis()

    # Render the result.html template and pass the sentiment result
    return render_template('result.html')
    # Render the result.html template
    # return render_template('result.html')


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
