import nltk
import string
from string import punctuation

from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
import newspaper
from newspaper import Article
import tkinter as tk
from tkinter import mainloop
import transformers
from transformers import pipeline


def summarize():
    url = utext.get('1.0', "end").strip()

    article = Article(url)

    article.download()
    article.parse()
    article.nlp()
    summary.config(state='normal')
    data = article.text
    nopunc = [word for word in data if word not in punctuation]
    nopunc = "".join(nopunc)

    process = pipeline('summarization')
    Summary = process(nopunc)

    summary.delete('1.0', 'end')
    summary.insert('1.0', Summary)

    summary.config(state='disabled')


root = tk.Tk()
root.title('Text Summarizer')
root.geometry('1400x800')

ulabel = tk.Label(root, text='Url')
ulabel.pack()

utext = tk.Text(root, height=2, width=150)
utext.pack()

btn = tk.Button(root, text='Summarize', command=summarize)
btn.pack()

slabel = tk.Label(root, text='Summary')
slabel.pack()

summary = tk.Text(root, height=20, width=150)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

root.mainloop()
