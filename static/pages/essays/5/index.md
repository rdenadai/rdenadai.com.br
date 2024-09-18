Ok, first things first...

Python has over 80k packages, and I’m pretty sure there are plenty of them that I don’t know or fully understand. So, here’s a simple list of packages that I like and use frequently or occasionally.

---

####**[requests][1]**

if you are a python developer you must have used requests. It's a great package that exposes a simple api to connect and get http responses.
It is so good, that people say is a reference in how to build a api.

requests was almost merged into the core python, but due to more rapidly updates the requests team decided to not merge the project to core python.

<pre><code class="language-python">
import requests

r = requests.get('http://www.google.com.br')
if r.status_code == 200:
    print(r.text)
</code></pre>

####**[Pillow][2]**

Perhaps one of the few packages that people know that exists, but doesn't use a lot.
Pillow is a fork of the good (but old) PIL (Python Image Library) library. When PIL stop receiving updates some great members of the python community decided to fork the old lib and implement from that a new one with new features.
If you ever need to work with images... give Pillow a change, is very good at what it does.

<pre><code class="language-python">
from PIL import Image

im = Image.open("lena.ppm")
box = (100, 100, 400, 400)
# crop image
region = im.crop(box)
region.show()
</code></pre>

####**[cython][3]**

Lots of people complain about python performance. The Cython project could speed up your code with just a fewer modifications.
The point here is using cython to convert python code to C...

A great project, with a great usage widespread....

####**[nltk][4]**

This one of the few libs in python that i find very special, nltk stands for _Natural Language Toolkit_. A library to make Natural Processing in python very easy.
If you need to work with lots of texts, perhaps this library can help you.

<pre><code class="language-python">
import nltk

sentence = '''Just a simple frase to make words. Also check out the stopwords function in nltk'''
tokens = nltk.word_tokenize(sentence)
</code></pre>

####**[numpy][5]**

numpy is the most used library in python for science.
numpy is a very stable library and one of the python success. Without numpy and scipy, i guess python for data science wouldn't happen!

<pre><code class="language-python">
import numpy as np

zeros_matrix = np.zeros( (3, 4) )
</code></pre>

####**[scikit-learn][6]**

I think this is the best lib i ever seen... machine learning is a new hype in technology nowdays... and scikit-learn is the way to go here.
Install and use it... but keep in mind this is a hard field, but very, very interesting one.

####**[skyfield][7] | [astropy][8]**

Those two libs are to work with astronomy, since i enjoy astronomy a lot, those two comes in very handy from time to time.
You can use both to lots of things... i use to calculate position of planets and satellites, but there's lots more.

####**[django][9]**

Web development in python is very good, and frameworks like django (and flask) can provide a lot of ready to use things.
I find django orm very useful, and this blog is built entirely with django and a few bunch of plugins!

####**[boto][10]**

Amazon nowdays is almost like a must use feature, and to use amazon ec2 the boto library is the way to go. Simple and to the point, boto library can be very easily integrated into your software.

####**[jupyter][11]**

Just like numpy | scipy the ipython notebook took python to data science in a easy to use way. Most of data science are built around notebooks.
Its easy to develop a python application and docs... you could even share the notebook to others, and can run all python libs in it.
Damn, you can even run other languages like Julia!!!

---

So, if you didn't know all or some of the packages above, i hope that you go ahead and check them out, it will make you software skills go to a higger level.
And if you got the time, is good to study the internals of the libs to even contribute to them!

[1]: http://docs.python-requests.org/en/master/
[2]: https://python-pillow.org/
[3]: http://cython.org/
[4]: http://www.nltk.org/
[5]: http://www.numpy.org/
[6]: http://scikit-learn.org
[7]: http://rhodesmill.org/skyfield/
[8]: http://www.astropy.org/
[9]: https://www.djangoproject.com/
[10]: https://github.com/boto/boto3
[11]: https://ipython.org/
