from xml.dom import minidom
from math import radians, cos, sin, asin, sqrt
doc = minidom.parse("transmilenio.xml")
estacion = doc.getElementsByTagName("nombre")

class Item():
  def __init__(self, obj, obj2, obj3, obj4, obj5):
    self.item = obj
    self.geoLat = obj2
    self.geoLong = obj3
    self.tipo = obj4
    self.troncal = obj5
    self.nxtc = None
    self.prvc = None
    self.nxtd = None
    self.prvd = None

class ListDynamic(object):
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
    self.headD = None
    self.tailD = None
    self.sizeD = 0

  def add_element(self, ele, b, c, d, e):
    new_item = Item(ele, b, c, d, e)
    if new_item.troncal=="C":
        if self.size == 0:
          self.head = new_item
          self.tail=new_item
          aux = self.head
          aux.nxtc=self.tail
          aux2 = self.tail
          aux2.prvc=self.head
        elif self.size == 1:
          self.tail = new_item
          aux=self.head
          aux2=self.tail
          aux.nxtc=self.tail
          aux2.prvc=self.head
        else:
          aux3 = self.head
          while(aux3.nxtc != None):
            aux3 = aux3.nxtc
          self.tail = new_item
          aux3.nxtc = self.tail
          aux2=self.tail
          aux2.prvc=aux3
        self.size += 1
    elif new_item.troncal=="D":
        if self.sizeD == 0:
          self.headD = new_item
          self.tailD=new_item
          aux = self.headD
          aux.nxtd=self.tailD
          aux2 = self.tailD
          aux2.prvd=self.headD
        elif self.sizeD == 1:
          self.tailD = new_item
          aux=self.headD
          aux2=self.tailD
          aux.nxtd=self.tailD
          aux2.prvd=self.headD
        else:
          aux3 = self.headD
          while(aux3.nxtd != None):
            aux3 = aux3.nxtd
          self.tailD = new_item
          aux3.nxtd = self.tailD
          aux2=self.tailD
          aux2.prvd=aux3
        self.sizeD += 1



  def print_list(self):
    item = self.head
    g=0
    if self.size > 0:
        g=self.size
    for i in range(g):
      print(item.item)
      print(item.geoLat)
      print(item.geoLong)
      print(item.tipo)
      print(item.troncal)
      print("--")
      item =  item.nxtc
    print("-------------------\n")

  def printinv_list(self):
    item = self.tail
    g=0
    if self.size > 0:
        g=self.size
    for i in range(g):
      print(item.item)
      print(item.geoLat)
      print(item.geoLong)
      print(item.tipo)
      print(item.troncal)
      print("--")
      item =  item.prvc
    print("-------------------\n")

  def print_listD(self):
      item = self.headD
      g=0
      if self.sizeD > 0:
          g=self.sizeD
      for i in range(g):
        print(item.item)
        print(item.geoLat)
        print(item.geoLong)
        print(item.tipo)
        print(item.troncal)
        print("--")
        item =  item.nxtd
      print("-------------------\n")

  def printinv_listD(self):
      item = self.tailD
      g=0
      if self.sizeD > 0:
          g=self.sizeD
      for i in range(g):
        print(item.item)
        print(item.geoLat)
        print(item.geoLong)
        print(item.tipo)
        print(item.troncal)
        print("--")
        item =  item.prvd
      print("-------------------\n")


  def calcular(self, ori, des):
      origen=ori
      destino=des
      lat1=0.0
      lon1=0.0
      lat2=0.0
      lon2=0.0
      aux4 = self.head
      aux5=self.headD
      aux6 = self.head
      aux7=self.headD
      m=self.size
      n=self.sizeD
      for i in range(m):
          if aux4.item==origen:
              lat1=aux4.geoLat
              lon1=aux4.geoLong
              break
          else:
              aux4=aux4.nxtc

      for i in range(n):
          if aux5.item==origen:
              lat1=aux5.geoLat
              lon1=aux5.geoLong
              break
          else:
              aux5=aux5.nxtd


      for i in range(m):
          if aux6.item==destino:
              lat2=aux6.geoLat
              lon2=aux6.geoLong
              break
          else:
              aux6=aux6.nxtc

      for i in range(n):
          if aux7.item==destino:
              lat2=aux7.geoLat
              lon2=aux7.geoLong
              break
          else:
              aux7=aux7.nxtd
      print(lista.haversine(lon1,lat1,lon2,lat2))


  def haversine(self,lon1, lat1, lon2, lat2):

    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r




lista = ListDynamic()

todasEst = doc.getElementsByTagName("estacion")
print("-----")
for estacion in todasEst:
    nombre=estacion.getElementsByTagName("nombre")[0]
    latitud = estacion.getElementsByTagName("latitud")[0]
    longitud = estacion.getElementsByTagName("longitud")[0]
    tipo=estacion.getElementsByTagName("tipo")[0]
    troncal=estacion.getElementsByTagName("troncal")[0]
    a = nombre.firstChild.data
    b = latitud.firstChild.data
    c = longitud.firstChild.data
    b=float(b)
    c=float(c)
    d = tipo.firstChild.data
    e = troncal.firstChild.data
    lista.add_element(a, b, c, d, e)


op=0
while ((op < 1) or (op > 6)):
    print("\n 1) Imprimir Troncal Suba\n 2) Imprimir Troncal Suba invertida\n 3) Imprimir Troncal Cl 80\n 4) Imprimir Troncal Cl 80 invertida\n 5) Calcular distancia\n 6) Salir")
    op=int(input("\n --Escoge una opcion: "))
    if op==1:
        lista.print_list()
        op=0
    if op==2:
        lista.printinv_list()
        op=0
    if op==3:
        lista.print_listD()
        op=0
    if op==4:
        lista.printinv_listD()
        op=0
    if op==5:
        origen =input("\n Escriba la estación de origen: ")
        destino=input("\n Escriba la estación de destino: ")
        print("\nLa distancia entre las dos estaciones es:")
        lista.calcular(origen, destino)
        op=0
