from flask import Flask, render_template_string, request, send_from_directory
import os
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import io

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def extract_colors(image_path, num_colors=5):
    img = Image.open(image_path)
    img = img.resize((150, 150))  # Resize for faster processing
    img_array = np.array(img)
    img_array = img_array.reshape((img_array.shape[0] * img_array.shape[1], 3))
    
    kmeans = KMeans(n_clusters=num_colors, random_state=0)
    kmeans.fit(img_array)
    colors = kmeans.cluster_centers_.astype(int)
    return ['#%02x%02x%02x' % (r, g, b) for r, g, b in colors]

@app.route('/', methods=['GET', 'POST'])
def index():
    colors = []
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            colors = extract_colors(filepath)
            os.remove(filepath)  # Clean up after processing
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Image Colour Palette Generator</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: #333;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }
            .container {
                background: rgba(255, 255, 255, 0.95);
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
                padding: 40px;
                max-width: 600px;
                width: 100%;
                text-align: center;
                animation: fadeIn 0.5s ease-in;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            h1 {
                color: #4a4a4a;
                margin-bottom: 20px;
                font-size: 2.5em;
            }
            p {
                font-size: 1.2em;
                margin-bottom: 30px;
                color: #666;
            }
            form {
                margin-bottom: 30px;
            }
            input[type="file"] {
                display: block;
                margin: 0 auto 20px;
                padding: 10px;
                border: 2px dashed #ccc;
                border-radius: 10px;
                background: #f9f9f9;
                cursor: pointer;
                transition: border-color 0.3s;
            }
            input[type="file"]:hover {
                border-color: #667eea;
            }
            button {
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                border: none;
                padding: 12px 30px;
                border-radius: 25px;
                font-size: 1.1em;
                cursor: pointer;
                transition: transform 0.2s;
            }
            button:hover {
                transform: scale(1.05);
            }
            .palette {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                margin-top: 30px;
            }
            .color {
                width: 80px;
                height: 80px;
                margin: 10px;
                border-radius: 50%;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s;
                cursor: pointer;
            }
            .color:hover {
                transform: scale(1.1);
            }
            .color-code {
                margin-top: 5px;
                font-size: 0.9em;
                color: #666;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Colour Palette Generator</h1>
            <p>Upload an image to extract its dominant colors and create a beautiful palette!<br> -Brylle</p>
            <form method="post" enctype="multipart/form-data">
                <input type="file" name="image" accept="image/*" required>
                <button type="submit">Generate Palette</button>
            </form>
            {% if colors %}
            <div class="palette">
                {% for color in colors %}
                <div class="color" style="background-color: {{ color }};" onclick="copyToClipboard('{{ color }}')">
                    <div class="color-code">{{ color }}</div>
                </div>
                {% endfor %}
            </div>
            <p style="margin-top: 20px; font-size: 0.9em; color: #888;">Click a color to copy its hex code!</p>
            {% endif %}
        </div>
        <script>
            function copyToClipboard(text) {
                navigator.clipboard.writeText(text).then(() => {
                    alert('Copied: ' + text);
                });
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html, colors=colors)

if __name__ == '__main__':
    app.run(debug=True)
