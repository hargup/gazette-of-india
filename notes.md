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
