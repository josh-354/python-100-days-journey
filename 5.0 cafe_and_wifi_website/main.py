from flask import Flask, render_template_string

app = Flask(__name__)

# Sample data for cafes (you can expand this with real data or a database)
cafes = [
    {"name": "Coffee Corner", "location": "Downtown", "wifi": "Fast", "power": "Multiple outlets", "rating": 4.5},
    {"name": "Tech Brew", "location": "Midtown", "wifi": "High-speed", "power": "Plenty of plugs", "rating": 4.7},
    {"name": "Remote Hub", "location": "Uptown", "wifi": "Reliable", "power": "USB ports available", "rating": 4.3},
    {"name": "Cafe Connect", "location": "Suburb", "wifi": "Stable", "power": "Good coverage", "rating": 4.0},
    {"name": "Work & Sip", "location": "City Center", "wifi": "Excellent", "power": "Dedicated workstations", "rating": 4.8}
]

@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cafes for Remote Work</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f4; }
            h1 { color: #333; text-align: center; }
            .cafe { background: white; margin: 10px 0; padding: 15px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
            .cafe h2 { margin: 0; color: #555; }
            .cafe p { margin: 5px 0; }
            .rating { color: #f39c12; }
        </style>
    </head>
    <body>
        <h1>Cafes with WiFi and Power for Remote Working</h1>
        {% for cafe in cafes %}
        <div class="cafe">
            <h2>{{ cafe.name }}</h2>
            <p><strong>Location:</strong> {{ cafe.location }}</p>
            <p><strong>WiFi:</strong> {{ cafe.wifi }}</p>
            <p><strong>Power:</strong> {{ cafe.power }}</p>
            <p class="rating"><strong>Rating:</strong> {{ cafe.rating }}/5</p>
        </div>
        {% endfor %}
    </body>
    </html>
    """, cafes=cafes)

if __name__ == '__main__':
    app.run(debug=True)
