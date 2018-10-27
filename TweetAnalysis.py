from textblob import TextBlob
import sys,tweepy
import matplotlib.pyplot as plt

def percentage(part, whole):
    return 10000 * float(part)/float(whole)

consumerKey ="YOur key"
consumerSecret = "YOur key"
accessToken="YOur key"
accessTokenSecret="YOur key"

auth = tweepy.OAuthHandler(consumerKey,consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("Enter hashtag to search about: ")
noOfSearchTerm = int(input("Enter how many tweets to analyze?"))


tweets = tweepy.Cursor(api.search, q=searchTerm, lang="English").items(noOfSearchTerm)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if(analysis.sentiment.polarity == 0):
        neutral +=1
    elif (analysis.sentiment.polarity < 0.00):
        negative += 1
    elif (analysis.sentiment.polarity > 0.00):
        positive += 1


positive = percentage(positive, noOfSearchTerm)
negative = percentage(negative, noOfSearchTerm)
neutral = percentage(neutral, noOfSearchTerm)

print("How people are reacting on "+ searchTerm+ " by analysing "+str(noOfSearchTerm)+" tweets!")
if(polarity==0):
    print("Neutral")
elif(polarity<0):
    print("Negative")
elif(polarity>0):
    print("Positive")

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

labels = ['Positive['+str(positive)+'%]', 'Neutral['+str(neutral)+'%]', 'Negative['+str(negative)+'%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'gold','red']
patches, texts = plt.pie(sizes,  colors=colors, startangle=90)
plt.legend(patches,labels,loc="best")
plt.title("How people are reacting on "+ searchTerm+ " by analysing"+str(noOfSearchTerm)+" tweets!")
plt.axis('equal')
plt.tight_layout()
plt.show()