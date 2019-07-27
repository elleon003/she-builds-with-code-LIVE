Title: I Am In Over My Head!
Intro: Diving into using a static site generator after using manual static has it's challenges!
Summary: Diving into using a static site generator after using manual static has it's challenges!
Date: 2019-07-12
Tag: static site

I had a bit of an indecisive moment before launching into the next phase of my site. As I had mentioned, I was set on building version 2 of the site with [Pelican Static Site Generator](https://blog.getpelican.com/) for a number of reasons:

1. It is written in Python, my primary language of choice
2. While there are other static site generators written in Python, none had the development or community around it the way Pelican did.
3. It uses [Jinja](http://jinja.pocoo.org/) templates to render the pages, which is also used by Flask
4. I plan to use Flask to build a custom blog in the final version of the site, so Pelican seemed like a good mid step.

However, I can't ever stop searching for the "right" answer, so I kept digging a little more around the internet for peoples opinions. In a Twitter feed, I think, someone mentioned [Lektor.](https://www.getlektor.com/) It's another static site generator built in Python. It was mentioned because it offered an admin panel, similar to a WordPress blog, something that other site generators didn't do.

My initial thought was "Oh, cool! That will give me the ability to post from my phone!"

<img style="max-height:40rem;" class="img-fluid d-block mx-auto mb-3" src="{static}/images/facepalm-cat.png" alt="Facepalm Cat Meme">

The admin panel is a locally housed admin panel...cause this is a static site generator that doesn't have a database. The code generates the static pages, then those pages get uploaded.

Anyway, on closer inspection, I found that Pelican still had the widest use and more features available. So I went back to the original plan.

I followed the quickstart installation instructions, and they were pretty easy to follow. I set up a second folder in my [GitHub](https://github.com/elleon003/she-builds-with-code) repo for the project files, and started to dive in.

I started reading through the documentation, but found myself following too many rabbit holes. So then I decided I'd start working on a specific goal, like converting my blog posts to Markdown. But I kept getting caught up in how to bring over the styling, which lead me to decide to start building my custom theme instead.

A note - this is the first time I've ever tried to build something on my own, just using the documentation without any tutorial. And after trying to understand what I was reading for about 5 minutes made me realize that I was in waaaaay over my head.0

For a second, I really panicked. *"Maybe this was a dumb idea. Maybe I'm not good enough yet to try this. Maybe I should take this down and do something else for a bit, gain more experience."*

But then I realized, there's really nothing to lose here. Sure, I don't fully understand what I'm doing yet, but that's the beauty of learning!

This project is mine - it's not for anyone else, no one is expecting this for a grade or as a client. The worst thing that would happen is I break my site and have to fix it. If I want to do this, that kind of thing would happen. Isn't it better that I learn it in a low-stakes situation first?

So I'm working through it, slowly. And if I don't understand something, I'm going to try what I think and see what happens. And if I'm right or wrong, I'll learn from it. Honestly, I'll retain better if I struggle through something vs. finding the answer in Google. I needed to remind myself that's the whole purpose of this.
