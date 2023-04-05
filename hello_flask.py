from flask import Flask, render_template, request, jsonify
import templates
import utils
app = Flask(__name__)

@app.route('/')
def hello_flask():
    return f'Hello from Flask'


def log_request(reg, res):
    with open('./log.txt', 'a') as f:
        print(reg.__dict__, res, file=f)


@app.route('/get_data', methods=['POST'])
def data_flask():
    data_txt1 = request.form['data_txt']
    title = 'Go text'
    result = utils.count_punkt(data_txt1)
    log_request(request, result)
    return render_template('results.html',
                           result=result,
                           the_title=title)


@app.route('/num_input', methods=['POST'])
def num_input():
    data_txt1 = request.form['data_txt']
    title = 'счастливым числом'
    verify_bool = utils.num_verify(data_txt1)
    if not type(verify_bool) == bool:
        title = verify_bool
        verify = " не является "
    else:
        if verify_bool:
            verify = " является "
        else:
            verify = " не является "
    return render_template('verify.html',
                           the_num=data_txt1,
                           the_verify=verify,
                           the_title=title)


@app.route('/entry')
def entry():
    return render_template('entry.html', the_title='12345')


@app.route('/entry_num')
def entry_num():
    return render_template('entry_num.html', the_title='Проверка на вшивость)')


@app.route('/random')
def random():
    from random import randint
    num = str(randint(-100, 100))
    title = 'Счасливое число'
    return render_template('rand.html', the_title=title,
                           the_num=num)


@app.route('/random_json')
def random_json():
    return jsonify(utils.data_get_json())


@app.route('/random_json_str')
def random_json_str():
    return utils.data_get_json()


app.run(debug=True)
