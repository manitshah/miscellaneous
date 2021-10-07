#!/usr/bin/python
# -*- coding: latin-1 -*-
#simple config parser
#Some Rules that this parser follows are below
#Boolean-like config values (on/off, yes/no, true/false) should return real booleans: true/false.
#Numeric config values should return real numerics: integers, doubles, etc
#Ignore or error out on invalid config lines, your choice

import os
import re 
import json

#main function to parse
def custom_parser(fullfilepath):
    
    config = {}
    #read file 
    file = open(fullfilepath,'r')
    #get lines 
    lines = file.readlines()
    #iterate 
    for line in lines:
        temp = {}
        line = line.strip()
        #if first line is a comment then ignore 
        if not re.search('\A#',line):
            try:
                arr = line.split('=')

                if arr:
                    key = arr[0].strip()

                    value = formatter(arr[1].strip())
                    config[key] = value
            except: 
                pass
    
    return json.dumps(config)

#determine type of value and format it 
def formatter(value):

    if value.isdigit():    
        #case string to number
       return int(value)
    elif value == 'on' or value == 'yes' or value == 'true': 
        return True
    elif value == 'no' or value == 'true' or value == 'false':
        return False
    elif value.replace('.','',1).isdigit():
        return float(value)
    else:    
        return value 

#call function above to parse config file 
#examle config.txt
#print(custom_parser(os.path.join(os.getcwd(),'config.txt')))


