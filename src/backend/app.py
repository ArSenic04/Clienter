from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import initialize_chatbot, generate_chatbot_response
import logging

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize chatbot components
logger.info("Initializing chatbot components...")
retriever, generator = initialize_chatbot()
logger.info("Chatbot components initialized successfully")

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        logger.info("Backend: Received chat request")
        message = request.json.get('message')
        logger.info(f"Backend: Processing message: {message}")
        
        if not message:
            logger.warning("Backend: No message provided in request")
            return jsonify({'error': 'No message provided'}), 400

        logger.info("Backend: Generating response...")
        response = generate_chatbot_response(retriever, generator, message)
        logger.info(f"Backend: Generated response: {response}")
        
        return jsonify({'response': response})
    except Exception as e:
        logger.error(f"Backend: Error processing request: {str(e)}", exc_info=True)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
