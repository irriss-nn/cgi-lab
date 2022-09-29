#!/usr/bin/env python3
import os
import json
#q1
#print("Content-Type: text/plain")
#print()
#print(os.environ)

#print ENV VARIABLES AS JSON
#print("Content-Type: application/json")#let the browser know to expect json
#print()
#print(json.dumps(dict(os.environ),indent=2))
#Q2
#print("Content-Type: text/html")
#print()
#print(f"<p>QUERY_STRING = {os.environ['QUERY_STRING']}</p>")


#Q3
print("Content-Type: text/html")
print()
print(f"<p>HTTP_USER_AGENT = {os.environ['HTTP_USER_AGENT']}</p>")
#env = {}

# Iterate through environment variables and add them to env
#for env_key, env_value in os.environ.items():
 #   env[env_key] = env_value
    #print('{} -> {}'.format(env_key,env_value))

#print("Content-Type: application/json")    # HTML is following
#print()                             # blank line, end of headers

# Print env dictionary in json format
#print(json.dumps(env))