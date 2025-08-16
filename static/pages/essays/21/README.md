This is my take on what to expect for 2025. Keep in mind that this is my personal opinion, based on possibilities and trends that I’ve been following closely (or lately). Let’s dive into some of the key areas I believe will shape the tech landscape next year.

<audio controls>
    <source src="/static/pages/essays/21/notebookllm.mp3" type="audio/mpeg">
    <source src="/static/pages/essays/21/notebookllm.ogg" type="audio/ogg">
    Your browser does not support the audio element.
</audio>

### 1. Rust and Go languages continue their Rise

I think this is a great example of two languages that are gaining popularity over the years. Both Rust and Go were created about 10-15 years ago (I'm using their 1.0 versions as a reference: Rust in 2015 [v1.0] and Go in 2012 [v1.0]), but in recent years their popularity has grown a lot. I think this is because people are looking for better approaches to solve problems, driven by curiosity, and/or to study new languages.

I don't think I can say that both languages were created to overcome the problems of other languages (yes, I'm talking about C and C++). They were developed around the same time, and both languages fit into that space.

I'm seeing more and more adoption of both languages in the industry: Rust in more systems and critical applications (we saw Rust entering in parts of the Linux Kernel), while Go's penetration is greater in cloud and backend applications (given the success of k8s, which is a highly successful tool written in Go).

My bet here is that both will continue to grow in 2025, and we'll probably see more and more companies adopt Go as their main language for backend development, replacing JavaScript / TypeScript, and even Java. That said, I think we'll see a major surge in Go's popularity in 2025.

![Tiobe Index 12/2024](/static/pages/essays/21/image.png)

As I'm writing this, Go has climbed from position 13 to 7 in just one year. I would attribute this rise in popularity especially to the language's ease of use and performance. Since I'm not a Go developer, I'm not familiar with the frameworks and libraries used to implement large enterprise applications, but it appears that this is the direction Go is heading. This means that well-established languages like Java (and, in recent years, JavaScript/TypeScript) will probably lose some market share.

