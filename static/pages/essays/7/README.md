# Review

![Cover A.I. a Guide for Thinking Humans][1]

> ©2020 Melanie Mitchell. All rights reserved.

Just like my previous review, i acquire the book from Amazon Audible and listen to the audiobook on my way to work every day. It took like 2 weeks 2 hours a day to listen to the entire book.

I tried as much as i can, drive and pay attention to what prof. Mitchell have to say about the past, the present and her personal view about the future of the A.I. field.

Different from the book written by prof. Russell, prof. Mitchell, focus her writing in present to us the modern way that the field of A.I. is going... it's strength and of course the weakness that the new models have. The book in this sense is more grounded in the present day and worry less about the possible superintelligence explotion and possibles ways that manking may need to realize how to deal with this "God Like" machines.

I really enjoy her way of telling the story and facts, and in the last 2 chapters prof. Mitchell exposes us to her thought about the way humans do their understanding of the world.

Like i did with prof. Russell book, here is a walk through the book chapters and my thoughts about it.

---

## Prologue

The prologue of the Audiobook version was narrated by prof. Mitchell itself, and show us the why she wrote the book. She explain that the book was born after from a meeting in Google that she and prof. Douglas Hofstadter participated, and in which prof. Hofstadter demonstrated a concern about how A.I. was able to imitate aspects of human kind the he was never thought it was possible.

"_Music is a language of emotions, and until programs have emotions as complex as ours, there is no way a program will write anything beautiful. [...]
The idea that pattern manipulation of the most superficial sort can yield things that sound as if they are coming from a human being’s heart is very, very troubling. I was just completely thrown by this._" Douglas Hofstadter

Taking this into account and of course the whole new A.I. spring that's happening right now, prof. Mitchell (as state above) presents the reason of why writing the book.

"_This book arose from my attempt to understand the true state of affairs in artificial intelligence, what computers can do now, and what we can expect from them over the next decades._"

## The Roots of Artificial Intelligence

This is a very good chapter for the new people entering in the field of AI and a good recall for those who are already living in the field for quite some time.

The chapter tells the history of the field explaining what's is **[Symbolic AI][2]** (nowdays know as **GOFAI** [Good Old Fashion AI]) and **Subsymbolic AI** (the original **[Perceptron][3]**, create by Frank Rosenblatt)

She end this chapter with the most important thing to keep in mind when working with computers and of course AI: **Easy Things Are Hard**.

"_The original goals of AI [..] are things that young children can easily do, but, surprisingly, these "easy things" have turned out to be harder for AI to achieve than diagnosing complex diseases, beating human champions at chess and Go, and solving complex algebraic problems._"

## Neural Networks and AI Spring

The following chapters prof. Mitchell exposes and explain how Neural Networks work (not in technical detail, but as a general guide) and the early days. Those NN are now called Vanilla NN (for some people) because of the different types of layers that we have nowdays.

After the explanation, she then tells about the new AI Spring that is happening after the early 2000s (with Kasparov losing the in game of Chess against Deep Blue), and the so proclaimed book **[The Singularity is Near][4]** by Ray Kurzweil relesead in 2005.

"_I set the date for the Singularity … as 2045. The nonbiological intelligence created in that year will be one billion times more powerful than all human intelligence today._" Ray Kurzweil

## Computer Vision Revolution

After some explanation about Neural Networks and exposing some future ideas from others researchers, prof. Mitchell turns her attention to the "revolution" that happened in Computer Vision, which in turn made Neural Networks get a new breath of air.

The first chapter (Chapter 4), prof. Mitchell explains how Convolution Neural Networks works (ConvNets for short), given a short of review history of how all of this start.

"_Like neurons in the visual cortex, the units in a ConvNet act as detectors for important visual features, each unit looking for its designated feature in a specific part of the visual field. And (very roughly) like the visual cortex, each layer in a ConvNet consists of several grids of these units, with each grid forming an activation map for a specific visual feature._"

In the following one (Chapter 5) the reader are presented with **[ImageNet][5]**, create by prof. Fei-Fei Li and other contributors from Princeton.

