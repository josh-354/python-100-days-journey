from flask import Flask, render_template_string, request, jsonify
import threading
import time

app = Flask(__name__)

# Global variables for the app state
text = ""
timer_active = False
timer_thread = None
grace_period = 5  # Seconds before deletion starts
deletion_speed = 0.5  # Seconds per character deletion

def delete_text():
    global text, timer_active
    while timer_active and text:
        time.sleep(deletion_speed)
        if text:
            text = text[:-1]  # Remove last character
    timer_active = False

@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Disappearing Writing App</title>
        <script>
            let timeout;
            function startTimer() {
                clearTimeout(timeout);
                timeout = setTimeout(() => {
                    alert('Deletion starting! Keep typing!');
                    fetch('/delete', { method: 'POST' });
                }, 5000);  // 5 seconds
            }
            function updateText() {
                const textarea = document.getElementById('text');
                fetch('/update', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ text: textarea.value })
                });
                startTimer();
            }
            function loadText() {
                fetch('/get_text')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('text').value = data.text;
                    });
            }
            window.onload = () => {
                loadText();
                startTimer();
            };
        </script>
    </head>
    <body>
        <h1>Disappearing Writing App</h1>
        <p>Type continuously! If you stop for 5 seconds, your text will start disappearing.</p>
        <textarea id="text" rows="20" cols="80" oninput="updateText()"></textarea>
        <br><br>
        <button onclick="location.reload()">Reset (Refresh Page)</button>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/update', methods=['POST'])
def update_text():
    global text, timer_active, timer_thread
    data = request.get_json()
    text = data['text']
    timer_active = False
    if timer_thread and timer_thread.is_alive():
        timer_thread.join()
    return jsonify({'status': 'updated'})

@app.route('/delete', methods=['POST'])
def start_deletion():
    global timer_active, timer_thread
    timer_active = True
    timer_thread = threading.Thread(target=delete_text)
    timer_thread.start()
    return jsonify({'status': 'deleting'})

@app.route('/get_text')
def get_text():
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)
