import csv
import pandas as pd
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from sqlalchemy import create_engine

# open file with downloaded tweets
df = pd.read_csv("MyTweets5.csv",index_col=0, parse_dates=True,low_memory=False)

# print(df.columns)
# new dataframe to select the columns to work with
df2 = df[["date","rawContent","replyCount","retweetCount","likeCount","quoteCount"]]

# Method to perform the sentiment analysis
def getSentiment(text):
    textBlobObj = TextBlob(text) #,analyzer=NaiveBayesAnalyzer()
    return textBlobObj.sentiment

# Applying getSentiment method on tweets
df2["Sentiment"] = df2['rawContent'].apply(getSentiment)

# Split the results of the analysis by columns
df2["Subjetivity"] = df2['Sentiment'].str[1].copy()
df2["Sentiment"] = df2['Sentiment'].str[0].copy()

# Polarity measures how positive or negative the comment is
# Subjetivity measures how much of an opininon it is versus how factual
# label method helps to classify tweets in function of their polarity
def label(val):
    # change the value of middle_range variable to modify 
    # the criteria of what will be a neutral value
    middle_range = 0.1
    if val >= 0 + middle_range:
        return "Positive"
    elif val <= 0 - middle_range:
        return "Negative"
    else:
        return "Neutral"
    
# Applying label method on the dataframe
df2["Sentiment_Label"] = df2["Sentiment"].apply(label)

print(df2['Sentiment_Label'].head())
print('\n***********************\n++DATAFRAME READY++\n***********************\n')

# Saving a csv backup file
df2.to_csv("C:/Users/Angel/Documents/JupiterFiles/MyTweets7.csv")
print('\n**************************\n++Backup File READY++\n**************************\n')

# Create MySQL connection
engine = create_engine('mysql+mysqlconnector://root:toor@localhost/twitter', echo=False) 
# converts dataframe into a table in the database
df2.to_sql("tweetseurovision2023v2",if_exists='replace', con=engine)
print('\n**************************\n++MySQL DATABASE READY++\n**************************\n')

print(f'My new columns: \n {df2.tail(10)}')



















# #==============================================================
# # Lists to collect sentiment analysis values and label
# Classif=[]
# P_pos=[]
# P_neg=[]

# # TextBlob instance using NaiveBayesAnalyzer for sentiment analysis
# for i, tweet in df2.iterrows():
    
#     tweet["TB_obj"] = TextBlob(str(tweet["rawContent"]),analyzer=NaiveBayesAnalyzer())
    
#     Classif.append(tweet["TB_obj"].sentiment.classification)
#     P_pos.append(tweet["TB_obj"].sentiment.p_pos)
#     P_neg.append(tweet["TB_obj"].sentiment.p_neg)
#     print(f'tweet {i} is ready')

# df2["SentimentLabel"] = Classif
# df2["p_positive"]= P_pos
# df2["p_negative"]= P_neg


# def getP_pos(text):
#     textBlobObj = TextBlob(text,analyzer=NaiveBayesAnalyzer())
#     return textBlobObj.sentiment.p_pos

# def getP_neg(text):
#     textBlobObj = TextBlob(text,analyzer=NaiveBayesAnalyzer())
#     return textBlobObj.sentiment.p_neg


# df2["p_positive"] = df2["rawContent"].apply(getP_pos)
# df2["p_negative"] = df2["rawContent"].apply(getP_neg)

# #==============================================================





# # good if you want to use csv
# with open("MyTweets5.csv") as tw:
#     reader = csv.reader(tw)
#     next(tw)

# let's try with pandas


# print(TextBlob(str(df2["rawContent"])))
    # sentimentVal= TextBlob(df2["rawContent"]) 


# import mysql.connector
# cnx = mysql.connector.connect(user='root', password='toor', host='localhost', database='twitter')

# https://stackoverflow.com/questions/20692122/edit-pandas-dataframe-row-by-row





# df2["TweetContentToString"] = sentimentVal

# df2["TweetContentToString"] = df2["rawContent"].str.upper()

# df2["SentimentValue"] = sentimentVal.sentiment
# df2["OtherSent"] = sentimentVal.sentiment_assessments

# print(f'THIS IS THE TAIL: \n {df[-5:]}') # it works The same as # print(df.tail())
# print(f'THIS IS THE HEAD: \n {df[:5]}') # it works The same as # print(df.head())
# print(df[:1]) # it works

# df2 = df[["date","rawContent"]]


# print(f'renderedContent \n {df2["renderedContent"]}')

# sub_df =df["date","rawContent", "renderedContent"]
# print(sub_df.head())
# https://textblob.readthedocs.io/en/dev/
# https://pypi.org/project/SQLAlchemy/2.0.14/
# https://www.pythonprogramming.in/sentiment-analysis-with-the-naivebayesanalyzer.html
# https://pandas.pydata.org/pandas-docs/stable/getting_started/tutorials.html