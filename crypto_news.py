from newsapi import NewsApiClient


def news():
    newsapi = NewsApiClient(api_key='YOUR_API_KEY')
    # all_articles = newsapi.get_everything(q='bitcoin',
    #                                     sources='bbc-news,the-verge',
    #                                    domains='bbc.co.uk,techcrunch.com',
    #                                      from_param='2022-11-23',
    #                                     to='2022-11-24',
    #                                      language='en',
    #                                     sort_by='relevancy',
    #                                      )

    top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                              category='business',
                                              language='en',
                                              country='us')

    top_headlines_data = top_headlines["articles"]
    three_articles = top_headlines_data[:3]

    formatted_articles = [
        f"Name: {article['source']['name']} \nAuthor: {article['author']}  \nHeadline: {article['title']}. \nBrief: {article['description']} \nURL: {article['url']}. \nPublished At: {article['publishedAt']}"
        for article in three_articles]

    last_articles = f"{formatted_articles[0]} \n\n{formatted_articles[1]} \n\n{formatted_articles[2]}"
    return last_articles
