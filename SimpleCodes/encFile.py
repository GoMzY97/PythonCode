#pip install PyPDF2

from PyPDF2 import PdfFileWriter, PdfFileReader

writer = PdfFileWriter()
#file u want to encyrpt
file = 'lmao.pdf'
reader = PdfFileReader(file)
#get all pdf pages 
for page in range(reader.numPages):
	writer.addPage(reader.getPage(page))
#encrypt pdf with password
writer.encrypt('@abc123')
#create new file with name as encrypted_file
# adn write the pdf pages into it
with open(f'encrypted_file_pdf','wb') as file:
	writer.write(file)
	file.close()
print('File ENcrypted')
