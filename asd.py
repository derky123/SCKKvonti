def olvas_es_szamol(fajl_nev, keresett):
    try:
        with open(fajl_nev, 'r', encoding='utf-8') as f:
            tartalom = f.read()
            sorok = tartalom.split('\n')
            db = sum(1 for sor in sorok if keresett in sor)
        return db
    except FileNotFoundError:
        print("A fájl nem található.")
    except UnicodeDecodeError:
        print("A fájl nem támogatott karakterkészletet használ.")

fajl_neve = "console-2023-12-25.log"
keresett_szoveg = "Wilson Soliver / TOW elfogadta a következő hívást:"
db = olvas_es_szamol(fajl_neve, keresett_szoveg)
print(f"A '{keresett_szoveg}' szöveg a fájlban {db} alkalommal fordul elő.")