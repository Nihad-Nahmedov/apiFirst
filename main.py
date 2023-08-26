from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

API_KEY = "4b1a0e44-0205-4ad8-9158-3c10c3e87ae9"


@app.route('/api/demo', methods=['GET'])
@cross_origin()
def demo():
    api_key = request.args.get('api_key')

    if api_key != API_KEY:
        return jsonify({'error': 'Invalid API key'}), 401

    message = "Demo"
    return jsonify({"Message ": message})


if __name__ == '__main__':
    app.run(debug=True)
