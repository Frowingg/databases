
# -*- coding: utf-8 -*-
"""
Uno dei meccanismi utilizzati per conservare e gestire grandi
quantità di dati è costituito dai database. Esistono tantissimi
tipi di database, ma quello che ha rivoluzionato il settore è
costituito dai database organizzati secondo il modello relazionale
teorizzato da Codd ormai mezzo secolo fa. Secondo questo modello
i dati sono organizzati in tabelle e relazioni fra di esse, in
modo da ottimizzare le richieste di memoria, favorire la coerenza
dei dati e minimizzare gli errori.

Dobbiamo progettare un insieme di funzioni che implementi una
semplice forma di database relazionale di una scuola di formazione
in cui ci sono quattro tabelle, ovvero students, teachers, courses
ed exams. I database sono di tre diverse dimensioni, ovvero small,
medium e large. Le tabelle del database di dimensione dbsize sono
salvate in quattro file json <dbsize>_<nometabella>.json (ad esempio,
il db small è composto dai file small_students.json, small_teachers.json,
small_courses.json e small_exams.json). Le tabelle sono organizzate in
liste di dizionari (si veda ad esempio small_students.json) e hanno le
seguenti strutture:
    - students: chiavi stud_code, stud_name, stud_surname, stud_email
    - teachers: chiavi teach_code, teach_name, teach_surname, teach_email
    - courses: chiavi course_code, course_name, teach_code
    - exams: chiavi exam_code, course_code, stud_code, date, grade.
La relazione fra le tabelle implica che ogni riga in ognuna delle
tabelle ha un riferimento ad un'altra tabella: ad esempio, un esame
(exam_code) corrisponde ad un voto (grade) dato da un docente
(teach_code) ad uno studente (stud_code) per aver sostanuto
l'esame di un certo corso (course_code) in una certa data (date). Ogni
studente può aver sostenuto diversi esami. Ogno docente può tenere
diversi corsi. Ogni corso è tenuto da un solo docente.

Il campo stud_code è una chiave primaria per la tabella students poiché
identifica univocamente uno studente, ovvero non esistono due studenti
con lo stesso stud_code. Similmente, teach_code, course_code ed exam_code
sono le chiavi primarie rispettivamente delle tabelle teachers, courses ed
exams. Per questo motivo, tali campi vengono utilizzati per realizzare
la relazione fra le tabelle.

Inoltre, i campi in tutte le tabelle non sono mai vuoti.

Dobbiamo realizzare alcune funzioni per poter interrogare i database delle
diverse dimensioni. Quindi, le funzioni prevedono di usare sempre il
parametro dbsize di tipo stringa, che può assumere i valori 'small',
'medium' e 'large'. Le funzioni sono:
    
    - media_studente(stud_code, dbsize), che riceve una stud_code di
      uno studente e ritorna la media dei voti degli esami sostenuti,
      dallo studente. --> da concludere
      
    - media_corso(course_code, dbsize), che riceve un identificatore per un
      corso e ritorna la media dei voti degli esami per quel corso,
      sostenuti da tutti gli studenti.
      
    - media_docente(teach_code, dbsize), che riceve un identificatore
      di un docente e ritorna la media dei voti per gli esami
      sostenuti in tutti i corsi del docente.
      
    - studenti_brillanti(dbisze), che ritorna la lista delle matricole
      (stud_code) con una media di esami sostenuti superiore o uguale a 28,
      ordinate in modo decrescente per media e, in caso di parità, in
      ordine lessicografico per il cognome e il nome dello studente. In
      caso di ulteriore parità, si usi il valore numerico dello stud_code
      in ordine crescente.  
      
    - stampa_esami_sostenuti(stud_code, fileout, dbsize), che riceve un
      numero di stud_code e salva nel file fileout la lista degli esami
      sostenuti dallo studente identificato dal valore stud_code.
      
      Le righe nel file devono essere ordinate in modo crescente
      per data di esame sostenuto e, in caso di stessa data, in ordine
      alfabetico. Il file ha una riga iniziale con il testo
       "Esami sostenuti dallo studente  <stud_surname> <stud_name>, matricola <stud_code>",
      mentre le righe seguenti hanno la seguente struttura
        "<course_name>\t<date>\t<grade>", in cui i campi sono allineati
      rispetto al nome del corso più lungo (ovvero tutte le date e
      i voti sono allineati verticalmente). La funzione ritorna
      il numero di esami sostenuti dallo studente.
      
    - stampa_studenti_brillanti(fileout, dbsize), che salva nel file
      fileout una riga per ogni studente con una media di esami
      sostenuti superiore o uguale a 28. Le righe nel file
      devono essere ordinate in modo decrescente per media e,
      in caso di parità, in ordine lessicografico per il
      cognome e il nome dello studente.
      Le righe nel file hanno la seguente struttura:
          "<stud_surname> <stud_name>\t<media>", in cui il valore media
      è allineato verticalmente per tutte le righe. La funzione
      ritorna il numero di righe salvate nel file.
      
    - stampa_verbale(exam_code, fileout, dbsize), che riceve un identificatore
      di esame e salva nel fileout le informazioni relative
      all'esame indicato, usando la seguente formula
        "Lo studente <stud_surname> <stud_name>, matricola <stud_code>, ha sostenuto in data <date> l'esame di <course_name> con il docente <teach_surname> <teach_name> con votazione <grade>."
      La funzione ritorna il voto dell'esame associato
      all'identificatore ricevuto in input.

Tutte le medie devono essere arrotondate alla seconda cifra decimale,
anche prima di ogni funzione di ordinamento.
Tutti i file devono avere encoding "utf8".
Per stampare agevolmente righe allineate considerare la funzione format con
i modificatori per l'allineamento (https://pyformat.info/#string_pad_align)
e con i parametri dinamici (https://pyformat.info/#param_align).
"""

