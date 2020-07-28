''' eredmenyek.csv
  0      1        2           3         4       5
hazai;idegen;hazai_pont;idegen_pont;helyszín;időpont
7up Joventut;Adecco Estudiantes;81;73;Palacio Mun. De Deportes De Badalona;2005-04-03
'''
class Kosár:
    def __init__(self,sor):
        s = sor.strip().split(';')
        hazai, idegen, hazai_pont, idegen_pont, helyszín, időpont = s
        self.hazai       = hazai
        self.idegen      = idegen
        self.hazai_pont  = int(hazai_pont)
        self.idegen_pont = int(idegen_pont)
        self.helyszín    = helyszín
        self.időpont     = időpont
# 2.
try:
    with open('eredmenyek.csv', encoding='utf-8') as f:
        fejléc = f.readline()
        lista  = [ Kosár(sor) for sor in f ]
except:
    with open('eredmenyek.csv', encoding='latin2') as f:
        fejléc = f.readline()
        lista  = [ Kosár(sor) for sor in f ]

# 3.
real_madrid_hazai  = sum( 1 for sor in lista if sor.hazai  == 'Real Madrid' )
real_madrid_idegen = sum( 1 for sor in lista if sor.idegen == 'Real Madrid' )
print(f'3. feladat: Real Madrid: Hazai: {real_madrid_hazai}, Idegen: {real_madrid_idegen}')

# 4.
döntetlenek_száma = sum( 1 for sor in lista if sor.hazai_pont == sor.idegen_pont )
res = 'igen' if döntetlenek_száma > 0 else 'nem'
print(f'4. feladat: Volt döntetlen? {res}')

# 5.
barcelonai = [ sor.hazai for sor in lista if 'Barcelona' in sor.hazai ][0]
print(f'5. feladat: barcelonai csapat neve: {barcelonai}')

# 6.
mérkőzések = [ sor for sor in lista if sor.időpont == '2004-11-21' ]
print( f'6. feladat:')
[print(f'        {sor.hazai}-{sor.idegen} ({sor.hazai_pont}:{sor.idegen_pont})') for sor in mérkőzések]

# 7.
statisztika = dict()

for sor in lista:
    stadion = sor.helyszín
    statisztika[stadion] = statisztika.get(stadion, 0) + 1

print( f'7. feladat:')
[print(f'        {helyszín}: {db}') for helyszín, db in statisztika.items() if db > 20 ]

                