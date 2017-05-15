# Gazette of India

Inspired by [Laws of India](http://lawsofindia.org/) this project aims to
collect all state and union gazettes of India at one place and add a search and
notification tool on them later.


| Government | Link | Dynamic website | pdf scrapped | text extracted | code |
|---|---|---|---|---|---|
| Union  | http://egazette.nic.in | Yes | Partly | No | [union.py](src/union.py) |
| Andra Pradesh  | http://gazette.ap.gov.in/gt_PublicReport.aspx | Yes| No | No | |
| Arunachal Pradesh  | http://arunachalpradesh.gov.in/csp_ap_portal/documents_new.html | No | No | No | |
| Assam | | ? | No | No | |
| Bihar  | http://egazette.bih.nic.in/ | Yes | No | No | |
| Chattisgarh  | http://cg.nic.in/egazette/ | Yes | No | No | |
| Delhi  | http://www.egazette.nic.in/(S(x5debhkdvvuvgxqzczr5bdx1))/SG_DL_Search.aspx | Yes | No | No | |
| Goa  | http://www.goaprintingpress.gov.in/gazettes/search_by_date/167 | Yes | No | No | |
| Gujarat | | ? | No | No | |
| Haryana  | http://www.egazetteharyana.gov.in/home.aspx | Yes | No | No | |
| Himachal Pradesh  | http://rajpatrahimachal.nic.in/ | Yes | No | No | |
| Jammu and Kashmir | | ? | No | No | |
| Jharkhand  | http://jhr2.nic.in/egazette/ | Yes | No | No | |
| Karnataka  | http://www.gazette.kar.nic.in/ | No | No | No | [karnataka.md](karnataka.md)|
| Kerala  | http://www.egazette.kerala.gov.in/ | No | No | No | |
| Madhya Pradesh  | http://govtpressmp.nic.in/gazette.html | No | No | No | |
| Maharashtra  | https://egazzete.mahaonline.gov.in/Forms/GazetteSearch.aspx | Yes | No | No | |
| Manipur  | http://manipurgovtpress.nic.in/index.php?option=com_gazette&Itemid=88 | Yes | No | No | |
| Meghalaya  | http://megpns.gov.in/gazette/archive.asp | Yes | No | No | |
| Mizoram  | https://printingstationery.mizoram.gov.in/gazette | No | No | No | |
| Nagaland | | ? | No | No | |
| Odisha  | http://odisha.gov.in/govtpress/department.htm | No | Yes | Partly | [odisha.sh](src/odisha.sh)|
| Punjab  | http://punjab.gov.in/notifications | Yes | No | No | |
| Rajasthan | | ? | No | No | |
| Sikkim  | http://www.sikkimgazettes.gov.in/ | Unreachable | No | No | |
| Tamil Nadu  | http://www.stationeryprinting.tn.gov.in/gazette/gazette_list.php | Yes | No | No | |
| Telangana  | http://tsgazette.cgg.gov.in | Yes | No | No | |
| Tripura  | http://tripura.gov.in/documents and http://tripura.gov.in/rules | No | No | No | |
| Uttar Pradesh | | ? | No | No | |
| Uttarakhand  | http://gazettes.uk.gov.in/ | Yes | No | No | |
| West Bengal  | https://wb.gov.in/portal/web/guest/circular-and-notifications | Yes | No | No | |


## Want to help?

You can help me by:

* Finding links to missing gazettes websites. As of now these states are Uttar
    Pradesh, Rajasthan, Nagaland, Jammu and Kashmir, Gujrat and Assam
* Writing scrappers for the pdfs and metadata
* Setting up a (web based) search tool on extracted text
* Funding this project
* Connecting me to people who are willing to help

I'm downloading the all scraped pdfs on my personal server send an email to
`mail AT hargup DOT in` with your ssh public key and I can give you access to
the server.