import json

def media_studente(stud_code, dbsize):
    media_voti = 0
    divisore = 0
    with open(str(dbsize)+'_exams.json', "r") as f:
        dati = json.load(f)
    for elemento in dati:
        if elemento['stud_code'] == stud_code:
            divisore += 1
            media_voti += elemento['grade']             
    return round(media_voti/divisore, 2)

def media_corso(course_code, dbsize):
    media_voti = 0
    divisore = 0
    with open(str(dbsize)+'_exams.json', "r") as f:
        dati = json.load(f)
    for elemento in dati:
        if elemento['course_code'] == course_code:
              divisore += 1
              media_voti += elemento['grade']                
    return round(media_voti/divisore, 2)

def media_docente(teach_code, dbsize):
    media_voti = 0
    divisore = 0
    esami = []
    with open(str(dbsize)+'_courses.json', "r") as f:
        dati = json.load(f)
    with open(str(dbsize)+'_exams.json', "r") as f:
        dati2 = json.load(f)
    for elemento in dati:
        if elemento['teach_code'] == teach_code:
            esami.append(elemento['course_code'])                        
    for ele in dati2:
        if ele['course_code'] in esami:
            divisore += 1
            media_voti += ele['grade']           
    return round(media_voti/divisore, 2)

def stampa_verbale(exam_code, dbsize, fileout):
    with open(str(dbsize)+'_exams.json', 'r') as f:
        dati = json.load(f)
        for elemento in dati:
            if elemento['exam_code']  == exam_code:
                stud_code = elemento['stud_code']
                date = elemento['date']
                grade = elemento['grade']
                course_code = elemento['course_code']

    with open(str(dbsize)+'_students.json', 'r') as F:
        dati2 = json.load(F)
        for elemento in dati2:
            if elemento['stud_code'] == stud_code:
                stud_name = elemento['stud_name'] 
                stud_surname = elemento['stud_surname']    
    with open(str(dbsize)+'_courses.json', 'r') as f:
        dati3 = json.load(f)
        for elemento in dati3:
            if elemento['course_code'] == course_code:
                course_name = elemento['course_name'] 
                teach_code = elemento['teach_code']    
    with open(str(dbsize)+'_teachers.json', 'r') as f:
        dati4 = json.load(f)
        for elemento in dati4:
            if elemento['teach_code'] == teach_code: 
                teach_name = elemento['teach_name']
                teach_surname = elemento['teach_surname']
    contenuto = "Lo studente {} {}, matricola {}, ha sostenuto in data {} l'esame di {} con il docente {} {} con votazione {}.".format(stud_name, stud_surname, stud_code , date, course_name, teach_name,teach_surname,  grade)
    with open(fileout, 'w') as f:
          f.write(contenuto) 
    return fileout and grade

