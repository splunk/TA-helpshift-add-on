
from asyncio import create_subprocess_shell
import base64
import os
import sys
import time
import datetime
import json
import requests
import configparser

def main():
    import sys
    

    for pos, arg in enumerate(sys.argv):
        print('Argument %d: %s' % (pos, arg))
    

def prepare_http_request(url, method, headers, data):
    """Prepare HTTP request.
    
    Args:
        url (str): The URL to send request to.
        method (str): The HTTP method to use.
        headers (dict): The HTTP headers to send.
        data (dict): The HTTP body to send.
    
    Returns:
        dict: The prepared request.
    """
    request = {
        'url': url,
        'method': method,
        'headers': headers,
        'data': data
    }
    return request

def send_http_request(request):
    """Send HTTP request.
    
    Args:
        request (dict): The request to send.
    
    Returns:
        dict: The response from HTTP request.
    """
    
    url = request['url']
    method = request['method']
    headers = request['headers']
    data = request['data']
    response = requests.request(method, url, headers=headers, data=data)
    return response

def get_issues(api_key, api_domain, start_date, end_date):
    """Get issues from HelpShift.
    
    Args:
        api_key (str): The API key to use.
        api_domain (str): The API domain to use.
        start_date (str): The start date to get issues from.
        end_date (str): The end date to get issues to.
    
    Returns:
        json: The issues from HelpShift.
    """

    # Base64 encode API key
    api_key = base64.b64encode(api_key.encode('utf-8')).decode('utf-8')

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + api_key
    }

    url = 'https://api.helpshift.com/v1/{}/issues'.format(api_domain)

    request = prepare_http_request(url, 'GET', headers, None)
    print("request: {}".format(request))
    response = send_http_request(request)
    print("response: {}".format(response))

    # Print response body
    print(response.text)

    return response.json()

if __name__ == '__main__':
    main()

    # Get secrets from config file
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), 'secrets.txt'))
    api_key = config['DEFAULT']['api_token']
    api_domain = config['DEFAULT']['api_domain']

    # Print out the secrets
    print('api_key: ' + api_key)
    print('api_domain: ' + api_domain)

    issues = get_issues(api_key, api_domain, '2019-01-01', '2019-01-31')


    # Loop through issues
    for issue in issues["issues"]:
        print(issue)
        print()