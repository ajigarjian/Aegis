#To Do: 1. Apply same logic to tables 2. add in suggested alternatives (add front parentheses). 
#region IMPORT & SETUP SECTION

#Importing packages
import spacy
import docx
from spacy.matcher import Matcher
from helpers import *
from docx.enum.text import WD_COLOR_INDEX

nlp = spacy.load("en_core_web_sm")

# endregion END IMPORT & SETUP SECTION


#takes in a docx Document, integer action flag, and optional str author, and returns nothing (but creates the new docx document).
def scan(docx, filename, action_flag, author="Aegis"):


    #Populate 'docs' dictionary where keys are the paragraph and the values are spaCy nlp paragraphs' text
    docs = {}
    for index, paragraph in enumerate(docx.paragraphs):
        docs[index] = (nlp(paragraph.text))

    # Initialize the matcher with the shared vocab using "matcher" function from helpers.py
    matcher, rationales = matching(nlp)

#region ACTUAL MATCHING SECTION

    #docmatches is a list of tuples - each tuple is a span (word or phrase) that was matched, and the paragraph # it is in
    docmatches = []

    # Calls the matcher on each paragraph to get the list of span matches, and then appends each paragraph's matches to a master list along with its paragraph number
    for paragraph, text in docs.items():
        paragraph_matches = matcher(text, as_spans=True)
        for span in paragraph_matches:
            docmatches.append((span, paragraph))

#endregion ACTUAL MATCHING SECTION

#region ALTERING WORD DOCX SECTION
    
    for index, match in enumerate(docmatches):
        run = isolate_run(docx.paragraphs[docmatches[index][1]], docmatches[index][0].start_char, docmatches[index][0].end_char)

        #decision branching options:

        if action_flag == 0:
            run.font.highlight_color = WD_COLOR_INDEX.YELLOW
        if action_flag == 1:
                run.add_comment((rationales[docmatches[index][0].label_])[0] + rationales[docmatches[index][0].label_][1], author=author)
        if action_flag == 2:
                run.add_comment((rationales[docmatches[index][0].label_])[0], author=author)
        if action_flag == 3:
                run.add_comment((rationales[docmatches[index][0].label_])[1], author=author)
        if action_flag == 4:
                run.add_comment("", author=author)


    #testing
    docx.save('/Users/arijigarjian/Documents/GitHub/NIST-Scanner/static/input_output_files/Output' + str(action_flag) + '.docx')
    #prod
    # docx.save('/Users/arijigarjian/Documents/GitHub/NIST-Scanner/static/input_output_files/' + filename)

#endregion ALTERING WORD DOCX SECTION

