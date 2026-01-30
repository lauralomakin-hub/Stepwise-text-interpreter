#demo stepwise interpreter - proof of concept
# Demo text used for coginitive walkthroughs load reduction
# Target user: people who get cognitively overloaded by dense instructions (e.g. NPF, stress, fatigue)
# Scope limit: does NOT interpret meaning, make decisions, or give advice — only splits and orders text
#              NOT for medical purposes!

#Note_to_me: tripple quotes for multi-line strings in Python
#            https://docs.python.org/3/tutorial/introduction.html#strings

# TODO (future): add optional LLM step to rewrite each step in calm, simplified language


example_text = """Betalning och anmälan
När du kommer till NU-sjukvården checkar du in och betalar via mobiltelefonen på vgregion.se/checkin eller självincheckningskiosk. Använd bank-id eller den självincheckningskod som du ser i kallelsen.
Det går även att anmäla sig och betala i receptionen i huvudentrén om du inte fått annat besked i din kallelse.
Det finns olika patientavgifter, beroende på vilken vård du får, och om du besöker en mottagning eller blir inlagd på sjukhuset. För besök och behandlingar på dagtid gäller högkostnadsskydd. All sjukvård för barn och ungdomar upp till och med 19 år är gratis, med undantag av hälsovård, vissa vacciner och vissa intyg.
Vi ser helst att du betalar med betalkort när du har tid hos en mottagning, men vi tar även emot kontanter. Blir du inlagd på sjukhuset får du en faktura efter din sjukhusvistelse.
Läs mer på 1177.se om patientavgifter och högkostnadsskydd."""

import re

# Normalize line breaks before any text interpretation.
# Text copied from PDF/web often contains mixed \r and \n.

example_text = example_text.replace("\r\n", "\n").replace("\r", "\n") 

# Split the text into paragraph divisions.:

paragraph_divisions = example_text.split("\n\n")




# Define patterns for stepwise interpretation (currently not used).
# Define on Sentencestarts like "du kan också/även", "man kan även/också", "det går också/även att" that indicate additional instructions.

PATTERNS = [
    r"^\s*du\s+kan\s+(?:\w+\s+)?(?:också|även)\b",
    r"^\s*du\s+kan\s+(?:också|även)\b",
    r"^\s*man\s+kan\s+(?:\w+\s+)?(?:också|även)\b",
    r"^\s*det\s+går\s+(?:också|även)\s+att\b",
]

# Function to check if a sentence indicates a new step following PATTERNS above.

def is_new_step(sentence: str) -> bool:       #"sentence: str" is a typehint for string, function returns True/False
    cleaned_sentence = sentence.strip().lower()
    return any(re.search(pattern, cleaned_sentence) for pattern in PATTERNS)

#loop through paragraphs 
for paragraph_index, paragraph in enumerate(paragraph_divisions):
    print(f"Paragraph {paragraph_index + 1}:\n")
    # Split the paragraph into sentences.
    sentences = paragraph.split(". ")
    
    # Loop through sentences in the paragraph.
    for sentence_index, sentence in enumerate(sentences):
        # Add a period back if it was removed during splitting.
        if not sentence.endswith("."):
            sentence += "."
        print(f"  Sentence {sentence_index + 1}: {sentence}")
    print("\n")  # Add a newline for better readability between paragraphs
  
#print(repr(example_text))
print(paragraph_divisions)

