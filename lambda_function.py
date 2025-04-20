import pandas as pd
import requests

def lambda_handler(event, context):
    print("Event Data: ", event)
    print("Context ---> ", context)
    
    response = requests.get("https://www.google.com")
    print(response.text)
    
    d = {'col1':[1,2], 'col2':[3,4]}
    df = pd.DataFrame(d,ignore_index=True)
    print(df.head(7))
    
    
