Title: The Site Grand Relaunch!
Date: 2019-07-28
Slug: grand-site-relaunch
Intro:...Yeah, it doesn't look any different.
Summary: This site is FINALLY powered by Pelican!
Tag: pelican site,

Finally! After weeks of fussing, cursing, and some weeping, I have changed my completely manual static site over to Pelican!

<img style="max-height:40rem;" class="img-fluid d-block mx-auto mb-3" src="{static}/images/snoopy-dance-woohoo-meme.jpg" alt="Snoopy victory dance!">

So what does that mean? In the [intro post]({filename}/blog/the-mvp-of-this-site.md) to this blog, I talked about using this site as an experiment, a live workplace for my web development education. Initially, it was completely static. And now, I'm employing code to do most of the manual lifting for my site.

Obviously, there's nothing visually different here. But sooo much has happened since my last post.

Learning Pelican was fun, but challenging. There aren't a ton of tutorials on it, so I pieced everything together between the docs and a few helpful blog posts.

So my workload to post to the site went from looking like this:

- Open *post.html* template, save as with new blog title
- Write post
- Edit *index.html* by copying and pasting the last post snippet, edit to match new post.
- Upload to site via FTP

to this:

- Create new Markdown file, with header info
- Write post
- Run  `make publish upload_ssh`

Still a little more than logging into a Wordpress site, but so much more satisfying! Having an understanding of everything I have so far (more or less) has been worth it.

There were a few things that I just had to give up and hack a workaround:

- Many parts of my theme are hard coded, instead of using template tags. While it was cool to learn ultimately I don't plan on distributing this theme, so cut myself some slack there.
- I didn't quite figure out how to add a custom 404 page to my theme, so I manually added it to the server. Since it's not in the content structure of Pelican, it will remain undisturbed.
- I also couldn't figure out how to strip the trailing *.html* from my URL's. I tried to adjust my URL settings in Pelican, and tried to edit my .htaccess rules, but after struggling with this for an hour I decided to let it be for now.
- Lastly, I don't have a great solution for comments on the site yet. There are some options, but I just don't know if it's worth the struggle right now. I don't have people banging down the door for comments, and at the very least I've got each post linked to my [Twitter](https://twitter.com/SheBuildsWCode) account, so I can at least engage people there.

Originally from here, I planned to build a custom CMS using Flask. However, I think I may stay in this format for a while. It's something I want to do, but to be honest it's not my top priority.

My main reason for trying to learn to code is that I have an idea for an app I want to build for myself. It's a budget that works for bi-weekly paychecks. I've seen a lot online, and tried to use them, but I find I'm always stringing a bunch of hacks together to work with it. I've yet to find the app I want,so I'm going to build it.

So I'm leaving Python for a little and switching to JavaScript. Specifically, I'm going to learn Vue & React Native. Why Vue? I heard it was a bit easier to grasp than React, and I found a tutorial that creates a budget app with Vue. Figure it's a great intro to what I'm trying to do.

Here we go!
