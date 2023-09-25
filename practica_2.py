import stanza

stanza.download('es')  # Comentar esta línea después de la primera ejecución

# Crear un pipeline NLP para el idioma español con los procesadores especificados
nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma')


def process_line(line):
    """Función para tokenizar y lematizar una línea."""
    doc = nlp(line)
    sentences_tokens_lemmas = []

    for sentence in doc.sentences:
        tokens_lemmas = []
        for word in sentence.words:
            tokens_lemmas.append((word.id, word.text, word.lemma))
        sentences_tokens_lemmas.append(tokens_lemmas)

    return sentences_tokens_lemmas


# Leer el contenido del archivo línea por línea y procesarlo
processed_content = []

with open("pinocho.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        processed_line = process_line(line.strip())
        if processed_line:
            processed_content.extend(processed_line)  # Usamos extend para añadir todas las frases de la línea

# Guardar el contenido original y procesado en un nuevo archivo
with open("pinocho_resultado.txt", "w", encoding="utf-8") as file:
    # Escribir el contenido original primero
    with open("pinocho.txt", "r", encoding="utf-8") as original:
        file.write(original.read())
    file.write("\n\n--- Resultado Tokenizado por Frases ---\n\n")

    for idx, sentence in enumerate(processed_content, start=1):
        file.write(f"----------\n")
        file.write(f"Frase {idx} tokenizada\n")
        for token_id, token, lemma in sentence:
            file.write(f"id: {token_id} | token: {token} | lema: {lemma}\n")
        file.write("\n")  # Salto de línea entre frases tokenizadas

print("El contenido original y procesado ha sido guardado en pinocho_resultado_1.txt")
