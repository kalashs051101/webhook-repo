from flask import Flask, request, jsonify, render_template
from models import save_event, get_latest_events
from utils import parse_event
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    event_type = request.headers.get('X-GitHub-Event')
    data = request.get_json()
    print("Webhook hit. Event Type:", event_type)
    print("Raw Payload:", data)
    
    event = parse_event(data, event_type)
    if event:
        save_event(event)
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "ignored"}), 200

@app.route('/events', methods=['GET'])
def events():
    events = get_latest_events()
    print(events)
    return jsonify([e["message"] for e in events])

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True)

