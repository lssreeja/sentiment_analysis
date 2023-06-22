import string
from collections import Counter
import os
import random
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
def perform_sentiment_analysis():
    file_path = os.path.join(os.getcwd(), 'read.txt')
    text = open(file_path, encoding='utf-8').read()
    lower_case = text.lower()
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

    # Using word_tokenize because it's faster than split()
    tokenized_words = word_tokenize(cleaned_text, "english")

    # Removing Stop Words
    final_words = []
    for word in tokenized_words:
        if word not in stopwords.words('english'):
            final_words.append(word)

    # Lemmatization - From plural to single + Base form of a word (example better-> good)
    lemma_words = []
    for word in final_words:
        word = WordNetLemmatizer().lemmatize(word)
        lemma_words.append(word)

    emotion_list = []
    file_pat = os.path.join(os.getcwd(), 'emotions.txt')
    with open(file_pat, 'r') as file:
        for line in file:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in lemma_words:
                emotion_list.append(emotion)

    print(emotion_list)
    w = Counter(emotion_list)
    print(w)
    n = len(w)
    colors = [
         'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanchedalmond',
        'blue',
        'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue',
        'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki',
        'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen',
        'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue',
        'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro',
        'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo',
        'khaki', 'lavender',  'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral',
         'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen',
        'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen',
        'linen',
        'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen',
        'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue',
        'mistyrose', 'moccasin', 'navajowhite', 'navy', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered',
        'orchid',
        'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred',  'peachpuff', 'peru', 'pink',
        'plum',
        'powderblue', 'purple', 'rebeccapurple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown',
        'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow',
        'springgreen',
        'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat',
        'yellow',
        'yellowgreen'
    ]
    colorlist=[]
    for i in range(n):
        ind = int(random.random()*(len(colors)))
        colorlist.append(colors[ind])

    def sentiment_analyse(sentiment_text):
        score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
        if score['neg'] > score['pos']:
            print("Negative Sentiment")
        elif score['neg'] < score['pos']:
            print("Positive Sentiment")
        else:
            print("Neutral Sentiment")


    sentiment_analyse(cleaned_text)

    fig, ax1 = plt.subplots()
    ax1.bar(w.keys(), w.values(), color=colorlist)
    print(colorlist)
    fig.autofmt_xdate()
    plt.savefig('static/graph.png')
    # plt.show()

if __name__ == '__main__':
    perform_sentiment_analysis()
    # print(sentiment_result)