import pandas as pd
import os

file="history.csv"

def save_history(objects):

    df = pd.DataFrame(objects,columns=["Object","Confidence"])

    if os.path.exists(file):

        old=pd.read_csv(file)

        df=pd.concat([old,df])

    df.to_csv(file, index=False)    