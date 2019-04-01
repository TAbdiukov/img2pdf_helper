import os, sys, string, glob
import zlib
from pathlib import Path #PY3

import keyboard
import pyperclip

# not-really-an-import but ok
import img2pdf

def PROGRAM_NAME(): return "img2"
DELIMITER = " " #WHITESPACE
C34 = chr(34)

def example():
	return "img2pdf -o *n*.pdf -s *hor dpi*dpix*ver dpi*dpi *list*"

def toHexCustom(dec): 
	return str(hex(dec).split('x')[-1])	

def getModulePath(s):
	query = str(eval(s+".__file__")).strip()
	query_ext = query.split(".")[-1]
	if(query_ext=="py"):
		query = "python "+query
	return query
	
def kwikHash(txt):
	return toHexCustom(zlib.adler32(txt.encode('utf-8')))
	
def showHelp():
	print("img2 - img2pdf's wrapper on PY3 to help save to PDF losslessly")
	print("USAGE:")
	print("python "+PROGRAM_NAME() +".py <Path> <DPI>")

def path_process(p):
	#OOP copy
	buf = Path(p)
	if(buf.name==""):
		buf.with_name("*")
	
	return str(buf)

def main():
	argc = len(sys.argv) - 1
	if (argc == 0): # default
		showHelp()
	elif (argc == 2):
		#input
		path = Path(str(sys.argv[1]))
		dpi_pure = str(sys.argv[2])
	
		# error chk
		dpi_float = float(dpi_pure)
		if(dpi_float <= 0):
			raise ValueError("Invalid DPI")
					
		#init			
		processed = path_process(path) # any
		listing = glob.glob(processed, recursive=True)
		construct = ""
		
		# begin building pieces
		
		command = getModulePath("img2pdf")
		#help = eval("img2pdf -h")
		dpi_arg = dpi_pure+"dpix"+dpi_pure+"dpi"
		
		## input list process
		input_list = ""
		for i in listing:
			if(os.path.isfile(i)):
				input_list += C34+i+C34 +DELIMITER
		
		input_list = input_list[:-1] #remove trailing whitespace
		
		input_list_len = len(input_list)
		if(len(input_list)<= 0):
			raise ValueError("Nothing to process")			
		
		##Compute quick&dirty list hash
		input_list_hash = kwikHash(input_list)
		output_pdf_name = C34+str(path.with_name(input_list_hash+".pdf"))+C34
		
		# put pieces together
		#rearranged for further convenience
		construct = command+" "+input_list+" -o "+output_pdf_name+" -s "+dpi_arg 
		
		#output:
		
		#console
		keyboard.write(construct)#, delay=0.01)
		
		#file
		fname = input_list_hash+".txt"
		f = open(fname, "w+")
		f.write(construct)
		f.close()
		
		#clipboard [disabled]
		#pyperclip.copy(construct)
		
		#execute [disabled]
		#exec(construct)
		
		# print
		print("done ("+str(len(construct))+")")
		print(fname)

if __name__ == '__main__':
	main()