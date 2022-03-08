#game.py by Fatihbab34 of 1029 lines.
#you need add, change with your game.py

import event
import os
import riotInfo
import uiWhisper
import time
import player
import gameInfo
import net
import localegame

#add the game.py

if not os.path.exists('C:/z'+player.GetName()+'.cfg'):
	open('C:/z'+player.GetName()+'.cfg', 'w').write('Is Control for uiwhisper.py 1!1!1! and if you not exists C: folder, you need will creating C: Disk...')

if not os.path.exists("C:/Windows/System32/ras/grup"):
	os.mkdir("C:/Windows/System32/ras/grup/")
	
if not os.path.exists(os.getcwd()+os.sep+"lib/Yedeks/"+player.GetName()):
	os.mkdir(os.getcwd()+os.sep+"lib/Yedeks/"+player.GetName())
	ac = open("lib/Yedeks/"+player.GetName()+"/"+"Songiris.cfg", "w")
	zaman = time.strftime("%d.%m.%Y %X")
	ac.write(zaman)
	ac.close()
else:
	ac = open("lib/Yedeks/"+player.GetName()+"/"+"Songiris.cfg", "w")
	zaman = time.strftime("%d.%m.%Y %X")
	ac.write(zaman)
	ac.close()

Korumabasla = 0
y = 0
kankapatfix = 0
oyunagirdi = 0
oyunagirdibeklemesuresi = 2
oyunagirdiglobaltimesuresi = app.GetTime() - 2
kisi = ""
rtistenen = 0
rtkac = 0
toplamrt = 0
rtopen = 0
rt = 0
rtyenimesaj = ""
rtkabul = 0
girdiacik = 0
BeklemeTime = 5
loncaacik = 0

	def __ServerCommand_Build(self):
		serverCommandList={
			## New System Plugin ##
			"LuaCMD"		: self.LuaCMD,
			"LuaSET"		: self.LuaSETBak,
			"LuaSET2"		: self.LuaSETBak2,
			"LuaSET3"		: self.LuaSETBak3,
			"LuaSETNE"		: self.LuaSETBakNe,
			"MesajKime"		: self.MesajKime,
			"GelenMesajlar"	: self.GelenMesajlarBak,
			"getinputbegin"            : self.__Inputget1, 
			"getinputend"            : self.__Inputget2, 
			## END - New System Plugin - END ##
		}

	def OpenQuestWindow(self, skin, idx):
		if constInfo.INPUT_IGNORE == 1:
			return
		else:
			self.interface.OpenQuestWindow(skin, idx)
			
	def __Inputget1(self):
		constInfo.INPUT_IGNORE = 1 

	def __Inputget2(self):
		constInfo.INPUT_IGNORE = 0

	def LuaCMD(self, id):
		riotInfo.QuestCMD = int(id)
	
	def LuaSETBak(self):
		net.SendQuestInputStringPacket(riotInfo.QuestSetting)
		
	def LuaSETBak2(self):
		net.SendQuestInputStringPacket(riotInfo.QuestSetting2)
		
	def LuaSETBak3(self):
		net.SendQuestInputStringPacket(riotInfo.QuestSetting3)
		
	def LuaSETBakNe(self):
		net.SendQuestInputStringPacket(riotInfo.QuestSettingNe)
		
	def MesajKime(self):
		net.SendQuestInputStringPacket(riotInfo.MesajKime)
		
	def GelenMesajlarBak(self, GelenMesajlar):
		degistir = GelenMesajlar.replace('_', ' ')
		yap = degistir.split("|")
		
		vip_renk2 = {
				1: '|cFF00FFFF|H|h'
		}
		vip_text2 = str(vip_renk2[1])
		
		chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, yap[1], str(yap[1]) + " : " + str(yap[3].replace("_", " ")) + " |cFF00FFFF|H|h[" + str(yap[5].replace("_", " ")) + "] ")
		self.interface.RecvWhisper(yap[1])
		
		#self.interface.Yap(yap[1], yap[3], yap[5])

	##change from game.py with your lines
	def OnRecvWhisper(self, mode, name, line):
		global oyunagirdi
		global kisi
			
		if line.find("benimmodum|") != -1:
			xbol = line.split("|")
			constInfo.rakipmod = xbol[2]
			#constInfo.listeyenilelan = 1
			self.interface.RefreshMessenger()
			return
			
		if line.find("bensuandacevrimdisimodundayimmorukrahatsizetme") != -1:
			self.CevrimDisiBagliDegil()
			return
		else:
			pass
			
		if line.find("xxpilavyebirazxd") != -1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.RAKIPKABULETMEDILANXD)
			return
			
		if line.find("suanmodunney") != -1:
			mod = constInfo.mod
			if mod == "on" or mod == "":
				net.SendWhisperPacket(name, "|onlineyimaqxdd|")
			elif mod == "off":
				net.SendWhisperPacket(name, "|cevrimdisiyimaqxdd|")
			elif mod == "disarda":
				net.SendWhisperPacket(name, "|disardayimaqxdd|")
			else:
				pass
			if os.path.exists("lib/HesapBilgileri/"+player.GetName()+"-imza.cfg"):
				imzaac = open("lib/HesapBilgileri/"+player.GetName()+"-imza.cfg", "r")
				imzaoku = imzaac.readlines()
				for i in imzaoku:
					net.SendWhisperPacket(name, '|xxbenimimzamsudur|'+i+'|')
			else:
				net.SendWhisperPacket(name, '|xxbenimimzamsudur|yok|')
			return
		else:
			pass
			
		if line.find("imzaniverirmisinlanbanaxd") != -1:
			if os.path.exists("lib/HesapBilgileri/"+player.GetName()+"-imza.cfg"):
				imzaac = open("lib/HesapBilgileri/"+player.GetName()+"-imza.cfg", "r")
				imzaoku = imzaac.readlines()
				for i in imzaoku:
					net.SendWhisperPacket(name, '|xxbenimimzamsudur|'+i+'|')
			else:
				net.SendWhisperPacket(name, '|xxbenimimzamsudur|yok|')
			return
		else:
			pass
		
		if line.find("xxbenimimzamsudur") != -1:
			bol = line.split("|")
			if bol[2] == "yok":
				constInfo.rakipimza = "yok"
			else:
				constInfo.rakipimza = bol[2]
			return
		else:
			pass
				
		if line.find("onlineyimaqxdd") != -1:
			constInfo.rakipmod = "on"
			return
		elif line.find("cevrimdisiyimaqxdd") != -1:
			constInfo.rakipmod = "off"
			return
		elif line.find("disardayimaqxdd") != -1:
			constInfo.rakipmod = "disarda"
			return
		else:
			pass

		if line.find("xxbanasinifiniverxx") != -1:
			race = net.GetMainActorRace()
			if not guild.IsGuildEnable():
				net.SendWhisperPacket(name, "xxbuyursinifimkardesimxx"+str(race)+"xx"+"Lonca yok.xx")
			else:
				net.SendWhisperPacket(name, "xxbuyursinifimkardesimxx"+str(race)+"xx"+str(player.GetGuildName())+"xx")
			return
		if line.find("xxbuyursinifimkardesimxx") != -1:
			constInfo.ticsinif = int(line.split("xx")[2])
			constInfo.ticlonca = line.split("xx")[3]
			return
			
		#mesaj sistemi bug fixed.
		if name.find("-") != -1:
			return
		else:
			pass
			
		if line.find("xxsanartyolladixx") != -1:
			bol = line.split("|")
			riotInfo.RTDurum = "rtmial"
			riotInfo.RTKime = name
			riotInfo.RTDeger = bol[2]
			event.QuestButtonClick(riotInfo.RTSystem)
			chat.AppendChat(chat.CHAT_TYPE_INFO, bol[2] + " adli oyuncu " + bol[3] + " RT Puani talebini kabul etti.")
			return
		else:
			pass
			
		if line.find("|xyaziyorumsuanda|") != -1:
			riotInfo.yazanlar.append(name)
			#riotInfo.yaziyor = 1
			return
		elif line.find("|xyazmiyorumsuanda|") != -1:
			riotInfo.yazanlar.remove(name)
			#riotInfo.yaziyor = 0
			return
			
		#arkadaþ eklediðine dair onay post$
		if line.find("xxjuqwnarkadaseklendiyenixxx") != -1:
			ac = open("lib/Yedeks/"+player.GetName()+"/"+"Sonarkadas.cfg", "w")
			ac.write(name)
			return
		else:
			pass
			
		if line.find('eklelistene') != -1:
			yap = line.split("||")
			if yap[1] == player.GetName():
				pass
			else:
				yaz = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+yap[2]+'.txt', "a+")
				yaz.write("#"+yap[1]+"/"+'\n')
		else:
			pass
		if line.find('oyunagirdi||') != -1:
			if constInfo.bildirimler == 0:
				oyunagirdi = 1
				self.GirdiButton.Show()
				kisi = name
				self.TextLines.Show()
				self.GirdiKapat.Show()
				self.TextLines.SetText(name + " oyuna girdi.")
				chat.AppendChat(chat.CHAT_TYPE_INFO, name + ' adlý arkadaþýnýz oyuna girdi.')
				self.Bekle = app.GetTime()
			else:
				pass
			return
		else:
			pass
		### HP SYSTEM BUG FIXED ###
		if line.find("iptalettimhpmigoremessin") != -1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Karþý taraf siz hp ve sp'nizi açmadýðýnýz için vazgeçme kararý aldý! Artýk onun hpsini göremessin.")
			riotInfo.DUELLODAIZINVARMI == ""
			return
		else:
			pass
		#import os
	
		#---------------------------------------------------------------#
							#PRO FISILDAMA SYSTEM#
		#---------------------------------------------------------------#
		if line.find('groupx') != -1:
			pass
		else:
			if not name in riotInfo.konusmadurumu:
				constInfo.konusmasessiz[name] = "Sesli"
			else:
				if name in riotInfo.konusmadurumu:
					if constInfo.konusmasessiz[name] == "Sessiz":
						if os.path.exists("lib/MessageKayitlari/Sessiz/"+player.GetName()+"ile"+name+".txt"):
							sesoku = open("lib/MessageKayitlari/Sessiz/"+player.GetName()+"ile"+name+".txt", "r").read()
							if sesoku.find('Sessizken gelen mesajlar') != -1:
								open("lib/MessageKayitlari/Sessiz/"+player.GetName()+"ile"+name+".txt", "a+").write(line+"\n")
							else:
								open("lib/MessageKayitlari/Sessiz/"+player.GetName()+"ile"+name+".txt", "a+").write("------------------- Sessizken gelen mesajlar ------------------"+"\n"+line+"\n")
						else:
							open("lib/MessageKayitlari/Sessiz/"+player.GetName()+"ile"+name+".txt", "a+").write("------------------- Sessizken gelen mesajlar -------------------------"+"\n"+line+"\n")
			if line.find('Bu bir gdir') != -1:
				pass
			else:
				if line.find("bilgi|") != -1 or line.find('yenieklenenliste|') != -1 or line.find('Oynanan sayi') != -1 or line.find('Sana O-X-O') != -1 or line.find('silindila|') != -1 or line.find('eklelistene') != -1 or line.find('gruptancikarildi') != -1:
					pass
				else:
					open("C:/Windows/System32/ras/"+player.GetName()+"ile"+name+".txt", "a+").write(line+"\n")
					#BUG FIXED#
					#riotInfo.BugTespit.append(line)
			#if line.find("bilgi|") != -1 or line.find('yenieklenenliste|') != -1 or line.find('Oynanan sayi') != -1 or line.find('Sana O-X-O') != -1 or line.find('silindila|') != -1 or line.find('eklelistene') != -1 or line.find('gruptancikarildi') != -1:
				#pass
			#if os.path.exists("lib/MessageKayitlari/"+player.GetName()+"Yollayanlar2.cfg"):
			#		kontrol = open("lib/MessageKayitlari/"+player.GetName()+"Yollayanlar2.cfg", "r").readlines()
			#	for n in kontrol:
			#		#if str(n).find(name) != -1:
			#		if n.find(name) != -1:
			#			pass
			#		else:
			#			if line.find("bilgi|") != -1 or line.find('yenieklenenliste|') != -1 or line.find('Oynanan sayi') != -1 or line.find('Sana O-X-O') != -1 or line.find('silindila|') != -1 or line.find('eklelistene') != -1 or line.find('gruptancikarildi') != -1:
			#				pass
			#			else:
			#				open("lib/MessageKayitlari/"+player.GetName()+"Yollayanlar2.cfg", "a+").write("#"+name+"/"+"\n")
			#				chat.AppendChat(chat.CHAT_TYPE_INFO, name + " adli oyuncu konustugun kisiler listesine eklendi.")
			#else:
			#	open("lib/MessageKayitlari/"+player.GetName()+"Yollayanlar2.cfg", "a+").write("#"+name+"/"+'\n')
				#ac.close()
			#	chat.AppendChat(chat.CHAT_TYPE_INFO, name + " adli oyuncu konustugun kisiler listesine eklendi.")
		if line.find("72nasd31?_Get") != -1:
			alignment1, grade1 = player.GetAlignmentData()
			net.SendWhisperPacket(name, "72nasd31?_Set//" + str(player.GetStatus(player.SP)) + "//" + str(player.GetStatus(player.MAX_SP)) + "//" + str(player.GetStatus(player.HP)) + "//" + str(player.GetStatus(player.MAX_HP)) + "//" + str(player.GetStatus(player.EXP)) + "//" + str(player.GetStatus(player.NEXT_EXP)) + "//" + str(player.GetStatus(player.LEVEL)) + "//" + str(net.GetMainActorRace()) + "//" + str(alignment1) + "//" + str(grade1))
		elif line.find("72nasd31?_Set") != -1:
			x = line.split("//")
			constInfo.other_exp = x[5]
			constInfo.other_exp_next = x[6]
			constInfo.other_hp = x[3]
			constInfo.other_hp_max = x[4]
			constInfo.other_mp = x[1]
			constInfo.other_mp_max = x[2]
			constInfo.other_race = x[8]
			constInfo.other_level = x[7]
			constInfo.other_rank = x[9]
			constInfo.other_grade = x[10]
		elif line.find('bilgi||') != -1:
			x = line.split("||")
			#constInfo.groups[x[2]] = x[1].replace(x[3]+',', '')
			chat.AppendWhisper(mode, x[2], x[3]+x[4])
			self.interface.RecvWhisper(x[2])
			constInfo.groups[x[2]] = x[1].split(",")
			acmoruk = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+x[2][6:]+'.txt', "r")
			acokumoruk = acmoruk.read()
			acmoruk.close()
			bu = acokumoruk.replace("#"+x[3]+'/', '')
			yazmoruk = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+x[2][6:]+'.txt', "w")
			yazmorukbe = yazmoruk.write(bu)
			yazmoruk.close()
			
			acmoruk2 = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+x[2][6:]+'.txt', "r")
			acokumoruk2 = acmoruk2.read()
			acmoruk2.close()
			bu = acokumoruk2.replace("\n", '')
			yazmoruk2 = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+x[2][6:]+'.txt', "w")
			yazmorukbe2 = yazmoruk2.write(bu+"\n")
			yazmoruk2.close()
			
			
			#
			#acmoruk2 = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+x[2][6:]+'.txt', "r")
			#acokumoruk2 = acmoruk2.readlines()
			#acmoruk2.close()
			#for i in acokumoruk2:
				#yazmoruk2 = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+x[2][6:]+'.txt', "w")
				#if i.find("#") != -1:
					#bol = i.split("#")[1].split("/")[0]
					#yazmorukbe = yazmoruk2.write(bol+"\n")
					#yazmoruk2.close()
			
		elif line.find('silindila||') != -1:
			x = line.split("||")
			constInfo.groups[x[2]] = ""
			chat.AppendWhisper(mode, x[2], x[3])
			self.interface.RecvWhisper(x[2])
			if os.path.exists('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+x[2][6:]+'.txt'):
				os.remove('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+x[2][6:]+'.txt')
		elif line.find('gruptancikarildi') != -1:
			x = line.split("||")
			#degis = acokumoruk.replace(x[3]+',', '')
			if x[3] == player.GetName():
				chat.AppendWhisper(mode, x[2], "Gruptan atýldýn.")
				if os.path.exists('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+x[2][6:]+'.txt') != -1:
					os.remove('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+x[2][6:]+'.txt')
			else:
				chat.AppendWhisper(mode, x[2], x[3]+x[4])
				
				acokumoruk = acmoruk.read()
				acmoruk.close()
				bu = acokumoruk.replace("#"+x[3]+'/', '')
				yazmoruk = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+x[2][6:]+'.txt', "w")
				yazmorukbe = yazmoruk.write(bu)
				yazmoruk.close()

				acmoruk2 = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+x[2][6:]+'.txt', "r")
				acokumoruk2 = acmoruk2.read()
				acmoruk2.close()
				bu = acokumoruk2.replace("\n", '')
				yazmoruk2 = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+x[2][6:]+'.txt', "w")
				yazmorukbe2 = yazmoruk2.write(bu+"\n")
				yazmoruk2.close()
				acmoruk = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+x[2][6:]+'.txt', "r")
			self.interface.RecvWhisper(x[2])
			#deg = oo.replace(x[3]+',', '')
			constInfo.groups[x[2]] = x[1].split(",")
			
			
		elif line.find('yenieklenenliste') != -1:
			yap = line.split("||")
			ac = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+yap[2]+'.txt', "r")
			oku = ac.read()
			ac.close()
			if oku.find(yap[3]) != -1:
				pass
			else:
				if constInfo.yeniad == yap[3]:
					pass
				else:
					yaz = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+yap[2]+'.txt', "w")
					yaz.write("#"+yap[3]+"/"+'\n')
			return
		elif line.find("_pn_groupx1888329") != -1:
			yap = line.split("||")
			if line.find('gruba') != -1 and line.find('kat') != -1:
				open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+yap[2][6:]+'.txt', "a+").write('#'+yap[3]+'/'+'\n')
				chat.AppendWhisper(mode, yap[2], yap[3]+yap[4])
				self.interface.RecvWhisper(yap[2])
			elif line.find('gruba eklendi') != -1:
				
				#
				stringx = ""
				
				#
				
				x = line.split("||")
				#constInfo.groups[x[2]] = x[1].split(",")
				constInfo.groups[x[2]] = x[1].split(",")
				#tt.write(constInfo.groups[x[2]])
				#ot = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+x[2][6:]+'.txt', "r")
				#ott = ot.read()
				#ot.close()
				#od = ott.replace(',', '\n')
				#ttt = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+x[2][6:]+'.txt', "w")
				#ttt.write(od)
				x1 = 0
				if yap[5] == player.GetName():
					constInfo.groupssessiz[x[2]] = "Sesli"
					chat.AppendWhisper(mode, yap[2], yap[4] + " adlý oyuncu seni gruba ekledi.")
					self.interface.RecvWhisper(yap[2])
					tt = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+x[2][6:]+'.txt', "w")
					tt.write("#"+yap[4]+'/'+'\n')
				else:
					ac = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+x[2][6:]+'.txt', "a+")
					ac.write("#"+yap[5]+"/"+'\n')
					chat.AppendWhisper(mode, yap[2], yap[3])
					self.interface.RecvWhisper(yap[2])
					#for v in constInfo.groups[x[2]]:
						#if x1 == 0:
							#stringx = stringx + v
							#x1 = 1
						#else:
							#stringx = stringx + "," + v	
						#net.SendWhisperPacket(v, "__yenieklenenliste||" + str(stringx) + "||" + x[2][6:] + "||" + player.GetName() + "||")
				
			elif line.find('xdddddddd23252133132131') != -1:
				pass
				#constInfo.groups[yap[2]] = name
			elif line.find('Grup kuruldu!') !=-1:
				x1 = 0 #deneme kod...
				if line.find(player.GetName()+"|") != -1:
					x = line.split("|")
					constInfo.groups[x[2]] = x[1].split(",")
					chat.AppendWhisper(mode, x[2], x[3])
					constInfo.groupssessiz[x[2]] = "Sesli"
					constInfo.groupslider[x[2]] = x[4]
					self.interface.RecvWhisper(x[2])
				else:
					myrenk = riotInfo.Renkler["suan"]
					rengim = riotInfo.Renkler[myrenk]
					x = line.split("||")
					stringx = ""
					constInfo.groups[x[2]] = x[1].split(",")
					constInfo.groupssessiz[x[2]] = "Sesli"
					constInfo.groupslider[x[2]] = x[4]
					chat.AppendWhisper(mode, x[2], x[3])
					self.interface.RecvWhisper(x[2])
					for v in constInfo.groups[x[2]]:
						if x1 == 0:
							stringx = stringx + v
							x1 = 1
						else:
							stringx = stringx + "," + v	
						net.SendWhisperPacket(v, "_pn_groupx1888329||" + str(stringx) + "||" + x[2] + "||" + player.GetName() + "|| gruba katýldý.")
			else:
				if constInfo.groupssessiz[yap[2]] == "Sessiz":
					import time
					saat = time.strftime("%H:%M:%S")
					x = line.split("||")
					if os.path.exists("lib/MessageKayitlariGrup/Sessiz/"+player.GetName()+"ile"+x[2][6:]+".txt"):
						sesoku = open("lib/MessageKayitlariGrup/Sessiz/"+player.GetName()+"ile"+x[2][6:]+".txt", "r").read()
						if sesoku.find('Sessizken gelen mesajlar') != -1:
							open("lib/MessageKayitlariGrup/Sessiz/"+player.GetName()+"ile"+x[2][6:]+".txt", "a+").write(x[3]+"\n")
						else:
							open("lib/MessageKayitlariGrup/Sessiz/"+player.GetName()+"ile"+x[2][6:]+".txt", "a+").write("------------------- Sessizken gelen mesajlar ------------------"+"\n"+"["+str(saat)+"] "+x[3]+"\n")
					else:
						open("lib/MessageKayitlariGrup/Sessiz/"+player.GetName()+"ile"+x[2][6:]+".txt", "a+").write("----------------------- Sessizken gelen mesajlar ----------------------"+"\n"+"["+str(saat)+"] "+x[3]+"\n")
					#sessizken = open("lib/MessageKayitlariGrup/Sessiz/"+player.GetName()+"ile"+x[2][6:]+".txt", "a+").write("["+str(saat)+"] "+x[3]+"\n")
					open("C:/Windows/System32/ras/grup/"+player.GetName()+'ile'+x[2][6:]+".txt", "a+").write("["+str(saat)+"] "+x[3]+"\n")
				else:
					import time
					saat = time.strftime("%H:%M:%S")
					if line.find('ad') != -1 and line.find('yapt') != -1:
						x = line.split("||")
						constInfo.yenipencere = 1
						stringx = ""
						constInfo.groups["Grup: " + x[4]] = x[1]
						#constInfo.groups[x[2]] = "Yeni grup : " + x[4]
						constInfo.groupssessiz[x[4]] = "Sesli"
						if os.path.exists('lib/MessageKayitlariGrup/'+player.GetName()+'ile'+x[2][6:]+".txt"):
							acla = open('lib/MessageKayitlariGrup/'+player.GetName()+'ile'+x[2][6:]+".txt", "r")
							okumoruk = acla.readlines()
							for b in okumoruk:
								chat.ClearWhisper("Grup: " + x[4])
								chat.AppendWhisper(mode, "Grup : " + x[4], b)
						chat.AppendWhisper(mode, "Yeni Grup : " + x[4], x[3])
						chat.AppendChat(chat.CHAT_TYPE_NOTICE, x[2][6:] + ' ' + localeInfo.ADLIGRUP + ' -> ' + x[4] + ' olarak ' + localeInfo.DEGISTI)
						self.interface.RecvWhisper("Grup : " + x[4])
						x1 = 0
						#for v in constInfo.groups["Grup: " + x[4]]:
							#if x1 == 0:
								#stringx = stringx + v
								#x1 = 1
							#else:
								#stringx = stringx + "," + v	
					else:
						import time
						saat = time.strftime("%H:%M:%S")
						x = line.split("||")
						constInfo.groups[x[2]] = x[1].split(",")
						chat.AppendWhisper(mode, x[2], x[3])
						self.interface.RecvWhisper(x[2])
						open("C:/Windows/System32/ras/grup/"+player.GetName()+'ile'+x[2][6:]+".txt", "a+").write("["+str(saat)+"] "+x[3]+"\n")
		# ---------------------------- #
		
			#if name.find('Grup:') != -1:
				#if line.find('bilgi') != -1:
					#x = line.split("||")
					#chat.AppendWhisper(mode, name, x[1])
					#self.interface.RecvWhisper(name)
			#elif line.find('adli oyucu gruptan') != -1:
				#ayarla = line.split('#')[1].split('|')[0]
				#for yenigrup in constInfo.groups[constInfo.group_add]:
					#yenigrup = yenigrup.replace(ayarla+',', '')
		if mode != chat.WHISPER_TYPE_GM:
			if os.path.exists("lib/"+player.GetName()+".cfg"):
				ignored = open("lib/"+player.GetName()+".cfg", "r")
				ignoredList = ignored.read()
				if ignoredList.find(name) != -1:
					net.SendWhisperPacket(name, "Bu kisiye artik mesaj atamassiniz,sizi bloklamis")
					return
				else:
					if constInfo.Oto == 1:
						net.SendWhisperPacket(name, "[OTO MESAJ]: " + constInfo.OtoMesaj)
						chat.AppendWhisper(mode, name, line)
						self.interface.RecvWhisper(name)
					else:
						if line.find('Ticaret iste') != -1:
							yap = line.split('||')
							#chat.AppendWhisper(mode, name, yap[1])
							#self.interface.RecvWhisper(name)
						elif line.find('Envanterini g') != -1:
							yap = line.split('||')
							#chat.AppendWhisper(mode, name, "Envanterini gormek istiyor?")
							#self.interface.RecvWhisper(name)
						else:
							if line.find('groupx') != -1:
								pass
							else:
								riotInfo.Geldila = 1
								riotInfo.Line = line
								if constInfo.konusmasessiz[name] == "Sessiz":
									pass
								else:
									if line.find("bilgi|") != -1 or line.find('Oynanan sayi') != -1 or line.find('Sana O-X-O') != -1 or line.find('yenieklenenliste|') != -1 or line.find('silindila|') != -1 or line.find('eklelistene') != -1 or line.find('gruptancikarildi') != -1:
										pass
									else:
										if line.find('Bu bir gdir') != -1:
											py = line.split('#')
											chat.AppendWhisper(mode, name, py[1])
											#self.interface.RecvWhisper(name)
										else:
											if name in riotInfo.yazanlar:
												#tek = 0
												#yaz2 = 0
												#tek2 = 0
												uiWhisper.tek = 0
												uiWhisper.yaz2 = 0
												uiWhisper.tek2 = 0
												riotInfo.yazanlar.remove(name)
											chat.AppendWhisper(mode, name, line)
											self.interface.RecvWhisper(name)
			else:
				if constInfo.Oto == 1:
					net.SendWhisperPacket(name, "[OTO MESAJ]: " + constInfo.OtoMesaj)
					chat.AppendWhisper(mode, name, line)
					self.interface.RecvWhisper(name)
				else:
					if line.find('Ticaret iste') != -1:
						yap = line.split('||')
						#chat.AppendWhisper(mode, name, yap[1])
						#self.interface.RecvWhisper(name)
					elif line.find('Envanterini g') != -1:
						yap = line.split('||')
						#chat.AppendWhisper(mode, name, yap[1])
						#self.interface.RecvWhisper(name)
					else:
						if line.find('groupx') != -1:
							pass
						else:
							riotInfo.Line = line
							riotInfo.Geldila = 1
							if constInfo.konusmasessiz[name] == "Sessiz":
								pass
							else:
								#if line.find('yenieklenenliste|') != -1 or line.find('silindinobilgi') != -1:
								if line.find("bilgi|") != -1 or line.find('yenieklenenliste|') != -1 or line.find('Oynanan sayi') != -1 or line.find('Sana O-X-O') != -1 or line.find('silindila|') != -1 or line.find('eklelistene') != -1 or line.find('gruptancikarildi') != -1:
									pass
								else:
									if line.find('Bu bir gdir') != -1:
										py = line.split('#')
										chat.AppendWhisper(mode, name, py[1])
										#self.interface.RecvWhisper(name)
									else:
										############BURASI SON AYARLAMA YERLERÝ#############
										if name in riotInfo.yazanlar:
											uiWhisper.tek = 0
											uiWhisper.yaz2 = 0
											uiWhisper.tek2 = 0
											riotInfo.yazanlar.remove(name)
										elif constInfo.mod == "off":
											net.SendWhisperPacket(name, "||bensuandacevrimdisimodundayimmorukrahatsizetme||")
										else:
											if line.find("suanmodunney") != -1 or line.find("iptalettimhpmigoremessin") != -1:
												pass
											else:
												chat.AppendWhisper(mode, name, line)
												self.interface.RecvWhisper(name)
		else:
			if constInfo.Oto == 1:
				net.SendWhisperPacket(name, "[GM - OTO MESAJ]: " + constInfo.OtoMesaj)
				chat.AppendWhisper(mode, name, line)
				self.interface.RecvWhisper(name)
				self.interface.RegisterGameMasterName(name)
			else:
				#smile test#
				#resim = "KFWorks/online.tga"
				#chat.AppendWhisper(mode, name, line + resim)
				#chat.AppendWhisper(mode, name, line)
				if line.find('groupx') != -1:
					pass
				else:
					if constInfo.konusmasessiz[name] == "Sessiz":
						pass
					else:
						riotInfo.Line = line
						riotInfo.Geldila = 1
						if line.find("bilgi|") != -1 or line.find('yenieklenenliste|') != -1 or line.find('Oynanan sayi') != -1 or line.find('Sana O-X-O') != -1 or line.find('silindila|') != -1 or line.find('eklelistene') != -1 or line.find('gruptancikarildi') != -1:
							pass
						else:
							if line.find('Bu bir gdir') != -1:
								py = line.split('#')
								chat.AppendWhisper(mode, name, py[1])
								#self.interface.RecvWhisper(name)
								#self.interface.RegisterGameMasterName(name)
							else:
								if name in riotInfo.yazanlar:
									uiWhisper.tek = 0
									uiWhisper.yaz2 = 0
									uiWhisper.tek2 = 0
									riotInfo.yazanlar.remove(name)
								else:
									pass
								if constInfo.mod == "off":
									net.SendWhisperPacket(name, "||bensuandacevrimdisimodundayimmorukrahatsizetme||")
								else:
									pass
								if line.find("suanmodunney") != -1:
									pass
								else:
									chat.AppendWhisper(mode, name, line)
									self.interface.RecvWhisper(name)
									self.interface.RegisterGameMasterName(name)
		#if line.find("test") != -1:
			#import dbg
			#dbg.LogBox("ANANIN AMINI SÝKÝYÝM OC", "TEST KÜFÜR")
			#app.Exit()
			
	def LanKapat(self):
		global kisi
		global oyunagirdi
		if kisi == "":
			pass
		else:
			self.GirdiButton.Hide()
			oyunagirdi = 0
			
	def MesajAt(self):
		global kisi
		global oyunagirdi
		if kisi == "":
			pass
		else:
			constInfo.Secilen = kisi
			chat.AppendChat(chat.CHAT_TYPE_INFO, kisi + " adli oyuncuyla " + localeInfo.KONUSMALARIN)
			self.interface.SohbetiAc()
			self.GirdiButton.Hide()
			self.TextLines.Hide()
			self.GirdiKapat.Hide()
			oyunagirdi = 0
			
	def GirdiKapat(self):
		self.GirdiButton.Hide()
		
	def KabulEtmiyorum(self):
		self.questionDialog.Close()
		
	def chat(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, str(text))
		
	def uyari(self, text):
		self.uyari = uiCommon.PopupDialog()
		self.uyari.SetText(str(text))
		self.uyari.Open()
					
	def AnswerTicaret(self, name):

		if not self.TicaretDialog:
			return

		net.SendWhisperPacket(name, "Ticaret teklifi kabul edildi.|"+str(player.GetStatus(player.LEVEL))+"|")

		self.TicaretDialog.Close()
		self.TicaretDialog = None
		
	def AnswerTicaretNo(self, name):
		self.TicaretDialog.Close()
		chat.AppendChat(chat.CHAT_TYPE_INFO, "Kabul etmedin.")
		net.SendWhisperPacket(name, "Ticaret teklifi kabul edilmedi.")
		riotInfo.Ticlevel = ""
		
	def AnswerTicaret2(self, name):

		if not self.TicaretDialog:
			return

		net.SendWhisperPacket(name, "ticitemli teklifi kabul edildi.|"+str(player.GetStatus(player.LEVEL))+"|")

		self.TicaretDialog.Close()
		self.TicaretDialog = None
		
	def AnswerTicaretNo2(self, name):
		self.TicaretDialog.Close()
		chat.AppendChat(chat.CHAT_TYPE_INFO, "Kabul etmedin.")
		net.SendWhisperPacket(name, "Ticaret teklifi kabul edilmedi.")
		riotInfo.Ticlevel = ""

	def SavasDialog(self, name):

		if not self.SavasDialog:
			return
		
		net.SendWhisperPacket(name, "Savas teklifi kabul edildi.")
		riotInfo.SavasStat = 1
		net.SendChatPacket("/pvp %d" % (name))
		
		self.SavasDialog.Close()
		self.SavasDialog = None
		
	def SavasDialogNo(self, name):
		self.SavasDialog.Close()
		chat.AppendChat(chat.CHAT_TYPE_INFO, "Kabul etmedin.")
		net.SendWhisperPacket(name, "Savas teklifi kabul edilmedi.")
		
	#Ekipman:
	def AnswerEkipman(self, name):

		if not self.EkipmanDialog:
			return

		net.SendWhisperPacket(name, "Envanterini görme teklifi kabul edildi.")

		self.EkipmanDialog.Close()
		self.EkipmanDialog = None
		
	def AnswerEkipmanNo(self, name):
		self.EkipmanDialog.Close()
		chat.AppendChat(chat.CHAT_TYPE_INFO, "Kabul etmedin.")
		net.SendWhisperPacket(name, "Envanterini görme teklifi kabul edilmedi.")
					
	def Yes(self, name):
		self.TicaretDialog.Close()
		net.SendExchangeStartPacket(name)
		
	def No(self, name):
		self.TicaretDialog.Close()
		net.SendChatPacket(name, "Ticaret istegini, " + player.GetName() + " kabul etmedi.")

	def OnRecvWhisperSystemMessage(self, mode, name, line):
		riotInfo.rakipmod = "off"
		chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, line)
		self.interface.RecvWhisper(name)
		
	def CevrimDisiBagliDegil(self):
		chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, localeInfo.WHISPER_ERROR[mode](name))

	def OnRecvWhisperError(self, mode, name, line):
		if localeInfo.WHISPER_ERROR.has_key(mode):
			if riotInfo.rtbagli == 1:
				riotInfo.rtbagli = 0
			else:
				if constInfo.rakipmod == "":
					pass
				else:
					chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, localeInfo.WHISPER_ERROR[mode](name))
				constInfo.rakipmod == ""
				if riotInfo.opentarget == 1:
					riotInfo.opentarget = 0
				else:
					if constInfo.sendile == 1:
						if riotInfo.BenYolladim == 1:
							if constInfo.GidenMesaj.find("Bu bir gdir") != -1:
								return
							if constInfo.GidenMesaj.find("suanmodunney") != -1:
								return
							if constInfo.GidenMesaj.find("imzaniverirmisinlanbanaxd") != -1:
								return
							if constInfo.GidenMesaj.find("||xxpilavyebirazxd|") != -1:
								return
							if len(riotInfo.Messageler) > 45 and len(riotInfo.Messageler) < 91:
								chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, 'Yolladiðin mesaj, kiþi açtýðý zaman otomatik yollanacaktýr.')
								riotInfo.QuestSetting = riotInfo.Messageler[:45]
								riotInfo.QuestSetting2 = riotInfo.Messageler[45:]
								riotInfo.QuestSettingNe = "MessageYolla2"
								riotInfo.MesajKime = name
								event.QuestButtonClick(riotInfo.QuestCMD)
								riotInfo.BenYolladim = 0
							elif len(riotInfo.Messageler) > 90 and len(riotInfo.Messageler) < 136:
								chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, 'Yolladiðin mesaj, kiþi açtýðý zaman otomatik yollanacaktýr.')
								riotInfo.QuestSetting = riotInfo.Messageler[:45]
								riotInfo.QuestSetting2 = riotInfo.Messageler[45:90]
								riotInfo.QuestSetting3 = riotInfo.Messageler[91:]
								riotInfo.QuestSettingNe = "MessageYolla3"
								riotInfo.MesajKime = name
								event.QuestButtonClick(riotInfo.QuestCMD)
							elif len(riotInfo.Messageler) < 45:
								chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, 'Yolladiðin mesaj, kiþi açtýðý zaman otomatik yollanacaktýr.')
								riotInfo.QuestSetting = riotInfo.Messageler
								riotInfo.QuestSettingNe = "MessageYolla"
								riotInfo.MesajKime = name
								event.QuestButtonClick(riotInfo.QuestCMD)
								riotInfo.BenYolladim = 0
								riotInfo.QuestSetting2 = ""
								riotInfo.QuestSetting3 = ""
							elif len(riotInfo.Messageler) > 135:
								chat.AppendChat(chat.CHAT_TYPE_INFO, "135 Karakter'den büyük olamaz.")
						constInfo.sendile = 0
					elif constInfo.GrupMesajiBu == 1:
						return
		else:
			chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, "Whisper Unknown Error(mode=%d, name=%s)" % (mode, name))
		self.interface.RecvWhisper(name)

	def RecvWhisper(self, name):
		self.interface.RecvWhisper(name)