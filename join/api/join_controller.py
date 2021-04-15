from flask import request
from firebase_admin import auth
import requests
from join import firebase
import ast
import time



def get_join():
    token = request.headers['authorization']
    decoded_token = auth.verify_id_token(token)
    email = decoded_token['firebase']['identities']['email'][0]
  
    
    
    tags_response = requests.get('http://tags:7000/api/users/tags', headers={'authorization': token}, verify=False)
    
    dict_tag = tags_response.content.decode("UTF-8")
    resp_tag = ast.literal_eval(dict_tag)
    
    if "error" in resp_tag.keys():
        return resp_tag

   

    tasks_response = requests.get('http://tasks:1000/api/users/tasks', headers={'authorization': token}, verify=False)
            
    dict_tasks = tasks_response.content.decode("UTF-8")
    resp_tasks = ast.literal_eval(dict_tasks)
    
    resp = {
        "msg":"succeess",
        "data":[{
            "email":email,
            "tags":resp_tag["data"][0]["tags"][0],
            "tasks":resp_tasks["data"][0]["tasks"][0]
        }],
        "status":"200"
    }


    return resp
    
    
    