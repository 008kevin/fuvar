class Fuvar:
    def __init__(self, id, startTime, idotartam, distance, price, tip, paymentType) -> None:
        self.id = id
        self.startTime = startTime
        self.idotartam = idotartam
        self.distance = distance
        self.price = price
        self.tip = tip
        self.paymentType = paymentType

fuvarList = []
f = open('fuvar.csv', 'rt', encoding='utf-8')
f.readline()
for line in f:
    line = line.strip().strip(';')
    fuvarList.append(Fuvar(line[0],line[1],line[2],line[3],line[4],line[5],line[6]))
f.close()

print(f"3. feladat: {len(fuvarList)} fuvar")