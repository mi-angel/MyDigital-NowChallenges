import pandas as pd
import snscrape.modules.twitter as snt
import itertools

search = '"Eurovision lang:en"'
scraped_tweets = snt.TwitterSearchScraper(search).get_items()

sliced_scraped_tweets = itertools.islice(scraped_tweets,150000)

df = pd.DataFrame(sliced_scraped_tweets) #[['date','content']]

df.to_csv("C:/Users/Angel/Documents/JupiterFiles/MyTweets5.csv")



# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# print(df)

# # Another option I
# tweets = []

# for i,tweet in enumerate(snt.TwitterSearchScraper(query = "data science").get_items()):
#     if i>10:
#         break
#     tweets.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.retweetCount, tweet.replyCount, tweet.lang,
#                    tweet.sourceLabel, tweet.content])


# # Another option II
# # with open("pTweets.csv","x") as pt:
# for tweet in snt.TwitterSearchScraper(query).get_items():
#     print (vars(tweet))
#     break
#         # if len(tweets)==limit:
#         #     break
#         # else:
#         #     # tweets.append([tweet.date,tweet.user.username, tweet.rawContent])
#         #     pt.write(f'{vars(tweet)}\n')

# # df = pd.DataFrame(tweets, columns= ['Date', 'User', 'Tweet'])
# # print(df)







# import twint

# c = twint.Config()


# # c.Username = "privacy"
# # c.Custom["tweet"] = ["id"]
# # c.Custom["user"] = ["bio"]
# c.Search = 'python'
# c.Limit = 10
# c.Store_csv = True
# c.Output = "someTwits.csv"

# twint.run.Search(c)



# import snscrape.modules.twitter as snst
# import pandas as pd
# import csv

# query = "please"
# #query = "(from:accommodation) until:2022-01-01 since:2023-01-01"
# # tweets= []
# # limit = 10




# a=[]
# a.append(1)
# a.append(2)
# a.append(3)
# a.append(4)
# a.append(5)
# with open("myTweetsFile.csv",'x') as tf:
#     for i in a:
#         if i==2 or i==3:
#             tf.write(f'Hello Sr Michael {i}\n')




print("finished")

# https://elitedatascience.com/python-web-scraping-libraries
# https://medium.com/swlh/how-to-scrape-tweets-by-location-in-python-using-snscrape-8c870fa6ec25
# https://github.com/JustAnotherArchivist/snscrape/issues/846
# https://www.kaggle.com/getting-started/222277