import requests

def most_common_word_in_web_page(words, url):
 
    response = requests.get(url)
    return most_common_word(words, response.text)
    

def most_common_word(words, text):
   
    word_frequency = {w: text.count(w) for w in words}
    return sorted(words, key=word_frequency.get)[-1]


