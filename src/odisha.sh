wget -mr -c -nd http://odisha.gov.in/govtpress/department.htm
ls | grep pdf | parallel -j 10 pdftotext {}
