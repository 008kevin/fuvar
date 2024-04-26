class Fuvar:
    def __init__(self, id, startTime, idotartam, distance, price, tip, paymentType) -> None:
        self.id = int(id)
        self.startTime = startTime
        self.idotartam = idotartam
        self.distance = distance
        self.price = float(price.replace(',', '.'))
        self.tip = float(tip.replace(',', '.'))
        self.paymentType = paymentType

fuvarList = []
f = open('fuvar.csv', 'rt', encoding='utf-8')
f.readline()
for line in f:
    line = line.strip().split(';')
    fuvarList.append(Fuvar(line[0],line[1],line[2],line[3],line[4],line[5],line[6]))
f.close()

print(f"3. feladat: {len(fuvarList)} fuvar")

fuvarCount = 0
incomeCounter = 0
for fuvar in fuvarList:
    if fuvar.id == 6185:
        fuvarCount += 1
        incomeCounter += fuvar.price + fuvar.tip
print(f"4. feladat: {fuvarCount} fuvar alatt: {str(incomeCounter).replace('.',',')}$")