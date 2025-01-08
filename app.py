# app.py
from flask import Flask, render_template

app = Flask(__name__)

menu_items = {
    "Royal Biryanis": [
        {"name": "Mutton Biryani", "price": 22, "description": "Traditional slow-cooked mutton biryani with aromatic spices", "veg": False, "spiciness": 2},
        {"name": "Chicken Biryani", "price": 19, "description": "Flavorful chicken biryani with saffron-infused rice", "veg": False, "spiciness": 2}
    ],
    "Maharaja's Choice": [
        {"name": "Talawa Gosht", "price": 22, "description": "Tender mutton pieces in a rich spicy gravy", "veg": False, "spiciness": 3},
        {"name": "Bhunawa Gosht", "price": 22, "description": "Slow-roasted mutton in thick gravy", "veg": False, "spiciness": 2}
    ],
    "Tandoori Treasures": [
        {"name": "Chicken 65", "price": 16, "description": "Spicy deep-fried chicken with curry leaves", "veg": False, "spiciness": 3},
        {"name": "Hot & Spicy Chicken", "price": 20, "description": "Fiery chicken curry with special spices", "veg": False, "spiciness": 3}
    ],
    "Garden Fresh": [
        {"name": "Kadai Paneer", "price": 15, "description": "Cottage cheese with bell peppers in spicy gravy", "veg": True, "spiciness": 2},
        {"name": "Shahi Paneer", "price": 16, "description": "Rich and creamy paneer curry", "veg": True, "spiciness": 1}
    ]
}

@app.route('/')
def home():
    return render_template('index.html', menu_items=menu_items)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')