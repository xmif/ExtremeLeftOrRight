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
        message_body = request.form['message_body']

        # if not title:
        #     flash('Title is required!')
        # elif not content:
        #     flash('Content is required!')
        if not message_body:
            # Flask.flash('Content is required!')
            # return ("Your needs a message", 402)
            message_body = "WHAT A WEASLY<br>LITTLE<br>LIAR<br>DUDE<br>SmashHit"
        data = {
            # This is bad, get better later:
            # https://flask.palletsprojects.com/en/2.2.x/templating/#controlling-autoescaping
            "text": message_body.replace("\n", "<br>"),
            "twitter_enabled": True,
            # "text": message_body,
        }
            # print(content)
            # messages.append({'title': title, 'content': content})
            # messages.append({'content': content})
            # return redirect(url_for('index'))
        return render_template('extreme.html', data=data)

    return render_template('extreme.html')

if __name__ == '__main__':
    app.run()
