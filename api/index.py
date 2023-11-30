from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return {"message": "You need to choose an endpoint. \nEndpoints available:\n- /substAtivas\n- /excipientes"}
	
@app.route('/substAtivas')
def substAtivas():
	return {"message": "substAtivas endpoint"}

@app.route('/excipientes')
def excipientes():
	return {"message": "excipientes endpoint"}
