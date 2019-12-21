
import csv
import os
import preprocessor.api as p
import tweepy

consumer_key = 'p7x4IB53L2HAS2n697YC4sUOz'
consumer_secret = 'f2mo9T10WtaiJKzYHI6ObR9M52lF6dak0vq6AYgzYlaHGIfXRM'

access_token = '1207310789058551808-9RhMagAjXU3oPuE27cmfURmUOmhI9C'
access_token_secret = 'R5xZXKvnZQZB7iQ1jTBpi2d8XHgvul6YQ0z7pfPWvheSg'

# perform authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create our twitter api to access tweets from it
api = tweepy.API(auth)

location = "%s,%s,%s" % ("37.09","-95.71","2000km")

loop = True

while loop:

    print(
        '''
        1. Search tweets by keywords
        2. Exit
        ''')

    user_input = input('Enter your option: ')

    if int(user_input) == 1:
        search_term = input('Enter tweet keyword/hashtag to search: ')
        no_of_search_items = int(input('Enter number of tweets to analyze: '))


        public_tweets = tweepy.Cursor(api.search,q=search_term,lang="en",geocode=location,include_entities=True).items(no_of_search_items)


        index = 0
        if os.path.isfile('./tweetbykeyword.csv'):
            my_csv_file = open('tweetbykeyword.csv', 'r+',encoding='utf-8')
            reader = csv.DictReader(my_csv_file)
            field_names = ['Index', 'Keyword', 'Tweets']
            for each_row in reader:
                if search_term == each_row['Keyword']:
                    index += 1
            writer = csv.DictWriter(my_csv_file, fieldnames=field_names)
        else:
            my_csv_file = open('tweetbykeyword.csv', 'w', encoding='utf-8')
            field_names = ['Index', 'Keyword', 'Tweets']
            writer = csv.DictWriter(my_csv_file, fieldnames=field_names)
            writer.writeheader()

        for each_tweet in public_tweets:
            data = p.clean(each_tweet.text)
            data = data.encode('utf-8')
            data = data.decode('unicode_escape')
            writer.writerow({'Index': index, 'Keyword': search_term, \
                             'Tweets': data})
            index += 1

    elif int(user_input) == 2:
        loop = False
    else:
        print('Please enter 1 or 2')
