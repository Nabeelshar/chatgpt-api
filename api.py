from flask import Flask, request, jsonify
from revChatGPT.ChatGPT import Chatbot

app = Flask(__name__)

chatbot = Chatbot({
  "session_token": "token"
}, conversation_id=none,  parent_id = none)

@app.route('/ask')
def ask():
    prompt = request.args.get('prompt')
    conversation_id = none
    parent_id = none
    
    response = chatbot.ask(prompt, conversation_id=conversation_id, parent_id=parent_id)
    
    return jsonify({
        "message": response['message'],
        "conversation_id": response['conversation_id'],
        "parent_id": response['parent_id']
    })

if __name__ == '__main__':
    app.run()
