import nltk
import string
import re
from nltk.stem import PorterStemmer
print("#REDUCE TO ORIGINAL ROOT#")
wd_stem=PorterStemmer()
print(wd_stem.stem("Eating"))
print("\n")
from nltk.corpus import stopwords
print("#TO REMOVE STOPWRODS#")
nltk.download("stopwords")
print(stopwords.words("English"))
print("\n")
print("#TO REMOVE WHITESPACE FROM TEXT#")
def remove_whitespace(text):
    return  " ".join(text.split())
input_str = "we   don't   need   the given   questions"
remove_whitespace(input_str)
print(input_str)
