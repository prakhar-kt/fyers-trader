from fyers_apiv3 import fyersModel
import webbrowser
import os
import json

redirect_uri = os.getenv("REDIRECT_URI")
client_id = os.getenv("CLIENT_ID")
secret_key = os.getenv("SECRET_KEY")

grant_type = "authorization_code"
response_type = "code"
state = "sample"

appSession = fyersModel.SessionModel(client_id=client_id, 
                                   secret_key=secret_key, 
                                   redirect_uri=redirect_uri, 
                                   response_type=response_type, 
                                   state=state, 
                                   grant_type=grant_type)

auth_url = appSession.generate_authcode()
webbrowser.open(auth_url)

code = input("Enter the code: ")
appSession.set_token(code)

response = appSession.generate_token()

try:
    access_token = response['access_token']
    print("token generated successfully", access_token)
except Exception as e:
    print("error generating token", e)

fyers = fyersModel.FyersModel(client_id=client_id, 
                              token=access_token,
                              log_path="logs/")

response = fyers.get_profile()
print("profile details", response)

# Save credentials to JSON file
os.makedirs("creds", exist_ok=True)
credentials = {
    "client_id": client_id,
    "access_token": access_token
}
with open("creds/credentials.json", "w") as f:
    json.dump(credentials, f, indent=2)

print("credentials saved successfully")

