# next step: # PoC: Stepwise text interpreter
# Current status: Sprint 2 (in progress)
# What works: Text is split into paragraphs and sentences and printed stepwise.
# started to sort sentences into steps based on patterns

# What needs to be done:
# assemble definitions for stepwise interpretation (def is_new_step and def split_into_steps)

# Next step:
# - Improve sentence splitting so that one instruction = one step
# - Concider handling simple break words: "eller", "om", "annars"
# Rule of thumb:
# - Prefer too many short steps over long, heavy ones


# ============================================================
# STEPWISE INTERPRETER – ARBETSPLAN (checklista)
# Följ stegen i ordning. Ett steg i taget. Kör koden efter varje.
# ============================================================

# [ ] Steg 0 – Versionering & trygg start
#     - Spara filen som: stepwise_poc_v1.py
#     - Lägg versionskommentar högst upp (t.ex. "# v1 – baseline")

# [ ] Steg 1 – Få koden att alltid köra
#     - Se till att paragraph_divisions faktiskt skapas
#     - Inga NameError eller krascher
#     - Output visar minst "Paragraph 1"

# [ ] Steg 2 – Robust stycke-delning
#     - Dela text på tom rad
#     - Trimma whitespace
#     - Filtrera bort tomma stycken
#     - Kontrollera med print(paragraph_divisions)

# [ ] Steg 3 – Stabil meningsdelning
#     - Byt från ". " till regex
#     - Dela på . ! ? följt av mellanslag ELLER radbrytning
#     - Undvik avancerad NLP – håll det enkelt

# [ ] Steg 4 – Hantera skiljetecken korrekt
#     - Lägg inte automatiskt till punkt
#     - Kontrollera om meningen redan slutar med . ! ?

# [ ] Steg 5 – Koppla in stepwise-logiken
#     - Skapa: steps = []
#     - Skapa: current_step = ""
#     - Loop genom meningar:
#         - Om is_new_step(sentence):
#             - spara current_step (om ej tom)
#             - starta nytt steg
#         - Annars: fortsätt på current_step
#     - Spara sista steget efter loopen

# [ ] Steg 6 – Snygg och läsbar output
#     - Skriv ut:
#         1) Steg 1
#         2) Steg 2
#     - Fokus: kognitivt lätt att läsa

# [ ] Steg 7 – Mini-test
#     - Testa med minst två olika texter
#     - En med många radbrytningar
#     - En med "Det går även att..." / "Du kan också..."

# Regel:
# ✔ Gör bara ETT steg åt gången
# ✔ Kör koden
# ✔ Spara filen
# ✔ Gå vidare först när output känns rimlig



