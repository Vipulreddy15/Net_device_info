import streamlit as st
import yaml
import socket
from netmiko import ConnectHandler
import platform
import pandas as pd

st.set_page_config(page_title="Network Device Info Collector", layout="wide")
st.title("Network Device Info Collector")

st.write("Upload a `devices.yaml` file to start scanning devices.")
uploaded_file = st.file_uploader("Upload your devices.yaml", type=["yaml", "yml"])

if uploaded_file:
    try:
        devices_data = yaml.safe_load(uploaded_file)
        devices = devices_data.get("devices", [])
        st.success(f"{len(devices)} device(s) loaded.")

        if st.button("🔍 Run Scan"):
            results = []

            for device in devices:
                name = device.get("name", "")
                ip = device.get("ip", "")
                username = device.get("username", "")
                password = device.get("password", "")
                dtype = device.get("device_type", "")
                port = device.get("port", 22)

                status = "DOWN"
                hostname = ""
                os_version = ""
                uptime = ""

                st.write(f"Checking {name} ({ip})...")

                try:
                    sock = socket.create_connection((ip, port), timeout=2)
                    status = "UP"
                    sock.close()
                except socket.error:
                    st.warning(f"{ip} is not reachable.")
                    results.append({
                        "Name": name,
                        "IP": ip,
                        "Status": status,
                        "Hostname": hostname,
                        "OS/Version": os_version,
                        "Uptime": uptime
                    })
                    continue 

                try:
                    ssh_info = {
                        "device_type": dtype,
                        "host": ip,
                        "username": username,
                        "password": password,
                        "port": port
                    }
                    conn = ConnectHandler(**ssh_info)

                    if dtype == "linux":
                        os_version = conn.send_command("uname -a")
                        hostname = conn.send_command("hostname")
                        uptime = conn.send_command("uptime -p")
                    elif dtype == "cisco_ios":
                        output = conn.send_command("show version")
                        for line in output.splitlines():
                            if "uptime is" in line:
                                hostname, up = line.split(" uptime is ")
                                uptime = up.strip()
                            if "Cisco IOS Software" in line:
                                os_version = line.strip()
                    conn.disconnect()
                except Exception as e:
                    st.error(f"SSH failed for {ip}: {e}")

                results.append({
                    "Name": name,
                    "IP": ip,
                    "Status": status,
                    "Hostname": hostname,
                    "OS/Version": os_version,
                    "Uptime": uptime
                })

            df = pd.DataFrame(results)
            st.subheader("Scan Results")
            st.dataframe(df)

            csv_file = df.to_csv(index=False).encode("utf-8")
            st.download_button("Download CSV", csv_file, "device_info.csv", "text/csv")

    except Exception as e:
        st.error(f"Failed to read YAML: {e}")
