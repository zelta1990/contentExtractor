import os,sys,io
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pdfminer.converter import PDFPageAggregator


my_file = os.path.join("28792454.PDF")

password = ""
extracted_text = ""

fp = open(my_file, "rb")

parser = PDFParser(fp)

document = PDFDocument(parser, password)

if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
	
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
n=0
text_file = open("log.txt",'w')
text= ""
for page in PDFPage.create_pages(document):
	interpreter.process_page(page)
	layout = device.get_result()
	n+=1
	for lt_obj in layout:
		if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
		    if "TARP" in lt_obj.get_text() or "Tarp" in lt_obj.get_text() or "tarp" in lt_obj.get_text():
			    text= text+"Page"+str(n)+"\n\n"
			    text += lt_obj.get_text()
		    else:
			    continue
	
	"""for out in layout:
	    if hasattr(out, "get_text"):
		   # print(out.get_text())
		    text=text+(out.get_text())	"""	
print(text+"\n")
text_file.write(text+"\n")
text_file.close()			



