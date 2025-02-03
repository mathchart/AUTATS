""" C:Users\Owner\Desktop\AUTATS\autats.py"""
""" Be auth standard starter template for my Python programs """
__author__ = "Joe Speier"
__email__ = "jspeier@xycharts.com"
__creation__ = 'Created 20250107, NLP #1'
__maintainer__ = 'jds'
__status__ = '8'

# support libraries
import random as r
import nltk as nl 
import os
import sys

#  function and global variables


def sample_function():
    """ This is the sample function header with
        doctest
    >>> sample_function()
    True
    """
    return True

class AlphFreq:
    def __init__(self,tit,author,lang,year):
        self.title = tit
        self.author = author
        self.lang = lang
        self.year = year
        self.alphFreq = {chr(c): [0,0] for c in range(97,123)}
    def __str__(self):
        return self.title+","+self.author+','+self.lang+','+self.year

def process_text(auth,fname):
    #with open(fname, 'r',encoding='utf-8') as f:
    try:
        with open(fname, 'r') as f:
            for line in f:
                words = line.split()
                for l in words:
                    for c in l:
                        if c in auth.alphFreq:
                            auth.alphFreq[c][0] += 1
    except FileNotFoundError:
        print(f"File {fname} not found.")
        raise
    except Exception as e:
        print (f"an error occurred: {e}")
        raise
                
def stats(tobj,fname):
    total = 0
    for i in tobj.alphFreq:
        total += tobj.alphFreq[i][0]

    print("Total letters ",total) 
    avgs = [0,0]
    totavg = 0

    for i in tobj.alphFreq:
        avg = tobj.alphFreq[i][0]/total
        tobj.alphFreq[i][1] = round(avg,3)
        #print(i,' is ',round(avg,3))
        totavg += round(avg,3)

    sFreq = sorted(tobj.alphFreq.items(),key=lambda x:x[1][1],reverse=True)
    # Use os.path to handle the file path and extract the base name 
    base_name = os.path.basename(fname)
    name_only = os.path.splitext(base_name)[0]
    try:
       with open(name_only + '.csv', 'w') as of:
         for i in sFreq:
            rec = i[0]+','+str(i[1][0])+','+str(i[1][1])+'\n'
            #print(rec)
            of.write(rec)
    except Exception as e:
        print(f"An error occurred while writing to file: {e}") 
        sys.exit(2) 

def main():
    #print(__author__)
    auth, fname = init()
    process_all(auth,fname)
    finish(auth, fname)

def init():
    fname = input("Enter file name: ")
    fname = "texts/"+fname+".txt"
    #Dname = r'texts/LordoftheFlies.txt'
    auth = AlphFreq('First Cat','Cicero','Latin','63 BC')
    return auth,fname
       
def process_all(auth, fname):
    try:
      process_text(auth, fname)
    except FileNotFoundError:
        print("Failed to process the file.")
        sys.exit(1)

def finish(auth, fname):
    #print(auth.alphFreq)
    stats(auth,fname)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    try:
        main()
    except SystemExit as e:
        print(f"Program exited with status: {e}")