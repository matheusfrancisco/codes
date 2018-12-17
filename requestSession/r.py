from requests import Request , Session
import requests

s = requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')


#Saida
print(r.text)
'''

{
  "cookies": {
    "sessioncookie": "123456789"
  }
}


'''



## creates a session begin, and navigates to the login page
s.get('http://......', timeout=30)
 
## define the form data
data = {
   
    'NAME': 'test',
    'PWD': 'test'
   
    }
 
## define the headers
headers = {   

    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9'
   
    }
 
## posts the username and password to the form
response = s.post('http://....', data=data, headers=headers)
 
## navigates to the system info page to scrape the data
r = s.get('http://....', data=data, headers=headers)

