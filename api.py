import nlpcloud


# def ner(text):
#         para = input('Enter the paragraph: ')
#         search_term = input('What do you like to search? ')


#         client = nlpcloud.Client("finetuned-gpt-neox-20b", "fdb150394173113fe99b5609a9f806bdab084fa2", gpu=True, lang="en")
#         response = client.entities(para, searched_entity=search_term)
#         print(response)

# obj = ner('my favourite programming language is python')

def sentiment_analysis(text):
    client = nlpcloud.Client("distilbert-base-uncased-emotion", "fdb150394173113fe99b5609a9f806bdab084fa2", gpu=False)
    client.sentiment(
        """Look what's just come on the market in #ValThorens! A recently renovated, charming 6 bed duplex apartment in the heart of the resort with superb views!"""
    )
    return client