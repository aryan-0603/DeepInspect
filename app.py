from flask import Flask, render_template
import pandas as pd

app = Flask(__name__, template_folder='templates')

@app.route('/')
def dashboard():
    df = pd.read_csv('data/network_traffic_with_anomalies.csv')
    traffic_data = df.to_dict(orient='records')  # Convert DataFrame to list of dictionaries
    return render_template('index.html', traffic_data=traffic_data)

if __name__ == '__main__':
    app.run(debug=True)
