from twython import Twython
import csv

TWITTER_APP_KEY = 'XXXX' 
TWITTER_APP_KEY_SECRET = 'XXXX' 
TWITTER_ACCESS_TOKEN = 'XXXX'
TWITTER_ACCESS_TOKEN_SECRET = 'XXXX'

api=Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

tweets                          =   []
MAX_ATTEMPTS                    =   50
COUNT_OF_TWEETS_TO_BE_FETCHED   =   100
cnt = 1

for i in range(0,MAX_ATTEMPTS):

    if(COUNT_OF_TWEETS_TO_BE_FETCHED < len(tweets)):
        break # we got 500 tweets... !!
    # STEP 1: Query Twitter
    if(0 == i):
        # Query twitter for data. 
        results    = api.search(q="http://www.youtube.com/watch?v=fOTs68E1WUI",count='100')
    else:
        # After the first call we should have max_id from result of previous call. Pass it in query.
        results    = api.search(q="http://www.youtube.com/watch?v=fOTs68E1WUI",include_entities='true',max_id=next_max_id)
    # STEP 2: Save the returned tweets
    for result in results['statuses']:
        a=str(result).replace("{u'"," ").replace(", u'","^").replace("u'"," ").replace("'"," ")
        DATE = result['created_at'].encode('utf-8')
        TEXT = result['text'].encode('utf-8')
        ID = result['id']
        print "\""+str(TEXT) + "\""+ "^" +"\"" + str(DATE) + "\""+ "^" +"\"" + str(ID )+ "\""+ "^" +"\""
        #print "\"" + str(a)
        
        #screen = result['screen_name']
        #print result
        #print str(cnt) + "^"+ a
        #cnt = cnt+1
        #tweets.append(tweet_text)
        
    # STEP 3: Get the next max_id
    try:
        # Parse the data returned to get max_id to be passed in consequent call.
        next_results_url_params    = results['search_metadata']['next_results']
        next_max_id        = next_results_url_params.split('max_id=')[1].split('&')[0]
    except:
        # No more next pages
        break

print tweets
