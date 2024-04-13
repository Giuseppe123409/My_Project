meme_dict = {
            "BOOMER": "Parola rivolta verso gli adulti che usano Facebook",
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            }
            
parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")
if parola in meme_dict.keys():
    # Cosa fare se la parola è stata trovata?
    print(meme_dict[parola])
else:
    # Cosa fare se la parola non è stata trovata?
    print("Non abbiamo tale parola")
