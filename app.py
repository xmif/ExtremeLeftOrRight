from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello, World!'

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/extreme')
def index(data={"text":"Sample text"}): 
    return render_template('extreme.html', data=data)

# @app.route('/extreme', methods=['POST'])
# def my_form_post():
#     data = dict()
#     text = request.form['text']
#     processed_text = text.upper()
#     # return processed_text
#     data["text"] = processed_text
#     return render_template('extreme.html', data=data)

@app.route('/extreme', methods=('GET', 'POST'))
def create(data=dict()):
    if request.method == 'POST':
        # title = request.form['title']
        content = request.form['content']

        # if not title:
        #     flash('Title is required!')
        # elif not content:
        #     flash('Content is required!')
        if not content:
            flash('Content is required!')
        else:
            data = {
                # This is bad, get better later:
                # https://flask.palletsprojects.com/en/2.2.x/templating/#controlling-autoescaping
                "text": content.replace("\n", "<br>"),
                "twitter_enabled": True,
                # "text": content,
            }
            # print(content)
            # messages.append({'title': title, 'content': content})
            # messages.append({'content': content})
            # return redirect(url_for('index'))
            return render_template('extreme.html', data=data)

    return render_template('extreme.html')
