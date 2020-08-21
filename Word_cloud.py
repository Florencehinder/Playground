#Word could created for books I am reviewing
from wordcloud import WordCloud, STOPWORDS # import package and its set of stopwords
from bs4 import BeautifulSoup
import ebooklib
from ebooklib import epub
import matplotlib.pyplot as plt

epub_path = 'C:\\PycharmProjects\\Playground\\Le deuxieme sexe.epub'

#words that I want to be removed from the count
added_stopwords = ('\n','de', 'le', 'la', 'les', 'et', 'il', 'des', 'se','ne', 'une','est','elle','au','ce','lui','ont',
                   'ou','aussi','son', 'du',"d'une", 'celle', 'cette', 'sa', 'avec', 'si', 'dit', 'non', "d'un", 'ses',
                   'dans', 'comme', 'en', "qu'une", 'pas', "n'est", 'san', 'aux', 'sur','sont', 'que', 'peut', 'plus',
                   'par', 'nous', 'qui', 'pour', "qu'il", 'ils fait', 'leur', 'ainsi', 'quand', "qu'il", "qu'elle",
                   'elles', 'dont','tout', 'un', 'ces', 'sans', 'ni', 'est', 'mai', "qu'on","tant", 'ils', "c'est",
                   'toute', "fait", 'mais', 'leurs','ou','celui','la', 'bien',"l'homme", "où", 'soit', 'être', 'parce',
                   'je', 'autre','cependant', 'contre', 'souvent', 'toutes', 'même', "n'a", 'chez', 'tous', 'moins',
                   'encore', 'alors', 'beaucoup', 'seulement', 'jamais', 'donc', 'autre', 'là', "d'autres", "qu'elles",
                   "s'est", "l'autre", "s'il", 'femme', 'homme', 'femmes', 'hommes', 'toujours', 'vie', 'faire', 'deux',
                   'été'

                   )

blocklist = [   '[document]',   'noscript', 'header',   'html', 'meta', 'head','input', 'script', ]
# there may be more elements you don't want, such as "style", etc.

def epub2thtml(epub_path):
    book = epub.read_epub(epub_path)
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    return chapters

def chap2text(chap):
    output = ''
    soup = BeautifulSoup(chap, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blocklist:
            output += '{} '.format(t)
    return output

def thtml2ttext(thtml):
    Output = []
    for html in thtml:
        text =  chap2text(html)
        Output.append(text)
    return Output

def epub2text(epub_path):
    chapters = epub2thtml(epub_path)
    ttext = thtml2ttext(chapters)
    return ttext

out=epub2text(epub_path)
deuxieme_novel = out

with open('your_file.txt', 'w') as f:
    for item in out:
        f.write("%s\n" % item)

# open the file and read it into a variable alice_novel
deuxieme_novel = open('your_file.txt', 'r').read()

stopwords = set(STOPWORDS)
for i in added_stopwords:
    stopwords.add(i) # add the words said to stopwords

# instantiate a word cloud object
deuxieme_wc = WordCloud(
    background_color='white',
    max_words=2000,
    stopwords=stopwords
)

# generate the word cloud
deuxieme_wc.generate(deuxieme_novel)

fig = plt.figure()
fig.set_figwidth(14) # set width
fig.set_figheight(18) # set height

# display the cloud
plt.imshow(deuxieme_wc, interpolation='bilinear')
plt.axis('off')
plt.show()
