import os, sys, string, glob
import zlib
from pathlib import Path #PY3

try:
	import keyboard
	import pyperclip
	
	# not-really-an-import but ok
	import img2pdf
except ImportError:
	print("="*25)
	print("pip install pyperclip keyboard img2pdf")
	print("="*25)

# Constants
DO = {
	"FILE": 0,
	"PREENTER": 1,
	"CLIPBOARD": 0,
	"EXEC": 0,
}
assert(1 in DO.values())

def VERSION(): return "1.2.0"
def PROGRAM_NAME(): return "img2"

DELIMITER = " " #WHITESPACE
C34 = chr(34)

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
	print(PROGRAM_NAME()+" v"+VERSION()+" - img2pdf's wrapper on PY3 to help save to PDF losslessly")
	print("USAGE:")
	print("python "+PROGRAM_NAME() +".py <Path> <DPI>")

def path_process(p):
	#OOP copy
	buf = Path(p)
	if(os.path.isdir(buf)):
		buf = buf.joinpath("*")
	
	return str(buf)
	
def list_all_do():
	for i, k in DO.items():
		print(f"\tDO - \t{i}: {k}")
	print("\r\n")


def main():
	argc = len(sys.argv) - 1
	if (argc == 2):
		#input
		path = Path(str(sys.argv[1]))
		dpi_pure = str(sys.argv[2])
	
		# error chk
		try:
			dpi_float = float(dpi_pure)
			assert(dpi_float > 0)
		except:
			raise ValueError("Invalid DPI")
					
		#init
		processed = path_process(path) # any
		listing = glob.glob(processed, recursive=True)
		construct = ""
		
		# Informational
		print("Mode of operation,")
		list_all_do()
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
		construct = '"'+command+'" '+input_list+" -o "+output_pdf_name+" -s "+dpi_arg 
		
		#output:
		
		#console
		if(DO["PREENTER"]):
			keyboard.write(construct)#, delay=0.01)
		
		#file
		if(DO["FILE"]):
			fname = input_list_hash+".txt"
			f = open(fname, "w+")
			f.write(construct)
			f.close()
		
		if(DO["CLIPBOARD"]):
			clipboard [disabled]
			pyperclip.copy(construct)
		
		if(DO["EXEC"]):
			execute [disabled]
			exec(construct)
		
		# print
		print("done ("+str(len(construct))+")")
		if(DO["FILE"]): print(fname)
	else:
		showHelp()

if __name__ == '__main__':
	main()