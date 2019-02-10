# remove-watermarks-from-pdf
remove watermarks from pdf using python opencv

### requirements 

- img2pdf library `python -m pip install img2pdf` 

- pdf2image `python -m pip install pdf2image`

### run

python wmremove.py logo.jpg input.pdf output.pdf 

### limitations: 

- you must have one blank page which has the same size as standard pdf pages and contains the logo on it __see `logo.jpg`__

- the output is a gray pdf 

