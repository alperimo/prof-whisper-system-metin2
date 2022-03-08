#Prof Whisper System, V.2.6
#by Fatihbab34™

import time
import os
import riotInfo
import constInfo
import uiWhisper
import event
import snd

#change from interfacemodule.py with your lines

	#####################################################################################

	#####################################################################################
	### Whisper ###

	def __InitWhisper(self):
		chat.InitWhisper(self)

	def OpenWhisperDialogWithoutTarget(self):
		if not self.dlgWhisperWithoutTarget:
			dlgWhisper = uiWhisper.WhisperDialog(self.MinimizeWhisperDialog, self.CloseWhisperDialog)
			dlgWhisper.BindInterface(self)
			dlgWhisper.LoadDialog()
			dlgWhisper.OpenWithoutTarget(self.RegisterTemporaryWhisperDialog)
			dlgWhisper.SetPosition(self.windowOpenPosition*30,self.windowOpenPosition*30)
			dlgWhisper.Show()
			self.dlgWhisperWithoutTarget = dlgWhisper

			self.windowOpenPosition = (self.windowOpenPosition+1) % 5

		else:
			self.dlgWhisperWithoutTarget.SetTop()
			self.dlgWhisperWithoutTarget.OpenWithoutTarget(self.RegisterTemporaryWhisperDialog)

	def RegisterTemporaryWhisperDialog(self, name):
		if not self.dlgWhisperWithoutTarget:
			return

		btn = self.__FindWhisperButton(name)
		if 0 != btn:
			self.__DestroyWhisperButton(btn)

		elif self.whisperDialogDict.has_key(name):
			oldDialog = self.whisperDialogDict[name]
			oldDialog.Destroy()
			del self.whisperDialogDict[name]

		self.whisperDialogDict[name] = self.dlgWhisperWithoutTarget
		self.dlgWhisperWithoutTarget.OpenWithTarget(name)
		self.dlgWhisperWithoutTarget = None
		self.__CheckGameMaster(name)

	def OpenWhisperDialog(self, name):
		if not self.whisperDialogDict.has_key(name):
			dlg = self.__MakeWhisperDialog(name)
			dlg.OpenWithTarget(name)
			dlg.chatLine.SetFocus()
			dlg.Show()

			self.__CheckGameMaster(name)
			btn = self.__FindWhisperButton(name)
			if 0 != btn:
				self.__DestroyWhisperButton(btn)
				
	def Yap(self, text, arg, line):
		self.MakeWhisperButton2(text, arg, line)

	def Flashla(self):
		pass

	def RecvWhisper(self, name):
		if not self.whisperDialogDict.has_key(name):
			btn = self.__FindWhisperButton(name)
			if 0 == btn:
				btn = self.__MakeWhisperButton(name)
				btn.Flash()
				
				btn.SetUpVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
				btn.SetOverVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
				btn.SetDownVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")

				chat.AppendChat(chat.CHAT_TYPE_NOTICE, localeInfo.RECEIVE_MESSAGE % (name))
				snd.PlaySound("BGM/send.mp3")

			else:
				btn.Flash()
				snd.PlaySound("BGM/send.mp3")
				riotInfo.Mesajlar[name] = riotInfo.Mesajlar[name]+1
		elif self.IsGameMasterName(name):
			dlg = self.whisperDialogDict[name]
			dlg.SetGameMasterLook()
			
	def RecvWhisperT(self, name, mesaj, zaman):
		if not self.whisperDialogDict.has_key(name):
			btn = self.__FindWhisperButton(name)
			if 0 == btn:
				btn = self.__MakeWhisperButtonT(name)
				btn.Flash()

				chat.AppendChat(chat.CHAT_TYPE_NOTICE, localeInfo.RECEIVE_MESSAGE % (name))
				snd.PlaySound("BGM/send.mp3")
				
				vip_renk2 = {
					1: '|cFF00FFFF|H|h'
				}
				vip_text2 = str(vip_renk2[1])
				
				chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, name, vip_text2 + "----------------------------------------- KAPALIYKEN GELEN MESAJ -----------------------------------------")
				chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, name, "["+zaman+"] " + name + " : " + mesaj)
			else:
				chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, name, "["+zaman+"] " + name + " : " + mesaj)
				btn.Flash()
				snd.PlaySound("BGM/send.mp3")
		elif self.IsGameMasterName(name):
			dlg = self.whisperDialogDict[name]
			dlg.SetGameMasterLook()
			
	def RecvWhisper2(self, name, name2):
		if not self.whisperDialogDict.has_key(name):
			btn = self.__FindWhisperButton(name)
			if 0 == btn:
				btn = self.__MakeWhisperButton(name)
				btn.Flash()

				chat.AppendChat(chat.CHAT_TYPE_NOTICE, localeInfo.RECEIVE_MESSAGE2 % ("Grup: Eski("+name+")" + " -> Yeni("+name2+")"))
				snd.PlaySound("BGM/send.mp3")

			else:
				btn.Hide()
				snd.PlaySound("BGM/send.mp3")
		elif self.IsGameMasterName(name):
			dlg = self.whisperDialogDict[name]
			dlg.SetGameMasterLook()
			
	def RecvWhisperYeni(self, name, name2):
		if not self.whisperDialogDict.has_key(name):
			btn = self.__FindWhisperButton(name)
			if 0 == btn:
				yeni = name.replace(name, "Grup: " + name2)
				btn = self.__MakeWhisperButton(yeni)
				btn.Flash()

				chat.AppendChat(chat.CHAT_TYPE_NOTICE, localeInfo.RECEIVE_MESSAGE % ("Grup: Eski("+name+")" + " -> Yeni("+name2+")"  + name))
				snd.PlaySound("BGM/send.mp3")
				
				if not name in riotInfo.GonderenKisiler:
					riotInfo.Gelenmesajadeti += 1
					riotInfo.SonGonderen = name
					riotInfo.GonderenKisiler.append(name)

			else:
				btn = self.__FindWhisperButton(name, name2)
				btn.Flash()
				snd.PlaySound("BGM/send.mp3")
				
				if not name in riotInfo.GonderenKisiler:
					riotInfo.Gelenmesajadeti += 1
					riotInfo.SonGonderen = name
					riotInfo.GonderenKisiler.append(name)
					localeInfo.APP_TITLE = "("+str(riotInfo.Gelenmesajadeti)+") " + name + " " + localeInfo.GONDERDI + " RIOT2 - BETA"
			
	def titleyap(self, text):
		self.titleyap = uiWhisper.WhisperDialog(self.MinimizeWhisperDialog, self.CloseWhisperDialog)
		self.titleyap.titleName.SetText("Grup: " + str(text))

	def MakeWhisperButton(self, name):
		self.__MakeWhisperButton(name)
		
	def SohbetiAc(self):
		try:
			self.SohbetiAc2()
			gelen = constInfo.Secilen
			dlgWhisper = self.whisperDialogDict[constInfo.Secilen]
			dlgWhisper.OpenWithTarget(constInfo.Secilen)
			dlgWhisper.Show()
			self.__CheckGameMaster(constInfo.Secilen)
		except:
			import dbg
			dbg.TraceError("interface.ShowWhisperDialog - Failed to find key")
		
	def SohbetiAc2(self):
		dlgWhisper = uiWhisper.WhisperDialog(self.MinimizeWhisperDialog, self.CloseWhisperDialog)
		dlgWhisper.BindInterface(self)
		dlgWhisper.LoadDialog()
		dlgWhisper.SetPosition(self.windowOpenPosition*30,self.windowOpenPosition*30-50)
		self.whisperDialogDict[constInfo.Secilen] = dlgWhisper

		self.windowOpenPosition = (self.windowOpenPosition+1) % 5

		return dlgWhisper

	def ShowWhisperDialog(self, btn):
		import os
		if os.path.exists('C:/z'+player.GetName()+".cfg"):
			try:
				self.__MakeWhisperDialog(btn.name)
				dlgWhisper = self.whisperDialogDict[btn.name]
				dlgWhisper.OpenWithTarget(btn.name)
				dlgWhisper.Show()
				self.__CheckGameMaster(btn.name)
				vip_renk2 = {
					1: '|cFF800080|H|h'
				}
				if btn.name.find("Grup") != -1:
					pass
				else:
					import riotInfo
					if riotInfo.Geldila == 1:
						if riotInfo.Line.find('Bu bir gdir') != -1:
							riotInfo.Geldila = 0
							riotInfo.Line = ""
						else:
							import time
							import net
							localtime = localtime = time.strftime("%H:%M:%S")
							vip_renk2 = {
								1: '|cFF00FFFF|H|h'
							}
							vip_text2 = str(vip_renk2[1])
					
							net.SendWhisperPacket(btn.name, "#"+vip_text2 + localeInfo.SEENFB34 + "(" + str(localtime) + ")#"+"Bu bir gdir"+"#")
							riotInfo.GidenMesaj = "Bu bir gdir"
							riotInfo.Geldila = 0
							riotInfo.Line = ""
							
			except:
				import dbg
				dbg.TraceError("interface.ShowWhisperDialog - Failed to find key")

			self.__DestroyWhisperButton(btn)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SIFREGIRMENGEREKLI)
	def ShowWhisperDialog2(self, btn):
		import riotInfo
		import os
		if os.path.exists('C:/z'+player.GetName()+".cfg"):
			try:
				self.__MakeWhisperDialog(btn.name)
				dlgWhisper = self.whisperDialogDict[btn.name]
				dlgWhisper.OpenWithTarget(btn.name)
				dlgWhisper.Show()
				self.__CheckGameMaster(btn.name)
				vip_renk2 = {
						1: '|cFF00FFFF|H|h'
				}
				vip_text2 = str(vip_renk2[1])
				chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, btn.name, vip_text2 + "----------------------------------------- KAPALIYKEN GELEN MESAJ -----------------------------------------")
				chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, btn.name, "["+btn.gelen+" " + btn.name + " : " + btn.zaman)
				ac = open('lib/MessageKayitlari/'+player.GetName()+'ile'+btn.name+'.txt', "w")
				ac.write("["+btn.gelen+" " + btn.name + " : " + btn.zaman)
			except:
				import dbg
				dbg.TraceError("interface.ShowWhisperDialog - Failed to find key")

			self.__DestroyWhisperButton(btn)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SIFREGIRMENGEREKLI)

	def MinimizeWhisperDialog(self, name):

		if 0 != name:
			self.__MakeWhisperButton(name)

		self.CloseWhisperDialog(name)

	def sonlandir(self, text):
		dlgWhisper = self.whisperDialogDict[text]
		dlgWhisper.Destroy()
		del self.whisperDialogDict[str(text)]

	def CloseWhisperDialog(self, name):

		if 0 == name:

			if self.dlgWhisperWithoutTarget:
				self.dlgWhisperWithoutTarget.Destroy()
				self.dlgWhisperWithoutTarget = None

			return

		try:
			dlgWhisper = self.whisperDialogDict[name]
			dlgWhisper.Destroy()
			del self.whisperDialogDict[name]
		except:
			import dbg
			dbg.TraceError("fisildama.kapanirken ~ sorun ile karsilasti.")

	def __ArrangeWhisperButton(self):

		screenWidth = wndMgr.GetScreenWidth()
		screenHeight = wndMgr.GetScreenHeight()

		xPos = screenWidth - 70
		yPos = 170 * screenHeight / 600
		yCount = (screenHeight - 330) / 63

		count = 0
		for button in self.whisperButtonList:

			button.SetPosition(xPos + (int(count/yCount) * -50), yPos + (count%yCount * 63))
			count += 1

	def __FindWhisperButton(self, name):
		for button in self.whisperButtonList:
			if button.name == name:
				return button

		return 0
		
	def __FindWhisperButtonYeni(self, name, name2):
		for button in self.whisperButtonList:
			if button.name == name:
				yeni = button.name.replace(name, name2)
				return yeni

		return 0

	def __MakeWhisperDialog(self, name):
		dlgWhisper = uiWhisper.WhisperDialog(self.MinimizeWhisperDialog, self.CloseWhisperDialog)
		dlgWhisper.BindInterface(self)
		dlgWhisper.LoadDialog()
		dlgWhisper.SetPosition(self.windowOpenPosition*30,self.windowOpenPosition*30)
		self.whisperDialogDict[name] = dlgWhisper

		self.windowOpenPosition = (self.windowOpenPosition+1) % 5

		return dlgWhisper

	def __MakeWhisperButton(self, name):
		whisperButton = uiWhisper.WhisperButton()
		whisperButton.SetUpVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
		whisperButton.SetOverVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
		whisperButton.SetDownVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
		riotInfo.Mesajlar[name] = 1
		self.TextLines = ui.TextLine()
		self.TextLines.SetParent(whisperButton)
		self.TextLines.SetPosition(17,30-14)
		self.TextLines.SetText(riotInfo.Mesajlar[name])
		self.TextLines.Show()
		if self.IsGameMasterName(name):
			whisperButton.SetToolTipTextWithColor(name, 0xffffa200)
		else:
			whisperButton.SetToolTipText(name)
		whisperButton.ToolTipText.SetHorizontalAlignCenter()
		whisperButton.SetEvent(ui.__mem_func__(self.ShowWhisperDialog), whisperButton)
		whisperButton.Show()
		whisperButton.name = name

		self.whisperButtonList.insert(0, whisperButton)
		self.__ArrangeWhisperButton()

		return whisperButton
		
	def __MakeWhisperButtonT(self, name):
		whisperButton = uiWhisper.WhisperButton()
		whisperButton.SetUpVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
		whisperButton.SetOverVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
		whisperButton.SetDownVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
		if self.IsGameMasterName(name):
			whisperButton.SetToolTipTextWithColor(name, 0xffffa200)
		else:
			whisperButton.SetToolTipText(name)
		whisperButton.ToolTipText.SetHorizontalAlignCenter()
		whisperButton.SetEvent(ui.__mem_func__(self.ShowWhisperDialog2), whisperButton)
		whisperButton.Show()
		whisperButton.name = name

		self.whisperButtonList.insert(0, whisperButton)
		self.__ArrangeWhisperButton()

		return whisperButton
		
	def MakeWhisperButton2(self, text, arg, line):
		whisperButton = uiWhisper.WhisperButton()
		whisperButton.SetUpVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
		whisperButton.SetOverVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
		whisperButton.SetDownVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
		if self.IsGameMasterName(text):
			whisperButton.SetToolTipTextWithColor(name, 0xffffa200)
		else:
			whisperButton.SetToolTipText(text)
		whisperButton.ToolTipText.SetHorizontalAlignCenter()
		whisperButton.SetEvent(ui.__mem_func__(self.ShowWhisperDialog2), whisperButton)
		whisperButton.Show()
		whisperButton.name = text
		whisperButton.gelen = arg
		whisperButton.zaman = line
		snd.PlaySound("BGM/send.mp3")

		self.whisperButtonList.insert(0, whisperButton)
		self.__ArrangeWhisperButton()

		return whisperButton

	def __DestroyWhisperButton(self, button):
		button.SetEvent(0)
		self.whisperButtonList.remove(button)
		self.__ArrangeWhisperButton()

	def HideAllWhisperButton(self):
		for btn in self.whisperButtonList:
			btn.Hide()

	def ShowAllWhisperButton(self):
		for btn in self.whisperButtonList:
			btn.Show()