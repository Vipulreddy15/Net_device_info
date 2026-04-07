# Network Device Info Collector

A Streamlit-based tool to scan and collect information from multiple network devices using SSH.  
Supports Linux and Cisco IOS devices, with results downloadable in CSV format.

------------------------------------------------------------
Features
------------------------------------------------------------
- Upload a `devices.yaml` file containing device details
- Automatically ping devices to check connectivity
- SSH into reachable devices using Netmiko
- Retrieve:
  - Hostname
  - OS / Version
  - Uptime
- Display results in a table within the app
- Download results as a CSV file
- Works with Linux and Cisco IOS devices

------------------------------------------------------------
Project Structure
------------------------------------------------------------
Net_device_info/
│
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
└── devices.yaml         # Sample device configuration file

------------------------------------------------------------
⚙️ Installation
------------------------------------------------------------
1. Clone the repository:
   git clone https://github.com/Vipulreddy15/Net_device_info.git
   cd Net_device_info

2. Create a virtual environment (optional but recommended):
   python3 -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows

3. Install dependencies:
   pip install -r requirements.txt

------------------------------------------------------------
devices.yaml Format
------------------------------------------------------------
Example:
devices:
  - name: Router1
    ip: 192.168.1.1
    username: admin
    password: admin123
    device_type: cisco_ios
    port: 22
  - name: Server1
    ip: 192.168.1.10
    username: root
    password: pass123
    device_type: linux
    port: 22

------------------------------------------------------------
Usage
------------------------------------------------------------
1. Run the Streamlit app:
   streamlit run app.py

2. Open the link in your browser (usually http://localhost:8501).

3. Upload your devices.yaml file.

4. Click "Run Scan" to:
   - Ping each device
   - Collect system information via SSH
   - View results in a table

5. Download results as device_info.csv.

------------------------------------------------------------
Dependencies
------------------------------------------------------------
- Streamlit – Web interface
- PyYAML – Reading YAML device configs
- Netmiko – SSH connections to network devices
- Pandas – Data processing & CSV export

Install manually:
   pip install streamlit pyyaml netmiko pandas

------------------------------------------------------------
Author
------------------------------------------------------------
Vipul Reddy Gundalu  
GitHub: https://github.com/Vipulreddy15
LinkedIn: https://www.linkedin.com/in/vipul-reddy-gundalu-1533742b1/
