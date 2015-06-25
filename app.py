from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello():
  backend_id = os.environ['BACKEND']
	return 'Successfull reach flask server : %s' % (backend_id)

if __name__ == "__main__":
	app.run(host='0.0.0.0')
