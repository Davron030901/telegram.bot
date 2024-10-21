#pip install requests
# git lab API
import requests

response=requests.get("https://gitlab.com/api/v4/users/23155619/projects")
print(response.text)
print(response.json())

print(type(response.text))
my_project=response.json()
for project in my_project:
    print(f"Project Name: {project['name']}  Project Url{project['web_url']}")