from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
	return jsonify({"message": "You need to choose an endpoint. \nEndpoints available:\n- /substAtivas\n- /excipientes"}), 200
	
@app.route('/substAtivas')
def substAtivas():
	return jsonify({"message": "substAtivas endpoint"}), 200

@app.route('/excipientes')
def excipientes():
	return jsonify({"message": "excipientes endpoint"}), 200
