# DDoSWatch 🚨🌐

A robust **DDoS Protection System** for cloud-hosted websites, utilizing machine learning and cloud infrastructure like **AWS** to detect and mitigate Distributed Denial of Service (DDoS) attacks.  

## 🚀 Table of Contents  

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [JMeter Configuration](#jmeter-configuration)  
- [Architecture](#architecture)  
- [License](#license)  
- [Acknowledgments](#acknowledgments)  

---

## 📄 Project Overview  

DDoSWatch is a **cloud-based DDoS protection system** designed to detect and mitigate attacks in real time. It uses a machine learning-based anomaly detection algorithm (**Isolation Forest**) and integrates with **AWS services** like Auto Scaling, Load Balancing, and CloudWatch to ensure high availability and performance for cloud-hosted websites.  

The system includes traffic simulation tools like **Apache JMeter** to create real-world attack scenarios, helping to evaluate the system's effectiveness.  

---

## 🔧 Features  

- **Anomaly Detection**: Detects abnormal traffic patterns using the Isolation Forest algorithm.  
- **Real-Time Mitigation**: Leverages AWS Auto Scaling and Load Balancing to minimize the impact of attacks.  
- **Traffic Simulation**: Uses JMeter to generate attack scenarios and validate system performance.  
- **Comprehensive Monitoring**: Tracks system metrics and alerts using AWS CloudWatch.  
- **Customizable Setup**: Allows configuration for different attack and traffic scenarios.  

---

## 🛠️ Installation  

### Prerequisites  

- Python 3.x  
- AWS account with necessary IAM permissions.  
- Apache JMeter installed for traffic simulation.  

### Installation Steps  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/footcricket05/DDoSWatch.git  
   cd DDoSWatch  
   ```  

2. Create and activate a Python virtual environment:  
   ```bash  
   python3 -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```  

---

## 🖥️ Usage  

Run the following scripts for each function:  

### 1. Anomaly Detection  
```bash  
python anomaly_detection.py  
```  

- **Input**: `traffic-data.csv` containing network traffic data.  
- **Output**: Identifies anomalies and generates a plot (`anomalies_plot.png`).  

### 2. Traffic Data Simulation  
```bash  
python generate_traffic_data.py  
```  

- Simulates network traffic data, including benign and attack traffic.  

---

## 🔧 JMeter Configuration  

JMeter was used to simulate traffic, including potential DDoS scenarios, for testing purposes.  

### Configuration Details  

1. **Thread Group**:  
   - Number of threads (users): `2000`.  
   - Ramp-up period: `60 seconds`.  
   - Loop count: Continuous traffic simulation.  

2. **HTTP Request Sampler**:  
   - Targeted a sample endpoint hosted on AWS.  
   - Configured for a mix of legitimate requests and requests designed to simulate attacks.  

3. **Listeners**:  
   - **Summary Report**: To capture response times and error rates.  
   - **Graphs**: For real-time traffic analysis.  

### Files  
If you created any specific JMeter test plan file (e.g., `.jmx`), ensure it’s documented and saved in the repository for reference.

---

## 📂 Key Files in the Project  

| File Name                     | Description                                                                 |  
|-------------------------------|-----------------------------------------------------------------------------|  
| `anomaly_detection.py`        | Detects anomalies in traffic data using Isolation Forest.                  |  
| `traffic-data.csv`            | Simulated network traffic data for anomaly detection.                      |  
| `anomalies_plot.png`          | Visual representation of anomalies detected in the traffic data.           |  
| `generate_traffic_data.py`    | Script to generate traffic data, including benign and attack traffic.      |  
| `DDoS-Alarm-2024_11_15.csv`   | Log file generated during testing, summarizing DDoS attack alarms.         |  

---

## 🏗️ Architecture  

### Key Components  

1. **Traffic Simulation**  
   - JMeter-generated traffic includes benign and attack scenarios.  

2. **Anomaly Detection**  
   - Python script with the Isolation Forest algorithm detects abnormal traffic patterns.  

3. **AWS Integration**  
   - Auto Scaling ensures resource availability during high traffic.  
   - CloudWatch monitors and logs traffic metrics, triggering alarms for anomalies.  

---

## 📄 License  

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.  

---

## 🚨 Acknowledgments  

- Thanks to **AWS** for providing the cloud infrastructure.  
- Special mention to **JMeter** for enabling realistic traffic simulation.  
- Credit to the **Isolation Forest** algorithm for anomaly detection.
