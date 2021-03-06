# img2pdf_helper
Does all the dirty [**img2pdf**](https://gitlab.mister-muffin.de/josch/img2pdf/) arguments work for you

## Trivia
[*img2pdf*](https://gitlab.mister-muffin.de/josch/img2pdf/) is the great piece of software to losslessly convert images to PDF. It is very well thought of (with the experiments and stuff!) and very well coded. The issue is, it is perhaps *too well* coded, such that to do trivial stuff I often have to go to the depths of my hard drive, find old snippets and what not. Thinking of that, it even supports getting images from stdin, crazy!

Moreover, it is coded to support both Python 3 and Python 2.X. Now thats truly the German quality at its best! Won't be surprised to find out it supports DOS in some super hacky way! But Because of that, in some specific aspects (listed below) the app is stuck with the old bugs + their workarounds + for both Python 2.X and 3. In particular, what bothers me personally is,
* Lack of wildcard support (at least by standard means)
* Lack of long paths support (requires encapsulating **each and every path** into quotation marks)
* Mediocre and often mistaken DPI recognition
* Does **NOT** generate a PDF in the same folder as pics are
* If fetch path not set up for Python scripts, you'll need to mess around with paths to get things working

Also to accomplish trivial tasks one'd need to deal with things above **+** enter common args over and over. Overall, it takes what 15 minutes every time, but time that time by the number of PDFs to create = lots of time wasted! This script saves time a little every time.

Possibly will embed something from here into img2pdf in the future, but I reckon it's too much of the hastle to do + don't wanna optimise for Python 2. Maybe another time.


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
    1 inch = 25.4 mm**

* It's actually PPI, but since colloquially everyone calculates DPI as such, and everyone says PPI is DPI (although that's not 100% true,  just like *bod* does not always mean *bit*), *cough-cough*, just call it DPI. Even img2pdf creator calls it DPI
* 1 inch is **always** 25.4 mm, i.e. a fixed relationship between these two, so to everyones surprise you don't need to worry about Imperial<->Metric system convertion error... this time
    
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

(Obviously easily adjustably by commenting things out in the script) Why three things at once, and not say, *exec(command_to_pass)* ? Remember I said it outputs the *pretty-much-ready-to-use* command? Chances are, with how  specific PDF is, you'd want to specify other options, or remove some files or something along these lines. But obviously if you automate it that way I'd be happy you found this script useful. If so, don't hestinate to make a PR, I'd sure cxonsider your ideas.


## Be caucious!

* **ALWAYS** figure out your DPI. PDF relies on DPI to display contents correctly
* Don't forget you specific needs arguments alongside
* And as always, dont use this tool for piracy purposes ( ͡° ͜ʖ ͡°)

## Credits

Nonetheless, big thanks goes to Johannes (**josch**) for such a useful an amazing script of [*img2pdf*](https://gitlab.mister-muffin.de/josch/img2pdf/)
   
    