As for Rust, I think the path is much clearer, and Rust does one thing that most developers want: replace C++ and maybe even C (it's possible, I mean). Anyway, we're still going to watch that rise in popularity (on TIOBE, Go's jump from last year was more impressive), and Rust will spread across more domains.

For Rust, I would like to see more adoption in web development and machine learning (this would definitely help the language grow). I think the slow rate of adoption is directly related to how hard it is to learn the language, especially for new developers.

> **_My Take: If you're starting in the area, choose Go. You'll probably find more job opportunities in backend development. But keep in mind that this is about doing what I'm telling you to do, not what I'm doing. I’m more leaning towards Rust._**

**LinkedIn stats:**

| Go in Brazil | Rust in Brazil |
| ------------ | -------------- |
| 3,002        | 1,373          |

### 2. Python 3.14: JIT and Free-Threaded Improvements

- [Making the Global Interpreter Lock Optional in CPython](https://peps.python.org/pep-0703/)
- [JIT Compilation](https://peps.python.org/pep-0744/)

For the most of the entire lifetime one of the main complaints I've heard people mention about Python is that it's slow because of the GIL.

This is a misconception that's deeply rooted in Python, and we will probably hold on to this idea for a few more years.

However, things have changed in recent years (lots of companies have shown interest in making Python faster, investing money and personal hours to accomplish this), and since Python 3.14, it has taken a totally new direction. This is the first Python release where you can use CPython (for those who are not aware, Python is the language, and CPython is the main interpreter or language implementation) without the GIL and with a Just-In-Time (JIT) compiler.

Ok, before you get too excited (or start criticizing too much, because Python this and that), keep in mind that this is all "experimental" (yes, it's shipped with the main interpreter, but it's disabled by default).

If everything goes well, this could mark the beginning of a major change for the main language interpreter. This doesn't mean that Python will become faster than any compiled language (as far as I know, this is probably impossible), but it definitely opens new possibilities in areas that could benefit from it, like web servers (such as Gunicorn, Uvicorn, and others) and in AI/ML (like scikit-learn).

We will probably start to see some real improvements in Python 3.15 (which releases in October 2025), but in the next few months, we might see some libraries experimenting with free-threading (and maybe the JIT).

Hopefully, everything will go smoothly... as for the free-threading part, there is a disclaimer about it.

"_**The Steering Council accepts PEP 703, but with clear proviso: that the rollout be gradual and break as little as possible, and that we can roll back any changes that turn out to be too disruptive – which includes potentially rolling back all of PEP 703 entirely if necessary (however unlikely or undesirable we expect that to be).**_"

> **_My Take: We will see some libraries starting to use free-threaded builds to improve performance, especially on the web platform. Python 3.15 will bring greater performance improvements, given the work done around the JIT (let's not forget the previous work that has been done since 3.11)._**

### 3. Quantum Computing

I have mixed feelings about this, but it's probably worth saying a few words about it.

Recently, Google announced it's new Quantum Computing chip [Willow](https://blog.google/technology/research/google-willow-quantum-chip/), and a couple of weeks later, China announced it's powerful chip [Zuchongzhi 3.0](https://arxiv.org/html/2412.11924v1).

I'm not sure if there's a real race here, but it seems that China is really invested in this (or at least that's what the news appears to indicate).

We will probably see some more scarce news in 2025, and maybe some people will be shocked and start saying the mantra that Quantum Computing is near!

> **_My Take: Please don't get fooled..._**

### 4. Generative AI: Evolving and Expanding

Now, the part you'll see in every post, video, or media about the trend for 2025: Generative AI.

As much as I really enjoy AI getting better and being able to use it in my daily work and life, I think the hype was too big in 2023. I do think that we’ve settled down a little bit this year, and even the latest release from OpenAI was not enough to hype people that much (I mean, for AGI expectations and such).

I consider myself both a critic and a lover of AI (and I’m referring here to the field, not specifically to Generative AI), and [I wrote a blog post last year about some of the things I was looking for in 2024](https://www.rdenadai.com.br/essay/generative-ai-and-the-near-future-humanity) (if you want to see how good or bad I am at predicting the future, take a look at that).

One of the things I mentioned I was hoping for was better audio models (text-to-speech and vice versa) and the probable hype we would see this year (text-to-video).

So, in the next sections, I will discuss (a little bit) what I’m expecting for 2025.

#### 3.1. The Text-to-Video Revolution

Looks like my hype expectations from last year about Text-to-Video were not 100% accurate. We did see improvements in video, and the release of [**Sora**](https://openai.com/sora/) in December might hype that kind of media (I'm really not sure this is going to be as impactful as image or audio, but anyway, it's a good milestone).

Maybe, just maybe, this will hit an all-time high in hype in 2025 with other companies release more models. [Google](https://deepmind.google/technologies/veo/veo-2/) and [Meta](https://ai.meta.com/blog/generative-ai-text-to-video/) have their models, so let's see how this evolves.

#### 3.2. Better Agents for Full Code Generation Tasks

There's much controversy about this topic, especially in the IT community. I understand both sides: on one hand, companies want to sell their products to replace developers, and on the other hand, developers are critically watching companies, saying that developers will be replaced by AIs.

I think the only agent that has really hit the news was **Devin**, which promises to change the way we produce code. It took several months from the initial release to an actual use case to confirm that Devin might be useful (and the use case is HUGE!!! ... [How Nubank refactors millions of lines of code to improve engineering efficiency with Devin](https://devin.ai/customers/nubank)).

Maybe this is a trend for this year, improvements in Github Copilot also land recently and a [free version](https://github.blog/news-insights/product-news/github-copilot-in-vscode-free/) was release.

So over the next year, more and more people will use LLMs to automatically perform simple development tasks. Copyright could also become a problem in this field, and only time will tell if this will impact code generation. But for now, nothing too crazy has hit the news.

#### 3.3. Audio Generation: A Slow Climb

This was definitely in line with my expectations for 2023, and we did receive better models (not open ones, at least) from OpenAI ([OpenAI released its advanced voice mode to more people.](https://www.technologyreview.com/2024/09/24/1104422/openai-released-its-advanced-voice-mode-to-more-people-heres-how-to-get-it/)). What they presented was really in the direction I was expecting last year, and if you check my blog post, you'll see that I link better audio models with 3D models like Make Human.

One thing that really caught my attention was [NotebookLLM](https://notebooklm.google/)... just wow!! This was an incredible accomplishment in text-to-audio, and I would definitely say that this is a milestone.

If you don't know what it is, don't worry. It's a model that converts any text to audio, but the audio is in podcast format with two hosts presenting what's inside the content you sent. See for yourself and become amazed (you can check at the beginning of this post a version generated by NotebookLLM)!

I really hope this continues to improve and that it gets more attention than video-to-text.

#### 3.4. Environmental Concerns

With more and more AI usage (especially LLMs), this becomes a concern for lots of people. We have several reports (like this [How data centers and the energy sector can sate AI’s hunger for power](https://www.mckinsey.com/industries/private-capital/our-insights/how-data-centers-and-the-energy-sector-can-sate-ais-hunger-for-power)) this year pointing to the excessive energy usage of datacenters, and even some big tech companies are making deals to use nuclear energy to fuel datacenters ([Microsoft chooses infamous nuclear site for AI power](https://www.bbc.com/news/articles/cx25v2d7zexo)).

> "_The power sector is rapidly becoming a protagonist in the AI story. Access to power has become a critical factor in driving new data center builds. As the power ecosystem grapples with meeting data centers’ voracious need for power, it faces substantial constraints, including limitations on reliable power sources, sustainability of power, upstream infrastructure for power access, power equipment within data centers, and electrical trade workers to build out facilities and infrastructure._"

I don't know about you, but this is probably a trend that will continue in 2025!

![nuclear power plant](/static/pages/essays/21/image-1.png)

> **_My Take: AI hype isn't over, and we will see more and more developments next year. Some will impact our daily lives, while others will be pure speculation. I would say that code generation tools will play major roles in 2025._**

### 5. The Social Media Split (X/Twitter migration)

Maybe this will be the most controversial item that I'm putting here. The final months of 2024 saw some splits in social media access. Since Brazil got "banned" from X/Twitter, we saw even more migration to other platforms (and that was not just from Brazil; other countries started to follow this pattern).

This will continue in 2025, mostly caused by the way Elon Musk's policies about X/Twitter continue to degrade the platform.

I mentioned split because lots of people migrated from X/Twitter to BlueSky, Threads, and Mastodon. Not that these people will stay on those platforms; we probably will see one of those platforms winning in the end (by far, I think BlueSky will win given the similarity with X/Twitter).

> **_My Take: BlueSky will win the race. It seems to be the platform people are looking for, as it resembles X/Twitter, has almost the same features, and is less chaotic for now.._**

## Wrapping up

Probably, not everything I mentioned above will happen in just a single year, but definitely, there will be some changes on a small scale.

Trying to figure out what the future holds is hard, even in the near future, but all this seems feasible.

Hopefully, you enjoyed all the things I mentioned here and will use this next year to call me out on what I got right or wrong.

🎉 Thanks, and Happy 2025!
