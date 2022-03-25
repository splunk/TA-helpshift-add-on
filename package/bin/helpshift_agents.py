
from asyncio import events
import os
import sys
import time
import datetime
import json

from utility import get_agents




bin_dir = os.path.basename(__file__)

'''
'''
import import_declare_test

import os
import os.path as op
import sys
import time
import datetime
import json

import traceback
import requests
from splunklib import modularinput as smi
from solnlib import conf_manager
from solnlib import log
from solnlib.modular_input import checkpointer
from splunktaucclib.modinput_wrapper import base_modinput  as base_mi 
import random

# encoding = utf-8


'''
    IMPORTANT
    Edit only the validate_input and collect_events functions.
    Do not edit any other part in this file.
    This file is generated only once when creating the modular input.
'''
'''
# For advanced users, if you want to create single instance mod input, uncomment this method.
def use_single_instance_mode():
    return True
'''

class ModInputhelpshift_agents(base_mi.BaseModInput):

    def __init__(self):
        use_single_instance = False
        super(ModInputhelpshift_agents, self).__init__("ta_helpshift", "helpshift_agents", use_single_instance)
        self.global_checkbox_fields = None

    def get_scheme(self):
        """overloaded splunklib modularinput method"""
        scheme = super(ModInputhelpshift_agents, self).get_scheme()
        scheme.title = ("helpshift_agents")
        scheme.description = ("Go to the add-on\'s configuration UI and configure modular inputs under the Inputs menu.")
        scheme.use_external_validation = True
        scheme.streaming_mode_xml = True

        scheme.add_argument(smi.Argument("name", title="Name",
                                         description="",
                                         required_on_create=True))

        """
        For customized inputs, hard code the arguments here to hide argument detail from users.
        For other input types, arguments should be get from input_module. Defining new input types could be easier.
        """
        scheme.add_argument(smi.Argument("start_date", title="Start Date",
                                         description="Date you want to start collecting events from. Leave blank to start collection of all events.",
                                         required_on_create=False,
                                         required_on_edit=False))
        return scheme

    def get_app_name(self):
        return "TA-helpshift"

    def validate_input(helper, definition):
        """Implement your own validation logic to validate the input stanza configurations"""
        # This example accesses the modular input variable
        # start_date = definition.parameters.get('start_date', None)
        pass
    

    def collect_events(helper, ew):
        global_helpshift_domain = helper.get_global_setting("helpshift_domain")
        global_api_token = helper.get_global_setting("api_token")
        
        # print(global_helpshift_domain)
        # print(global_api_token)
        
        #helper.set_log_level("debug")
        # helper.log_debug(global_helpshift_domain)
        # helper.log_debug(global_api_token)

        # Get agents from helpshift API
        helper.log_info(f'[dave] Domain: {global_helpshift_domain}')
        helper.log_info(f'[dave] Token: {global_api_token}')
        get_agents_result = get_agents(global_api_token, global_helpshift_domain, '2019-01-01', '2019-01-31', helper)

        helper.log_info(f'[dave] agents Result: {get_agents_result}')

        # Write event to Splunk with helper
        for agent in get_agents_result:
            # helper.log_debug(agent)
            # helper.log_debug(type(agent))
            # helper.log_debug(json.dumps(agent))
            # helper.new_event(data, time=None, host=None, index=None, source=None, sourcetype=None, done=True, unbroken=True)
            event = helper.new_event(source=helper.get_input_type(), index=helper.get_output_index(), sourcetype=helper.get_sourcetype(), data=json.dumps(agent))
            ew.write_event(event)

            
        """Implement your data collection logic here
    
        # The following examples get the arguments of this input.
        # Note, for single instance mod input, args will be returned as a dict.
        # For multi instance mod input, args will be returned as a single value.
        opt_start_date = helper.get_arg('start_date')
        # In single instance mode, to get arguments of a particular input, use
        opt_start_date = helper.get_arg('start_date', stanza_name)
    
        # get input type
        helper.get_input_type()
    
        # The following examples get input stanzas.
        # get all detailed input stanzas
        helper.get_input_stanza()
        # get specific input stanza with stanza name
        helper.get_input_stanza(stanza_name)
        # get all stanza names
        helper.get_input_stanza_names()
    
        # The following examples get options from setup page configuration.
        # get the loglevel from the setup page
        loglevel = helper.get_log_level()
        # get proxy setting configuration
        proxy_settings = helper.get_proxy()
        # get account credentials as dictionary
        account = helper.get_user_credential_by_username("username")
        account = helper.get_user_credential_by_id("account id")
        # get global variable configuration
        global_userdefined_global_var = helper.get_global_setting("userdefined_global_var")
    
        # The following examples show usage of logging related helper functions.
        # write to the log for this modular input using configured global log level or INFO as default
        helper.log("log message")
        # write to the log using specified log level
        helper.log_debug("log message")
        helper.log_info("log message")
        helper.log_warning("log message")
        helper.log_error("log message")
        helper.log_critical("log message")
        # set the log level for this modular input
        # (log_level can be "debug", "info", "warning", "error" or "critical", case insensitive)
        helper.set_log_level(log_level)
    
        # The following examples send rest requests to some endpoint.
        response = helper.send_http_request(url, method, parameters=None, payload=None,
                                            headers=None, cookies=None, verify=True, cert=None,
                                            timeout=None, use_proxy=True)
        # get the response headers
        r_headers = response.headers
        # get the response body as text
        r_text = response.text
        # get response body as json. If the body text is not a json string, raise a ValueError
        r_json = response.json()
        # get response cookies
        r_cookies = response.cookies
        # get redirect history
        historical_responses = response.history
        # get response status code
        r_status = response.status_code
        # check the response status, if the status is not sucessful, raise requests.HTTPError
        response.raise_for_status()
    
        # The following examples show usage of check pointing related helper functions.
        # save checkpoint
        helper.save_check_point(key, state)
        # delete checkpoint
        helper.delete_check_point(key)
        # get checkpoint
        state = helper.get_check_point(key)
    
        # To create a splunk event
        helper.new_event(data, time=None, host=None, index=None, source=None, sourcetype=None, done=True, unbroken=True)
        """
    
        '''
        # The following example writes a random number as an event. (Multi Instance Mode)
        # Use this code template by default.
        import random
        data = str(random.randint(0,100))
        event = helper.new_event(source=helper.get_input_type(), index=helper.get_output_index(), sourcetype=helper.get_sourcetype(), data=data)
        ew.write_event(event)
        '''
    
        '''
        # The following example writes a random number as an event for each input config. (Single Instance Mode)
        # For advanced users, if you want to create single instance mod input, please use this code template.
        # Also, you need to uncomment use_single_instance_mode() above.
        import random
        input_type = helper.get_input_type()
        for stanza_name in helper.get_input_stanza_names():
            data = str(random.randint(0,100))
            event = helper.new_event(source=input_type, index=helper.get_output_index(stanza_name), sourcetype=helper.get_sourcetype(stanza_name), data=data)
            ew.write_event(event)
        '''

    def get_account_fields(self):
        account_fields = []
        return account_fields

    def get_checkbox_fields(self):
        checkbox_fields = []
        return checkbox_fields

    def get_global_checkbox_fields(self):
        if self.global_checkbox_fields is None:
            checkbox_name_file = os.path.join(bin_dir, 'global_checkbox_param.json')
            try:
                if os.path.isfile(checkbox_name_file):
                    with open(checkbox_name_file, 'r') as fp:
                        self.global_checkbox_fields = json.load(fp)
                else:
                    self.global_checkbox_fields = []
            except Exception as e:
                self.log_error('Get exception when loading global checkbox parameter names. ' + str(e))
                self.global_checkbox_fields = []
        return self.global_checkbox_fields

if __name__ == "__main__":
    exitcode = ModInputhelpshift_agents().run(sys.argv)
    sys.exit(exitcode)
