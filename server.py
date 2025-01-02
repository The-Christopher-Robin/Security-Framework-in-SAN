from flask import Flask, render_template
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the log DataFrame (replace with your actual file path)
log_df = pd.read_csv('log_file.csv')  # Assuming logs are saved in a CSV file

@app.route('/')
def index():
    # Convert DataFrame to HTML for display
    log_html = log_df.to_html(classes='table table-bordered', index=False)
    return render_template('index.html', log_html=log_html)

if __name__ == "__main__":
    app.run(debug=True)
