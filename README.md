# DeepInspect: AI-Based Network Security System

## Overview

This project is a web-based dashboard designed to visualize network traffic data and detect anomalies using Machine Learning. It processes network data from a CSV file and identifies suspicious patterns using an Isolation Forest model.

## Features

- Load network traffic data from a CSV file (exported from Wireshark or manually created).
- Train an ML model to detect anomalies in network traffic.
- Visualize network traffic and anomalies using interactive graphs.
- User-friendly web interface built with Flask and Plotly.
- Automated Threat Response System that blocks suspicious IPs and sends alerts.
- Continuous Learning Mechanism to update models with new threats.

## Technologies & Frameworks Used

### Programming Languages

- Python – Backend, ML model development, and data processing.
- HTML, CSS, JavaScript – Web dashboard design.
- JavaScript (Plotly.js) – Interactive data visualization.

### Machine Learning & Data Processing

- TensorFlow/PyTorch – Building and training ML models for anomaly detection.
- Scikit-learn – Feature extraction and anomaly detection using Isolation Forest.
- Pandas/Numpy – Data manipulation and processing.

### Network Security Tools

- Wireshark – Capturing and analyzing network traffic.
- Snort – Real-time network monitoring and intrusion detection.

### Web Framework & Database

- Flask – Lightweight backend for serving the web dashboard.
- SQLite/MySQL – Storing network traffic logs and anomalies.

### Visualization & Deployment

- Plotly/D3.js – Interactive visualizations.
- Docker – Containerization for deployment.
- AWS/Azure/GCP – Cloud hosting options.

## Project Structure

```
AI_based_Network_Security_System/
├── data/
│   ├── network_traffic.csv                 # Raw network traffic data
│   ├── network_traffic_with_anomalies.csv  # Data with anomaly predictions
├── static/
│   ├── style.css                           # Dashboard styling
├── templates/
│   ├── index.html                          # Frontend dashboard
├── app.py                                  # Flask backend server
├── train_model.py                          # ML model training script
├── requirements.txt                        # Project dependencies
└── README.md                               # Project documentation
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AI_based_Network_Security_System.git
cd AI_based_Network_Security_System
```

### 2. Install Dependencies

Ensure you have **Python 3.x** installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Prepare the Data

- Place your network traffic data (exported from Wireshark) in `data/network_traffic.csv`.
- Ensure the file has the following columns: `Time, Source, Destination, Protocol, Length`.

### 4. Train the Machine Learning Model

```bash
python train_model.py
```

- This script trains an **Isolation Forest model** and generates `network_traffic_with_anomalies.csv`.

### 5. Run the Web Dashboard

```bash
python app.py
```

- Open `http://127.0.0.1:5000` in your browser to view the dashboard.

## System Components

### **1. Anomaly Detection System**

- Uses **machine learning** to detect suspicious network activity.
- Identifies anomalies based on features like **packet size and protocol type**.
- **Real-time monitoring** with integration to Snort and Wireshark.

### **2. Automated Threat Response**

- **Blocks suspicious IPs** and **shuts down network ports** upon detecting anomalies.
- **Sends alerts** to administrators via email or dashboard notifications.
- **Categorizes threats** based on severity.

### **3. Continuous Learning Mechanism**

- **Retrains models dynamically** with new network traffic data.
- Implements a **feedback loop** for administrators to validate threats.
- **Improves detection accuracy** by learning from past attack patterns.

### **4. Web-Based Dashboard**

- **Interactive traffic visualization** using Plotly.
- **Real-time updates** on anomalies and alerts.
- **User controls** for configuring security settings.

### **5. Data Storage & Management**

- Securely **stores network traffic logs and anomaly data**.
- Supports **SQL (MySQL/PostgreSQL) or NoSQL (MongoDB)**.
- Implements **backup and recovery mechanisms**.

## Future Enhancements

- **Real-time packet capture** for live monitoring.
- **Deep learning models** for more accurate anomaly detection.
- **Advanced threat categorization** based on attack signatures.
- **Multi-user authentication** with role-based access control.

## License

This project is licensed under the **MIT License**.

---

Let me know if you need any modifications or additional sections! 🚀

"# AI-Based-Network-Security-System" 
