import sqlite3



def tokenize(text):
    text = text.replace("?"," ?")
    text = text.replace("!"," !")
    text = text.replace(", ","")

    sentences = text.lower().replace(".", "")

    tokenized_sentences = []


    return sentences.split(" ")

    #return tokenized_sentences
    # for sentence in tokenized_sentences:
    #     for word in sentence:
    #         print(word)

print("[+] Connecting to polimorf.db...")
conn2polimorf = sqlite3.connect('polimorf.db')
conn2polimorf.text_factory = str
cur2plimorf = conn2polimorf.cursor()

print("[+] Connecting to brain.db...")
conn2brain = sqlite3.connect('brain.db')
conn2brain.text_factory = str
cur2brain = conn2brain.cursor()

#Get data:
print("[+] Fetching all data from conversations...")

query = 'SELECT * FROM Conversations'
cur2brain.execute(query)

anses4brain = cur2brain.fetchall()



for a in anses4brain:
    #Generowanie polimorficznego zdania:
    normalised = []
    grammar = []
    sentence = a[0]
    print("[+] Parsing: "+sentence)
    tokens = tokenize(sentence)
    print("[+] Tokenised: "+str(tokens))
    for word in tokens:

        elements = (word,)
        query = 'SELECT * FROM polimorf_pure WHERE field1=(?)'
        cur2plimorf.execute(query, elements)
        anses4polimorf = cur2plimorf.fetchall()
        if not anses4polimorf:
            elements = (word.title(),)
            cur2plimorf.execute(query, elements)
            anses4polimorf = cur2plimorf.fetchall()


        if(anses4polimorf):
            normalised.append(str(anses4polimorf[0][1]))
            grammar.append(str(anses4polimorf[0][2].split(":")[0]))
        else:
            normalised.append(word)
            if word in "!?.":
                grammar.append(word)
            else:
                grammar.append("NULL")
    norm = " ".join(list(normalised))
    print("Normalised: "+norm)
    gram = ":".join(list(grammar))
    print("gramatyka: "+gram)

    t = (norm, gram,a[0],)
    query = "UPDATE Conversations SET normalized = (?), grammar = (?) WHERE Question = (?)"
    cur2brain.execute(query, t)

conn2brain.commit()
# t = (previousAns,question,previous_question)
# cur.execute("INSERT INTO Conversations VALUES (?, ?, ?)", t)
# conn.commit()
