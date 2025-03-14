from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Set the website name dynamically
    website_name = "Floofy Counter Website"
    
    # Path to the Html folder in the emulated storage (on Android)
    html_file_path = '/storage/emulated/0/Html/index.html'
    
    # Check if the HTML file exists in the specified location
    if not os.path.exists(html_file_path):
        return f"Error: {html_file_path} not found! The website name is {website_name}."
    
    # Read the HTML file from the specified location
    with open(html_file_path, 'r') as file:
        html_content = file.read()

    # Render the HTML content with the website name
    return render_template_string(html_content, website_name=website_name)

if __name__ == '__main__':
    # Print the URL dynamically
    print("Server is running at: http://127.0.0.1:5000/")  # This will be the local URL
    app.run(debug=True, host='0.0.0.0', port=5000)