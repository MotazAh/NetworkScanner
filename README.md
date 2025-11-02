# NetworkScanner
Scans for ports and service names of open ports.

### Setup
1. Run ```git clone https://github.com/MotazAh/NetworkScanner.git```
2. Run ```cd NetworkScanner```
3. Edit the hosts.txt to add the hosts you wish to scane
4. Run ```python3 -m venv .venv``` to create virtual environment
5. Run ```source .venv/bin/activate``` for Mac/Linux or ```.venv\bin\activate``` for Windows
6. Run ```pip install -r requirements.txt```
7. Run the network_scanner.py ```python network_scanner.py```

### Dependencies
python-nmap==0.71