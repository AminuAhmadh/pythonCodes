import bitly_api
TOKEN = '96665cc515cd7a8195360c3b64fbe42f88598d5a' # Your token from bit.ly

access = bitly_api.Connection(access_token = TOKEN)
# Collect long URL
try:
    full_link = input('Enter long URL: ')
    short_url = access.shorten(full_link) 
    print('Short URL = ',short_url['url'])
except Exception as network_error:
    print('Error! Please check your network connection or try again.')