# I downloaded many pdfs by observing the url pattern of the pdf
# `seq 160000 # 169999 | parallel wget http://egazette.nic.in/Write^CadData/2016/{}.pdf`

from splinter import Browser
from bs4 import BeautifulSoup
import time
import json

url = "http://egazette.nic.in"
browser = Browser()
browser.visit(url)
browser.click_link_by_text("Digital Directory")

assert browser.is_element_present_by_id("ContentPlaceHolder1_ddlcat1", wait_time=10)
elem = browser.find_by_id("ContentPlaceHolder1_ddlcat1").first
elem.select("Extra Ordinary")

time.sleep(1)
elem = browser.find_by_id("ContentPlaceHolder1_ddlyear1").first
elem.select("2014")

time.sleep(2)
search_button = browser.find_by_id("ContentPlaceHolder1_Button1").first
search_button.click()

# x = browser.find_by_xpath("//input[@src='images/pdf_icon.png']")
# I'm able to get links to all pdfs using this but I also want the metadata.

browser.is_text_present("Scroll to Top", wait_time=60)
# The code breaks at this and browser stops loading

print("2014 page opened")

metadata = list()
rows = list(browser.find_by_tag('tr'))
for i in range(len(rows)):
    # The page is refereshed each time the link is clicked and rows object we
    # obtained is detached from the dom, hence we need to revaluate it
    rows = list(browser.find_by_tag('tr'))
    row = rows[i]

    if 'input' not in row.html:
        continue

    row_data = [z.text for z in list(row.find_by_tag('td'))[1:-1]]
    # link = row.find_by_xpath("//input[@src='images/pdf_icon.png']").first
    link = row.find_by_tag("input").first
    link.click()

    # At max wait for 30 sec till the page with pdf appears
    wait_time = 30
    start_time = time.time()
    end_time = time.time()
    url = browser.windows[-1].url
    while 'pdf' not in url or end_time - start_time < wait_time:
        time.sleep(1)
        url = browser.windows[-1].url
        end_time = time.time()
        # print(end_time)

    print(url)
    if 'pdf' in url:
        browser.windows[-1].close()
    row_data.append(url)
    metadata.append(row_data)

    if i % 10 == 0:
        with open('metadata_{}.json'.format(i), 'w') as fp:
            json.dump(metadata, fp)
