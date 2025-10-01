import requests
import json

# Using the postcode API

# post_codes_req = requests.post("https://api.postcodes.io/postcodes")

# print(type(post_codes_req))
# print("")
# print(post_codes_req.status_code)
# print("")
# print(post_codes_req.headers)
# print("\nHeaders type is: " + str(type(post_codes_req.headers)))
# print("")
# print(post_codes_req.content)
# print("\nContent type is: " + str(type(post_codes_req.content)))
# print("")
# print(post_codes_req.json())
# print("\nJSON type is: " + str(type(post_codes_req.json())))  # method type class, looks close enough to a dict
# print("")

# How to get specific info - here I was getting the region for my postcode.

# data_dict = dict(post_codes_req.json())
# print(data_dict.keys())
# result = (data_dict["result"])
# print(f"Region is {result['region']}")
#
# json_body = json.dumps(result)
# print(json_body)
# print(type(json_body))

postcodes_dict = {'postcodes': ["PR3 0SG", "M45 6GN", "EX165BL"]}
json_formatted_str = json.dumps(postcodes_dict)
headers = {'Content-Type': 'application/json'}
post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_formatted_str)
print(post_multi_req)
print(json.dumps(post_multi_req.json(), indent =2))