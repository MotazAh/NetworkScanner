# NetworkScanner
Scans for ports and service names of open ports.

### Setup
1. Run ```git clone https://github.com/MotazAh/NetworkScanner.git```
2. Run ```cd NetworkScanner```
3. Edit the hosts.txt to add the hosts you wish to scan
4. Run ```python3 -m venv .venv``` to create virtual environment
5. Run ```source .venv/bin/activate``` for Mac/Linux or ```.venv\bin\activate``` for Windows
6. Run ```pip install -r requirements.txt```
7. Run the network_scanner.py ```python network_scanner.py```

### Dependencies
python-nmap==0.71

### Usage Example
<img width="832" height="439" alt="Screenshot 2025-11-02 182957" src="https://github.com/user-attachments/assets/4160cb7a-422e-4fd1-ba44-6a2c7f87db69" />

### Known Limitations
The script is currently lacking the ability to pick desired ports. The script can also be improved by reporting more details that are reported by the nmap module.
Giving the user the ability to pick more flags for the nmap scan would further enhance the script's function.
