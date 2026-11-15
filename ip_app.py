
import json
import urllib.request


def fetch_ip_info():
    """
    Fetches public IP, geolocation, ISP, and ASN data
    from the ipapi.co REST API.

    Returns a parsed JSON dictionary or None on failure.
    """
    url = "https://ipapi.co/json/"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        req = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                return json.loads(response.read().decode("utf-8"))
            else:
                print(f"[ERROR] API returned HTTP Status: {response.status}")
                return None

    except Exception as e:
        print(f"[ERROR] Network communication failed: {e}")
        return None


def display_network_info(data):
    """
    Formats and displays network diagnostics
    in a structured CLI interface.
    """
    if not data:
        print("[-] Unable to retrieve network details.")
        return

    print("=" * 60)
    print("       NETWORK TECHNICIAN DIAGNOSTIC UTILITY")
    print("=" * 60)

    print(f" Public IP Address : {data.get('ip', 'N/A')}")
    print(f" IP Version        : {data.get('version', 'N/A')}")
    print(f" City / Region     : {data.get('city', 'N/A')}, {data.get('region', 'N/A')}")
    print(f" Country           : {data.get('country_name', 'N/A')} ({data.get('country_code', 'N/A')})")
    print(f" Postal Code       : {data.get('postal', 'N/A')}")
    print(f" Coordinates       : Lat {data.get('latitude', 'N/A')}, Long {data.get('longitude', 'N/A')}")
    print(f" ISP Provider      : {data.get('org', 'N/A')}")
    print(f" ASN               : {data.get('asn', 'N/A')}")

    print("=" * 60)


if __name__ == "__main__":
    ip_data = fetch_ip_info()
    display_network_info(ip_data)
