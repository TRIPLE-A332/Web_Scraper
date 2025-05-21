from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form.get('url')
        keyword = request.form.get('keyword')
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text().lower()
            keyword_lower = keyword.lower()
            count = text.count(keyword_lower)

            if count > 0:
                result = f"The word '{keyword}' was found {count} time(s) on the page."
            else:
                result = f"The word '{keyword}' was NOT found on the page."
        except Exception as e:
            result = f"An error occurred: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)