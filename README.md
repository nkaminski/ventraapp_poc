# Ventra Mobile Application Multiple Data Integrity Vulnerabilities

DISCLAIMER: This code is for testing and educational purposes only. All vulnerabilities contained within this repository have been disclosed to the vendor and I do not support or condone the use of this code for illegal or unethical purposes. Use at your own risk and please don't steal.

Full documentation is located under the `doc` directory, and all PoC code is located under the `code` directory.

Required python3 libraries for PoC code: falcon, requests and gunicorn(or other WSGI server, only needed for app API server).

Running the PoC code: 
    Metadata and security code downloader: 
    
        python3 v_client.py
    
    App API server: 
    
        gunicorn -b :443 -w3 --certfile=<your_cert> --keyfile=<your_privkey> app_server:api

# Timeline
  * 6/24/16 - Ventra v. 1.2.1.39 released and patches 1st vulnerabilty discussed in report.
  * 6/20/16 - Acknowledgement from vendor of vulnerability via phone. Brief discussion of impacts and tech details.
  * 6/20/16 - 2nd attempt to report to vendor, this time via phone.
  * 6/16/16 - Canned response from submission of vendor contact form.
  * 6/13/16 - Initial report to vendor via online feedback form.
