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
