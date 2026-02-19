
# v1 – baseline

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

# # Split text into paragraphs by empty lines (robust to extra whitespace from PDF/web text).
# Trims each paragraph and removes empty entries:

paragraph_divisions = [p.strip() for p in re.split(r"\n\s*\n", example_text) if p.strip()]




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
    # Split paragraph into sentences using a rule-based approach.
    # A sentence boundary is defined as:
    # - punctuation (. ! ?) followed by whitespace AND a capital letter, OR
    # - one or more line breaks.
    # This avoids splitting inside URLs or domain names (e.g. "1177.se/checkin").   
    sentences = re.split(r"(?<=[.!?])\s+(?=[A-ZÅÄÖ])|\n+", paragraph.strip())
    
    title = ""
    if sentences:
        first = sentences[0].strip()
        first_lower = first.lower() #check if first sentence is title
        
        looks_like_instruction = first_lower.startswith(
            ("när ", "om ", "du ", "ni ", "det ", "vi ", "blir ", "läs ", "använd ")
            )
        is_short_enough = 1 <= len(first.split()) <= 10
        ends_like_sentence = first.endswith((".", "!", "?"))

        if(
            not looks_like_instruction and
            is_short_enough and
            not ends_like_sentence
        ):
            title = sentences.pop(0)
        



    steps = []
    current_step = ""

    # Loop through sentences in the paragraph.
    for sentence_index, sentence in enumerate(sentences):
        sentence = re.sub(r"\s+", " ", sentence).strip()  # Normalize whitespace within sentences
        if is_new_step(sentence) and current_step:        #if sentence indicates new step and current_step is not empty
            steps.append(current_step)                    #save current step
            current_step = sentence                       #start new step with current sentence
        else:                        #if current_step is not empty
            if not current_step:     #if current_step is empty
                current_step = sentence      #start new step
            else:
                current_step += " " + sentence  #continue current step
    if current_step:
        steps.append(current_step)  #save last step after loop

    if title:
        print(title)
    print("Steps: ")
    for i, step in enumerate(steps, start= 1):
        print(f" {i}. {step}")
    print("\n")  # Add a newline for better readability between paragraphs

