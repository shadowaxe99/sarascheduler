from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    message = data['message']
    
    # Process the message
    response = process_message(message)
    
    return jsonify(response)

if __name__ == '__main__':
    app.run()
