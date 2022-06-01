"""
BEKLENİLENLER;
1---Oyunda kontrol edebildigimiz 1 karakter

2---Karakterimize zarar veren engeller

3---SKORUMUZU CANLI TAKİP ETMEMİZİ SAĞLAYABİLSİN

4---Skor belli bir seviyeye ulaştığında kazandınız mesajini gör

5---Engellere çarptığında kaybettiniz mesajini gör

6---Subway surf havası estir

ALGORİTMA;

1----Yarıs SINIFINI OLUŞTUR

2---Yarıs SINIFINA PARAMETRELERİYLE BİRLİKTE EMİR GELİR İSE BAŞLAT 

3---BAŞLANGIÇ HIZLARINI SELF.X (X ÇİZGİSİ ÜZERİNDEKİ HIZI) OLARAK AYARLA

4---FONKSİYONLARI OLUŞTUR

5---FONKSİYONLARİN YARDİMİ İLE KARAKTERİ CİZ

6---RANDOM BİR DEĞER OLUŞTUR VE BU DEĞERİ Yarıs SINIFIMIZDA BELİRTTİĞİMİZ FONKSİYONA SELF ET (SELF.X = RANDOM DEĞERİMİZ)

7--- OYUN DURUMU BELİRT 0 = OYUN DEVAM EDİYOR 1 = KARAKTER KalemYA CARPTİ 2= OYUNU KAZANDI

8---OYUN DONGUSUNU BAŞLAT
"""
from tkinter import *
import random
import time
from PIL import ImageTk
import datetime
import threading
sorgu = 0
sayac = 0
syy =0
sorgu2 = 0
i = 0
class Yarıs:
	def __init__(self, Araba, Dusmanlar, canvas, Arkaplan):
		self.canvas = canvas
		self.Araba = Araba
		self.Dusmanlar = Dusmanlar
		self.ArkaPlan = Arkaplan
		self.idAraba= canvas.create_image(500, 850, image = self.Araba)
		self.canvas.bind_all('<KeyPress-d>', self.Sag)
		self.canvas.bind_all('<KeyPress-a>', self.Sol)
		self.canvas.bind_all('<KeyPress-s>', self.superguc)
		self.x = 0
		self.y = 0
	def Ciz(self):
		self.canvas.move(self.idAraba, self.x, self.y) 
		Koordinat = self.canvas.coords(self.idAraba)
		#print(Koordinat)
		if Koordinat[0] == 1000 or Koordinat[0] == 20:
			self.x = 0
			self.y = 0
		if self.Kalems(Koordinat) == True: 
			self.canvas.move(self.ArkaPlan,0,0)
	def Durum(self):
		Koordinat = self.canvas.coords(self.idAraba)
		if self.Kalems(Koordinat) == True:
			return 1
	def Fin(self):
		Koordinat = self.canvas.coords(self.ArkaPlan)
		return Koordinat
		Koordinat = skor
	def Sag(self, event): 
		Koordinat = self.canvas.coords(self.idAraba)
		if Koordinat[0] != 1000:
			self.x = 20
	def Sol(self, event): 
		Koordinat = self.canvas.coords(self.idAraba)
		if Koordinat[0] != 10:
			self.x = -20
	def superguc(self,event):
		t1 = threading.Thread(target=yap1, args = ("self", "event"))
		t1.start()
	def Kalems(self, pos):
		self.KalemKoor = {}
		for ai in range(0, 70):
			self.KalemKoor[ai] = self.canvas.coords(self.Dusmanlar.idKalem[ai])

			if pos[0] > self.KalemKoor[ai][0] - 130 and pos[0] < self.KalemKoor[ai][0] +130:
					if pos[1] - 37 < self.KalemKoor[ai][1] +37 and pos[1] + 37 > self.KalemKoor[ai][1] - 37:
						return True
class Kalem:
	def __init__(self, canvas, BoruResim):
		self.idKalem = {} 
		for ai in range(0,70):
			startsX = float(random.randint(200,800))
			startsY = float(random.randint(-10000,0))
			self.idKalem[ai] = canvas.create_image(startsX, startsY, image = BoruResim)
	def Ciz(self):
		for ai in range(0, 30):
			a = ai + 0.01
			canvas.move(self.idKalem[ai],0,a); 
tk = Tk()
tk.title('SPİDERMAN 8 YAZİLİM HAREKETİ') 
canvas = Canvas(tk, width=1080, height=2340, bd=0, highlightthickness=0)
ArkaPlan = ImageTk.PhotoImage(file = "assets/background.png")
idArkaPlan = canvas.create_image(0, -4500, image = ArkaPlan, anchor = NW)
canvas.pack()
tk.update()
KalemResim = PhotoImage(file = 'assets/dusman.png')
ArabaResim = PhotoImage(file = 'assets/player.png')
Kalem = Kalem(canvas, KalemResim)
Yarıs = Yarıs(ArabaResim, Kalem, canvas, idArkaPlan)
Durum_0_1_2 = 0;
while 1:
	def skor():
		canvas.create_text(70, 100, text="Skorunuz = ", font=("Arial", 5), fill="white",tags="yw13")
		global i
		if sorgu2 == 0:
			canvas.create_text(160, 100, text=i, font=("Arial", 5), fill="white",tags="yw11")
			i = i +1
			time.sleep(0.0001)
		if sorgu2 == 1:
			canvas.create_text(160, 100, text=i, font=("Arial", 5), fill="white",tags="yw12")
	canvas.delete("yw11")
	skor()
	if Durum_0_1_2 == 0: 
		canvas.move(idArkaPlan,0, 10); #ARKA PLANI HAREKET ETTİRİYORUZ
		Kalem.Ciz(); #ELEMANLARI OLUŞTURUYORUZ
		Yarıs.Ciz();
		def yap1(self,event):
			global sorgu #özel güç uyguladık
			sorgu = 1
			time.sleep(5)
			sorgu = 0
			time.sleep(15)
		if sorgu == 1:
			canvas.create_text(500, 200,text="Özel güç Devam ediyor... 5 saniyen var", font=("Arial", 10), fill="white" ,tags="yazi43")
			if Yarıs.Durum() == 99:
				Durum_0_1_2 = 1;
				canvas.create_text(500, 200, text="Kaybettin", font=("Arial", 20), fill="red")
			if Yarıs.Fin()[1] > 5000:
				Durum_0_1_2 = 2;
				canvas.create_text(500, 200, text="Kazandın", font=("Arial", 20), fill="green")
		else:
			canvas.delete("yazi43")
			if Yarıs.Durum() == 1:
				sorgu2 = 1
				Durum_0_1_2 = 1;
				canvas.create_text(500, 200, text="Kaybettin", font=("Arial", 20), fill="red")
			if Yarıs.Fin()[1] > 5000:
				Durum_0_1_2 = 2;
				canvas.create_text(500, 200, text="Kazandın", font=("Arial", 20), fill="green")
	tk.update_idletasks()
	tk.update()
	time.sleep(0.01)
