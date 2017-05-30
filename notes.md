## Scraping the pdfs

Some of the websites in list are static, as in, they consists of simple html, css and
javascript and no server is dynamically serving the content. Such websites are
easy to scrape as we can simply download all the files accessible from the
website using `wget -mr -nd http://website.com` and delete everything that is not pdf.

We'll have to deal with dynamic websites on case by case basis. I believe we'll able
to able to scrape some of them using simple
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), in
other cases we might have automate browser actions, which I'm doing for union
government website using [splinter](http://splinter.readthedocs.io/).


## Extracting the text

Most of the recent gazettes contains text information in the pdfs themselves
and that can be extracted using `pdftotext`. For pdfs which are generated
though scan copies, we'll have to do optical character recognition (ocr) on
them. As of now, we won't deal with pdfs which needs OCR.


## Metadata

The metadata of a gazette consists of name of the issuing ministry, date of
notification and subject. Such information is often given along with the link
of the pdf and we should scrape this wiling write scraping he pdfs. In other
cases this information needs to be extracted out of the pdf which can be hard.
