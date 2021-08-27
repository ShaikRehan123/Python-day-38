import requests as rqs
import datetime as dt
TODAY = dt.date.today().strftime('%Y%m%d')
# // Add User
user_name = 'shaikrehan'
token = 'farruboti786'
add_user_endpoint = 'https://pixe.la/v1/users'
user_params = {
    "token": token,
    "username": user_name,
    "agreeTermsOfService":'yes',
    "notMinor":'yes',
}
# response = rqs.post(url=pixela_end_point , json=user_params)
# print(response.text)
# =========================================================== 
# // Add Graph
add_graph = 'https://pixe.la/v1/users/shaikrehan/graphs'
graph_params= {
    "id":'graph1',
    "name":'Sleeping Graph',
    "unit":"Hours",
    "type":'float',
    "color":'sora'
}
headers = {
    "X-USER-TOKEN":token,
}
# response = rqs.post(url=add_graph, json=graph_params , headers=headers)
# print(response.text)
# ! Post Pixel data 
post_pixel_endpoint = f'https://pixe.la/v1/users/{user_name}/graphs/graph1'
post_pixel_data = {
    "date":TODAY,
    "quantity":"10",
}
response = rqs.post(url=post_pixel_endpoint , json=post_pixel_data , headers=headers)
print(response.text)
# print(response.text)