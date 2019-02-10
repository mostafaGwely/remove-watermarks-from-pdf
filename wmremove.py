from pdf2image import convert_from_path
import cv2 as c 
import time 
import sys 
import shutil 
import os 

tick = time.time()
logo = c.imread(sys.argv[1],0)

if not os.path.exists('./images'):
    os.mkdir('./images')

p = 0
while True:
	p += 1
	try:
		pages = convert_from_path(sys.argv[2],fmt='jpg',first_page=p,last_page=p, dpi=500)
		pages[0].save('out.jpg', 'JPEG')		
		sample = c.imread('out.jpg',0)
		sample = c.resize(sample,(logo.shape[1],logo.shape[0]))
		result = c.subtract(logo ,sample)
		result = c.bitwise_not(result)
		ret,result = c.threshold(result,100,250 ,c.THRESH_BINARY)
		result = c.blur(result,(3,3))

		c.imwrite('./images/page'+str(p)+'.jpg',result)
		temp = 100*p/300.0 
		line = str('['+'='*int(round(temp))+' '*(100-int(round(temp)))+'] '+str(round(temp))+'%')
		print(line,end='\r')

	except Exception as e:
		print(e)
		print(round((time.time() - tick)/60,2))
		break

import os
import img2pdf

with open(sys.argv[3], "wb") as f:
    f.write(img2pdf.convert(['./images/'+i for i in os.listdir('./images')]))

shutil.rmtree('./images')

