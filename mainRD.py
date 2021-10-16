


import requests


# First Stage
json_format = {'StartDate': '2021-10-25 00:30:00', 'Stage' : 'first'}
obj = requests.post('http://0.0.0.0/dcgs20api_post',json=json_format)
print('-----First Stage-----')
print(obj.text)



# Second Stage
json_format = {'StartDate': '2021-10-25 00:30:00', 'Stage' : 'second'}
#obj = requests.post('https://hsucheng-api-test.herokuapp.com/test_post',json=json_format)
obj = requests.post('http://0.0.0.0/dcgs20api_post',json=json_format)
print('-----Second Stage-----')
print(obj.text)


# Error Stage
json_format = {'StartDate': '2021-10-25 00:30:00', 'Stage' : 'cknmfovd'}
#obj = requests.post('https://hsucheng-api-test.herokuapp.com/test_post',json=json_format)
obj = requests.post('http://0.0.0.0/dcgs20api_post',json=json_format)
print('-----Error Stage-----')
print(obj.text)