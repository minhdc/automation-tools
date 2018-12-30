from underthesea import word_tokenize, pos_tag
import constant
import os


def get_tagged_sentence_as_list(qa_as_dict):        
        tagged_sentences = []
        for k,v in qa_as_dict.items():                
                tagged_sentences.append(pos_tag(k))        
        return tagged_sentences

def get_tagged_sentence(sentence_as_string):
        return pos_tag(sentence_as_string)

def get_pattern_from_tagged_sentence(tagged_sentence):             
        temp = []
        for word,tag in tagged_sentence:
                if tag not in constant.EXCLUDING_TAGS:
                        temp.append(word)
        return '^ '+ ' ^ '.join(temp) + ' ^'