def stampa_esami_sostenuti(stud_code, dbsize, fileout):
    reg = {}
    with open(str(dbsize)+'_exams.json', 'r') as f:
        dati = json.load(f)
        for elemento in dati:
            if elemento['stud_code']  == stud_code:
                reg[elemento['course_code']] = elemento['date'], elemento['grade']
    reg = dict(sorted(reg.items(), key=lambda x: (x[1][0],x))) 
    registro_studente = {}
    with open(str(dbsize)+'_students.json', 'r') as f:
        dati= json.load(f)
        for elemento in dati:
                registro_studente[elemento['stud_code']] = elemento['stud_surname'], elemento['stud_name']
    reg_esami = {}
    with open(str(dbsize)+'_courses.json', 'r') as f:
        dati= json.load(f)
        lista = list(reg.keys())
        for elemento in dati:
            for x in range(len(lista)):
                if elemento['course_code'] == lista[x]:
                    reg_esami[elemento['course_code']] = elemento['course_name']        
    lista2 = list(reg.values())
    contenuto = """Esami sostenuti dallo studente {} {}, matricola {}\n""".format(registro_studente[stud_code][0], registro_studente[stud_code][1], stud_code)
    contenuto3 = ""
    reg_esami_sort = sorted(reg_esami.values(), key = len, reverse= True)
    for x in range(len(lista)):
        for key in reg:
            if lista[x] == key:
                    contenuto3 += '{:{align}{width}}\t{}\t{}\n'.format(reg_esami[key], lista2[x][0], lista2[x][1],align= '<',width=len(reg_esami_sort[0]))
    with open(fileout, 'w') as F:
            F.write(contenuto)
            F.write(contenuto3)
    return fileout and len(lista)                               
                        
def stampa_studenti_brillanti(dbsize, fileout):
    reg={}
    contenuto = ''
    min_28 = []
    mag_28 = {}
    with open(str(dbsize)+'_exams.json', 'r') as f:
        exams=json.load(f)
    with open(str(dbsize)+'_students.json', 'r') as f:
        students=json.load(f)
    for matricola in exams:
        if matricola['stud_code'] in min_28 or matricola['stud_code'] in mag_28:
            pass
        else:
            media = media_studente(matricola['stud_code'], dbsize)
            if media >= 28:
                mag_28[matricola['stud_code']] = media 
            else:
                min_28.append(matricola['stud_code'])
    for matricola_ in students:
            if matricola_['stud_code'] in mag_28:
                reg[matricola_['stud_code']]=(matricola_['stud_surname']+' '+matricola_['stud_name']),mag_28[matricola_['stud_code']]
            else:
                min_28.append(matricola['stud_code'])                
            if matricola['stud_code'] in min_28 or matricola['stud_code'] in mag_28:
                pass
            else:
                media = media_studente(matricola['stud_code'], dbsize)
                if media >= 28: 
                    mag_28[matricola['stud_code']] = media
                else:
                    min_28.append(matricola['stud_code']) 
    lunghezza_max=len(sorted(reg.values(), key= lambda x: len(x[0]), reverse = True)[0][0])    
    for ele in list(dict(sorted(reg.items(),key=lambda x:(-x[1][1],x[1][0])))):        
        contenuto += '{:{width}}\t{}\n'.format(reg[ele][0], reg[ele][1], width=lunghezza_max) 
    with open(fileout, 'w') as f:
        f.write(contenuto) 
    return fileout and len(reg)   
          
def studenti_brillanti(dbsize):
    reg={}
    min_28 = []
    mag_28 = {}
    with open(str(dbsize)+'_exams.json', 'r') as f:
        exams=json.load(f)
    with open(str(dbsize)+'_students.json', 'r') as f:
        students=json.load(f)  
    for matricola in exams: 
        if matricola['stud_code'] in min_28 or matricola['stud_code'] in mag_28:
            pass
        else:
            media = media_studente(matricola['stud_code'], dbsize)
            if media >= 28: 
                mag_28[matricola['stud_code']] = media
            else:
                min_28.append(matricola['stud_code']) 
    for matricola_ in students:
        if matricola_['stud_code'] in mag_28:
            reg[matricola_['stud_code']]=(matricola_['stud_surname']+' '+matricola_['stud_name']),mag_28[matricola_['stud_code']]
    return list(dict(sorted(reg.items(), key = lambda x: (-x[1][1],x[1][0],x))))

