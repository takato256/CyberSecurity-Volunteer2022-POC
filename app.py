from flask import Flask, request, render_template
import mecab_fun


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('index.html')
    else:
        form_input = request.form['input']  # 検索フォームの値
        flag_message = mecab_fun.analayze(form_input)
        print(flag_message)
        return render_template('sample.html')


if __name__ == '__main__':
    app.run(debug=True)
