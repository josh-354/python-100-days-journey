from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for tasks (use a database for persistence)
tasks = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            tasks.append({'text': task, 'done': False})
        return redirect(url_for('home'))
    
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>To-Do List</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f4; }
            h1 { text-align: center; color: #333; }
            form { text-align: center; margin-bottom: 20px; }
            input[type="text"] { padding: 10px; width: 300px; }
            button { padding: 10px 20px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
            button:hover { background-color: #45a049; }
            ul { list-style-type: none; padding: 0; }
            li { background: white; margin: 10px 0; padding: 15px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); display: flex; justify-content: space-between; align-items: center; }
            .done { text-decoration: line-through; color: #888; }
            a { color: #f44336; text-decoration: none; }
        </style>
    </head>
    <body>
        <h1>My To-Do List</h1>
        <form method="POST">
            <input type="text" name="task" placeholder="Add a new task" required>
            <button type="submit">Add Task</button>
        </form>
        <ul>
            {% for task in tasks %}
            <li class="{% if task.done %}done{% endif %}">
                {{ task.text }}
                <div>
                    <form method="POST" action="/toggle/{{ loop.index0 }}" style="display:inline;">
                        <button type="submit">{{ 'Undo' if task.done else 'Done' }}</button>
                    </form>
                    <form method="POST" action="/delete/{{ loop.index0 }}" style="display:inline;">
                        <button type="submit" style="background-color: #f44336;">Delete</button>
                    </form>
                </div>
            </li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """, tasks=tasks)

@app.route('/toggle/<int:index>', methods=['POST'])
def toggle(index):
    if 0 <= index < len(tasks):
        tasks[index]['done'] = not tasks[index]['done']
    return redirect(url_for('home'))

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
