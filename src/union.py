from splinter import Browser
from bs4 import BeautifulSoup
import time

url = "http://egazette.nic.in"
browser = Browser()
browser.visit(url)
browser.click_link_by_text("Digital Directory")

assert browser.is_element_present_by_id("ContentPlaceHolder1_ddlcat1", wait=10)
elem = browser.find_by_id("ContentPlaceHolder1_ddlcat1").first
elem.select("Extra Ordinary")

time.sleep(1)
elem = browser.find_by_id("ContentPlaceHolder1_ddlyear1").first
elem.select("2014")

time.sleep(2)
search_button = browser.find_by_id("ContentPlaceHolder1_Button1").first
search_button.click()

# TODO: will have to add wait between all of these actions

soup = BeautifulSoup(browser.html, 'html.parser')

# TODO: Wait till "scroll to top" appears

# ContentPlaceHolder1_rptmmain_imgbtndownload_10

# ContentPlaceHolder1_rptmmain_imgbtndownload_13

# x = browser.find_by_xpath("//input[@src='images/pdf_icon.png']")
# I'm able to get links to all pdfs using this but I also want the metadata.

assert browser.is_text_present("Scroll to Top", wait=10)
metadata = list()
rows = list(browser.find_by_tag('tr'))
for row in rows[:20]:
    if 'input' not in row.html:
        continue

    row_data = [z.text for z in list(row.find_by_tag('td'))[1:-1]]
    # link = row.find_by_xpath("//input[@src='images/pdf_icon.png']").first
    link = row.find_by_tag("input").first
    link.click()

    # Two sends wait is not enough
    start_time = time.time()
    end_time = time.time()
    url = browser.windows[-1].url
    while 'pdf' not in url or end_time - start_time > 120:
        time.sleep(1)
        url = browser.windows[-1].url
        end_time = time.time()

    print(url)
    if 'pdf' in url:
        browser.windows[-1].close()
    row_data.append(url)
    metadata.append(row_data)
