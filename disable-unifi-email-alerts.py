import requests
import json

server_list = []
username = ''
password = ''
email = ''

for server in server_list:
    print "Starting " + server

    url = "https://" + server + ":8443"
    s = requests.Session()

    params = {'username': username, 'password': password}
    params = json.dumps(params)
    login_url = url
    login_url += '/api/login'

    # Login
    r = s.post(url=login_url, data=params, verify=False, timeout=5)
    print r.text
    print r.status_code

    # Disable alerts
    update_admin_settings_url = url
    update_admin_settings_url += "/api/self"
    params = json.dumps({"name": username,"email": email,"email_alert_enabled": False,"email_alert_grouping_enabled": True,"html_email_enabled": True,"is_professional_installer": False,"x_oldpassword": password})
    r = s.put(timeout=5, verify=False, url=update_admin_settings_url, data=params)
    print r.text
    print r.status_code
