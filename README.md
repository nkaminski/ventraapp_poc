# Ventra Mobile Application Multiple Data Integrity Vulnerabilities

DISCLAIMER: This code is for testing and educational purposes only. All vulnerabilities contained within this repository have been disclosed to the vendor and I do not support or condine the use of this code for illegal or unethical purposes. Use at your own risk and please don't steal.

Full documentation is located under the `doc` directory, and all PoC code is located under the `code` directory.

Required python3 libraries for PoC code: falcon, requests and gunicorn(or other WSGI server, only needed for app API server).

Running the PoC code: 
        Metadata downloader: python3 v_client.py
        App API server: gunicorn -b :443 -w3 --certfile=<your_cert> --keyfile=<your_privkey> app_server:api
