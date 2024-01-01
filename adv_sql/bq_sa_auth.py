import os
from google.cloud import bigquery
from google.oauth2 import service_account

def client():
    
    # Working directory
    
    current_dir = os.getcwd()
    
    # Get the list of files in the directory with json extension, make sure there are not any other json file in the local directory
    json_key = [f for f in os.listdir(current_dir) if f.endswith('.json')]
    
    key_path = current_dir + '/' + json_key[0]

    # Set key_path to the path to the service account key file.
    # key_path = "path/to/service_account.json"
    
    credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],)

    # Create a "Client" object with right credentials and the project_id that we created using our google cloud account
    
    bq_client = bigquery.Client(credentials=credentials, project=credentials.project_id,)

    return bq_client