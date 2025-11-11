from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# --- Route Definitions ---

@app.route('/')
def home():
    """Renders the Home page."""
    return render_template('index.html', page_title='Home', active_page='home')

@app.route('/about')
def about():
    """Renders the About Us page."""
    return render_template('about.html', page_title='About Us', active_page='about')

@app.route('/membership')
def membership():
    """Renders the Membership page."""
    # Example dynamic data (can be replaced with a database query later)
    plans = [
        {'name': 'Basic Access', 'price': 39, 'features': ['Access to Cardio Floor', 'Standard Hours', 'Free Wi-Fi']},
        {'name': 'Gold Standard', 'price': 59, 'features': ['All Basic Features', 'Unlimited Group Classes', 'Sauna Access']},
        {'name': 'Platinum Elite', 'price': 99, 'features': ['All Gold Features', '2 Free PT Sessions', 'Guest Pass (1/mo)', 'Priority Booking']}
    ]
    return render_template('membership.html', page_title='Membership Plans', active_page='membership', plans=plans)

# --- Run the Application ---

if __name__ == '__main__':
    # Setting debug=True allows the server to auto-reload on code changes
    app.run(debug=True)