Thanks to ImageNet, ConvNets show their true power and won the competition multiple times, each time closing the gap between human and machine accuracy. Taking to the point where the error rate of the machines is lower then human.

But, looking more closely, prof. Mitchell makes us aware that even though machines have reach this "superhuman level" in object recognition, they in fact don't understand what is happening in the scene and even truly don't understand the meaning of the things, actions that's in the image.

"_Here’s another caveat. Consider the claim, "Humans have an error rate of about 5% on ImageNet." It turns out that saying "humans" is not quite accurate; this result is from an experiment involving a single human, one Andrej Karpathy, who was at the time a graduate student at Stanford, researching deep learning._"

Exploring more the so called "Machine Learning" term, the Chapter 6, she dive in showing us what means learning in term of ConvNets. One important aspect describe in this Chapter is the named "**[Long-Tail][6]**" in Distributions, which represents some small percentage of probabilities of things (or objects / situations) that may happen, but have very little change. But this turns out to influence corner cases that the machine learning models may never be able to make correct assumptions because are parts of the distribution that are to hard to have examples and train the network for good predictions.

![Long Tail Distribution example][7]

Prof. Mitchell also exemplify this learning with a study made when training a ConvNet to classify image and non images with animals.

"_... By performing a careful study, Will found an unexpected answer: in part, the network learned to classify images with blurry backgrounds as "contains an animal", whether or not the image actually contained an animal. The nature photos in the training and test sets obeyed an important rule of photography: focus on the subject of the photo. When the subject of the photo is an animal, the animal is the focus and the background is blurred,_"

This demonstrated that what we think as important in images may not be what a Neural Network also may find important. So the learning process is different from our own.

Others things discussed in this chapter are bias in those networks and how to fool them (im not discuss this here, this by itself deserves a blog post, or even a book). Just to make the reader aware (if you are not), fooling algorithms is a science in itself, but as more and more systems are put in production and permeate our lives, fooling them may cause very unpleasant surprises.

## Reinforcement Learning and Games

Through chapter 7 to 10, prof. Mitchell explains and demonstrate us the evolution of Reinforcement Learning through the use of Neural Networks, something that came to be called "_[Deep Reinforcement Learning][8]_" with Deep Q-Learning (_DQN_) being the first merge between Neural Nets and the "**[Q-Learning][9]**" algorithm.

I myself tested one variation of DQN applying into the snake game, you could check out the **[github repository][10]**, and bellow is a gif of the game played by the algorithm after a long time of training.

![Snake Game][11]

One problem presented in those chapters is "**Transfer Learning**", which is an hot and active are of study in Deep Learning. Actually, transfer learning is most important to AI field. A way to transfer what an agent learn from a specific domain to another, much the same way we humans do. We learn something and part of that learn may be shared to improve our learning rate in a different domain, or a slightly different domain from the original one.

"_Humans exhibit this kind of transfer from one task to another seemingly effortlessly; our ability to generalize what we learn is a core part of what it means for us to think. Thus, in human-speak, we might say that another term for transfer learning is, well, learning.
In stark contrast with humans, most "learning" in current-day AI is not transferable between related tasks._"

## Natural Language Processing and Chatbos

At the same pace, prof. Mitchell holds 3 chapters to talk about another important domain in AI, the field of Natural Language Processing.

The hot topics in this area (at least whats is describe in the book) are **Recurrent Neural Networks** (with **[LSTM][12]** being the most important aspect) and word embeddings (or a word vector space) with **[Word2Vec][13]** being the most important algorithm. Nowdays a new architecture dominate most of state-of-art in NLP, the Transformers. Prof. Mitchell didn't mention this, but as in 2020 these models (like the famouse **BERT** and **GPT-2**) are the state-of-art.

One special thing to notice about word vectors is said by prof. Mitchell:

"_... Several groups have shown that these word vectors, perhaps unsurprisingly, capture the biases inherent in the language data that produces them._"

Yes, this is a very important thing to notice, machine learning models extract patterns that exist in the data. As we saw previous, when working with images (finding that blur images have animals) or with text, biases of our society will appear in your model, even indirectly, so this means that before put a model in production you and the company you work must be aware that this could happen!

