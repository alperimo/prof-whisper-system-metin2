import uiCommon
import chat
import time
import os
import event
import riotInfo
import constInfo

Yeter = 0
siralama = 0
OkunmayanStat = 0
SecKapanmaDurum = 0
playerlar = []
tekliksiralama = 0

mod = 0
toplam = 0

	##search
	def OnUpdate(self):
		"bla bla bla..."
	#add
	def OnUpdate(self):
		global Yeter
		import riotInfo
		import os
		global siralama
		import chat
		
		if constInfo.mod == "" or constInfo.mod == "on":
			self.GetChild("durum").LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.mod == "off":
			self.GetChild("durum").LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif constInfo.mod == "disarda":
			self.GetChild("durum").LoadImage("d:/ymir work/ui/game/windows/messenger_list_mobile.sub")

	#search
	def RefreshCharacter(self):
		"bla bla bla..."
	#change
	def RefreshCharacter(self):

		if self.isLoaded==0:
			return

		try:
			characterName = player.GetName()
			guildName = player.GetGuildName()
			self.characterNameValue.SetText(characterName)
			self.guildNameValue.SetText(guildName)
			if not guildName:
				if localeInfo.IsARABIC():
					self.characterNameSlot.SetPosition(190, 34)
				else:
					self.characterNameSlot.LoadImage("d:/ymir work/ui/public/Parameter_Slot_03.sub")
					self.characterNameSlot.SetPosition(109, 34)

				self.guildNameSlot.Hide()
			else:
				if localeInfo.IsJAPAN():
					self.characterNameSlot.SetPosition(143, 34)
				else:
					self.characterNameSlot.LoadImage("d:/ymir work/ui/public/Parameter_Slot_01.sub")
					self.characterNameSlot.SetPosition(153, 34)
				self.guildNameSlot.Show()
		except:
			import exception
			exception.Abort("CharacterWindow.RefreshCharacter.BindObject")
			
	#search
	def RefreshStatus(self):
		"bla bla bla..."
	#change
	def RefreshStatus(self):
		global playerlar
		global SecKapanmaDurum
		global OkunmayanStat
		global tekliksiralama
		
		if self.isLoaded==0:
			return
		
		try:
			self.GetChild("sec").SetEvent(ui.__mem_func__(self.Sec))
			
			empire_color = {
				1: '|cFFFF0000|H|h',
				2: '|cFFFFFF00|H|h',
				3: '|cFF0080FF|H|h'
				}
			empire_name = {
				1: 'Kirm.',
				2: 'Sari',
				3: 'Mavi',
				}
				
			playerlar = []
			
		except:
			pass

	""" new add function your uicharacter.py """
	def Sec(self):
		global mod
		if mod == 0:
			constInfo.modduzenle = 1
			self.ChannelListBase = ui.SlotBar()
			self.ChannelListBase.SetParent(self)
			self.ChannelListBase.AddFlag("float")
			self.ChannelListBase.SetSize(120+10, 80+20+15+70+45+5+30-60 - 140+15)
			self.ChannelListBase.SetPosition(153 + 95 + 15 - 15 - 20 - 60 - 30 - 30, 25+6+2 + 12+10)
			self.ChannelListBase.Show()
			
			self.ChannelList = ui.ListBoxScroll()
			self.ChannelList.SetParent(self.ChannelListBase)
			self.ChannelList.SetSize(self.ChannelListBase.GetWidth(), self.ChannelListBase.GetHeight())
			self.ChannelList.SetPosition(0, 0)
			self.ChannelList.SetEvent(ui.__mem_func__(self.__ModSec))
			self.ChannelList.Show()
			
			self.on = ui.ExpandedImageBox()
			self.on.SetParent(self.ChannelListBase)
			self.on.SetPosition(7, 5)
			self.on.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
			self.on.Show()
			
			self.off = ui.ExpandedImageBox()
			self.off.SetParent(self.ChannelListBase)
			self.off.SetPosition(7, 15+8)
			self.off.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
			self.off.Show()
			
			self.disarda = ui.ExpandedImageBox()
			self.disarda.SetParent(self.ChannelListBase)
			self.disarda.SetPosition(7, 15+15+10)
			self.disarda.LoadImage("d:/ymir work/ui/game/windows/messenger_list_mobile.sub")
			self.disarda.Show()
			
			self.ChannelList.InsertItem(1, localeInfo.ONLINE)
			self.ChannelList.InsertItem(2, localeInfo.OFFLINE)
			self.ChannelList.InsertItem(3, localeInfo.DISARDA)
			self.ChannelList.InsertItem(4, localeInfo.IMZADEGIS)
			
			mod = 1
			
		else:
			self.ChannelListBase.Hide()
			mod = 0
			constInfo.modduzenle = 0
			
	def __ModSec(self):
		global mod
		import chat
		secilkontrol = self.ChannelList.GetSelectedItem()
		secilen = self.ChannelList.GetSelectedItemAdi()
		if secilen.find("evrim") != -1:
			if constInfo.mod == "on" or constInfo.mod == "":
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.ZATENONLINESIN)
				return
			elif constInfo.mod == "off":
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OFFLINEDENONLINEYE)
			elif constInfo.mod == "disarda":
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DISARDADANONLINEYE)
			constInfo.mod = "on"
			self.ChannelListBase.Hide()
			mod = 0
		elif secilen.find("mez") != -1:
			if constInfo.mod == "on" or constInfo.mod == "":
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.ONLINEDENGORUNMEZE)
			elif constInfo.mod == "off":
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.ZATENOFFLINESIN)
				return
			elif constInfo.mod == "disarda":
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DISARDADANGORUNMEZE)		
			constInfo.mod = "off"
			self.ChannelListBase.Hide()
			mod = 0
		elif secilen.find("Uzakta") != -1:
			if constInfo.mod == "on" or constInfo.mod == "":
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.ONLINEDENDISARIYA)
			elif constInfo.mod == "off":
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OFFLINEDENDISARIYA)
			elif constInfo.mod == "disarda":
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.ZATENDISARDASIN)
				return
			constInfo.mod = "disarda"
			self.ChannelListBase.Hide()
			mod = 0
		elif secilen.find("mza") != -1 and secilen.find("tir") != -1:
			if os.path.exists("lib/HesapBilgileri/"+player.GetName()+"-imza.cfg"):
				oku = open("lib/HesapBilgileri/"+player.GetName()+"-imza.cfg", "r")
				okua = oku.readlines()
				self.inputDialog = uiCommon.InputDialogWithDescription()
				self.inputDialog.SetMaxLength(90)
				self.inputDialog.SetAcceptEvent(lambda arg=TRUE: self.__Yeniad())
				self.inputDialog.SetCancelEvent(ui.__mem_func__(self.__Yeniadyapma))
				self.inputDialog.SetTitle(localeInfo.YENIAD)
				self.inputDialog.SetText(okua)
				self.inputDialog.SetDescription(localeInfo.IMZAGIRIN)
				self.inputDialog.Open()
				self.ChannelListBase.Hide()
				mod = 0
			else:
				self.inputDialog = uiCommon.InputDialogWithDescription()
				self.inputDialog.SetMaxLength(90)
				self.inputDialog.SetAcceptEvent(ui.__mem_func__(self.__Yeniad))
				self.inputDialog.SetCancelEvent(ui.__mem_func__(self.__Yeniadyapma))
				self.inputDialog.SetTitle(localeInfo.YENIAD)
				self.inputDialog.SetText(localeInfo.IMZAYOK)
				self.inputDialog.SetDescription(localeInfo.IMZAGIRIN)
				self.inputDialog.Open()
				self.ChannelListBase.Hide()
				mod = 0
				
	def __Yeniad(self):
		import chat
		imza = self.inputDialog.GetText()
		if imza == "" or len(imza) < 2:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.IMZAYIDOGRU)
		else:
			if os.path.exists("lib/HesapBilgileri/"+player.GetName()+"-imza.cfg"):
				oku = open("lib/HesapBilgileri/"+player.GetName()+"-imza.cfg", "r")
				okua = oku.readlines()
				if imza == okua:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.ESKIIMZAILEAYNI)
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.IMZADEGISTI)
					yaz = open("lib/HesapBilgileri/"+player.GetName()+"-imza.cfg", "w")
					yaz.write(imza)
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.IMZADEGISTI)
				yaz = open("lib/HesapBilgileri/"+player.GetName()+"-imza.cfg", "w")
				yaz.write(imza)
			self.inputDialog.Close()
			
	def __Yeniadyapma(self):
		self.inputDialog.Close()