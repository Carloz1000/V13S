import os
import zipfile
import base64

# Base64-encoded ZIP file containing the entire project
encoded_zip = """
UEsFBgAAAAAAAAAAAAAAAAAAAAAAAA==
"""

def extract_project():
    # Decode the base64-encoded ZIP file
    zip_data = base64.b64decode(encoded_zip)
    
    # Extract the ZIP file
    with open("project.zip", "wb") as zip_file:
        zip_file.write(zip_data)
    
    with zipfile.ZipFile("project.zip", "r") as zip_ref:
        zip_ref.extractall("NovaSwarm_Full_UI_Prod")
    
    os.remove("project.zip")

def main():
    extract_project()
    # Change directory to the project folder
    os.chdir("NovaSwarm_Full_UI_Prod")
    # Execute the main script
    os.system("python3 run.py")

if __name__ == "__main__":
    main()
