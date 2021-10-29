client_id = " ********** "
redirect_uri = "https://trade.fyers.in/api-login/redirect-uri/index.html"
response_type = "200"
state = "successfull"
secret_key = " ********** "
hash = "4e10a8f4c3f835aebb3fb587b7ee5c30466dc300217a59236e3733f61574ff27"



from fyers_api import fyersModel
from fyers_api import accessToken

session=accessToken.SessionModel(client_id=client_id, secret_key=secret_key, redirect_uri=redirect_uri, response_type=response_type, state=state)

auth_code = session.generate_authcode()

auth_codeone = "https://api.fyers.in/api/v2/generate-authcode?client_id=JD9J0LMC9Y-100&redirect_uri=https%3A%2F%2Ftrade.fyers.in%2Fapi-login%2Fredirect-uri%2Findex.html&response_type=8686&state=successfull"
response = session.generate_token()
access_token = response["access_token"]
print("The access token is: {}".format(access_token))

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token)

is_async = True

print(response)
print(auth_code)


