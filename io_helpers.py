####
####    IO helpers for the ADA project
####
####


import pandas as pd
import gzip



''' This function was provided on the amazon dataset's webpage
    It loads a gzipped file directly into a dataframe
'''
def json_gz_to_dataframe(filepath):
    def parse(path): 
        g = gzip.open(path, 'rb') 
        for l in g: 
            yield eval(l) 
    def getDF(path): 
        i = 0 
        df = {} 
        for d in parse(path): 
            df[i] = d 
            i += 1 
        return pd.DataFrame.from_dict(df, orient='index') 
    return getDF(filepath)

# wrapper for compatibility    
def gz_to_dataframe(filepath) :
    return json_gz_to_dataframe(filepath)
    
    
def read_txt(path) :
    #Returns the lines of a .txt file, with '\n' characters removed 
    
    file = open(path, "r")
    tmplist = file.read().split("\n")# the last line is an empty line 
    return tmplist[:len(tmplist)-1]    
