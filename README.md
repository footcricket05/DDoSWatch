# DDoSWatch 🚨🌐

A powerful **DDoS Protection System** for cloud-hosted websites, designed to detect and mitigate Distributed Denial of Service (DDoS) attacks using machine learning and cloud infrastructure like **AWS**. 

## 🚀 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📄 Project Overview

DDoSWatch is a **cloud-based DDoS protection system** that leverages machine learning algorithms like **Isolation Forest** and **AWS services** (Auto Scaling, Load Balancing, and CloudWatch) to detect and mitigate attacks in real-time. The system ensures high availability and smooth user experience for cloud-hosted websites.

---

## 🔧 Features

- **DDoS Attack Detection** using machine learning-based anomaly detection.
- **Real-time Mitigation** using **AWS Auto Scaling** and **Load Balancing**.
- **Traffic Simulation** with **JMeter** to simulate real-world attack scenarios.
- **AWS Integration**: Seamless integration with AWS services for scalable DDoS defense.
- **Customizable**: Ability to configure and test different attack scenarios.

---

## 🛠️ Installation

Follow these steps to get the project up and running locally:

### 🐍 Install Dependencies

First, clone the repository:

```bash
git clone https://github.com/footcricket05/DDoSWatch.git
cd DDoSWatch
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

---

## 🖥️ Usage

Once installed, you can start the system by running the main application:

```bash
python main.py
```

### 💻 Simulate DDoS Attack

Use JMeter to simulate DDoS traffic. Run the following command:

```bash
jmeter -n -t attack_plan.jmx
```

You can customize the attack scenario based on your needs by editing the `attack_plan.jmx` file.

---

## 🏗️ Architecture

![Architecture](https://github.com/user-attachments/assets/4e0e7623-b452-4fe3-be2c-9d95e476811a)


### Key Components:

- **Traffic Simulation**: Simulates real-world traffic and DDoS attack scenarios using **JMeter**.
- **Anomaly Detection**: Uses **Isolation Forest** to identify abnormal traffic patterns.
- **DDoS Mitigation**: Implements **AWS Auto-Scaling** and **Load Balancing** for real-time attack mitigation.
- **Monitoring**: Uses **AWS CloudWatch** to monitor traffic and performance metrics.

---

## 🤝 Contributing

We welcome contributions! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Write tests to ensure everything works as expected.
5. Commit your changes (`git commit -m 'Add new feature'`).
6. Push your changes to your fork (`git push origin feature-name`).
7. Open a pull request.

Make sure your contributions follow the project's style and include necessary tests.

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---


## 🚨 Acknowledgments

- Thanks to **AWS** for providing the cloud infrastructure.
- Special thanks to **Isolation Forest** for helping with anomaly detection.
- Thanks to the **JMeter** community for creating an excellent traffic simulation tool.
