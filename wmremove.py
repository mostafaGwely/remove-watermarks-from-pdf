from pdf2image import convert_from_path
import cv2 as c 
import time 
import sys 
import shutil 
import os 
from fpdf import FPDF

logo = c.imread(sys.argv[1],0)


tick = time.time()
if not os.path.exists('./images'):
    os.mkdir('./images')

print('removing the mark ...')
p = 0
while True:
	p += 1
	try:
		pages = convert_from_path(sys.argv[2],fmt='jpg',first_page=p,last_page=p, dpi=500,thread_count=30)
		pages[0].save('out.jpg', 'JPEG')		
		sample = c.imread('out.jpg',0)
		sample = c.resize(sample,(logo.shape[1],logo.shape[0]))
		result = c.subtract(logo ,sample)
		result = c.bitwise_not(result)
# 		ret,result = c.threshold(result,100,250 ,c.THRESH_BINARY)
# 		result = c.blur(result,(3,3))

		c.imwrite('./images/page_'+str(p)+'.jpg',result)
		temp = 100*p/300.0 
		line = str('['+'='*int(round(temp))+' '*(100-int(round(temp)))+'] '+str(round(temp))+'%')
		print(line,end='\r')

	except Exception as e:
		print('\n',e)
		print(round((time.time() - tick)/60,2))
		break


imgs  = [i for i in os.listdir('./images')]
imgs.sort(key=lambda f: int(f.split('_')[1].split('.')[0]))

pdf = FPDF()
k = 0

sampleImage = c.imread('./images/'+imgs[0],0)

print('generating the pdf ...')
for image in imgs:
	k+=1
	pdf.add_page()
	pdf.image('./images/'+image,0,0,200,310)
	print('number of pages '+str(k),end='\r')

pdf.output(sys.argv[3], "F")



  
# output 
print("Successfully made pdf file") 

shutil.rmtree('./images')
