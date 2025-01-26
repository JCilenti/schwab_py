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
token_path = 'token.json'

c = auth.easy_client(api_key, app_secret, callback_url, token_path)

#r = c.get_price_history_every_day('DDD')
#r.raise_for_status()
#print(json.dumps(r.json(), indent=4))

account_info = c.get_account_numbers()
account_info.raise_for_status()
print(json.dumps(account_info.json(), indent=4))

spec_account_1 = c.get_account('7CECEEC61EC849EFF3879027F2BBE6479479B61F45EFAFEACAB017C57210E4A4')
spec_account_1.raise_for_status()
print(json.dumps(spec_account_1.json(), indent=4))

spec_account_2 = c.get_account('8C2E655CAFFE120E8A189818C5D8FACE042E93FFB6F8A99143352AE1684D028A')
spec_account_2.raise_for_status()
print(json.dumps(spec_account_2.json(), indent=4))




