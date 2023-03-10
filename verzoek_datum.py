import io
from PyPDF2 import PdfReader
import datefinder

# Hiermee is het mogelijk om pdf's te lezen uit een pdfreader wellicht waardeloos, maar kan in sommige gevallen wellicht 
# wel handig blijken want soms is de verzoekdatum wel makkelijk te achthttps://open.overheid.nl/Details/ronl-b1ffb1d37c52ac6e77427cffeaf330381012b589/1#panel-teksterhalen (in uw brief van ... ) om maar een vb te noemen

def verzoek_datum(url):
    
    bools = []
    
    r = requests.get(url)
    f = io.BytesIO(r.content)
    
    try:
        reader = PdfReader(f)
    except:
        return np.nan

    # leest eerste pagina enige mogelijk nuttige pagina lijkt mij
    contents = reader.pages[0].extract_text().split('\n')
    contents = [content.strip() for content in contents]
    
    if contents == ['']:
        return "image"
    
    if any("betreft" in s.lower() for s in contents):
        bools.append(True)

    if any("datum" in s.lower() for s in contents):
        bools.append(True)

    if any(bools) == False:
        return np.nan
    

    
    matching = []
    possible_matches = ['in uw', 'inuw']
    for content in contents:
        if any(i in content.lower() for i in possible_matches) == True:
            matching.append(content)
    
    
    if matching == []:
        return np.nan
    
    # weird empty spaces that occur often will be removed
    matching = matching[0].split(' ')
    if '' in matching:
        matching = [i for i in matching if i != '']
    
    matching = ' '.join(matching)

    
    maanden = ['januari','februari','maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december']
    
    reg = re.findall(r"\b(0?[1-9]|[12][0-9]|3[01])\s?(:januari|februari|maart|april|mei|juni|juli|september|augustus|oktober|november|december)\s?(:19[7-9]\d|2\d{3})(?=\D|$)", matching)
    
    if reg == []:
        return np.nan
    
    reg = reg[0]

    for n in enumerate(maanden):
        if reg[1] == n[1]:
            reg = list(reg)
            if n[0] < 9:
                reg[1] = '0' + str(n[0] + 1)
            else:
                reg[1] = str(n[0] + 1)
    
    if len(reg[0]) == 1:
        reg[0] = '0' + reg[0]
    
    reg = '-'.join(reg)
    return reg

print(verzoek_datum('https://open.overheid.nl/documenten/ronl-33436ebbd0de54022e1a14caf5b601efca1b1e1b/pdf'))
