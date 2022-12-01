from wordcloud import WordCloud
def generate_cloud(df):
    wc=WordCloud(width=400, height=300, min_font_size=10, background_color='white')
    df_wc=wc.generate(df[df['msg']!='<Media omitted>']['msg'].str.cat(sep=" "))
    return df_wc
