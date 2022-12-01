import imp
import streamlit as st
import preprocessor
import get_stats
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import helper 
st.sidebar.title('WhatsApp Chat Analyzer')
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data=bytes_data.decode('utf-8')
    df=preprocessor.preprocess(data)
    st.dataframe(df)
    # Get users
    user_list=df['user'].unique().tolist()
    user_list.sort()
    user_list.insert(0,'Overall')
    selected_user=st.sidebar.selectbox('Analyse a user activity',user_list)
    # Show stats
    total_msg, total_words, tota_links, total_media=get_stats.get_stats(selected_user,df)
    col1, col2, col3, col4= st.columns(4)
    with col1:
        st.header('Total messages')
        st.title(total_msg)
    with col2:
        st.header('Total words')
        st.title(total_words)
    with col3:
        st.header('Total links')
        st.title(tota_links)
    with col4:
        st.header('Total media')
        st.title(total_media)
    
    st.title('Most Busy user')
    col1, col2= st.columns(2)
    with col1:
        fig, ax = plt.subplots()
        ax=sns.countplot(x=df['user'], order=df['user'].value_counts()[:10].index)
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
    with col2:
        activity_df=(df['user'].value_counts()/df.shape[0]*100).reset_index().rename(columns={'index': 'name', 'user':'activity(%)'})
        activity_df['activity(%)']=activity_df['activity(%)'].apply(lambda x: round(x,2))
        st.dataframe(activity_df)
    cloud=helper.generate_cloud(df)
    # wordcloud
    fig, ax=plt.subplots()
    ax.imshow(cloud)
    st.pyplot(fig)