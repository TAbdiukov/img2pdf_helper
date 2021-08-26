import os, sys, string, glob, zlib
from pathlib import Path, PurePath #PY3
import re

DEF_RECURSIVE = False
HEADER = """<html><title>{}</title>
   <body>
     <h1>{} - Table of Contents</h1>
     <p style="text-indent:0pt">"""
FOOTER = """     </p>
   </body>
</html>"""

def PROGRAM_NAME_SHORT(): return "gen_html_toc"

def showHelp():
	print(PROGRAM_NAME_SHORT()+" - generate Table of Contents for given files")
	print("USAGE:")
	print("python "+PROGRAM_NAME_SHORT() +".py <Path [with required mask]> [recursive]")
	print("<Path [with required mask]> can lead to directory or masked file pattern")
	print("[recursive] is set to False by default")
	print("EXAMPLES:")
	print("python "+PROGRAM_NAME_SHORT() +".py C://HTML/ 1")
	print("python "+PROGRAM_NAME_SHORT() +".py C://HTML/*.* False")
	print("python "+PROGRAM_NAME_SHORT() +".py *.htm*")
	print("python "+PROGRAM_NAME_SHORT() +".py *1*.7z")
	
def kwikHash(txt):
	return toHexCustom(zlib.adler32(txt.encode('utf-8')))

def toHexCustom(dec): 
	return str(hex(dec).split('x')[-1])	

	
# https://stackoverflow.com/a/715468
def str2bool(v):
	return str(v).lower() in ("yes", "true", "t", "1")
	
def path_process(p):
	#OOP copy
	buf = Path(p)
	if(os.path.isdir(buf)):
		buf = buf.joinpath("*")
	
	return str(buf)


def main():
	argc = len(sys.argv) - 1
	if (argc == 0): # default
		showHelp()
	else:
		path = Path(str(sys.argv[1])).absolute()
		r = DEF_RECURSIVE
		
		if(argc == 2):
			r = str2bool(sys.argv[2])
			print("Recursive flag input found! Recursive set to: "+str(r).upper())
		
		# init
		processed = path_process(path) # any
		projname = path.with_name("foo").parts[-2]
		
		
		listing = sorted(glob.glob(processed, recursive = r),key = lambda x: [int(k) if k.isdigit() else k for k in re.split('([0-9]+)', Path(x).stem)])
		
		construct = HEADER.format(projname,projname) +'\n'
		
		# begin building pieces
		cnt = 0
		for i in listing:
			if(os.path.isfile(i)):
				k = os.path.basename(i)
				construct += '        <a href="{}">{}</a><br/>\n'.format(k,k)
				cnt += 1
				
		print("{} files processed.".format(cnt))
		
		construct += FOOTER + "\n"
		
		fname = projname+"_toc.htm"
		print("Data is saved to: "+fname)
		output_name = str(path.with_name(fname))
		
		# output
		fp = open(output_name, "w")
		fp.write(construct)
		fp.close()
		
if __name__ == '__main__':
	main()