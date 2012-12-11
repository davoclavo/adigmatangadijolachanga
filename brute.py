import requests
f = open('DICT.txt', 'r')
query = f.next().strip()

payload = {
  '01_solucion':  query,
  '02_rally':     'RALLYNAME',
  '03_accion':    'Enviar',
  '04_alpin':     'ALPIN#',
  '05_cod':       'STAGE#'
}

r = requests.get("http://www.adigma.com.mx/r/rally_rev.php", params=payload)
while r.text.find('no es satisfactoria') > -1:
    query = f.next().strip()
    payload['01_solucion'] = query
    print 'Probando: ' + query
    r = requests.get("http://www.adigma.com.mx/r/rally_rev.php",
                     params=payload)
    print 'Url: ' + r.url + ' - Code: ' + str(r.status_code)


print 'La respuesta es: ' + query
