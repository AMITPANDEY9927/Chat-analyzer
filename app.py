import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns



st.sidebar.title("whatsapp chat analyzer")
upload_file=st.sidebar.file_uploader("chose a file with 24 hour chat format")
if upload_file is not None:
    bytes_data=upload_file.getvalue()
    data=bytes_data.decode("utf8")
    df=preprocessor.preprocess(data)

    # st.dataframe(df) print message list

    # fetch unique users
    user_list=df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user=st.sidebar.selectbox("show analysis wrt",user_list)
    if st.sidebar.button("show analysis"):
        num_messages,words,num_media_messages,num_links=helper.fetch_stats(selected_user,df)

        st.title("Top Statistics")
        col1,col2,col3,col4=st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)
        with col4:
            st.header("links  Shared")
            st.title(num_links)
        # monthly timeline
        st.title('Monthly Timeline')
        timeline=helper.monthly_timeline(selected_user,df)
        fig,ax=plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # daily timeline
        st.title('Daily Timeline')
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        st.title('Activity Map')
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='purple')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='yellow')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)



        if selected_user=='Overall':
            st.title('Most busy user')
            x,new_df=helper.most_busy_users(df)
            fig, ax=plt.subplots()

            col1,col2=st.columns(2)
            with col1:
                ax.bar(x.index, x.values,color='green')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)
        # creating word cloud
        df_wc=helper.create_wordcloud(selected_user, df)
        fig,ax=plt.subplots()
        ax.imshow(df_wc)
        st.title("Word Cloud")
        st.pyplot(fig)

        # most common words
        most_common_df= helper.most_common_words(selected_user, df)
        fig,ax=plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1])
        plt.xticks(rotation='vertical')
        st.title("Most Common Words")
        st.pyplot(fig)

         #emoji analysis
        emoji_df=helper.emoji_helper(selected_user,df)
        st.title("Emoji analysis")
        col1,col2=st.columns(2)
        if not emoji_df.empty:
            with col1:
                st.dataframe(emoji_df)
            with col2:
                emoji_font = fm.FontProperties(fname='C:\Windows\Fonts\seguiemj.ttf')
                fig, ax = plt.subplots()
                ax.pie(emoji_df[1].head(10), labels=emoji_df[0].head(10), autopct='%.2f%%',
                   textprops={'fontproperties': emoji_font})
                st.pyplot(fig)
        else:
            # st.write("No emojis used by the selected user.")
            st.markdown(
                "<h3 style='color: #FF6347; text-align: center;'>No Emojis used by the selected user.</h3>",
                unsafe_allow_html=True
            )




