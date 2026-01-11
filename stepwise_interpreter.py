#demo stepwise interpreter - proof of concept
# Demo text used for coginitive walkthroughs load reduction
# NOT for medical purposes!

#Note_to_me: tripple quotes for multi-line strings in Python
#            https://docs.python.org/3/tutorial/introduction.html#strings

example_text = """Betalning och anmälan
När du kommer till NU-sjukvården checkar du in och betalar via mobiltelefonen på vgregion.se/checkin eller självincheckningskiosk. Använd bank-id eller den självincheckningskod som du ser i kallelsen.
Det går även att anmäla sig och betala i receptionen i huvudentrén om du inte fått annat besked i din kallelse.
Det finns olika patientavgifter, beroende på vilken vård du får, och om du besöker en mottagning eller blir inlagd på sjukhuset. För besök och behandlingar på dagtid gäller högkostnadsskydd. All sjukvård för barn och ungdomar upp till och med 19 år är gratis, med undantag av hälsovård, vissa vacciner och vissa intyg.
Vi ser helst att du betalar med betalkort när du har tid hos en mottagning, men vi tar även emot kontanter. Blir du inlagd på sjukhuset får du en faktura efter din sjukhusvistelse.
Läs mer på 1177.se om patientavgifter och högkostnadsskydd."""

# Split the text into paragraph divisions.:

paragraph_divisions = example_text.split("\n\n")

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
  

print(paragraph_divisions)


