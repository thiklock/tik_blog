import streamlit as st
import requests

def get_ip_info():
    try:
        # Get public IP address
        response = requests.get("https://api64.ipify.org?format=json")
        ip_data = response.json()

        # Get detailed information about the IP address using ipinfo.io
        ip_address = ip_data.get("ip", "")
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        ip_info = response.json()

        return ip_info
    except Exception as e:
        return {"error": str(e)}

def main():
    st.title("IP Address and Localization App")

    # Get IP information
    ip_info = get_ip_info()

    # Display IP information
    st.write(f"Your public IP address is: {ip_info.get('ip', 'N/A')}")
    st.write(f"Location: {ip_info.get('city', 'N/A')}, {ip_info.get('region', 'N/A')}, {ip_info.get('country', 'N/A')}")
    st.write(f"Latitude and Longitude: {ip_info.get('loc', 'N/A')}")

if __name__ == "__main__":
    main()
