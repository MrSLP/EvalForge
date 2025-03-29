from flask import Flask, request, jsonify
import logging
import time

app = Flask(__name__)
logger = logging.getLogger(__name__)

@app.route('/run_model', methods=['POST'])
def run_model():
    data = request.get_json()
    # Simulate model processing (replace with actual Ollama calls)
    model = data.get("model", "mistral")
    prompt = data.get("prompt", "")
    time.sleep(2)  # simulate processing delay
    response = f"[{model} summary] {prompt[:100]}..."
    return jsonify({"response": response})

@app.route('/parse_pdf', methods=['POST'])
def parse_pdf_route():
    data = request.get_json()
    # Simulate PDF parsing
    pdf_text = f"Simulated parsed text for: {data.get('pdf_path', 'unknown')}"
    return jsonify({"text": pdf_text})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "timestamp": time.time()})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
