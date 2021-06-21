from flask import Flask, request, jsonify

app = Flask(__name__)
d = {}

@app.route('/')
def home():
  return """Jeremy's app is running!!"""


@app.route('/test', methods=['POST'] )
def every_third():
  string_to_cut = request.values['string_to_cut']
  solution = []
  if len(string_to_cut) < 3:
    return ''
  for i in string_to_cut[2::3]:
    solution.append(i)
  return_string = ''.join(solution)
  return jsonify({'return_string':return_string})

if __name__ == "__main__":
  app.run()


