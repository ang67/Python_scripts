import requests
from requests.auth import HTTPBasicAuth

# Define your Harbor instance details
harbor_url = "https://your-harbor-instance.com"
username = "your-username"
password = "your-password"
file_path = "images.ixi"

# Function to trigger a scan
def trigger_scan(scan_url, username, password):
    response = requests.post(scan_url, auth=HTTPBasicAuth(username, password), verify=False)
    if response.status_code == 202:
        print(f"Scan triggered successfully for {scan_url}")
    else:
        print(f"Failed to trigger scan for {scan_url}. Status code: {response.status_code}, Response: {response.text}")

# Function to read image details from the .ixi file and trigger scans
def trigger_scans_from_file(file_path, harbor_url, username, password):
    with open(file_path, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace and newline characters
            image_info = line.strip()
            if not image_info:
                continue
            
            # Split the image info into components
            parts = image_info.split('/')
            if len(parts) < 3:
                print(f"Invalid image format: {image_info}")
                continue

            host = parts[0]
            project_name = parts[1]
            repo_and_tag = parts[2].split(':')
            if len(repo_and_tag) != 2:
                print(f"Invalid repository and tag format: {parts[2]}")
                continue

            repository_name = repo_and_tag[0]
            tag = repo_and_tag[1]

            # Construct the URL for triggering a scan
            scan_url = f"{harbor_url}/api/v2.0/projects/{project_name}/repositories/{repository_name}/artifacts/{tag}/scan"
            
            # Trigger the scan
            trigger_scan(scan_url, username, password)

# Trigger scans for all images listed in the file
trigger_scans_from_file(file_path, harbor_url, username, password)
