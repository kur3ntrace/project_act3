# project_act3 - IPv4 Address Application

## Project Description

The IPv4 Address Application is a Python-based command-line utility designed to help network technicians retrieve and view public IPv4 address information and related network details.

The application integrates the ipapi.co REST API to retrieve network information and display it in an organized terminal interface.

## Project Objectives

- Retrieve the public IPv4 address of the current internet connection.
- Identify the IP version returned by the API.
- Display geographical information associated with the public IP address.
- Identify the Internet Service Provider (ISP).
- Retrieve the Autonomous System Number (ASN).
- Provide a simple and organized command-line diagnostic interface.

## Features

1. Public IPv4 Address Retrieval
2. IP Version Identification
3. City and Region Information
4. Country and Postal Code Information
5. Latitude and Longitude Display
6. ISP Provider Identification
7. ASN Information
8. Error Handling for Network Communication

## Technologies Used

- Programming Language: Python
- API: ipapi.co REST API
- Data Format: JSON
- HTTP Communication: urllib.request
- Development Environment: Visual Studio Code
- Version Control: Git and GitHub

## Requirements

- Python 3 installed.
- An active internet connection.
- Access to the ipapi.co API.

## Installation and Execution

1. Clone or download this repository.
2. Open the project folder in Visual Studio Code.
3. Open the integrated terminal.
4. Run the following command:

```bash
python ip_app.py
```

5. Wait for the application to retrieve the network information.
6. View the diagnostic results displayed in the terminal.

## API Integration

The application uses the following API endpoint:

`https://ipapi.co/json/`

The API returns network information in JSON format. Python processes the response and displays the available information in the terminal.

## Error Handling

The application includes error handling for network communication failures and displays an error message when network information cannot be retrieved.

Missing dictionary keys are displayed as `N/A`.

## Project Limitations

- Requires an active internet connection.
- Depends on the availability of the ipapi.co API.
- Geolocation information may not represent the exact physical location.
- Currently retrieves and displays the public IP information returned by the API.
- Does not currently include ping or latency testing.
- Does not currently export diagnostic results into files.
- Does not include a separate IPv6 detection or querying feature.

## Future Enhancements

- Ping and latency testing.
- CSV and JSON export functionality.
- Graphical User Interface (GUI).
- Improved API timeout handling.
- Additional network diagnostic features.

## Quality Assurance

The application undergoes functional testing and error-handling testing to verify its expected behavior.

Testing includes:

- Successful API retrieval.
- Public IP address and IP version display.
- Network information display.
- Missing information handling.
- Network communication errors.
- API response errors.

Detailed testing results are documented in the project's QA Test Cases spreadsheet.

## Project Repository

GitHub Repository: `project_act3`

## License

This project was developed for academic purposes.
