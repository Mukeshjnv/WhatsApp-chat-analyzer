import imp
import re
import pandas as pd
def preprocess(data):
    pattern="\d{2}\/\d{2}\/\d{2}, \d{1,2}:\d{2} (?:am|pm) - "
    messeges=re.split(pattern,data)[1:]
    pattern="\d{2}\/\d{2}\/\d{2}, \d{1,2}:\d{2} (?:am|pm)"
    dates=re.findall(pattern,data)
    df=pd.DataFrame({'msg_date':dates,
                'msg':messeges})
    df['user']=df['msg'].apply(lambda x:x.split(':')[0])
    df['msg']=df['msg'].apply(lambda x:x.split(':')[1] if len(x.split(':'))>1 else None)
    df.dropna(inplace=True)
    df=df[['user','msg','msg_date']]
    df['msg_date']=pd.to_datetime(df['msg_date'])
    df['msg']=df['msg'].apply(lambda x:x[1:-1])
    df.reset_index(drop=True,inplace=True)
    df['year']=df['msg_date'].dt.year
    df['month']=df['msg_date'].dt.month_name().apply(lambda x:x[:3])
    df['time']=df['msg_date'].dt.time
    df['hour']=df['msg_date'].dt.hour
    df.drop('msg_date', axis=1, inplace=True)
    return df