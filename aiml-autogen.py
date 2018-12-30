from xcel_to_aiml import read_xlsx_file, get_xlsx_files
from underthesea import word_tokenize, pos_tag
import constant
import os


input_excel_files = get_xlsx_files(constant.INPUT_XCEL_FILES)

qa_as_dict = read_xlsx_file(os.path.join(constant.INPUT_XCEL_FILES,input_excel_files[3]))

tokenized_sentences = []
tagged_sentences = []
excluding_tags = ['C','Cc','CH','E','Fw','FW','I','L','M','P','S','T','X','Z']

for k,v in qa_as_dict.items():
    tokenized_sentences.append(word_tokenize(k))
    tagged_sentences.append(pos_tag(k))


for each in tagged_sentences:
    temp = []
    for word,tag in each:
        if tag not in excluding_tags:
            temp.append(word)
    print(word_tokenize(temp,format="text"))