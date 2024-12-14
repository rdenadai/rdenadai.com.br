# BlueSky: Writing a Bot using ATProtocol

Recently, I was on BlueSky, and after a few jokes about making a bot for the platform, I gave some suggestions on how to do it.

Well, this post is exactly about that. Let's go step by step on how to create a bot for BlueSky and learn a little bit about what the AT Protocol is.

## What is ATProtocol?

In a nutshell, and took from the [official documentation](https://atproto.com/).

> The AT Protocol is an open, decentralized network for building social applications.

OK, but what does it mean? It means that with it, you could create your own social network. It's more complex than that, and there are tons of discussions on the internet nowadays about [Decentralized Social Media](https://sopa.tulane.edu/blog/decentralized-social-networks). However, you'll find other terms that are somewhat related, such as [Distributed social network
](https://en.wikipedia.org/wiki/Distributed_social_network).

There's even more to this, but to keep it simple (because I'm definitely not an expert on the subject), let's keep going and get our hands dirty.

## How to create a bot for BlueSky?

Well, here's the sad part, oficially only `Typescript` and `Go` are supported ((not that much because, at least we've some `Python` community support)).

[SDKs](https://atproto.com/sdks)

![BlueSky sdk's](/static/pages/essays/20/image.png)

I'm not a hatter of `Javascript` on the backend, but, for me we have better langs to work on that space. The "problem" in using `Go` for this post is that I'll run the bot as a AWS Lambda, and, you know, AWS support is not that good for `Go` as it is for `Python` or `Javascript`.

![aws lambda creation warning](/static/pages/essays/20/image-1.png)

Given all the above, I'll use `Python` for this post.

## Requirements

For this post we're going to use (I'm assuming you're using a `Linux` distro and have all this installed or know how to install):

- Python 3.12 (you can install using [pyenv](https://github.com/pyenv/pyenv) or [asdf](https://github.com/asdf-vm/asdf))
- [uv](https://docs.astral.sh/uv/) (the new python package manager from Astral)
- [docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) (to build the lambda package)
- Have an account on [BlueSky](https://bsky.social/)
- Have an account on [AWS](https://aws.amazon.com/)

## Creating the bot

Alright, let's start by creating our new project, since we're using `Python`, we'll use `uv` to manage our dependencies.

```bash
$> mkdir bs-bot
$> uv init
```

![project](/static/pages/essays/20/image-2.png)

With that, let's rename `hello.py` to `main.py`.

```bash
$> mv hello.py main.py
```

Let's keep our code apart from the lambda code we'll generate later, create a new folder called `app` and move `main.py` to it.

```bash
$> mkdir app
$> mv main.py app
```

Also, let's create a new folder called `lambda`, this is where our lambda generated code will be.

```bash
$> mkdir lambda
```

Since we going to use the `Python` lib `atproto` let's install it.

```bash
$> uv add atproto
```

![atproto installed](/static/pages/essays/20/image-3.png)

**CODING!!! Finally!!!**

```python
from atproto import Client
from atproto_client.namespaces.sync_ns import (
    AppBskyFeedNamespace,
    AppBskyNotificationNamespace,
)


class BlueSkyBot:
    def __init__(
        self,
        username: str = "username",
        password: str = "password",
    ):
        self._client = Client(base_url="https://bsky.social")
        self._client.login(username, password)
        self._namespace = AppBskyNotificationNamespace(self._client)
        self._feed = AppBskyFeedNamespace(self._client)

    def get_author_feed(self, handle: str) -> list[dict[str, str]]:
        """Getting the author feed using it's handle (this could also be a valid did)

        Args:
            handle (str): handle (or valid did)

        Returns:
            list[dict[str, str]]: list of posts
        """
        profile_feed = self._client.get_author_feed(actor=handle)
        posts_obj = (feed.post for feed in profile_feed.feed or [])
        return list(
            (
                {
                    "did": post.author.did,
                    "name": post.author.display_name,
                    "handle": post.author.handle,
                    "message": {
                        "cid": post.cid,
                        "uri": post.uri,
                        "text": post.record.text,
                        "created_at": post.record.created_at,
                    },
                }
                for post in posts_obj or []
            )
        )


def main():
    # replace with your username and password for account login
    bot = BlueSkyBot("<username>", "<password>")
    # replace with the handle of the user you want to get the feed
    posts = bot.get_author_feed("<username>.bsky.social")
    # replace with the string you want to search in the posts
    something_we_want_to_search = "<something>"
    for post in posts:
        if something_we_want_to_search in post.get("message", {}).get("text", ""):
            print(post)


if __name__ == "__main__":
    main()
```

Run the code, and check the output, you should see the posts of the user '\<username>.bsky.social' that contains the string 'something'.

```bash
$> uv run python -m app.main
{'did': 'did:plc:3cftygah4elv4znu3wrxtujv', 'name': 'Pablo Galindo Salgado', 'handle': 'pablogsal.com', 'message': {'cid': 'bafyreif33nvf5zqzybkrredierklmz7msco6mhgh67hq2qtcl347qsa75i', 'uri': 'at://did:plc:3cftygah4elv4znu3wrxtujv/app.bsky.feed.post/3ld4ey26vmk2z', 'text': 'We are very exited to share with you PEP 768 🐍, which proposes a safe external debugger interface to Python. We think this is a really exciting change that would allow debuggers and tools to safely attach to running Python processes without stopping or restarting them. 🔨🐛\n\npeps.python.org/pep-0768/', 'created_at': '2024-12-12T13:31:40.690Z'}}
```

In the above I search all posts on my profile that contains the word `python`!

The bot itself is very simple and I leave for the reader to improve it. You could, for example, repost that post, like it, or even add a follow up message on it, anyway, have fun with it!

## Building the Lambda function

Nice, so we build our bot and can run it locally on our machine. The big deal is to run it on the cloud, right? So, let's do it!

Since we have a dependency on `atproto`, a good way to create the Lambda function is to build a `.zip` package with everything inside.

To do that, the first step is to create a `requirements.txt` file with the dependencies.

> P.S.: From now on, all the operations describe here should go inside the `lambda` folder.

```bash
$> uv pip compile pyproject.toml -o lambda/requirements.txt
```

Next, create a `Dockerfile` inside the `lambda` folder. . We are going to use it to build the `.zip` package.

Something like:

```Dockerfile
FROM amazonlinux:latest

# Install necessary tools and libraries including tar
RUN yum install -y gcc openssl-devel bzip2-devel libffi-devel zlib-devel make wget tar gzip

# Install Python 3.12
RUN wget https://www.python.org/ftp/python/3.12.0/Python-3.12.0.tgz && \
    tar xzf Python-3.12.0.tgz && \
    cd Python-3.12.0 && \
    ./configure --enable-optimizations && \
    make altinstall

# Upgrade pip for Python 3.12
RUN python3.12 -m ensurepip --upgrade && \
    python3.12 -m pip install --upgrade pip

# Install the dependencies in a directory
COPY ./requirements.txt .
RUN python3.12 -m pip install -r requirements.txt -t /package

# Copy your Lambda function code
COPY ./lambda_function.py /package
COPY ./app /package/app

# Set the working directory
WORKDIR /package
```

**Why we're doing this?**

You may ask why using a Dockerfile to build the `.zip` package?

As I mentioned before, for this simple bot we only have `atproto` as a dependency, but our bot (or other function) could have many more dependencies, many more files, and that complicate a lot our lambda function. So a good way of doing this is create `.zip` package with dependencies and the code inside.

More can be learn [here](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html).

The `Dockerfile` is a good shortcurt to do this, but you can also do it manually.

Moving on...

---

Create a `lambda_function.py` file inside the `lambda` folder.

```bash
$> touch lambda/lambda_function.py
```

And add the following code:

```python
import os
import sys

# Add the directory containing lambda_bot.py to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.main import main


def lambda_handler(event, context):
    main()
    return {"statusCode": 200, "body": "Lambda function executed successfully"}
```

You can see that we need our `app.main`, so copy the `app` folder to the `lambda` folder.

```bash
$> cp -R app/ lambda/
```

Ok, all set ... let's build!

```bash
$> cd lambda
$> docker build -t lambda-package .
```

This might take a while to build, but once it's done, running the following command should create a `lambda_function.zip` inside the `lambda` folder.

```bash
$>  docker run --rm -v $(pwd):/output lambda-package zip -r /output/lambda_function.zip .
```

## Registering the Lambda function and EventBridge

Ok, we have all we need for our bot to run on AWS! We also tested locally just to see if eveything is fine.

I'm not going to cover it here, but if you want to you could test the code generated by the Dockerimage locally using the [Serverless Framework](https://www.serverless.com/framework/docs/providers/aws/cli-reference/invoke-local).

But for the porpuse of this post, let's go to the AWS Console and create our Lambda function. Keep in mind that you could use other tools to create you lambda, like [Terraform](https://developer.hashicorp.com/terraform/docs) and [CloudFormation](https://docs.aws.amazon.com/pt_br/lambda/latest/dg/services-cloudformation.html).

![AWS Console Lambda](/static/pages/essays/20/image-4.png)

Click on the `Create function` button, and fill the form with the following information:

![Create Function screen](/static/pages/essays/20/image-5.png)

> P.S.: A super important thing here is to set the `Permissions` correctly! This will impact your Lambda function's ability to run properly, especially if you're trying to use `boto` to access other resources like S3 or DynamoDB.

> P.S.2: I lied at the beginning. We can use other versions of Python, but if you do so, please keep in mind to change everything in the code to match the version you're using.

After creating the function, you should see the following screen:

![Lambda edit page](/static/pages/essays/20/image-6.png)

What's missing here? We never uploaded our `.zip` package!

To do that you should click on the right middle button `Upload From` and select the `.zip` file we created before.

After the upload, reload the page, and you can see the code we written before. Now, to test if everything is working, click on the `Test` tab and on the `Test` button.

![Lambda error](/static/pages/essays/20/image-7.png)

You probably going to see the error above!

That's because we need a little more config given the peculiarities of our bot. We need more memory and a bigger timeout, because the whole thing took a little more than 3 seconds to run (remember that we're calling an external API!).

Head to the `Configuration` tab and change the `Memory` to 512MB and the `Timeout` to 60 seconds (or 1 minute).

I'm relaxing these values, but you could try to tune them to the minimum possible. Not that this is a problem, because normally you don't pay for up to a minimum of 1 million requests per month (or something like that).

![Configuring Lambda](/static/pages/essays/20/image-8.png)

Move back to the `Test` tab and click on the `Test` button again.

![Success](/static/pages/essays/20/image-9.png)

Alright! Our Lambda runs successfully!

But there's one missing piece that we need to configure, the EventBridge. As of now, our lambda only runs if we click the `Test` button, but we want it to run every, I don't know, 2-3 minutes.

To do that we need to attach to the Lambda an event to trigger it. This can be accomplished using the AWS EventBridge.

If you go to `Configuration` tab, and in the left menu, click on `Triggers` you can add a new trigger.

![lambda trigger](/static/pages/essays/20/image-10.png)

Click on the `Add trigger` button, and select `EventBridge (CloudWatch Events)`, just like my screenshot bellow.

![Create Trigger](/static/pages/essays/20/image-11.png)

I'm setting the `Schedule expression` to `rate(5 minutes)`, but you could set it to whatever you want, and AWS EventBridge accept other patterns (like CRON patterns).

And that's it! Our bot is running on AWS!

![AWS BlueSky Bot](/static/pages/essays/20/image-12.png)

## Where to go from here?

Well, I implemented a simple and very basic bot for BlueSky in this post. You could explore even more the `atproto` library and since we're running the bot via Lambda on AWS you could integrate other AWS resources into it (like databases, S3, etc).

Also, keep in mind that Python libraries can be attached to the Lambda function as a layer, making the `.zip` package smaller, deployments faster, and the code reusable across other functions.

For our username and password, this is fixed in code right now, but Lambda offers a way to store secrets as Environment Variables (this is set in the `Configuration` tab).

I guess that's it, if you find anything wrong or have any questions, please let me know!

Thanks!
