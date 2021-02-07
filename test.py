iban = input('Enter a IBAN: ')
# Valid IBAN: GB82 WEST 1234 5698 7654 32

pyletter_dic = {"AL": 28, "AD": 24, "AT": 20, "AZ": 28, "BH": 22, "BY": 28, "BE": 16, "BA": 20, "BR": 29, "BG": 22, "CR": 22,
              "HR": 21, "CY": 28, "CZ": 24, "DK": 18, "DO": 28, "TL": 23, "EG": 29, "SV": 28, "EE": 20, "FO": 18, "FI": 18,
              "FR": 27, "GE": 22, "DE": 22, "GI": 23,
              "GR": 27, "GL": 18, "GT": 28, "HU": 28, "IS": 26, "IQ": 23, "IE": 2, "IL": 23, "IT": 27, "JO": 30,
              "KZ":20,"XK":20,"KW":30,"LV":21,"LB":28,"LY":25,"LI":21,"LT":20,"LU":20,
              "MK":19,"MT":31,"MR":27,"MU":30,"MC":27,"MD":24,"ME":22,"NL":18,"NO":15,"PK":24,
              "PS":29,"PL":28,"PT":25,"QA":29,"RO":24,"LC":32,"SM":27,"ST":25,
              "SA":24,"RS":22,"SC":31,"SK":24,"SI":19, "ES":24,"SE":24,"CH":21,
              "TN":24,"TR":26,"UA":29,"AE":23,"GB":22,"VA":22,"VG":24, "A":10,"B":11,"C":12,"D":13,"E":14,"F":15,
              "G":16,"H":17,"I":18,"J":19,"K":20,"L":21,"M":22,"N":23,"O":24,
              "P":25,"Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,"W":32,"X":33,"Y":34,"Z":35}

nospace = "".join(iban.split())
first_4chars = nospace[0:4]
final = nospace.replace(first_4chars, '')
final += first_4chars
if not(iban[:2] in pyletter_dic.keys() and len(iban)==pyletter_dic.get(iban[:2])):
    print('Character check failed, skipping Digit check')
    exit()

temp = ''
for letter in final:
    if letter in pyletter_dic.keys():
        temp+=str(pyletter_dic[letter])
    else:
        temp+=letter

final = int(temp)
modulo = final % 97

if modulo == 1:
    print("Digit check passed. IBAN might be valid!")
else:
    print(modulo)
    print("Digit check failed. IBAN is not valid!")