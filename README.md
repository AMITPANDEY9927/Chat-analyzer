# Chat-analyzer
WhatsApp Chat Analyzer
A Python-based tool to analyze WhatsApp chat exports and extract meaningful insights such as message frequency, active users, word cloud, emoji usage, and more.

Features:
Upload WhatsApp chat export files (txt format) for analysis.
Analyze overall or specific user statistics (messages, word count, media, links).
Visualize message activity over time with monthly and daily timelines.
Identify the most active days and months with activity maps.
Generate word clouds and display the most common words (excluding stop words).
Analyze emoji usage in the chat with pie charts.

Technologies:
Streamlit: For building interactive web applications.
Pandas: For data processing.
Matplotlib & Seaborn: For data visualization.
WordCloud: For generating word clouds.
Urlextract: For extracting URLs.
Emoji: For emoji analysis.

**Usage:**
Upload a WhatsApp chat export file.
Select a user or view overall statistics.
Explore various charts and visualizations to analyze chat data.

Installation:
Clone the repository.
Install dependencies: pip install -r requirements.txt.
Run the Streamlit app: streamlit run app.py.
