from schwab import auth, client
import json

# this code should be ready
# awaiting my app to be approved at schwab
# still need to get a token when the app is ready for use

with open('../../schwab_api_key.txt', 'r') as api_file:
    schwab_api_key = api_file.readline()
    print(schwab_api_key)

with open('../../schwab_app_secret.txt', 'r') as secret_file:
    schwab_app_secret = secret_file.readline()
    print(schwab_app_secret)


api_key = schwab_api_key
app_secret = schwab_app_secret
callback_url = 'https://127.0.0.1:8182/'
token_path = '../../schwab_token.json'

c = auth.easy_client(api_key, app_secret, callback_url, token_path)

#r = c.get_price_history_every_day('DDD')
#r.raise_for_status()
#print(json.dumps(r.json(), indent=4))

r = c.get_quote('DDD')
r.raise_for_status()
print(json.dumps(r.json(), indent=4))
