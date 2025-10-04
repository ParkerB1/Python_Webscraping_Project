import requests 
from bs4 import BeautifulSoup 
import nltk 
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist 
import string

nltk.download('punkt')
nltk.download('punkt_tab')


url = 'https://www.gutenberg.org/files/16/16-h/16-h.htm' #Peter Pan
url_md = 'https://www.gutenberg.org/cache/epub/2701/pg2701-images.html' #Moby Dick
r = requests.get(url)
r_md = requests.get(url_md)
r.encoding = 'utf-8'
r_md.encoding = 'utf-8'

soup = BeautifulSoup(r.text, "html.parser")
text = soup.text

soup_md = BeautifulSoup(r_md.text, "html.parser")
text_md = soup_md.text

#CHANGE THIS CODE\/

start_line_pp = "*** START OF THE PROJECT GUTENBERG EBOOK PETER PAN ***" #Must change title("PETER PAN") if using different book
end_line_pp = "*** END OF THE PROJECT GUTENBERG EBOOK PETER PAN ***" #Must change title("PETER PAN") if using different book
start_pp = text.find(start_line_pp) + len(start_line_pp)
end_pp = text.find(end_line_pp)
book_text_pp = text[start_pp:end_pp].strip()

start_line_md = "*** START OF THE PROJECT GUTENBERG EBOOK MOBY DICK; OR, THE WHALE ***"
end_line_md = "*** END OF THE PROJECT GUTENBERG EBOOK MOBY DICK; OR, THE WHALE ***"
start_md = text.find(start_line_md) + len(start_line_md)
end_md = text.find(end_line_md)
book_text_md = text_md[start_md:end_md].strip()

#tokenizes each sentence and word in the text
sentences_pp = sent_tokenize(book_text_pp)
words_pp = word_tokenize(book_text_pp)

sentences_md = sent_tokenize(book_text_md)
words_md = word_tokenize(book_text_md)

#Removes punctuation and lowercases all alpabetic words
words_clean_pp = [
    word.lower() for word in words_pp
        if word.isalpha()
                ]

words_clean_md = [
    word.lower() for word in words_md
        if word.isalpha()
                ]

freq_dist_pp = FreqDist(words_clean_pp)
freq_dist_md = FreqDist(words_clean_md)

print(f"\n\nSentence count\nPeter Pan: {len(sentences_pp)}\nMoby Dick: {len(sentences_md)}\n")
print(f"Word count\nPeter Pan: {len(words_pp)}\nMoby Dick: {len(words_md)}\n")
print(f"Top 10 most common words\nPeter Pan: {freq_dist_pp.most_common(10)}\nMoby Dick: {freq_dist_md.most_common(10)}")

#CHANGE THIS CODE/\