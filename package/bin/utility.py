
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


def get_issues(api_key, api_domain, start_date, end_date, helper=None):
    """Get issues from HelpShift.
    
    Args:
        api_key (str): The API key to use.
        api_domain (str): The API domain to use.
        start_date (str): The start date to get issues from.
        end_date (str): The end date to get issues to.
    
    Returns:
        json: The issues from HelpShift.
    """


    additional_fields = "[\"meta\", \"custom_fields\"]"
    
    # Print additional fields
    #print("Additional fields: {}".format(additional_fields))

    # Add additional fields to url query string
    #url = 'https://api.helpshift.com/v1/{}/issues?includes={}'.format(api_domain, additional_fields)
    

    # Base64 encode API key
    api_key = base64.b64encode(api_key.encode('utf-8')).decode('utf-8')

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + api_key
    }

    # URL Encode additional_fields

    url = 'https://api.helpshift.com/v1/{}/issues?includes={}'.format(api_domain, additional_fields)

    #print("url: {}".format(url))

    #helper.log_info("headers: {}".format(headers))
    request = prepare_http_request(url, 'GET', headers, None)
    #helper.log_info("request: {}".format(request))
    response = send_http_request(request)

    #helper.log_info("response code: {}".format(response.status_code))
    #helper.log_info("response: {}".format(response))

    # Print response body
    #helper.log_info(response.text)

    return response.json()["issues"]


def get_users(api_key, api_domain, start_date, end_date, helper=None):
    """Get users from HelpShift.
    
    Args:
        api_key (str): The API key to use.
        api_domain (str): The API domain to use.
        start_date (str): The start date to get users from.
        end_date (str): The end date to get users to.
    
    Returns:
        json: The users from HelpShift.
    """

    # Base64 encode API key
    api_key = base64.b64encode(api_key.encode('utf-8')).decode('utf-8')

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + api_key
    }

    app_id_url = 'https://api.helpshift.com/v1/{}/apps'.format(api_domain)
    request = prepare_http_request(app_id_url, 'GET', headers, None)
    response = send_http_request(request)

    response.json()["users"]

    url = 'https://api.helpshift.com/v1/{}/user-profiles'.format(api_domain)

    #helper.log_info("headers: {}".format(headers))
    request = prepare_http_request(url, 'GET', headers, None)
    #helper.log_info("request: {}".format(request))
    response = send_http_request(request)

    #helper.log_info("response code: {}".format(response.status_code))
    #helper.log_info("response: {}".format(response))

    # Print response body
    #helper.log_info(response.text)

    return response.json()["users"]


def get_agents(api_key, api_domain, start_date, end_date, helper=None):
    """Get agents from HelpShift.
    
    Args:
        api_key (str): The API key to use.
        api_domain (str): The API domain to use.
        start_date (str): The start date to get agents from.
        end_date (str): The end date to get agents to.
    
    Returns:
        json: The agents from HelpShift.
    """

    # Base64 encode API key
    api_key = base64.b64encode(api_key.encode('utf-8')).decode('utf-8')

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + api_key
    }

    url = 'https://api.helpshift.com/v1/{}/agents'.format(api_domain)

    #helper.log_info("headers: {}".format(headers))
    request = prepare_http_request(url, 'GET', headers, None)
    #helper.log_info("request: {}".format(request))
    response = send_http_request(request)

    #helper.log_info("response code: {}".format(response.status_code))
    #helper.log_info("response: {}".format(response))

    # Print response body
    #helper.log_info(response.text)

    return response.json()["profiles"]


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


    # # Loop through issues
    for issue in issues:
        print(issue)
        print()

    #agents = get_agents(api_key, api_domain, '2019-01-01', '2019-01-31')


    # Loop through issues
    # for agent in agents:
    #     print(agent)
    #     print()