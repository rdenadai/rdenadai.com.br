In my current job, we are building a Data Dictionary System, and one key requirement is to ensure that the names of tables and attributes maintain a certain level of consistency and correctness.

The Data Administration (D.A.) team already has a glossary in place, but they don’t fully trust it, and with good reason, since there are duplicated terms and conflicting definitions.

In a discussion with my manager, I suggested building a new glossary using words from our language (Portuguese, as we are based in Brazil) and creating a set of rules to guide this process.

We came up with a simple rule:

- Terms should have a maximum of 4 letters;
- Words with more than 4 letters should be truncated to the first 4;
- Words with fewer than 4 letters should be used in full;

During the discussion, it was proposed that if a 4-letter term already exists, we should take the next letter from the word and create a new term. This sounds logical, but it can lead to some strange outcomes, especially when dealing with common words versus less familiar ones.

> Im putting a translation here

> DESCER => come down

> DESCRICAO => Description

**DESCER
DESCRICAO**

Notice that the first 4 letters of both words are **DESC**! "Description" is much more commonly used in tech than "come down." To solve this issue, we could use the `FreqDist` object from the NLTK library.

Here’s my implementation:

```python
from unicodedata import normalize
from collections import defaultdict
import logging
import codecs
import nltk
import requests
from bs4 import BeautifulSoup
import json

dicionario = set()
palavras = nltk.FreqDist()

stopwords = nltk.corpus.stopwords.words('portuguese') + nltk.corpus.stopwords.words()
names = nltk.corpus.names.words()
names = [name.lower() for name in names]
stopwords = stopwords + names

def remover_non_alpha(text):
    """Remove all non alpha chars from our text"""
    text = ''.join([i for i in text if not i.isdigit()])
    text = ''.join(c for c in text if c.isalnum())
    return text

def remover_acentos(txt, codif='utf-8'):
    """Remove all accent from our text"""
    return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')

def import_machado_words():
    """Import a FreqDist of all words (except stopwords) that exist in machado work"""
    machado_obras = nltk.corpus.machado.fileids()
    machado_texto = nltk.FreqDist()
    for i, text in enumerate(machado_obras):
        machado_texto += nltk.FreqDist(nltk.corpus.machado.words(machado_obras[i]))
    machado_texto = nltk.FreqDist(w.lower() for w in machado_texto if w not in stopwords)
    return machado_texto

def import_macmorpho_words():
    """Same as above, but for MacMorpho set"""
    return nltk.FreqDist(w.lower() for w in nltk.corpus.mac_morpho.words() if w not in stopwords)

def import_floresta_words():
    """Same as above, but for Floresta set"""
    return nltk.FreqDist(w.lower() for w in nltk.corpus.floresta.words() if w not in stopwords)

def generate_word_list(filename):
    """Given a file, lets import all words in it and return a set"""
    palavras = set()
    with codecs.open(filename, 'r', 'utf-8') as dic:
        for word in dic:
            index = len(word)
            if '/' in word:
                index = word.index('/')
            if '-' not in word:
                word = word[:index].replace('\n', '').lower()
                palavras.add(word)
    return palavras

def generate_text(url):
    """Given a url, lets import all words (except stopwords) in it and return a FreqDist"""
    try:
        r = requests.get(url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'lxml')
            raw = soup.find('body').get_text().lower().replace('.', '')
            words = sorted(raw.split())
            words = nltk.FreqDist(remover_non_alpha(w.lower()) for w in words if w not in stopwords)
            return words
        return nltk.FreqDist()
    except:
        logging.info("Erro ao carregar url %s " % (url))

def run(dicionario, palavras):
    for pal in dicionario:
        if pal in palavras and len(pal) > 2:
            yield {remover_acentos(pal.encode('utf-8')): (pal, palavras[pal])}

def varre_final_dict(key, final_dic):
    return True if key in final_dic.keys() else False

def get_valid_glossary(key, final_dic):
    # Get the term from the key
    sort_key = key[0:4]
    return sort_key

if __name__ == '__main__':
    # Import all words from these 2 files
    # http://www.nltk.org/howto/portuguese_en.html
    dicionario |= generate_word_list('pt-BR.dic')
    dicionario |= generate_word_list('palavras.txt')
    dicionario = set(w.lower() for w in dicionario if w not in stopwords)

    # DONWLOAD CORPORA
    palavras += import_machado_words()
    print('MACHADO DOWNLOADED!!')
    palavras += import_macmorpho_words()
    print('MACMORPHO DOWNLOADED!!')
    palavras += import_floresta_words()
    print('FLORESTA DOWNLOADED!!')

    # DOWNLOAD HTML

    # IDG NOW
    palavras += generate_text('http://idgnow.com.br/ti-corporativa/2016/03/30/conheca-os-10-empregos-de-ti-que-terao-aumento-de-salario-acima-da-media/')
    palavras += generate_text('http://idgnow.com.br/ti-corporativa/2016/03/29/computador-watson-da-ibm-ja-e-capaz-de-detectar-emocoes-humanas/')
    palavras += generate_text('http://idgnow.com.br/ti-corporativa/2016/03/31/setor-de-ti-cobra-apuracao-de-fatos-no-cenario-politico-nacional/')
    palavras += generate_text('http://idgnow.com.br/ti-corporativa/2016/03/29/ti-bimodal-nuvem-e-infraestrutura-fisica-como-prosperar-nesse-cenario-convergente/?utm_source=idgnow2&utm_medium=site&utm_campaign=TI+Bimodal%2C+nuvem+e+infraestrutura+f%EDsica%3A+como+prosperar+nesse+cen%E1rio+convergente+&utm_content=viewletMaisLidas')
    print('IDG NOW DOWNLOADED!!')

    # WIKIPEDIA
    palavras += generate_text('https://pt.wikiversity.org/wiki/Introdu%C3%A7%C3%A3o_%C3%A0_L%C3%B3gica_Matem%C3%A1tica')
    palavras += generate_text('https://pt.wikiversity.org/wiki/Introdu%C3%A7%C3%A3o_%C3%A0_L%C3%B3gica_de_Programa%C3%A7%C3%A3o')
    palavras += generate_text('https://pt.wikiversity.org/wiki/Introdu%C3%A7%C3%A3o_%C3%A0_Arquitetura_de_Computadores') palavras += generate_text('https://pt.wikiversity.org/wiki/Introdu%C3%A7%C3%A3o_%C3%A0s_Linguagens_Formais_e_Aut%C3%B4matos')
    palavras += generate_text('https://pt.wikiversity.org/wiki/Introdu%C3%A7%C3%A3o_%C3%A0_Teoria_dos_Compiladores/Defini%C3%A7%C3%B5es')
    palavras += generate_text('https://pt.wikiversity.org/wiki/Introdu%C3%A7%C3%A3o_%C3%A0_Teoria_dos_Compiladores/Teoria_das_Linguagens_Formais')
    palavras += generate_text('https://pt.wikiversity.org/wiki/Introdu%C3%A7%C3%A3o_%C3%A0_Teoria_dos_Compiladores/Linguagens_Regulares_e_Aut%C3%B4matos_Finitos')
    palavras += generate_text('https://pt.wikiversity.org/wiki/Introdu%C3%A7%C3%A3o_%C3%A0_Teoria_dos_Compiladores/Linguagens_Livres_de_Contexto')
    palavras += generate_text('https://pt.wikiversity.org/wiki/Introdu%C3%A7%C3%A3o_%C3%A0_Teoria_dos_Compiladores/An%C3%A1lise_Sint%C3%A1tica')
    print('WIKIPEDIA DOWNLOADED!!')

    # http://www.dca.fee.unicamp.br/cursos/EA876/apostila/HTML/node1.html
    for i in xrange(0, 100):
        palavras += generate_text('http://www.dca.fee.unicamp.br/cursos/EA876/apostila/HTML/node%s.html' % (str(i)))
    print('DCA UNICAMP DOWNLOADED!!')

    # Generate a list with all words that appears in the FreqDist set
    new_dict = list(run(dicionario, palavras))
    new_dict.sort(key = lambda s: s.keys()[0]) # sorts normally by alphabetical order
    new_dict.sort(key = lambda s: s.values()[0][1], reverse=True) # sorts by freq
    new_dict.sort(key = lambda s: len(s.keys()[0]), reverse=False) # sorts by descending length

    final_dic = dict()
    # For each word in the dict
    for w in new_dict[0:2000]:
        value = w.values()[0]
        # Get a word, to generate a future term
        key = remover_acentos(value[0].encode('utf-8'))
        # Check if this word term already exists in the final dict
        key = get_valid_glossary(key, final_dic)
        value = w.values()[0]
        # If we could not generate a new term, well we must compact the words that represents this term together
        if key in final_dic.keys():
            if not final_dic[key]:
                final_dic[key] = []
        else:
            final_dic[key] = []
        final_dic[key] += [({'palavra': value[0], 'freq': value[1]})]

    final_dic = sorted(final_dic.items(), key=lambda x: x[1][0].values()[1], reverse=True)
    # Generate a json file with all terms and words!
    with open('palavras.json', 'wb') as js:
        js.write(json.dumps(final_dic))
```

In the code above im not doing the complex part mentioned above, im just returning the 4 first letters of a word and done, new term created.
In next weeks i'll improve the script above making it more like a class base or ready to use app on heroku.
