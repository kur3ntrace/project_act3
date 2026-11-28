
import json
from unittest.mock import MagicMock, patch

from ip_app import fetch_ip_info, display_network_info


# Sample API response for testing
SAMPLE_IP_DATA = {
    "ip": "120.29.76.97",
    "version": "IPv4",
    "city": "Angeles City",
    "region": "Central Luzon",
    "country_name": "Philippines",
    "country_code": "PH",
    "postal": "2009",
    "latitude": 15.15,
    "longitude": 120.58333,
    "org": "ComClark Network & Technology Corp",
    "asn": "AS17639"
}


def test_fetch_ip_info_success():
    """Test whether valid API data is retrieved successfully."""

    mock_response = MagicMock()
    mock_response.__enter__.return_value.status = 200
    mock_response.__enter__.return_value.read.return_value = (
        json.dumps(SAMPLE_IP_DATA).encode("utf-8")
    )

    with patch(
        "ip_app.urllib.request.urlopen",
        return_value=mock_response
    ):
        result = fetch_ip_info()

    assert result is not None
    assert result["ip"] == "120.29.76.97"
    assert result["version"] == "IPv4"


def test_fetch_ip_info_network_error(capsys):
    """Test whether network errors are handled properly."""

    with patch(
        "ip_app.urllib.request.urlopen",
        side_effect=Exception("Network unavailable")
    ):
        result = fetch_ip_info()

    captured = capsys.readouterr()

    assert result is None
    assert "Network communication failed" in captured.out


def test_display_network_info_success(capsys):
    """Test whether retrieved network information is displayed."""

    display_network_info(SAMPLE_IP_DATA)

    captured = capsys.readouterr()

    assert "120.29.76.97" in captured.out
    assert "IPv4" in captured.out
    assert "Angeles City" in captured.out
    assert "Philippines" in captured.out
    assert "AS17639" in captured.out


def test_display_network_info_missing_fields(capsys):
    """Test whether missing information displays N/A."""

    incomplete_data = {"ip": "192.168.1.1"}

    display_network_info(incomplete_data)

    captured = capsys.readouterr()

    assert "192.168.1.1" in captured.out
    assert "N/A" in captured.out


def test_display_network_info_empty_data(capsys):
    """Test whether the application handles empty data."""

    display_network_info(None)

    captured = capsys.readouterr()

    assert "Unable to retrieve network details" in captured.out
