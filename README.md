# img2pdf_helper
Simplifies [**img2pdf**](https://gitlab.mister-muffin.de/josch/img2pdf/) arguments work for you

## Additional scripts
* "gen_html_toc.py" - Generate HTML-based Table of Contents (ToC) of the given files with embedded links. Useful to subsequent generation of merged PDF with 'aftermarket' ToC in Adobe Acrobat, as ToC generation is not natively supported in Adobe Acrobat. Also may be useful for data scrapping purposes.

## Trivia
[*img2pdf*](https://gitlab.mister-muffin.de/josch/img2pdf/) is the great piece of software to losslessly convert images to PDF. It is very well thought of (with the experiments and stuff!) and very well coded. The issue is, it is perhaps *too well* coded with disregard of KISS. It even supports getting images from stdin!

Moreover, it is coded to support both Python 3 and Python 2.X. Now thats truly the German quality at its best! But Because of that, in some specific aspects the app is stuck with the old bugs + their workarounds + for both Python 2.X and 3. In particular,
* Lack of wildcard support (at least by standard means)
* Lack of long paths support (requires encapsulating **each and every path** into quotation marks)
* Mediocre and often incorrect DPI recognition
* Does **NOT** generate a PDF in the same folder as pics are
* If fetch path not set up for Python scripts, you'll need to mess around with paths to get things working

Also to accomplish trivial tasks one'd need to deal with things above **+** enter common args over and over. Overall, this tool saves 5-15 minutes of time every time.

## Usage
Install,
    
    pip install -r requirements.txt

...And then use it!

	python img2.py <path> <DPI>
    
    <path> - Path to files. Both wildcards notation and 'just path' notations are supported
    <DPI> - Float/int number representing DPI
DPI is essential for PDFs, so you need to find it out, either mathematically or from image meta tags (eg [IrfanView](https://www.irfanview.com/))

Mathematically, you'd want to know these constants:

	DPI = pixels / inches*
    1 inch = 2.54 cm**

* It's actually PPI, but colloquially PPI is DPI (although that's not 100% true,  just like *baud* does not always mean *bit*). Even img2pdf creator calls it DPI
* 1 inch is **always** 2.54 cm.

### For example
Both wildcards notation and 'just path' notations are supported

	python img2.py C:/my_snapchat_photos/*.jpg 300
Will only pick .jpg (but not JPEG or PNG) files within path, AND
	
    python img2.py /system/app/pics 150
Will pick up all pics within the specified directory

### What's after?
After that the script will output the **pretty-much-ready-to-use** command; to
* console
* file (named *<hash_aedler32>.pdf*)
* clipboard [disabled]
* execution [disabled]

(Obviously easily adjustably by commenting things out in the script) Why three things at once, and not say, *exec(command_to_pass)* ? Remember it outputs the *pretty-much-ready-to-use* command? Chances are, with how specific PDF is, you'd want to specify other options, or remove some files or something along these lines. But obviously if you automate it that way I'd be happy you found this script useful. If so, don't hestinate to make a PR, I'd sure consider your ideas.

## Be caucious!

* **ALWAYS** figure out your DPI. PDF relies on DPI to display contents correctly
* Don't forget you specific needs arguments alongside
* No illegal use

## Credits

Big thanks goes to Johannes (**[josch](https://github.com/josch)**) for such a useful an amazing script of [*img2pdf*](https://gitlab.mister-muffin.de/josch/img2pdf/)
