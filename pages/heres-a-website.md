title: I've Made a Website
date: 14-04-2017
tags: [HTML, CSS, Python, Flask, Website]
image: imgs/site-image.png

After saying that I'd it for the better part of three years, I've finally made a website.
See? You're looking at it. I'm still in the process of figuring out exactly what I intend
to do with this, but mostly I'll be using it to show off some of the programming projects
I've been working on in my spare time. I might also ramble about politics, music or whatever
else I fancy &mdash; I'll see how the mood takes me.

Anyway, in the meantime, I'll start here by explaining how I've made this.

# How it works

Since I'm hosting this on github-pages, it has to be a static site. There's lots of good
ways of making static sites, and github-pages works particularly well with Pelican. However,
I spent a while trying to learn how to use Pelican and I found it rather difficult. I'm sure
with a little more time and effort it'd turn out to be straightforward, but I realised that
I was using it as an excuse to put off working on the site.

Instead, I decided to stick to what I know &mdash; and the python web framework I know best is Flask.
Flask is designed for running servers, not for static sites, but there's a couple of libraries
that enable you to make static sites with it: Flask-FlatPages and Frozen-Flask. I'm not going to
bother explaining exactly how to do so, since there's a neat little example
[here](https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/)
that does so much better than I ever could.

The result is a simplistic but un-complicated tool for building the site from markdown files.
After that, all that remained was to design the layout, write the CSS, and push the compiled
site to my github-pages repo.

# The future

There's a lot more that I'd like to do with this in the future, but right now my priority is
just to get something up on the internet &mdash; the rest I'll deal with later. Whenever I get around
to making improvements, I'll write about it on this site.

As for the immediate future, the main thing now is to actually get some stuff on here! Over the
next few weeks I'm going to start posting retrospectives on some of the more interesting ways that
I've wasted my spare time since first started programming, about a decade ago.