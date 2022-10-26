import MeCab
import unidic

bad_list = ["バカ", "アホ"]

def analayze(input):
    
    flag_var = 0
    
    tagger = MeCab.Tagger("-Owakati")
    tagger_split = tagger.parse("バカでアホ").split()
    for letter in tagger_split:
        if letter in bad_list:
            flag_var = 1
            
    if flag_var == 1:
        return "flag"
    else:
        return "safe"