import mechanicalsoup

my_address = "http://finance.yahoo.com/quote/yhoo?ltr=1"
my_browser = mechanicalsoup.Browser()
page = my_browser.get(my_address)
page_text = page.soup

for span in page_text.select("[class='Fw(b) D(ib) Fz(36px) Mb(-4px)']"):
	#print (span)
	if ' '.join(span['class']) == "Fw(b) D(ib) Fz(36px) Mb(-4px)":
		print (span.text)
