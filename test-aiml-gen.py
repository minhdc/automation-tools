from xcel_to_aiml import get_xlsx_files, create_and_fill_single_aiml_file, read_xlsx_file
from aiml_autogen import get_tagged_sentence, get_pattern_from_tagged_sentence
import constant
import os

list_of_xcel_files = get_xlsx_files(constant.INPUT_XCEL_FILES)

for each in list_of_xcel_files:
    content_as_dict = read_xlsx_file(os.path.join(constant.INPUT_XCEL_FILES,each))
    pattern_template_as_dict = {}
    for k,v in content_as_dict.items():
        if '^' in k or '#' in k or '_' in k or '*' in k :
            pattern_template_as_dict[k] = v            
        else:
            question = get_tagged_sentence(k)
            #print(question)
            pattern = get_pattern_from_tagged_sentence(question)
            #print(k)
            #print(pattern)
            pattern_template_as_dict[pattern] = v
        
    create_and_fill_single_aiml_file(each,constant.OUTPUT_AIML_FILES,pattern_template_as_dict)