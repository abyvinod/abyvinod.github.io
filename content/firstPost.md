Title: Setting up this blog using the Pelican+Conda+GitHub Pages framework
date: 2010-10-03 10:20
modified: 2010-10-04 18:40
tags: thats, awesome
category: yeah
authors: Abraham Vinod
summary: The customary hello world post when blogging with Pelican

# Prelude
I have been postponing my foray into blogging for some time now. Well, this
holiday season I decided to present myself with the gift of blogging. I had done
a bit of blogging using [DokuWiki](https://www.dokuwiki.org/) back when I was at
IIT Madras, but my site was hacked due to my neglience of the security settings.
To make things simple, I am choosing a static website for blogging, and I will
stick with [Pelican](https://blog.getpelican.com/) due to my comfort level with
Python. 

On reading about the blogs, the norm appears to be to replace the customary
'Hello World!' post with a post on how one sets up the blog using Pelican. The
journey definitely is not straight-forward as one would like to hope for.

# How did I get this blog setup?

I am working on Windows 10 OS, and I will by using
[msysgit](https://git-for-windows.github.io/) to emulate the Unix terminal in my
PC. I had already installed conda in Windows, and this is easily accessible from
msysgit as well. I used [conda](https://github.com/conda/conda) to create a
basic python environment for Pelican.
~~~
$ conda create -n blog python=3
~~~
    
    , and hosted my blog on GitHub.

Hell yeah!
http://ntanjerome.org/blog/how-to-setup-github-user-page-with-pelican/
