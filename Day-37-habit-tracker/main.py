import requests
import os
from dotenv import load_dotenv
load_dotenv()
pixela_endpoint = "https://pixe.la/v1/users"
token = os.getenv("token")
username = "usama015"
graph_name = "walktracker"
user_parameters = {
    "token": token,
    "username":username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# User created so im commenting it out

# response = requests.post(url=pixela_endpoint,json=user_parameters)
# print(response.text)

# Creating Graph

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_config = {
    "id":graph_name,
    "name":"Walk",
    "unit":"minutes",
    "type":"float",
    "color":"momiji",
    "timezone":"Asia/Karachi",
    "description":"Track of my daily Walk"
}
headers ={
    "X-USER-TOKEN":token
}

# Graph Created

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

# Posting to Graph
date = input("Enter Date(yyyyMMdd): ")
quantity = input("Enter Time Of Today's Walk: ")
post_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_name}"
post_parameters = {
    "date":date,
    "quantity":quantity,
}

post_response = requests.post(url=post_endpoint, json=post_parameters,headers=headers)
print(post_response.text)

# testing update(PUT) method

# update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_name}/{date}"

# update_parameter = {
#     "quantity": quantity,
# }

# update_response = requests.put(url=update_endpoint, json=update_parameter, headers=headers)
# print(update_response.text)

# Testing delete method

# delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_name}/{date}"

# delete_response = requests.delete(url=delete_endpoint,headers=headers)
# print(delete_response.text)