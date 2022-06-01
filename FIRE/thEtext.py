def get_text(text:str):
    LETTERS = "abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ. !"
    letters = "asÆCBxfnMJqKGIHPgøELXyeVåkpFr.OTNlAcRYidSbvQWØUtohmZÅDæwzju !"
    new_text = ""
    for i in text:
        for m, n in enumerate(letters):
            if i == n:
                new_text += LETTERS[m]
                break
    return new_text