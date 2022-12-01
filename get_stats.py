import re
def get_stats(selected_user,df):
    if selected_user=='Overall':
        words=[]
        for msg in df['msg']:
            words.extend(msg.split())
        
        # total links
        pattern = r'(http)' 
        url=[]
        for msg in df['msg']:
            url.extend(re.findall(pattern, msg))
        # total media
        media=[]
        for msg in df['msg']:
            if msg =='<Media omitted>':
                media.append(msg)
        return df.shape[0], len(words),len(url),len(media)
    else:
        words=[]
        for msg in df[df['user']=='Purnendu']['msg']:
            words.extend(msg.split())
        # total links
        pattern = r'(http)' 
        url=[]
        for msg in df[df['user']==selected_user]['msg']:
            url.extend(re.findall(pattern, msg))
        # total media
        media=[]
        for msg in df[df['user']==selected_user]['msg']:
            if msg =='<Media omitted>':
                media.append(msg)
        return df[df['user']==selected_user].shape[0], len(words),len(url), len(media)
    