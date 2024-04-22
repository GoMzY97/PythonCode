#decrypt
#pip install PyPDF2

from PyPDF2 import PdfFileWriter, PdfFileReader

writer = PdfFileWriter()
#file u want to encyrpt
file = 'lmao.pdf'
reader = PdfFileReader(file)
if reader.isEncrypted
	#decrypt pdf with password
	reader.decrypt('@abc123')
	#get all pdf pages 
	for page in range(reader.numPages):
            writer.addPage(reader.getPage(page))

	#create new file with name as encrypted_file
	# and write the pdf pages into it
	with open(f'encrypted_file_pdf','wb') as file:
        	writer.write(file)
        	file.close()
	print('File ENcrypted')
else:
	print('File has no encryption')

