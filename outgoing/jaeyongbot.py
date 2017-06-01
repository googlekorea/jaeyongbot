from flask import Flask, request, Response
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
   if request.form['user_id'] != 'USLACKBOT':
       text = '{{"text":"{}"}}'.format(request.form['text'])
       resp = Response(response=text, status=200, mimetype="application/json")
       return resp
   else:
       return "ok"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)
   