# img2pdf_helper
Simplifies [**img2pdf**](https://gitlab.mister-muffin.de/josch/img2pdf/) configuration and usage.

## Additional scripts
* "gen_html_toc.py" - Generate HTML-based Table of Contents (ToC) of the given files with embedded links. Useful to subsequent generation of merged PDF with an 'aftermarket' ToC in Adobe Acrobat, as ToC generation is not natively supported in Adobe Acrobat. Also, it may be useful for data scrapping.

## Trivia
[*img2pdf*](https://gitlab.mister-muffin.de/josch/img2pdf/) is a great piece of software to convert images to PDF without quality loss. It is very well designed. But it is coded to support both Python 2.x and 3, but has some limitations,
* Lack of Windows globbing support (at least by standard means)
* Lack of long paths support (requires encapsulating each path into quotation marks)
* DPI guess is often incorrect.
* Does not generate a PDF in the same folder as pictures.
* If fetch path is not set up for Python scripts, it must be set up manually.

Overall, to accomplish trivial tasks, there is a need to deal with limitations above and enter common arguments repeatedly. As such, this tool saves the user 5-15 minutes every time.

## Usage
Install,
    
    pip install -r requirements.txt

Use,

	python img2.py <path> <DPI>
    
    <path> - Path to files. Both wildcards notation and 'just path' notations are supported
    <DPI> - Float/int number representing DPI
DPI is essential for PDFs, so you need to find it out, either mathematically or from image meta tags (such as with [IrfanView](https://www.irfanview.com/))

These mathematical constants are important:

	DPI = pixels / inches*
	1 inch = 2.54 cm**

* Actually PPI, but colloquially PPI is called DPI. Even img2pdf creator calls it DPI
* 1 inch is **always** 2.54 cm.

### Example
Both wildcards notation and 'just path' notations are supported

	python img2.py C:/my_snapchat_photos/*.jpg 300
Will only pick .jpg (but not JPEG or PNG) files within path
	
    python img2.py /system/app/pics 150
Will pick up all pics within the specified directory

Note: figure out your DPI. PDF relies on DPI to display contents correctly

### Result
The script will output the **pretty-much-ready-to-use** command; to
* console
* file (named *<hash_aedler32>.pdf*)
* clipboard [disabled]
* execution [disabled]

The output may be adjusted in the `helper` script depending on the user's needs.
