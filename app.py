from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def intro():
    return 'this is the beginning'


@app.route('/test')
def every_third(word_to_cut):
    solution = []
    if len(word) < 3:
        return ''
    for i in word[2::3]:
        solution.append(i)
    return ''.join(solution)


