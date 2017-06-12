Odisha's gazette's can be downloaded easily using wget;

* It is hard to do the same for union gazettes because it is aspx website and
    there is only a search tool over the gazettes; no permanent urls

* Found ghost.py (http://ghost-py.readthedocs.io/en/latest/);

# Wednesday 03 May 2017 04:11:30 PM IST

ghost.py in not working on my local computer; probably due to proxy troubles;
running it on the server now.
Tried to install it but a dependency of the package pyside conflicts with
python 3; Installing python 2.7 anaconda enviornment now.

# Wednesday 03 May 2017 04:37:12 PM IST

THe author has specified dependencies properly; I should make a PR later
updating the documentation

I needed to install

* cookiejar
* pyside
* Qt by `sudo apt-get install qt5-default qttools5-dev-tools`
* PyQt by `conda install pyqt`

Didn't work opened an issue at https://github.com/jeanphix/Ghost.py/issues/326

Other options try: https://splinter.readthedocs.io/en/latest/

btw here is the directory of gazettes by year http://egazette.nic.in/(S(3tye31mihkriqhvbwg10sezb))/Digital.aspx

# Wednesday 03 May 2017 05:37:37 PM IST

I manually downloaded one file and its url was in format http://egazette.nic.in/WriteReadData/2016/168299.pdf
so used wget with gnu paralle.

`seq 160000 169999 | parallel -j 20 wget http://egazette.nic.in/WriteReadData/2016/{}.pdf`

That was pretty quick but 2544 docs, the website shows some 5K doc.

# Wednesday 03 May 2017 05:39:51 PM IST

Found out that 16xxxx is not necessarily the format for the url, as I found this
http://egazette.nic.in/WriteReadData/2016/171706.pdf

# Wednesday 03 May 2017 05:43:16 PM IST

Ran the command for another set of number

`seq 160000 169999 | parallel -j 20 wget http://egazette.nic.in/WriteReadData/2016/{}.pdf`

I should write a bash script which does this for all years. Though this is
dirty hack; scraping though page will also give use hte metadata without
extracting it out of the pdf. Also this method might now always work, for
example 2012 has this url format http://egazette.nic.in/WriteReadData/2012/E_1_2012_186.pdf

# Saturday 13 May 2017 11:23:09 PM IST

I'm starting with scraping union notifications again. `ghost.py` has really bad
documentation. I has started working on my laptop since I'm now at home with
an internet without proxy. I'll try selenium, that might work better.

# Sunday 14 May 2017 01:22:38 AM IST

I'm using splinter to automate the process. It is wrapper on selenium and
appears to have more usable api. I was facing some trouble running those with
the non latest version of firefox. I had to manually download the latest
version and installed it using this guide http://libre-software.net/how-to-install-firefox-on-ubuntu-linux-mint/

Now I'm able to programmatically access the page programmatically.

But the table is huge and the links aren't urls. I'll do the work of
downloading them tomorrow.

# Sunday 14 May 2017 10:40:01 PM IST

Using `x = browser.find_by_xpath("//input[@src='images/pdf_icon.png']")` I'm
able to get links to all pdfs using this but I also want the metadata. This
opens the pdf in a new window, I can get the window url using
`browser.windows[-1].url`, which I can save and download later.

# Monday 15 May 2017 12:06:29 AM IST

Okay, I'm calling it a day. Till now I was able to open the pdf in a new window
and also get a metadata. The issue is that I need to wait till the pdf opens in
a new window that for some reason I'm not able to do properly. After this is
over I need to run the script on my server. Splinter or Selenium needs a
display to run firefox. I found this (https://en.wikipedia.org/wiki/Xvfb) which
will run a display in memory without showing anything so that I can close my
own computer and sleep.

# Monday 15 May 2017 07:15:42 PM IST

Central government website is slow to an extent of being annoying. Sometimes
even 30 second wait time is not enough which really waits down my iteration
cycle.


# Monday 15 May 2017 09:15:52 PM IST

The script to scrape information from the central government website appears to
work properly. Now I need to run it on the server. I have install splinter,
geckodriver and firefox on it again. I should write a installation scrip too!
BTW get gecko from https://github.com/mozilla/geckodriver/releases


# Monday 15 May 2017 10:27:34 PM IST

I've run the script to script to scrape all the metadata (date, subject and
ministry) for all 2014 gazettes of union government. It is taking a lot of time
to run on the server, lets see how it turns out, after that I'll run it for
other years.

Meanwhile running the scrapper for other state governments. For websites which
can mirrored using wget, I'm mirroring them using wget and will scrape the
metadata later.

# Tuesday 16 May 2017 10:27:21 PM IST

I think I should start building the search tool with whatever pdfs I've been
scrape till now. I came across `pdftohtml` tool and it soo good! I also came
across [django-haystack](http://django-haystack.readthedocs.io) and it appears
to be the right tool for the job.

For the next one or so hour I'll try to follow this haystack tutorial
https://www.slideshare.net/MarcelChastain/advanced-search-solr-djangohaystack

# Tuesday 16 May 2017 10:49:35 PM IST

Okay, it is an old tutorial, 3 years old using really old version of solr and
java and is python 3 incompatible, I should find something else.

# Tuesday 16 May 2017 10:52:49 PM IST

I'll try to follow the official tutorial
http://django-haystack.readthedocs.io/en/v2.6.0/tutorial.html Following it
requires basic knowledge of django, so I should first take a basic tutorial of
django.

# Tuesday 16 May 2017 10:59:52 PM IST

I'm starting with tango with django book http://www.tangowithdjango.com I
remember Himanshu mentioning it once.

# Tuesday 16 May 2017 11:32:45 PM IST

:/ this tutorial also appears to be old with broken links to django
documentation, but not too old to be useless.

# Wednesday 17 May 2017 12:05:57 AM IST

The tutorial is not bad, I completed the first two chapters and will do the
rest tomorrow.

# Wednesday 17 May 2017 11:19:58 PM IST

I've completed basic django tutorial, the "Tango with Django" book was often
redirecting me to the official tutorial, so I just read the official tutorial
an skipped the book. The tutorial is in many parts I completed teh first 4, the
rest talks about tests, looks and feel and re-usability which I'll look into
later.

# Thursday 18 May 2017 12:11:17 AM IST 

I'm not able to follow and run haystack's tutorial. Some of the instructions
are not clear. For example at one point we are asked to add the following line to URLConf
`(r'^search/', include('haystack.urls')),`

but I'm sure where this `include` is coming from. See http://django-haystack.readthedocs.io/en/v2.6.0/tutorial.html#add-the-searchview-to-your-urlconf

Also later the author asks us to run `./manage.py rebuild_index`, but when I do
so it says
```
 Unknown command: 'rebuild_index'
Type 'manage.py help' for usage
```

I would rather have a working demo of haystack and tinker with it rather than
following this tutorial where the instructions don't work.

# Thursday 18 May 2017 12:22:08 AM IST 

Found this demo given at BangPyper's meetup
https://github.com/jitendraag/books/ and the corresponding instructions
https://docs.google.com/document/d/1XYsnJJDSiHNCFVe8KLCXpGbGegTZ_QBQnGE_5mky4W0/edit

I'm calling it a day for today. See you tomorrow.

# Thursday 18 May 2017 08:52:22 PM IST 

I'm not sure why but I was getting 404 error when I tried to run by downloading
tar and just staring it using `bin/solr start` as instructed in starting guide.
Passing the host address also doesn't help, though installing solr using
apt-get fixed the thing. See https://askubuntu.com/a/677829/421703

I should come back after I get the MVP and see what was wrong.

# Thursday 18 May 2017 09:01:39 PM IST

I thought lets fix the installation from source issue and I'm getting these
strange java call stacks which I know nothing about see https://dpaste.de/ujvJ

# Thursday 18 May 2017 09:38:11 PM IST 

There is some issue with the java installation as `java --version` is
completing. I thought of doing this when I though I should post a question on
stackoverflow.

# Thursday 18 May 2017 09:44:20 PM IST

[facepalm] I ran `java --version` and it turned out it gives error even if java
is installed properly. I needed to run `java -version`, a single hyphen, in
python and many other places it is convention to start long arguments by double
hyphen. Anyway I've reinstalled java lets see if solr works now.

# Thursday 18 May 2017 09:49:39 PM IST

Okay, solr admin panel opened up! phew.

# Friday 19 May 2017 12:14:15 AM IST 

Okay, I was able to setup a basic search locally, lets try it on remote

# Friday 19 May 2017 12:41:28 AM IST

Okay, things also work on the remote server, as of it only gives the file name
for the search query. I extracted text of some union gazettes and searched
"Aadhaar" and the file it showed had the term. It uses Whoosh as backend, I'll
change it to solr, also I'll try the highlighting feature. The present aim will
be to create the website for all 2016 and 2017 gazettes by union of India.

# Friday 19 May 2017 02:53:42 PM IST

On hindsight, haystack documentation wasn't bad, I could have been more
careful in the whole process. `include` thing that I was talking about was part
of django utils, though I should make a PR to clarify that in the docs.
Okay, it is time to get a deeper understanding of haystack. Today I'll try to
add two things, 1. the full result and just the name, 2. highlight of the
relevant part.

# Friday 19 May 2017 11:26:33 PM IST

Slept for the most part of day. Okay, I got both of these things and now I've
got a fair idea of how to proceede. `django-haystack` is a good library but
with poor documentation in example they said use `{% highlight result.summary
with query %}` to highlight the result summary. There are two issue with that,
first they didn't tell that I had to load the `highlight` template, I got to
know of that looking at the example templates they have. Second,
`result.summary` isn't an actual object and `.summary` part needs to replaced
with whatever thing you want to highlight. They might have thought this is
obvious but it isn't that much.

# Friday 19 May 2017 11:42:51 PM IST

Now that I've got a fair idea of all the building blocks I can start off with
making the main site. Though I still need to extract the subject and
publication date. `pdfinfo` gives a creation date and a modification date,
though I'm not sure how accurate that might be. I case I find no reliable way
to find the subject, I'll use the publication date as title.

# Friday 26 May 2017 01:47:37 AM IST

I was off from this project from last few days because I went to village with
nani. I was trying to highlight html generated from `pdftohtml`, but it doesn't
seem to work quite well. I guess the html is making search difficult, will find
out.

# Friday 26 May 2017 03:46:31 PM IST

Okay, fixed the highlighting issue. I've also created added a parameter
`full_doc` in `django-haystack` which will allow one to highlight the whole
document. I'll make a pull request soon.

BTW I'm finding it hard to decide who to divide up project into apps, so as
of now I'm going to put everything in a single app, I'll do the refactoring
later as things will become clearer. Premature abstraction is also a root of
evil.

# Friday 26 May 2017 04:26:46 PM IST

I was encountering `OperationalError` when I tried to move my code from the
test app I created by following django tutorial to the new app. This answer
helped (https://stackoverflow.com/a/37799885) but not sure why. Understating
django's migration process goes to my technical debt account
https://docs.djangoproject.com/en/1.11/topics/migrations/
