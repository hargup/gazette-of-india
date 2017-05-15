Copied the lines with the links to pdfs from http://www.gazette.kar.nic.in/ A
line is of form `<option value="20040805/Contents(05-08-04).pdf">5 August 2004</option>`,
I need only the part between the quotes, to do so, I pasted these lines in vim,
selected them and ran following commands:
`%norm df"` and `%norm f"d$`
And then added www.gazette.kar.nic.in/ at the start of each line. See
[karnataka.txt](karnataka.txt)

Then I can use aria2c to parallel download files from this list of urls.
`aria2c --input-file=karnataka.txt`