In those chapters, prof. Mitchell also talks about Encoder-Decoder architecture, used to do machine translation between languages, and tells the story of Watson winning the Jeopardy Game in 2011, at the time a great milestone for the AI field, but a bigger one for IBM and its shareholders.

As much as she talk about NLP and related subjects, the Turing Test was touched and explain earlier on the book, in the chapter where the history of the field was told.

## The Barrier of Meaning

The whole book is great in explain most of the fields struggles and advances in recently years, but the last 2 chapters (14 and 15) in my humble opinion are what this book stands for. I mean, don't get me wrong, is good to get an ideia or even a refresh about the AI field, but as a practitioner and possible future research (i'm trying to enter in master degree and who knows about the future, even a PhD) those chapters contains valuable insights and prof. Mitchell vision of what means to be a human and the way our brains works.

"_These core bodies of intuitive knowledge constitute the foundation for human cognitive development, underpinning all aspects of learning and thinking, such as our ability to learn new concepts from only a few examples, to generalize these concepts, and to quickly make sense of situations [...] and decide what actions we should take in response._"

Those core bodies refer above are:

- Intuitive physics: Understand the world around us and how to interact with it.
- Intuitive biology: Understand other living beings and how to interact with them.
- Intuitive psychology: Understand other human beings and how to interact with them.

This leaves prof. Mitchell to build a ideia propose by Lawrence Barsalou of "_[Understanding as Simulation][14]_".

"_In his view, our understanding of the situations we encounter consists in our (subconsciously) performing these kinds of mental simulations. Moreover, Barsalou has proposed that such mental simulations likewise underlie our understanding of situations that we don't directly participate in - that is, situations we might watch, hear, or read about._"

Following those intuitions, prof. Mitchell exposes us to ideas from Metaphors, Abstraction and Analogy.

In the final chapter she presents the reader with the Bongard problem, and how hard are this for machines, because of lack of truth understand and analogy.

"_The modern age of artificial intelligence is dominated by deep learning, with its triumvirate of deep neural networks, big data, and ultrafast computers. However, in the quest for robust and general intelligence, deep learning may be hitting a wall: the all-important "barrier of meaning."_"

## Conclusion

I really enjoy listen to this book, its well written and narrated. By the end you feel that you truly understand better the AI field and it's future struggles.

As other books, this is one is not too technical that you could listen to it, i some parts i think it make senses to have the physical copy by your side, or check the companion pdf with the audiobook, specially if you ever heard about most of the topics found in the book.

To **buy** the book or the **Audible** version:

[Artificial Intelligence: A Guide for Thinking Humans][15]

Thanks

[1]: /static/pages/essays/7/ai_guide_for_thinking_humans.jpg
[2]: https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence
[3]: https://en.wikipedia.org/wiki/Perceptron
[4]: https://www.amazon.com/Singularity-Near-Humans-Transcend-Biology/dp/0670033847/ref=tmm_hrd_swatch_0?_encoding=UTF8&qid=1582395470&sr=8-1
[5]: http://www.image-net.org/
[6]: https://en.wikipedia.org/wiki/Long_tail
[7]: /static/pages/essays/7/long_tail.png
[8]: https://en.wikipedia.org/wiki/Deep_reinforcement_learning
[9]: https://en.wikipedia.org/wiki/Q-learning
[10]: https://github.com/rdenadai/snakeplissken
[11]: https://raw.githubusercontent.com/rdenadai/snakeplissken/master/img/snake3.gif
[12]: https://en.wikipedia.org/wiki/Long_short-term_memory
[13]: https://en.wikipedia.org/wiki/Word2vec
[14]: https://royalsocietypublishing.org/doi/full/10.1098/rstb.2008.0319
[15]: http://%20https://www.amazon.com/Artificial-Intelligence-Guide-Thinking-Humans-ebook/dp/B07MYWPQSK/ref=tmm_kin_swatch_0?_encoding=UTF8&qid=1582570495&sr=8-1
