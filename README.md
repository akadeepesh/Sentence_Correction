# Sentence_Correction
## Grammar and Spelling Corrector
### This Python script uses the `gingerit` library to interact with the Ginger grammar checker API. It retrieves text from the clipboard using `pyperclip`, converts it to lowercase, and parses it using `GingerIt`. The conversion was important because the Gingetit model works better on lowercase words. The script then retrieves the corrected text from the parser, capitalizes it, and copies it back to the clipboard using `pyperclip`.
