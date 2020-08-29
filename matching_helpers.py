###
###     Functions commonly used for matching artists/metadata/reviews
###

import pandas as pd


def std_actors_names(series) : 
    return series.str.lower()
    
def std_actors_names_list(liste) : 
    return std_actors_names(pd.Series(liste)).tolist()


def cleanstr(string) : 
    tmp = string.lower().split('(')[0].split(')')[0].split('|')[0].replace('\\', ' ')
    res = ''
    for w in tmp.split(' '): 
        if len(w)>0 :
            res = res+' '+w
    res = res[1:]
    return res

def clean_comas(list_):
    ''' fix for unclosed parenthesis screwing up regex
    '''
    clean_ = []
    for word in list_:
        clean_.append(word.split('(')[0].replace('(','').replace(')',''))
    return clean_

def df_rm_punctuation(df, columns=None) : 
    # Check arguments
    if columns == None : 
        columns = df.columns
    else :
        # todo
        raise NotImplementedError
    # process column by column
    res = pd.DataFrame(columns=columns)
    for col in columns : 
        res[col] = _serie_rm_punctuation(df[col])
    return res


def clean_serie(serie) : 
    _serie_rm_punctuation(serie)
    
def a() : 
    print("a    ")


########################################################################
## Private helpers

def _serie_rm_punctuation(series_):
    return series_.str.replace("[", "").str.replace("]","")\
                    .str.replace("'","").str.replace(".","")\
                    .str.replace(", ",",").str.replace('"','')\

