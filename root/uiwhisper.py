#Prof Whisper System, V.2.6
#by Fatihbab34™
import ui
import net
import chat
import player
import app
import localeInfo
import ime
import interfacemodule
import chr
import constInfo
import riotInfo
import os
import uiGroup
import uiGroupadd
import uiCommon
import messenger
import event
import gameInfo

temizli = []
temizlikonusma = []
konusmadurumu = []
OkunmayanStat = 0
SecKapanmaDurum = 0
adamsil = 0
grupmesajatilacakkisi = ""
stringx = 0
yer = 0
tek = 0
tek2 = 0
yaz2 = 0
yerim = 0
renktek = 0
engelli = 0
sikayetlerim = []

sonuzunluk = 0

chr.PLAYER_NAME_MAX_LEN = 35
class WhisperButton(ui.Button):
	def __init__(self):
		ui.Button.__init__(self, "TOP_MOST")

	def __del__(self):
		ui.Button.__del__(self)

	def SetToolTipText(self, text, x=0, y = 32):
		ui.Button.SetToolTipText(self, text, x, y)
		self.ToolTipText.Show()

	def SetToolTipTextWithColor(self, text, color, x=0, y = 32):
		ui.Button.SetToolTipText(self, text, x, y)
		self.ToolTipText.SetPackedFontColor(color)
		self.ToolTipText.Show()

	def ShowToolTip(self):
		if 0 != self.ToolTipText:
			self.ToolTipText.Show()

	def HideToolTip(self):
		if 0 != self.ToolTipText:
			self.ToolTipText.Show()
			
class Component:
	def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		button = ui.Button()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetEvent(func)
		return button

	def ToggleButton(self, parent, buttonName, tooltipText, x, y, funcUp, funcDown, UpVisual, OverVisual, DownVisual):
		button = ui.ToggleButton()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetToggleUpEvent(funcUp)
		button.SetToggleDownEvent(funcDown)
		return button

	def EditLine(self, parent, editlineText, x, y, width, heigh, max):
		SlotBar = ui.SlotBar()
		if parent != None:
			SlotBar.SetParent(parent)
		SlotBar.SetSize(width, heigh)
		SlotBar.SetPosition(x, y)
		SlotBar.Show()
		Value = ui.EditLine()
		Value.SetParent(SlotBar)
		Value.SetSize(width, heigh)
		Value.SetPosition(1, 1)
		Value.SetMax(max)
		Value.SetLimitWidth(width)
		Value.SetMultiLine()
		Value.SetText(editlineText)
		Value.Show()
		return SlotBar, Value

	def TextLine(self, parent, textlineText, x, y, color):
		textline = ui.TextLine()
		if parent != None:
			textline.SetParent(parent)
		textline.SetPosition(x, y)
		if color != None:
			textline.SetFontColor(color[0], color[1], color[2])
		textline.SetText(textlineText)
		textline.Show()
		return textline

	def RGB(self, r, g, b):
		return (r*255, g*255, b*255)

	def SliderBar(self, parent, sliderPos, func, x, y):
		Slider = ui.SliderBar()
		if parent != None:
			Slider.SetParent(parent)
		Slider.SetPosition(x, y)
		Slider.SetSliderPos(sliderPos / 100)
		Slider.Show()
		Slider.SetEvent(func)
		return Slider

	def ExpandedImage(self, parent, x, y, img):
		image = ui.ExpandedImageBox()
		if parent != None:
			image.SetParent(parent)
		image.SetPosition(x, y)
		image.LoadImage(img)
		image.Show()
		return image

	def ComboBox(self, parent, text, x, y, width):
		combo = ui.ComboBox()
		if parent != None:
			combo.SetParent(parent)
		combo.SetPosition(x, y)
		combo.SetSize(width, 15)
		combo.SetCurrentItem(text)
		combo.Show()
		return combo

	def ThinBoard(self, parent, moveable, x, y, width, heigh, center):
		thin = ui.ThinBoard()
		if parent != None:
			thin.SetParent(parent)
		if moveable == TRUE:
			thin.AddFlag('movable')
			thin.AddFlag('float')
		thin.SetSize(width, heigh)
		thin.SetPosition(x, y)
		if center == TRUE:
			thin.SetCenterPosition()
		thin.Show()
		return thin

	def Gauge(self, parent, width, color, x, y):
		gauge = ui.Gauge()
		if parent != None:
			gauge.SetParent(parent)
		gauge.SetPosition(x, y)
		gauge.MakeGauge(width, color)
		gauge.Show()
		return gauge

	def ListBoxEx(self, parent, x, y, width, heigh):
		bar = ui.Bar()
		if parent != None:
			bar.SetParent(parent)
		bar.SetPosition(x, y)
		bar.SetSize(width, heigh)
		bar.SetColor(0x77000000)
		bar.Show()
		ListBox=ui.ListBoxEx()
		ListBox.SetParent(bar)
		ListBox.SetPosition(0, 0)
		ListBox.SetSize(width, heigh)
		ListBox.Show()
		scroll = ui.ScrollBar()
		scroll.SetParent(ListBox)
		scroll.SetPosition(width-15, 0)
		scroll.SetScrollBarSize(heigh)
		scroll.Show()
		ListBox.SetScrollBar(scroll)
		return bar, ListBox

class WhisperDialog(ui.ScriptWindow):

	class TextRenderer(ui.Window):
		def SetTargetName(self, targetName):
			self.targetName = targetName

		def OnRender(self):
			(x, y) = self.GetGlobalPosition()
			chat.RenderWhisper(self.targetName, x, y)

	class ResizeButton(ui.DragButton):

		def __init__(self):
			ui.DragButton.__init__(self)

		def __del__(self):
			ui.DragButton.__del__(self)

		def OnMouseOverIn(self):
			app.SetCursor(app.HVSIZE)

		def OnMouseOverOut(self):
			app.SetCursor(app.NORMAL)

	def __init__(self, eventMinimize, eventClose):
		print "NEW WHISPER DIALOG  ----------------------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)
		self.targetName = ""
		self.eventMinimize = eventMinimize
		self.eventClose = eventClose
		self.eventAcceptTarget = None
	def __del__(self):
		print "---------------------------------------------------------------------------- DELETE WHISPER DIALOG"
		ui.ScriptWindow.__del__(self)		

	def LoadDialog(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/WhisperDialog.py")
		except:
			import exception
			exception.Abort("WhisperDialog.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			self.titleName = GetObject("titlename")
			self.group = GetObject("group_chat")
			self.titleNameEdit = GetObject("titlename_edit")
			self.closeButton = GetObject("closebutton")
			self.scrollBar = GetObject("scrollbar")
			self.chatLine = GetObject("chatline")
			self.minimizeButton = GetObject("minimizebutton")
			self.ignoreButton = GetObject("ignorebutton")
			self.acceptButton = GetObject("acceptbutton")
			self.sendButton = GetObject("sendbutton")
			self.board = GetObject("board")
			self.editBar = GetObject("editbar")
			self.gamemasterMark = GetObject("gamemastermark")
			self.group_chat = GetObject("group_chat")
			self.group_add = GetObject("group_add")
			self.group_del = GetObject("group_delete")
			#Message Sistem:
			self.sec = GetObject("sec")
			self.delete = GetObject("delete")
			self.konustuklarim = GetObject("okunmayantext")
			self.konusmalar = GetObject("okunmayankisiler")
			self.karaktersayi = GetObject("karakterkelime")
			self.araslotbar = GetObject("araslotbar")
			self.ara = GetObject("AraButton")
			self.arananmesaj = GetObject("oyuncuara")
			self.yaziyor = GetObject("yaziyor")
			self.renkbutton2 = GetObject("renkbutton")
			self.smiles = GetObject("smiles")
			
		except:
			import exception
			exception.Abort("DialogWindow.LoadDialog.BindObject")

		self.gamemasterMark.Hide()
		self.group_add.Hide()
		self.titleName.SetText("")
		self.titleNameEdit.SetText("")
		self.minimizeButton.SetEvent(ui.__mem_func__(self.Minimize))
		self.closeButton.SetEvent(ui.__mem_func__(self.Close))
		self.scrollBar.SetPos(1.0)
		self.scrollBar.SetScrollEvent(ui.__mem_func__(self.OnScroll))
		self.chatLine.SetReturnEvent(ui.__mem_func__(self.SendWhisper))
		self.chatLine.SetEscapeEvent(ui.__mem_func__(self.Minimize))
		self.chatLine.SetMultiLine()
		self.sendButton.SetEvent(ui.__mem_func__(self.SendWhisper))
		self.titleNameEdit.SetReturnEvent(ui.__mem_func__(self.AcceptTarget))
		self.titleNameEdit.SetEscapeEvent(ui.__mem_func__(self.Close))
		#self.ignoreButton.SetEvent(ui.__mem_func__(self.IgnoreTarget))
		self.acceptButton.SetEvent(ui.__mem_func__(self.AcceptTarget))
		self.group.SetToggleDownEvent(ui.__mem_func__(self.Group))
		self.group_add.SetToggleDownEvent(ui.__mem_func__(self.Group_add))
		self.group_del.SetEvent(ui.__mem_func__(self.Group_del))
		
		self.ignoreButton.Hide()
		
		#Message System:
		self.sec.SetEvent(ui.__mem_func__(self.Sec))
		self.delete.SetEvent(ui.__mem_func__(self.Delete))
		self.ara.SetEvent(ui.__mem_func__(self.AramaYap))
		
		#50 + 30 - 95 - 86 + 30
		self.renkbutton2.SetPosition(450 - 80 + 150 + 25 - 6, self.GetHeight() - 40 + 30 + 5)
		self.renkbutton2.SetEvent(ui.__mem_func__(self.RenkDegistir))
		
		#END,RETURN; SON.
		self.textRenderer = self.TextRenderer()
		self.textRenderer.SetParent(self)
		self.textRenderer.SetPosition(20, 28)
		self.textRenderer.SetTargetName("")
		self.textRenderer.Show()
		
		self.group_del.Hide()
		self.ignoreButton.Hide()
		self.delete.Hide()
		self.araslotbar.Hide()
		self.ara.Hide()
		self.smiles.Hide()
		
		
		##RENK TABLOSU - Son update: 00:59 - 01.02.2015 ##
		
		self.renkArka = ui.Button()
		self.renkArka.SetParent(self)
		self.renkArka.SetPosition(450 - 80 + 150 + 7, self.GetHeight() - 50 + 30 - 95 - 86)
		self.renkArka.SetUpVisual("locale/ui/config/renkler/arkaplanbuton.tga")
		self.renkArka.SetOverVisual("locale/ui/config/renkler/arkaplanbuton.tga")
		self.renkArka.SetDownVisual("locale/ui/config/renkler/arkaplanbuton.tga")
		#self.renkArka.SetEvent(ui.__mem_func__(self.AddFrind))
		self.renkArka.Hide()
		
		self.renkSiyah = ui.Button()
		self.renkSiyah.SetParent(self.renkArka)
		self.renkSiyah.SetPosition(10+4-2-4+1, 5+8)
		self.renkSiyah.SetUpVisual("locale/ui/config/renkler/siyah1.tga")
		self.renkSiyah.SetOverVisual("locale/ui/config/renkler/bos.tga")
		self.renkSiyah.SetDownVisual("locale/ui/config/renkler/bos.tga")
		self.renkSiyah.SetToolTipText(localeInfo.RENGISIYAHYAP)
		self.renkSiyah.SetEvent(ui.__mem_func__(self.renkSiyah2))
		#self.renkSiyah.Hide()
		
		self.renkBeyaz = ui.Button()
		self.renkBeyaz.SetParent(self.renkArka)
		self.renkBeyaz.SetPosition(10+4-2 - 1, 5+42-15+12-6 + 3 - 2 - 2)
		self.renkBeyaz.SetUpVisual("locale/ui/config/renkler/beyaz.tga")
		self.renkBeyaz.SetOverVisual("locale/ui/config/renkler/bos.tga")
		self.renkBeyaz.SetDownVisual("locale/ui/config/renkler/bos.tga")
		self.renkBeyaz.SetToolTipText(localeInfo.RENGIBEYAZYAP)
		self.renkBeyaz.SetEvent(ui.__mem_func__(self.renkBeyaz2))
		#self.renkBeyaz.Hide()
		
		self.renkYesil = ui.Button()
		self.renkYesil.SetParent(self.renkArka)
		self.renkYesil.SetPosition(10+4-2, 5+42+42-15-14 + 6 + 2 - 2 - 2 - 2)
		self.renkYesil.SetUpVisual("locale/ui/config/renkler/yesil.tga")
		self.renkYesil.SetOverVisual("locale/ui/config/renkler/bos.tga")
		self.renkYesil.SetDownVisual("locale/ui/config/renkler/bos.tga")
		self.renkYesil.SetToolTipText(localeInfo.RENGIYESILYAP)
		self.renkYesil.SetEvent(ui.__mem_func__(self.renkYesil2))
		#self.renkYesil.Hide()
		
		self.renkMavi = ui.Button()
		self.renkMavi.SetParent(self.renkArka)
		self.renkMavi.SetPosition(10+4-2, 5+42+42+42-15-14 - 9 - 9 + 6 + 5 - 3 - 2 - 2)
		self.renkMavi.SetUpVisual("locale/ui/config/renkler/mavi.tga")
		self.renkMavi.SetOverVisual("locale/ui/config/renkler/bos.tga")
		self.renkMavi.SetDownVisual("locale/ui/config/renkler/bos.tga")
		self.renkMavi.SetToolTipText(localeInfo.RENGIMAVIYAP)
		self.renkMavi.SetEvent(ui.__mem_func__(self.renkMavi2))
		#self.renkMavi.Hide()
		
		self.renkPembe = ui.Button()
		self.renkPembe.SetParent(self.renkArka)
		self.renkPembe.SetPosition(10+4-2-1, 5+42+42+42+42-15-14 - 9 - 17 - 9 + 6 - 2)
		self.renkPembe.SetUpVisual("locale/ui/config/renkler/mor.tga")
		self.renkPembe.SetOverVisual("locale/ui/config/renkler/bos.tga")
		self.renkPembe.SetDownVisual("locale/ui/config/renkler/bos.tga")
		self.renkPembe.SetToolTipText(localeInfo.RENGIPEMBEYAP)
		self.renkPembe.SetEvent(ui.__mem_func__(self.renkPembe2))
		#self.renkPembe.Hide()
		
		self.renkKirmizi = ui.Button()
		self.renkKirmizi.SetParent(self.renkArka)
		self.renkKirmizi.SetPosition(10+4-2-1, 5+42+42+42+42+42-15-14 - 9 - 17 - 9 - 13 - 3+2 - 2)
		self.renkKirmizi.SetUpVisual("locale/ui/config/renkler/kirmizi.tga")
		self.renkKirmizi.SetOverVisual("locale/ui/config/renkler/bos.tga")
		self.renkKirmizi.SetDownVisual("locale/ui/config/renkler/bos.tga")
		self.renkKirmizi.SetToolTipText(localeInfo.RENGIKIRMIZIYAP)
		self.renkKirmizi.SetEvent(ui.__mem_func__(self.renkKirmizi2))
		#self.renkKirmizi.Hide()
		
		self.renkSari = ui.Button()
		self.renkSari.SetParent(self.renkArka)
		self.renkSari.SetPosition(10+4-2-1, 5+42+42+42+42+42+42-15-14 - 9 - 17 - 30 - 12)
		self.renkSari.SetUpVisual("locale/ui/config/renkler/sari.tga")
		self.renkSari.SetOverVisual("locale/ui/config/renkler/bos.tga")
		self.renkSari.SetDownVisual("locale/ui/config/renkler/bos.tga")
		self.renkSari.SetToolTipText(localeInfo.RENGISARIYAP)
		self.renkSari.SetEvent(ui.__mem_func__(self.renkSari2))
		#self.renkSari.Hide()
		
		##RENK TABLOSU SON##

		self.resizeButton = self.ResizeButton()
		self.resizeButton.SetParent(self)
		self.resizeButton.SetSize(20, 20)
		self.resizeButton.SetWindowVerticalAlignBottom()
		self.resizeButton.SetPosition(280, 180)
		self.resizeButton.SetMoveEvent(ui.__mem_func__(self.ResizeWhisperDialog))
		self.resizeButton.Show()
		
		self.modButton = ui.Button()
		self.modButton.SetParent(self)
		self.modButton.SetPosition(119-8, 10)
		self.modButton.SetUpVisual("d:/ymir work/ui/game/windows/messenger_add_friend_01.sub")
		self.modButton.SetOverVisual("d:/ymir work/ui/game/windows/messenger_add_friend_02.sub")
		self.modButton.SetDownVisual("d:/ymir work/ui/game/windows/messenger_add_friend_03.sub")
		self.modButton.SetToolTipText("")
		#self.modButton.SetEvent(ui.__mem_func__(self.AddFrind))
		#self.modButton.Show()
		
		self.friendButton = ui.Button()
		self.friendButton.SetParent(self)
		self.friendButton.SetPosition(119+16, 10)
		self.friendButton.SetUpVisual("d:/ymir work/ui/game/windows/messenger_add_friend_01.sub")
		self.friendButton.SetOverVisual("d:/ymir work/ui/game/windows/messenger_add_friend_02.sub")
		self.friendButton.SetDownVisual("d:/ymir work/ui/game/windows/messenger_add_friend_03.sub")
		self.friendButton.SetToolTipText(localeInfo.EKLE)
		self.friendButton.SetEvent(ui.__mem_func__(self.AddFrind))
		#self.friendButton.Show()
		
		if not messenger.IsFriendByName(self.targetName):
			self.modButton.SetPosition(119-8, 10)
			self.group_del.SetPosition(119+16, 10)
			#self.modButton.Show()
		else:
			self.modButton.SetPosition(119, 10)

		self.ResizeWhisperDialog()
				
		self.resizeButton2 = self.ResizeButton()
		self.resizeButton2.SetParent(self)
		self.resizeButton2.SetSize(80, 60)
		self.resizeButton2.SetWindowVerticalAlignBottom()
		self.resizeButton2.SetPosition(280+260+15+8, 180+150+11+6)
		self.resizeButton2.SetMoveEvent(ui.__mem_func__(self.ResizeWhisperDialog2))
		self.resizeButton2.Show()

	def Destroy(self):

		self.eventMinimize = None
		self.eventClose = None
		self.eventAcceptTarget = None

		self.ClearDictionary()
		self.scrollBar.Destroy()
		self.titleName = None
		self.titleNameEdit = None
		self.closeButton = None
		self.scrollBar = None
		self.chatLine = None
		self.sendButton = None
		self.ignoreButton = None
		self.acceptButton = None
		self.minimizeButton = None
		self.textRenderer = None
		self.board = None
		self.editBar = None
		self.resizeButton = None

	def ResizeWhisperDialog(self):
		(xPos, yPos) = self.resizeButton.GetLocalPosition()
		if xPos < 280:
			self.resizeButton.SetPosition(280, yPos+90)
			return
		if yPos < 150:
			self.resizeButton.SetPosition(xPos, 150+90)
			return
		self.SetWhisperDialogSize(xPos + 20+300, yPos + 20+160)
		
	def ResizeWhisperDialog2(self):
		(xPos, yPos) = self.resizeButton2.GetLocalPosition()
		if xPos < 280:
			self.resizeButton.SetPosition(280, yPos+90)
			return
		if yPos < 150:
			self.resizeButton.SetPosition(xPos, 150+90)
			return
		self.resizeButton.SetPosition(xPos+20, yPos+10)
		self.SetWhisperDialogSize(xPos + 20+25, yPos + 20)

	def SetWhisperDialogSize(self, width, height):
		try:

			max = int((width-90)/6) * 3 - 6

			self.board.SetSize(width, height)
			self.scrollBar.SetPosition(width-25, 35)
			self.scrollBar.SetScrollBarSize(height-100-10)
			self.scrollBar.SetPos(1.0)
			self.editBar.SetSize(width-18, 50)
			self.chatLine.SetSize(width-90-60, 40)
			self.chatLine.SetLimitWidth(width-90)
			self.SetSize(width, height)

			if 0 != self.targetName:
				chat.SetWhisperBoxSize(self.targetName, width, height - 90)			
			
			if localeInfo.IsARABIC():
				self.textRenderer.SetPosition(width-20, 28)
				self.scrollBar.SetPosition(width-25+self.scrollBar.GetWidth(), 35)
				self.editBar.SetPosition(10 + self.editBar.GetWidth(), height-60)
				self.sendButton.SetPosition(width - 80 + self.sendButton.GetWidth(), 10)
				self.minimizeButton.SetPosition(width-42 + self.minimizeButton.GetWidth(), 12)
				self.closeButton.SetPosition(width-24+self.closeButton.GetWidth(), 12)				
				self.board.SetPosition(self.board.GetWidth(), 0)
			else:
				self.textRenderer.SetPosition(20, 28)
				self.scrollBar.SetPosition(width-25, 45)
				self.editBar.SetPosition(10, height-60)
				self.sendButton.SetPosition(width-80, 10)
				self.chatLine.SetPosition(50-40, 5)
				self.minimizeButton.SetPosition(width-24, 28)
				self.closeButton.SetPosition(width-24, 12)
				self.karaktersayi.SetPosition(width-100, 15)
				self.renkbutton2.SetPosition(width-30 - 12 - 15 - 15 + 6, self.GetHeight() - 70 - 21)
				self.renkArka.SetPosition(width + 25 - 6 - 92, self.GetHeight() - 70 - 71 - 120 - 30)

			self.SetchatLineMax(max)

		except:
			import exception
			exception.Abort("WhisperDialog.SetWhisperDialogSize.BindObject")

	def SetchatLineMax(self, max):
		self.chatLine.SetMax(max)

		from grpText import GetSplitingTextLine

		text = self.chatLine.GetText()
		if text:
			self.chatLine.SetText(GetSplitingTextLine(text, max, 0))

	def OpenWithTarget(self, targetName):
		global temizli
		global temizlikonusma
		global adamsil
		global yer
		global renktek
		global yerim
		adamsil = 0
		renktek = 0
		yer = 0
		yerim = 1
		import os
		if os.path.exists('C:/z'+player.GetName()+'.cfg'):
			yerim = 1
			constInfo.rakipimza = ""
				#constInfo.Adi = targetName
			chat.CreateWhisper(targetName)
			try:
				pnblock = open("lib/"+player.GetName()+".cfg", "r")
				pnauslese = pnblock.read()
				pnblock.close()
			except:
				a = open("lib/"+player.GetName()+".cfg", "w")
				a.close()
				#self.ignoreButton.Show()
				pnauslese = ""
			#
			pnblock = open("lib/"+player.GetName()+".cfg", "r")
			pnauslese = pnblock.read()
			#
			pnblock = open("lib/"+player.GetName()+".cfg", "r")
			pnauslese = pnblock.read()
			if pnauslese.find(targetName) != -1:
				pass
				#self.ignoreButton.Show()
				#self.ignoreButton.SetText(localeInfo.ENGELIKALDIR)
			else:
				pass
				#self.ignoreButton.Show()
				
			if targetName.find("Grup:") != -1:
				pass
			else:
				constInfo.rakipmod = ""
				riotInfo.opentarget = 1
				net.SendWhisperPacket(targetName, "||suanmodunney||")
				riotInfo.GidenMesaj = "suanmodunney"
				#net.SendWhisperPacket(targetName, "||imzaniverirmisinlanbanaxd||")
				#riotInfo.GidenMesaj = "imzaniverirmisinlanbanaxd"
				
			chat.SetWhisperBoxSize(targetName, self.GetWidth() - 60, self.GetHeight() - 90)
			self.chatLine.SetFocus()
			self.titleName.SetText(targetName)
			self.targetName = targetName
			self.textRenderer.SetTargetName(targetName)
			self.titleNameEdit.Hide()
			self.acceptButton.Hide()
			self.gamemasterMark.Hide()
			self.group_del.Hide()
			self.araslotbar.Hide()
			self.ara.Hide()
			self.smiles.Hide()
			self.delete.Show()
			self.minimizeButton.Show()
			self.group_chat.SetPosition(148 + 10+25+20+8 + 30 + 20, 10-2)
			#TEST#->Emin değilim
			if not self.targetName in riotInfo.konusmadurumu:
				constInfo.konusmasessiz[self.targetName] = "Sesli"
				riotInfo.konusmadurumu.append(self.targetName)
			if self.targetName.find('Grup') !=-1:
				constInfo.suan = 1
			import messenger
			if not messenger.IsFriendByName(self.targetName):
				#self.friendButton = ui.Button()
				#self.friendButton.SetParent(self)
				#self.friendButton.SetPosition(119+16, 10)
				#self.friendButton.SetUpVisual("d:/ymir work/ui/game/windows/messenger_add_friend_01.sub")
				#self.friendButton.SetOverVisual("d:/ymir work/ui/game/windows/messenger_add_friend_02.sub")
				#self.friendButton.SetDownVisual("d:/ymir work/ui/game/windows/messenger_add_friend_03.sub")
				#self.friendButton.SetToolTipText(localeInfo.EKLE)
				#self.friendButton.SetEvent(ui.__mem_func__(self.AddFrind))
				self.friendButton.Show()
			#self.ayarlarButton = ui.Button()
			#self.ayarlarButton.SetParent(self)
			#self.ayarlarButton.SetPosition(119+25, 10)
			#self.ayarlarButton.SetUpVisual("")
			#self.ayarlarButton.SetOverVisual("")
			#self.ayarlarButton.SetDownVisual("")
			#self.ayarlarButton.SetToolTipText("Sohbet ayarlari")
			#self.ayarlarButton.SetEvent(ui.__mem_func__(self.Ayarlar))
			#self.ayarlarButton.Show()
			if self.targetName in temizli or self.targetName in temizlikonusma:
				pass
			else:
				if self.targetName.find("Grup:") != -1:
					if os.path.exists("C:/Windows/System32/ras/grup/"+player.GetName()+"ile"+targetName[6:]+".txt"):
						#import base64
						oku = open("C:/Windows/System32/ras/grup/"+player.GetName()+"ile"+targetName[6:]+".txt", "r").readlines()
						#oku = base64.b64decode(oku)
						chat.ClearWhisper(self.targetName)
						for u in oku:
							chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, u)
					else:
						if constInfo.yenipencere == 0:
							chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, "Hic mesaj yok.")
						else:
							constInfo.yenipencere = 1
				else:
					if os.path.exists("C:/Windows/System32/ras/"+player.GetName()+"ile"+targetName+".txt"):
						oku = open("C:/Windows/System32/ras/"+player.GetName()+"ile"+targetName+".txt", "r").readlines()
						chat.ClearWhisper(self.targetName)
						for u in oku:
							chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, u)
					else:
						chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, "Hic mesaj yok.")
			#if not os.path.exists("lib/MessageKayitlari/"+player.GetName()+"Yollayanlar2.cfg"):
				#self.sec.Hide()
				#self.konustuklarim.SetText("Konusma yok.")
			#else:
				#self.konustuklarim.SetText("Konusmalarim:")
			if self.targetName.find("Grup:") != -1:
				#self.ignoreButton.Hide()
				self.group_chat.Hide()
				#self.ignoreButton.Hide()
				self.group_add.Show()
				self.group_del.Show()
				self.friendButton.Hide()
				self.sec.Hide()
				self.delete.Hide()
				self.konustuklarim.Hide()
				self.konusmalar.Hide()
				self.friendButton.Hide()
			else:
				pass
			#import riotInfo
			#if riotInfo.Acildi == 1:
				#chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, riotInfo.GelenMesaj)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, 'Envanter sifresini girmelisiniz.')
			return
		
	def OpenWithoutTarget(self, event):
		global yerim
		yerim = 0
		self.eventAcceptTarget = event
		#self.ignoreButton.Hide()
		self.titleName.SetText("")
		self.titleNameEdit.SetText("")
		self.titleNameEdit.SetFocus()
		self.targetName = 0
		self.titleNameEdit.Show()
		self.acceptButton.Show()
		self.minimizeButton.Hide()
		self.gamemasterMark.Hide()
		self.group_del.Hide()
		self.delete.Hide()
		self.araslotbar.Hide()
		self.ara.Hide()
		self.smiles.Hide()
		self.group_chat.SetPosition(148 + 10+25+20+8, 10)
		
	def AramaYap(self):
		if self.targetName == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, 'Mesaj aramak için bir konuşma aç.')
		else:
			chat.ClearWhisper(self.targetName)
			if self.targetName.find("Grup:") != -1:
				ac = open("C:/Windows/System32/ras/grup/"+player.GetName()+"ile"+self.targetName[6:]+".txt", "r")
				for i in ac.readlines():
					if i.find(self.arananmesaj.GetText()) != -1:
						chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, i)
			else:
				ac = open("C:/Windows/System32/ras/"+player.GetName()+"ile"+self.targetName+".txt", "r")
				for i in ac.readlines():
					if i.find(self.arananmesaj.GetText()) != -1:
						chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, i)

	def SetGameMasterLook(self):
		self.gamemasterMark.Show()

	def Minimize(self):
		self.titleNameEdit.KillFocus()
		self.chatLine.KillFocus()
		self.Hide()

		if None != self.eventMinimize:
			self.eventMinimize(self.targetName)
			
	def Yeniadicinbitir(self, text):
		self.interface.sonlandir(str(text))

	def Close(self):
		global OkunmayanStat
		global SecKapanmaDurum
		global adamsil
		global yer
		
		if "#"+str(self.targetName)+"#" in gameInfo.WHISPER_YOLLANANLAR:
			gameInfo.WHISPER_YOLLANANLAR.remove("#"+str(self.targetName)+"#")

		if SecKapanmaDurum == 1:
			SecKapanmaDurum = 0
			self.SecMenu.Hide()
		SecKapanmaDurum = 0
		OkunmayanStat = 0
		riotInfo.BenYolladim = 0
		if str(self.targetName).find('Grup') !=-1:
			constInfo.suan = 0
		adamsil = 0
		yer = 0

		chat.ClearWhisper(self.targetName)
		self.titleNameEdit.KillFocus()
		self.chatLine.KillFocus()
		
		self.Hide()

		if None != self.eventClose:
			self.eventClose(self.targetName)
	
	def AddFrind(self):
		net.SendMessengerAddByNamePacket(self.targetName)
		self.friendButton.Hide()
		self.delete.SetPosition(119, 10)
		
	def Ayarlar(self):
		pass
			
	def Close2(self):
		self.Board.Hide()
	def IgnoreTarget(self):
		ig = self.targetName
		r = open("lib/"+player.GetName()+".cfg", "r")
		re = r.read()
		if re.find(self.targetName) != -1:
			selected = self.targetName
			old = open("lib/"+player.GetName()+".cfg", "r+")
			oldList = old.read()
			newList = str(oldList).replace(str(selected), str(""))
			old.close()
			new = open("lib/"+player.GetName()+".cfg", "w+")
			new.write(newList)
			new.close()
			self.__RefreshFileList()
			self.__RefreshFileList()
			chat.AppendChat(chat.CHAT_TYPE_INFO, self.targetName + ' ' + localeInfo.OYUNCUENGELKALDIRILDI)
		else:
			try:
				a = open("lib/"+player.GetName()+".cfg", "a")
				a.write(self.targetName + "\n")
				a.close()
				net.SendWhisperPacket(self.targetName, localeInfo.BUKONUSMAENGELLENDI)
			except:
				a = open("lib/"+player.GetName()+".cfg", "w")
				a.write(self.targetName + "\n")
				a.close()
				net.SendWhisperPacket(self.targetName, localeInfo.BUKONUSMAENGELLENDI)

	def IgnoreTargetxD(self):
		global engelli
		if constInfo.rakipmod == "off" or constInfo.rakipmod == "":
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OYUNDAOLMASILAZIM)
			self.questionDialogRT2.Close()
		else:
			ig = self.targetName
			r = open("lib/"+player.GetName()+".cfg", "r")
			re = r.read()
			if re.find(self.targetName) != -1:
				selected = self.targetName
				old = open("lib/"+player.GetName()+".cfg", "r+")
				oldList = old.read()
				newList = str(oldList).replace(str(selected), str(""))
				old.close()
				new = open("lib/"+player.GetName()+".cfg", "w+")
				new.write(newList)
				new.close()
				self.__RefreshFileList()
				self.__RefreshFileList()
				chat.AppendChat(chat.CHAT_TYPE_INFO, self.targetName + ' ' + localeInfo.OYUNCUENGELKALDIRILDI)
				self.questionDialogRT2.Close()
			else:
				try:
					a = open("lib/"+player.GetName()+".cfg", "a")
					a.write(self.targetName + "\n")
					a.close()
					net.SendWhisperPacket(self.targetName, localeInfo.BUKONUSMAENGELLENDI)
				except:
					a = open("lib/"+player.GetName()+".cfg", "w")
					a.write(self.targetName + "\n")
					a.close()
					net.SendWhisperPacket(self.targetName, localeInfo.BUKONUSMAENGELLENDI)
				self.questionDialogRT2.Close()
				
	def Group(self):
		self.micha = uiGroup.GroupDialog()
		self.group.SetUp()
		self.micha.Show()
		
	def Group_add(self):
		self.micha2 = uiGroupadd.GroupADDDialog()
		constInfo.group_add = self.targetName
		self.group_add.SetUp()
		self.micha2.Show()
		
	def renkSiyah2(self):
		global renktek
		renktek = 0
		riotInfo.Renkler['suan'] = "siyah"
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.RENKSIYAHOLDU)
		self.renkArka.Hide()
		
	def renkBeyaz2(self):
		global renktek
		renktek = 0
		riotInfo.Renkler['suan'] = "beyaz"
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.RENKBEYAZOLDU)
		self.renkArka.Hide()
		
	def renkYesil2(self):
		global renktek
		renktek = 0
		riotInfo.Renkler['suan'] = "yesil"
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.RENKYESILOLDU)
		self.renkArka.Hide()
		
	def renkMavi2(self):
		global renktek
		renktek = 0
		riotInfo.Renkler['suan'] = "mavi"
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.RENKMAVIOLDU)
		self.renkArka.Hide()
		
	def renkPembe2(self):
		global renktek
		renktek = 0
		riotInfo.Renkler['suan'] = "pembe"
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.RENKPEMBEOLDU)
		self.renkArka.Hide()
		
	def renkKirmizi2(self):
		global renktek
		renktek = 0
		riotInfo.Renkler['suan'] = "kirmizi"
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.RENKKIRMIZIOLDU)
		self.renkArka.Hide()
		
	def renkSari2(self):
		global renktek
		renktek = 0
		riotInfo.Renkler['suan'] = "sari"
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.RENKSARIOLDU)
		self.renkArka.Hide()
		
	def RenkDegistir(self):
		global renktek
		if renktek == 0:
			self.renkArka.Show()
			self.renkSiyah.Show()
			self.renkBeyaz.Show()
			self.renkYesil.Show()
			self.renkMavi.Show()
			self.renkPembe.Show()
			self.renkKirmizi.Show()
			self.renkSari.Show()
			renktek = 1
		else:
			self.renkArka.Hide()
			self.renkSiyah.Hide()
			self.renkBeyaz.Hide()
			self.renkYesil.Hide()
			self.renkMavi.Hide()
			self.renkPembe.Hide()
			self.renkKirmizi.Hide()
			self.renkSari.Hide()
			renktek = 0
		
	def Group_del(self):
		global yer
		global adamsil
		if adamsil == 0:
			self.DeleteBase = ui.SlotBar()
			self.DeleteBase.SetParent(self)
			self.DeleteBase.AddFlag("float")
			self.DeleteBase.SetSize(120+10+40-16, 80+20+15+15)
			self.DeleteBase.SetPosition(119+25+35+25, 10)
			self.DeleteBase.Show()
			
			self.DelList = ui.ListBoxScroll()
			self.DelList.SetParent(self.DeleteBase)
			self.DelList.SetSize(self.DeleteBase.GetWidth()- 20, self.DeleteBase.GetHeight())
			self.DelList.SetPosition(0, 0)
			self.DelList.SetEvent(ui.__mem_func__(self.__OnSelectGruptanCikar))
			self.DelList.Show()
			
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GRUP_NOTICE)
			
			if yer == 1:
				self.GruptakilerBase.Hide()
			
			#self.DelScrollBar = ui.ScrollBar()
			#self.DelScrollBar.SetParent(self.DeleteBase)
			#self.DelScrollBar.SetPosition(18, 3)
			#self.DelScrollBar.SetScrollBarSize(83)
			#self.DelScrollBar.SetWindowHorizontalAlignRight()
			##self.DelScrollBar.SetScrollEvent(ui.__mem_func__(self.__OnScrollDeleteList))
			#self.DelScrollBar.Show()
			
			if constInfo.groupssessiz[self.targetName] == "Sesli":
				self.DelList.InsertItem(1, localeInfo.TUMKONUSMALAR)
				self.DelList.InsertItem(2, localeInfo.GRUPTAKILER)
				self.DelList.InsertItem(3, localeInfo.GRUPTANCIKMENU)
				self.DelList.InsertItem(4, localeInfo.GRUPSESSIZEAL)
				self.DelList.InsertItem(5, localeInfo.GRUPTEMIZLE)
				self.DelList.InsertItem(6, localeInfo.GRUPADINIDEGIS)
				self.DelList.InsertItem(7, localeInfo.GRUBUSIL)
			elif constInfo.groupssessiz[self.targetName] == "Sessiz":
				self.DelList.InsertItem(1, localeInfo.TUMKONUSMALAR)
				self.DelList.InsertItem(2, localeInfo.GRUPTAKILER)
				self.DelList.InsertItem(3, localeInfo.GRUPTANCIKMENU)
				self.DelList.InsertItem(4, localeInfo.GRUPSESLIYEAL)
				self.DelList.InsertItem(5, localeInfo.GRUPTEMIZLE)
				self.DelList.InsertItem(6, localeInfo.GRUPADINIDEGIS)
				self.DelList.InsertItem(7, localeInfo.GRUBUSIL)
				
			adamsil = 1
		else:
			self.DeleteBase.Hide()
			if yer == 1:
				self.GruptakilerBase.Hide()
			adamsil = 0
			
	def Delete(self):
		global yer
		global adamsil
		global engelli
		if adamsil == 0:
			self.DeleteBase2 = ui.SlotBar()
			self.DeleteBase2.SetParent(self)
			self.DeleteBase2.AddFlag("float")
			#self.DeleteBase2.SetSize(120+10+40-16, 80+20+15-15-10)
			#self.DeleteBase2.SetPosition(119+25+35+25-15, 10)
			self.DeleteBase2.SetSize(120+10+40-16-15, 80+20+15-9-11+20-6+20 - 4 -1)
			self.DeleteBase2.SetPosition(119+25+35+25-15, 10-2)
			
			self.DeleteBase2.Show()
			
			riotInfo.ScrollKapat = 1
			engelli = 0
			self.DelList2 = ui.ListBox()
			self.DelList2.SetParent(self.DeleteBase2)
			self.DelList2.SetSize(self.DeleteBase2.GetWidth(), self.DeleteBase2.GetHeight())
			self.DelList2.SetPosition(0, 0)
			self.DelList2.SetEvent(ui.__mem_func__(self.__OnSelectSohbetAyarlari))
			self.DelList2.Show()
			
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SOHBET_NOTICE)
			
			#if yer == 1:
				#self.GruptakilerBase.Hide()
			
			#self.DelScrollBar = ui.ScrollBar()
			#self.DelScrollBar.SetParent(self.DeleteBase)
			#self.DelScrollBar.SetPosition(18, 3)
			#self.DelScrollBar.SetScrollBarSize(83)
			#self.DelScrollBar.SetWindowHorizontalAlignRight()
			##self.DelScrollBar.SetScrollEvent(ui.__mem_func__(self.__OnScrollDeleteList))
			#self.DelScrollBar.Show()
			if constInfo.konusmasessiz[self.targetName] == "Sesli":
				self.DelList2.InsertItem(1, localeInfo.TUMKONUSMALAR)
				self.DelList2.InsertItem(2, localeInfo.GRUPSESSIZEAL)
				self.DelList2.InsertItem(3, localeInfo.GRUPTEMIZLE)
				self.DelList2.InsertItem(4, localeInfo.TUMKONUSMALARISIL)
				self.DelList2.InsertItem(5, localeInfo.KONUSTUKLARIMISIL)
				self.DelList2.InsertItem(6, "Sohbette mesaj ara")
				#self.DelList2.InsertItem(7, localeInfo.REPVER)
				if os.path.exists("lib/"+player.GetName()+".cfg"):
					ac = open("lib/"+player.GetName()+".cfg", "r")
					aco = ac.read()
					if aco.find(self.targetName) != -1:
						engelli = 1
						self.DelList2.InsertItem(7, localeInfo.SPAMLAVEYAENGELIAC)
					else:
						self.DelList2.InsertItem(7, localeInfo.SPAMLAVEYASIKAYETET)
				else:
					self.DelList2.InsertItem(7, localeInfo.SPAMLAVEYASIKAYETET)
			elif constInfo.konusmasessiz[self.targetName] == "Sessiz":
				self.DelList2.InsertItem(1, localeInfo.TUMKONUSMALAR)
				self.DelList2.InsertItem(2, localeInfo.GRUPSESLIYEAL)
				self.DelList2.InsertItem(3, localeInfo.GRUPTEMIZLE)
				self.DelList2.InsertItem(4, localeInfo.TUMKONUSMALARISIL)
				self.DelList2.InsertItem(5, localeInfo.KONUSTUKLARIMISIL)
				self.DelList2.InsertItem(6, "Sohbette mesaj ara")
				#self.DelList2.InsertItem(7, localeInfo.REPVER)
				if os.path.exists("lib/"+player.GetName()+".cfg"):
					ac = open("lib/"+player.GetName()+".cfg", "r")
					aco = ac.read()
					if aco.find(self.targetName) != -1:
						engelli = 1
						self.DelList2.InsertItem(7, localeInfo.SPAMLAVEYAENGELIAC)
					else:
						self.DelList2.InsertItem(7, localeInfo.SPAMLAVEYASIKAYETET)
				else:
					self.DelList2.InsertItem(7, localeInfo.SPAMLAVEYASIKAYETET)
				
			adamsil = 1
		else:
			self.DeleteBase2.Hide()
			adamsil = 0
			engelli = 0
		
	def IgnoreTarget2(self):		
		a = open("lib/"+player.GetName()+".cfg")
		b = a.read()
		a.close()
		b = b.replace(self.targetName + "\n", "")
		c = open("lib/"+player.GetName()+".cfg", "w")
		c.write(b)
		c.close()
		#self.ignoreButton.Show()
		
	def AcceptTarget(self):
		name = self.titleNameEdit.GetText()
		if len(name) <= 0:
			self.Close()
			return

		if None != self.eventAcceptTarget:
			self.titleNameEdit.KillFocus()
			self.eventAcceptTarget(name)

	def OnScroll(self):
		chat.SetWhisperPosition(self.targetName, self.scrollBar.GetPos())
		
	#Message System:
	def Sec(self):
		self.comp = Component()
		#KONUSTUKLARİM LİSTESİ OPEN#
		global OkunmayanStat
		global SecKapanmaDurum
		if OkunmayanStat == 0:
			#self.Board = ui.Board()
			#self.Board.SetParent(self)
			#self.Board.SetSize(self.GetWidth(), self.GetHeight()-250+100)
			#self.Board.SetPosition(0, 0)
			#self.Board.AddFlag("movable")
			#self.Board.AddFlag("float")
			#self.Board.Show()
			#self.TitleBar = ui.TitleBar()
			#self.TitleBar.SetParent(self.Board)
			#self.TitleBar.SetPosition(7, 7)
			#self.TitleBar.MakeTitleBar(self.GetWidth() - 2 * 7, 'bloodyblue')
			#self.TitleBar.SetCloseEvent(self.Close2)
			#self.TitleBar.Show()
			#self.TitleText = ui.TextLine()
			#self.TitleText.SetParent(self.TitleBar)
			#self.TitleText.SetPosition(0, 4)
			#self.TitleText.SetText("Konuştuklarım")
			#                                          "CH - Switcher"
			#self.TitleText.SetWindowHorizontalAlignCenter()
			#self.TitleText.SetHorizontalAlignCenter()
			#self.TitleText.Show()
			self.ChannelListBase = ui.SlotBar()
			self.ChannelListBase.SetParent(self)
			self.ChannelListBase.AddFlag("float")
			self.ChannelListBase.SetSize(120+10, 80+20+15+70+45+5+30)
			self.ChannelListBase.SetPosition(148 + 10+25+20+8+40+50+15-8-6-1+50+20, 30-15-5+15+5)
			self.ChannelListBase.Show()

			#self.ChannelList2, self.ChannelList = self.comp.ListBoxEx(self.ChannelListBase, 0, 0, self.ChannelListBase.GetWidth()- 20 + 35 - 11 - 5, self.ChannelListBase.GetHeight())
			#self.ChannelList.SetSelectEvent(self.__OnSelectKonustuklarim)
			self.ChannelList = ui.ListBoxScroll()
			self.ChannelList.SetParent(self.ChannelListBase)
			self.ChannelList.SetSize(self.ChannelListBase.GetWidth(), self.ChannelListBase.GetHeight())
			self.ChannelList.SetPosition(0, 0)
			self.ChannelList.SetEvent(ui.__mem_func__(self.__OnSelectKonustuklarim))
			self.ChannelList.Show()
			
			#self.ChangeButton = ui.Button()
			#self.ChangeButton.SetParent(self.ChannelListBase)
			#self.ChangeButton.SetPosition(self.ChannelListBase.GetWidth()- 20-40-18, self.ChannelListBase.GetHeight()+40-40-15)
			#self.ChangeButton.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
			#self.ChangeButton.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
			#self.ChangeButton.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
			##self.ChangeButton.SetEvent(self.__OnSelectKonustuklarim)
			#self.ChangeButton.SetText("K")
			#self.ChangeButton.SetToolTipText("Konuşmayi başlat!")
			#                                                "SEÇ"
			#self.ChangeButton.Show()
			#self.DisableChangeButton()				
			#self.ChannelList.InsertItem(0, "Deneme")
			#self.ChannelList.InsertItem(1, "Deneme2")
			if os.path.exists("C:/Windows/System32/ras/"+player.GetName()+"Yollayanlar2.cfg"):
				ac = open("C:/Windows/System32/ras/"+player.GetName()+"Yollayanlar2.cfg", "r").readlines()
				for a in ac:
					if str(a).find("#") != -1:
						bu = str(a).split("#")[1].split("/")[0]
						self.ChannelList.InsertItem3(1, bu)
					#self.ChannelList.AppendItem(Item(a))
				#chat.AppendChat(chat.CHAT_TYPE_INFO, "Konusulanlar : " + ac)
			else:
				self.ChannelList.InsertItem(1, "Yok")
				
			OkunmayanStat = 1
			SecKapanmaDurum = 1
		else:
			if SecKapanmaDurum == 1:
				self.ChannelListBase.Hide()
				SecKapanmaDurum = 0
				OkunmayanStat = 0
				riotInfo.YerNO = 0
				
		#chat.AppendChat(chat.CHAT_TYPE_INFO, "riotInfo 1.siradaki : " + riotInfo.Konusmalarim['KONUSMALAR'][1])
			
	def DisableChangeButton(self):
		self.ChangeButton.Disable()
		self.ChangeButton.Down()
		self.ChangeButton.ButtonText.SetFontColor(0.4, 0.4, 0.4)
 
	def EnableChangeButton(self):
		self.ChangeButton.Enable()
		self.ChangeButton.SetUp()
		self.ChangeButton.ButtonText.SetFontColor(1, 1, 1)
		
	def __OnSelectSohbetAyarlari(self):
		global adamsil
		global temizlikonusma
		global yer
		secilkontrol = self.DelList2.GetSelectedItem()
		secilen = self.DelList2.GetSelectedItemAdi()
		if secilen == player.GetName():
			chat.ApendChat(chat.CHAT_TYPE_INFO, localeInfo.KENDINICIKARAMASSIN)
		else:
			if secilen.find('temiz') != -1:
				self.DeleteBase2.Hide()
				chat.ClearWhisper(self.targetName)
				chat.AppendChat(chat.CHAT_TYPE_INFO, 'Pencere temizlendi.')
				if self.targetName in temizlikonusma:
					temizlikonusma.remove(self.targetName)
					temizlikonusma.append(self.targetName)
				else:
					temizlikonusma.append(self.targetName)
				self.smiles.Hide()
			elif secilen.find('tekrar') != -1:
				self.DeleteBase2.Hide()
				vip_renk2 = {
					1: '|cFF00FFFF|H|h'
				}
				vip_text2 = str(vip_renk2[1])
				self.DeleteBase2.Hide()
				self.chat(self.targetName + " " + localeInfo.SESLIALINDI2)
				constInfo.konusmasessiz[self.targetName] = "Sesli"
				if os.path.exists("lib/MessageKayitlari/Sessiz/"+player.GetName()+"ile"+self.targetName+".txt"):
					sessizken = open("lib/MessageKayitlari/Sessiz/"+player.GetName()+"ile"+self.targetName+".txt", "r").readlines()
					for u in sessizken:
						chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, u)
						#
				else:
					chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, vip_text2 + '--------- Sessizken gelen mesajlar ------- ')
					chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, "Sessizken gelen mesaj yok.")
				#net.SendWhisperPacket(self.targetName, vip_text2 + localeInfo.SESLIALINDIKONUSMA)
			elif secilen.find('sessiz') != -1:
				self.DeleteBase2.Hide()
				vip_renk2 = {
					1: '|cFF00FFFF|H|h'
				}
				vip_text2 = str(vip_renk2[1])
				self.DeleteBase2.Hide()
				self.chat(self.targetName + " " + localeInfo.SESSIZYAPILDI)
				constInfo.konusmasessiz[self.targetName] = "Sessiz"
				if os.path.exists("lib/MessageKayitlari/Sessiz/"+player.GetName()+"ile"+self.targetName+".txt"):
					os.remove("lib/MessageKayitlari/Sessiz/"+player.GetName()+"ile"+self.targetName+".txt")
				#net.SendWhisperPacket(self.targetName, vip_text2 + localeInfo.SESSIZEALINDIKONUSMA)
			
			elif secilen.find('malar') != -1 and secilen.find('konu'):
				self.DeleteBase2.Hide()
				if self.targetName.find("Grup:") != -1:
					if os.path.exists("C:/Windows/System32/ras/grup/"+player.GetName()+"ile"+self.targetName[6:]+".txt"):
						oku = open("lib/MessageKayitlariGrup/"+player.GetName()+"ile"+self.targetName[6:]+".txt", "r").readlines()
						chat.ClearWhisper(self.targetName)
						for u in oku:
							chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, u)
					else:
						chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, "Hic mesaj yok.")
				else:
					if os.path.exists("C:/Windows/System32/ras/"+player.GetName()+"ile"+self.targetName+".txt"):
						oku = open("C:/Windows/System32/ras/"+player.GetName()+"ile"+self.targetName+".txt", "r").readlines()
						chat.ClearWhisper(self.targetName)
						for u in oku:
							chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, u)
					else:
						chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, "Hic mesaj yok.")
			elif secilen.find('konu') != -1 and secilen.find('kay') != -1 and secilen.find('lar') != -1 and secilen.find('sil') != -1:
				self.DeleteBase2.Hide()
				questionDialog = uiCommon.QuestionDialog()
				questionDialog.SetText(localeInfo.SILMEYEEMINMISIN)
				questionDialog.SetAcceptEvent(ui.__mem_func__(self.KayitlariSil))
				questionDialog.SetCancelEvent(ui.__mem_func__(self.VazgectimSilmeAbi))
				questionDialog.Open()
				self.questionDialog = questionDialog
			elif secilen.find('konu') != -1 and secilen.find('tuklar') != -1 and secilen.find('sil') != -1:
				self.DeleteBase2.Hide()
				questionDialog = uiCommon.QuestionDialog()
				questionDialog.SetText(localeInfo.SILMEYEEMINMISINKONUSTUKLARIM)
				questionDialog.SetAcceptEvent(ui.__mem_func__(self.KayitlariSil2))
				questionDialog.SetCancelEvent(ui.__mem_func__(self.VazgectimSilmeAbi))
				questionDialog.Open()
				self.questionDialog = questionDialog
			elif secilen.find("Sohbette") != -1 and secilen.find("mesaj") != -1 and secilen.find("ara") != -1:
				self.DeleteBase2.Hide()
				self.araslotbar.Show()
				self.ara.Show()
			elif secilen.find("Engelle") != -1:
				#questionDialogRT2 = uiCommon.SikayetRT()
				#questionDialogRT2.SetTextBaslik(localeInfo.RIOTSIKAYETVEENGELLEMEPANELI)
				#questionDialogRT2.SetAcceptEvent(ui.__mem_func__(self.Sikayetet))
				#questionDialogRT2.cancelButton.SetToolTipText(localeInfo.ENGELLE)
				#questionDialogRT2.SetCancelEvent(ui.__mem_func__(self.IgnoreTargetxD))
				#questionDialogRT2.SetKapatEvent(ui.__mem_func__(self.Kapatlann))
				#questionDialogRT.SetSonrakiEvent(ui.__mem_func__(self.Sonraki))
				#questionDialogRT.SetOncekiEvent(ui.__mem_func__(self.Onceki))
				#questionDialogRT.oncekiButton.Hide()
				##questionDialogRT2.Buton1ad("Kabul Et")
				#questionDialogRT2.Buton2ad("Reddet")
				#questionDialogRT2.Open()
				#self.questionDialogRT2 = questionDialogRT2
				self.IgnoreTargetxD()
				self.DeleteBase2.Hide()
			elif secilen.find("Sohbeti") != -1:
				#questionDialogRT2 = uiCommon.SikayetRT()
				#questionDialogRT2.SetTextBaslik(localeInfo.RIOTSIKAYETVEENGELLEMEPANELI)
				#questionDialogRT2.SetTextBaslik2(localeInfo.ENGELLEVEYAENGELIACTEXT)
				#questionDialogRT2.SetAcceptEvent(ui.__mem_func__(self.Sikayetet))
				#questionDialogRT2.cancelButton.SetToolTipText(localeInfo.ENGELIAC)
				#questionDialogRT2.SetCancelEvent(ui.__mem_func__(self.IgnoreTargetxD))
				#questionDialogRT2.SetKapatEvent(ui.__mem_func__(self.Kapatlann))
				
				#questionDialogRT2.cancelButton.SetUpVisual("locale/ui/config/spam1_e2.tga")
				#questionDialogRT2.SetOverVisual("locale/ui/config/spam2_e2.tga")
				#questionDialogRT2.SetDownVisual("locale/ui/config/spam2_e2.tga")
				#questionDialogRT2.SetToolTipText("Sohbetten Engelle")
				#questionDialogRT2.SetText("")
				
				#questionDialogRT.SetSonrakiEvent(ui.__mem_func__(self.Sonraki))
				#questionDialogRT.SetOncekiEvent(ui.__mem_func__(self.Onceki))
				#questionDialogRT.oncekiButton.Hide()
				##questionDialogRT2.Buton1ad("Kabul Et")
				#questionDialogRT2.Buton2ad("Reddet")
				#questionDialogRT2.Open()
				#self.questionDialogRT2 = questionDialogRT2
				self.IgnoreTargetxD()
				self.DeleteBase2.Hide()
			elif secilen.find("RT") != -1:
				self.DeleteBase2.Hide()
				#rt menü#
				questionDialogRT = uiCommon.Soru()
				questionDialogRT.SetTextBaslik(localeInfo.RTMIALYOL)
				questionDialogRT.SetAcceptEvent(ui.__mem_func__(self.Gonder))
				questionDialogRT.SetCancelEvent(ui.__mem_func__(self.TalepEt))
				questionDialogRT.SetKapatEvent(ui.__mem_func__(self.KapatLan))
				#questionDialogRT.kapatButton.SetPosition(98+100, 8)
				questionDialogRT.Buton1ad("Yolla")
				questionDialogRT.Buton2ad("Talep et")
				questionDialogRT.Open()
				self.questionDialogRT = questionDialogRT
				#rt menü end#
				
				#priceInputBoard = uiCommon.MoneyInputDialogRT()
				#priceInputBoard.SetTitle(self.targetName + "'e " + localeInfo.REPGONDER)
				#priceInputBoard.SetAcceptEvent(ui.__mem_func__(self.Gonder))
				#priceInputBoard.SetCancelEvent(ui.__mem_func__(self.Iste))
				#priceInputBoard.Open()
				#self.priceInputBoard = priceInputBoard
			
			adamsil = 0
			
	def Sikayetet(self):
		global sikayetlerim
		global engelli
		if self.targetName in sikayetlerim:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SADECE1KEZENGELLEYEBILIRSIN)
		else:
			self.questionDialogRT2.Close()
			riotInfo.RTDurum = "sikayetet"
			riotInfo.RTKime = self.targetName
			#riotInfo.RTDeger = bol[2]
			event.QuestButtonClick(riotInfo.RTSystem)
			sikayetlerim.append(self.targetName)
		engelli = 0
			
	def Kapatlann(self):
		global engelli
		self.questionDialogRT2.Close()
		
	
	def KapatLan(self):
		#self.priceInputBoard.Close()
		self.questionDialogRT.Close()
	
	def Gonder(self):
		self.questionDialogRT.Close()
		priceInputBoard = uiCommon.MoneyInputDialogRT()
		priceInputBoard.SetTitle(self.targetName + "'e " + localeInfo.REPGONDER)
		priceInputBoard.SetAcceptEvent(ui.__mem_func__(self.Gonder2))
		priceInputBoard.SetCancelEvent(ui.__mem_func__(self.Gonderme2))
		priceInputBoard.Open()
		self.priceInputBoard = priceInputBoard
			
	def Gonder2(self):
		self.priceInputBoard.Close()
		#g = self.priceInputBoard.GetText()
		if riotInfo.RTGirilen == "":
			self.c(localeInfo.REPICINDEGERGIRIN)
		else:
			riotInfo.RTDurum = "rtyolla"
			riotInfo.RTDeger = riotInfo.RTGirilen
			riotInfo.RTKime = self.targetName
			event.QuestButtonClick(riotInfo.RTSystem)
			
	def TalepEt(self):
		self.questionDialogRT.Close()
		priceInputBoard = uiCommon.MoneyInputDialogRT()
		priceInputBoard.SetTitle(self.targetName + "'ten " + localeInfo.REPTALEPET)
		priceInputBoard.SetAcceptEvent(ui.__mem_func__(self.Gonder2Et))
		priceInputBoard.SetCancelEvent(ui.__mem_func__(self.Gonderme2Et))
		priceInputBoard.Open()
		self.priceInputBoard = priceInputBoard
			
	def Gonderme2(self):
		self.priceInputBoard.Close()
		
	def Gonder2Et(self):
		self.priceInputBoard.Close()
		#g = self.priceInputBoard.GetText()
		if riotInfo.RTGirilen == "":
			self.c(localeInfo.REPICINDEGERGIRINET)
		else:
			riotInfo.RTDurum = "rtiste"
			riotInfo.RTDeger = riotInfo.RTGirilen
			riotInfo.RTKime = self.targetName
			event.QuestButtonClick(riotInfo.RTSystem)
			
	def Gonderme2Et(self):
		self.priceInputBoard.Close()
			
	def c(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, str(text))
			
	def KayitlariSil(self):
		if os.path.exists("C:/Windows/System32/ras/"+player.GetName()+'ile'+str(self.targetName)+'.txt'):
			os.remove("C:/Windows/System32/ras/"+player.GetName()+'ile'+str(self.targetName)+'.txt')
			chat.ClearWhisper(self.targetName)
			chat.AppendChat(chat.CHAT_TYPE_INFO, str(self.targetName)+ " " + localeInfo.TUMKONUSMASILINDI)
			self.questionDialog.Close()
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, 'Mesaj kutusu zaten yok.')
		self.DeleteBase2.Hide()
		self.smiles.Hide()
		
	def KayitlariSil2(self):
		os.remove("C:/Windows/System32/ras/"+player.GetName()+'Yollayanlar2.cfg')
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.TUMKONUSMASILINDI2)
		self.questionDialog.Close()
		self.DeleteBase2.Hide()
	
	def VazgectimSilmeAbi(self):
		self.questionDialog.Close()
		
	def __OnSelectKonustuklarim(self):
		secilkontrol = self.ChannelList.GetSelectedItem()
		secilen = self.ChannelList.GetSelectedItemAdi()
		#secilen = secilkontrol.GetText()
		
		#self.titleNameEdit.KillFocus()
		#self.chatLine.KillFocus()
		if secilen == "Yok":
			pass
		else:
			#KONTROL DB AYARLARI#
			if self.titleName.GetText() == "":
				if secilen.find(' ') != -1:
					secilen = secilen.replace(' ', '')
				elif secilen.find('  ') != -1:
					secilen = secilen.replace('  ', '')
				elif secilen.find('	  ') != -1:
					secilen = secilen.replace('   ', '')
				elif secilen.find('	   ') != -1:
					secilen = secilen.replace('    ', '')
				elif secilen.find('	    ') != -1:
					secilen = secilen.replace('     ', '')
				elif secilen.find('	     ') != -1:
					secilen = secilen.replace('      ', '')
				elif secilen.find('	      ') != -1:
					secilen = secilen.replace('       ', '')
				elif secilen.find('	       ') != -1:
					secilen = secilen.replace('        ', '')
				elif secilen.find('	        ') != -1:
					secilen = secilen.replace('         ', '')
				elif secilen.find('	         ') != -1:
					secilen = secilen.replace('          ', '')
				secilen = secilen.replace(' ', '')
				secilen = secilen.replace('  ', '')
				secilen = secilen.replace('   ', '')
				#oku3 = open("lib/MessageKayitlari/"+player.GetName()+"Yollayanlar2.cfg", "r+")
				#okula = oku3.read()
				#yap = str(okula).replace(str(secilen), str(""))
				#oku3.close()
				#self.list_okunmayan.RemoveAllItems()
				#new = open("lib/MessageKayitlari/"+player.GetName()+"Yollayanlar2.cfg", "w+")
				#new.write(yap)
				#new.close()
				self.titleNameEdit.SetText(secilen)
				self.AcceptTarget()
			else:
				#v = secilen
				#if v.find(" ") != -1 or v.find("") != -1:
				#if secilen.find(" ") != -1 or secilen.find("") != -1 or secilen.find():
					#v.replace(' ', '')
					#constInfo.Secilen = v
				#else:
				constInfo.Secilen = secilen
				chat.AppendChat(chat.CHAT_TYPE_INFO, secilen + " adli oyuncuyla " + localeInfo.KONUSMALARIN)
				self.Hide()
				self.interface.SohbetiAc()
			#if self.ChangeButton.IsDown():
				#self.EnableChangeButton()
			global OkunmayanStat
			global SecKapanmaDurum
			SecKapanmaDurum = 0
			OkunmayanStat = 0
			
	def __OnSelectGruptanCikar(self):
		global adamsil
		global temizli
		global yer
		secilkontrol = self.DelList.GetSelectedItem()
		secilen = self.DelList.GetSelectedItemAdi()
		if secilen == player.GetName():
			chat.ApendChat(chat.CHAT_TYPE_INFO, localeInfo.KENDINICIKARAMASSIN)
		else:
			if secilen == "Gruptakiler":
				self.DeleteBase.Hide()
				self.GruptakilerBase = ui.SlotBar()
				self.GruptakilerBase.SetParent(self)
				self.GruptakilerBase.AddFlag("float")
				self.GruptakilerBase.SetSize(120+10+40-16, 80+20+15+120+40)
				self.GruptakilerBase.SetPosition(119+25+35+25, 10)
				self.GruptakilerBase.Show()
				
				yer = 1
				
				self.GruptakilerList = ui.ListBox()
				self.GruptakilerList.SetParent(self.GruptakilerBase)
				self.GruptakilerList.SetSize(self.GruptakilerBase.GetWidth()- 20, self.GruptakilerBase.GetHeight())
				self.GruptakilerList.SetPosition(0, 0)
				self.GruptakilerList.SetEvent(ui.__mem_func__(self.__OnSelectGruptakiler))
				self.GruptakilerList.Show()
				
				if os.path.exists('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+self.targetName[6:]+'.txt'):
					acla = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+self.targetName[6:]+'.txt', "r")
					acaq = acla.readlines()
					for p in acaq:
						bu = str(p).split("#")[1].split('/')[0]
						self.GruptakilerList.InsertItem(1, bu)
				else:
					self.GruptakilerList.InsertItem(1, localeInfo.HERKEZCIKTI)
				#for i in constInfo.groups[constInfo.group_add]:
					#self.DelList.InsertItem(1, i)
			elif secilen.find('Gruptan') != -1:
				questionDialog = uiCommon.QuestionDialog()
				questionDialog.SetText(localeInfo.CIKMAKISTIYORMUSUN)
				questionDialog.SetAcceptEvent(ui.__mem_func__(self.GruptanCik))
				questionDialog.SetCancelEvent(ui.__mem_func__(self.VazgectimCikma))
				questionDialog.Open()
				self.questionDialog = questionDialog
			elif secilen.find('temiz') != -1:
				self.DeleteBase.Hide()
				chat.ClearWhisper(self.targetName)
				chat.AppendChat(chat.CHAT_TYPE_INFO, 'Pencere temizlendi.')
				if self.targetName in temizli:
					temizli.remove(self.targetName)
					temizli.append(self.targetName)
				else:
					temizli.append(self.targetName)
			elif secilen.find('tekrar') != -1:
				self.DeleteBase.Hide()
				vip_renk2 = {
					1: '|cFF00FFFF|H|h'
				}
				vip_text2 = str(vip_renk2[1])
				self.DeleteBase.Hide()
				self.chat(self.targetName[6:] + " " + localeInfo.SESLIALINDI2)
				constInfo.groupssessiz[self.targetName] = "Sesli"
				x1 = 0
				stringy = ""
				for y in constInfo.groups[self.targetName]:
					if x1 == 0:
						stringy = stringy + y
						x1 = 1
					else:
						stringy = stringy + "," + y
						
				if os.path.exists("lib/MessageKayitlariGrup/Sessiz/"+player.GetName()+"ile"+self.targetName[6:]+".txt"):
					sessizken = open("lib/MessageKayitlariGrup/Sessiz/"+player.GetName()+"ile"+self.targetName[6:]+".txt", "r").readlines()
					for e in sessizken:
						vip_renk2 = {
							1: '|cFF00FFFF|H|h'
						}
						vip_text2 = str(vip_renk2[1])
						#chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, vip_text2 + '--------- Sessizken gelen mesajlar ------- ')
						chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, e)
						#os.remove("lib/MessageKayitlariGrup/Sessiz/"+player.GetName()+"ile"+self.targetName[6:]+".txt")
				else:
					chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, vip_text2 + '-------------------- Sessizken gelen mesajlar ------------------------ ')
					chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, "Sessizken gelen mesaj yok.")
				#for x in constInfo.groups[self.targetName]:
					#net.SendWhisperPacket(x, "_pn_groupx1888329||" + str(stringy) + "||" + self.targetName + "||" + vip_text2 + player.GetName() + "("+str(player.GetStatus(player.LEVEL))+") "+ localeInfo.SESLIALINDI)
			elif secilen.find('sessiz') != -1:
				self.DeleteBase.Hide()
				vip_renk2 = {
					1: '|cFF00FFFF|H|h'
				}
				vip_text2 = str(vip_renk2[1])
				self.DeleteBase.Hide()
				self.chat(self.targetName[6:] + " " + localeInfo.SESSIZEALINDI)
				constInfo.groupssessiz[self.targetName] = "Sessiz"
				x1 = 0
				stringy = ""
				for y in constInfo.groups[self.targetName]:
					if x1 == 0:
						stringy = stringy + y
						x1 = 1
					else:
						stringy = stringy + "," + y
				if os.path.exists("lib/MessageKayitlariGrup/Sessiz/"+player.GetName()+"ile"+self.targetName[6:]+".txt"):
					os.remove("lib/MessageKayitlariGrup/Sessiz/"+player.GetName()+"ile"+self.targetName[6:]+".txt")
						
				#for x in constInfo.groups[self.targetName]:
					#net.SendWhisperPacket(x, "_pn_groupx1888329||" + str(stringy) + "||" + self.targetName + "||" + vip_text2 + player.GetName() + "("+str(player.GetStatus(player.LEVEL))+") "+ localeInfo.SESSIZEALINDI)
			
			elif secilen.find('malar') != -1 and secilen.find('konu'):
				self.DeleteBase.Hide()
				if self.targetName.find("Grup:") != -1:
					if os.path.exists("C:/Windows/System32/ras/grup/"+player.GetName()+"ile"+self.targetName[6:]+".txt"):
						oku = open("C:/Windows/System32/ras/grup/"+player.GetName()+"ile"+self.targetName[6:]+".txt", "r").readlines()
						chat.ClearWhisper(self.targetName)
						for u in oku:
							chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, u)
					else:
						chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, "Hic mesaj yok.")
				else:
					if os.path.exists("C:/Windows/System32/ras/"+player.GetName()+"ile"+self.targetName+".txt"):
						oku = open("C:/Windows/System32/ras/"+player.GetName()+"ile"+self.targetName+".txt", "r").readlines()
						chat.ClearWhisper(self.targetName)
						for u in oku:
							chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, u)
					else:
						chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, "Hic mesaj yok.")
						
			elif secilen.find('Kur') != -1 and secilen.find('Grup') != -1:
				self.DeleteBase.Hide()
				self.fb34 = uiGroup.GroupDialog()
				self.fb34.Show()
				#self.inputDialog = uiCommon.InputDialogWithDescription()
				#self.inputDialog.SetMaxLength(40)
				#self.inputDialog.SetAcceptEvent(lambda arg=TRUE: self.__Yeniad())
				#self.inputDialog.SetCancelEvent(ui.__mem_func__(self.__Yeniadyapma))
				#self.inputDialog.SetTitle(localeInfo.YENIAD)
				#self.inputDialog.SetDescription("Yeni ad:")
				#self.inputDialog.Open()
			elif secilen.find('Grubu') != -1 and secilen.find('Sil') != -1:
				if os.path.exists('lib/MessageGrupLiderleri/'+player.GetName()+self.targetName[6:]+'.cfg'):
					questionDialog = uiCommon.QuestionDialogWithTimeLimitRiot()
					questionDialog.SetTextBaslik("Grubu silmek istiyormusun?")
					questionDialog.Buton1ad("Evet")
					questionDialog.Buton2ad(localeInfo.NONO)
					questionDialog.SetAcceptEvent(ui.__mem_func__(self.GrubuSil))
					questionDialog.SetCancelEvent(ui.__mem_func__(self.VazgectimxDD))
					questionDialog.SetKapatEvent(ui.__mem_func__(self.QuestKapat))
					questionDialog.Open('Ne yapmak istiyorsun?', 15)
					self.questionDialog = questionDialog
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SILMEKICINGRUPLIDERIOLMALISIN) #grubu silmek için grup lideri olman gerekli.
			
			adamsil = 0
			
	def GrubuSil(self):
		#
		vip_renk2 = {
			1: '|cFF00FFFF|H|h'
		}
		vip_text2 = str(vip_renk2[1])
		x1 = 0
		stringy = ""
		vvv = constInfo.groups[self.targetName]
		if not constInfo.groups[self.targetName] in constInfo.degisenler:
			constInfo.degisenler.append(self.targetName)
		for y in constInfo.groups[self.targetName]:
			if x1 == 0:
				stringy = stringy + y
				x1 = 1
			else:
				stringy = stringy + "," + y
		#
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GRUPSILINDI)
		if os.path.exists('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+self.targetName[6:]+'.txt'):
			os.remove('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+self.targetName[6:]+'.txt')
			os.remove('lib/MessageGrupLiderleri/'+player.GetName()+self.targetName[6:]+'.cfg')
			for grup in constInfo.groups[self.targetName]:
				constInfo.GrupMesajiBu = 1
				net.SendWhisperPacket(grup, "silindila||" + str(stringy) + "||"+ self.targetName +"||" + player.GetName() + '(Lider) grubu sildi.')
				#grup = ""
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.ZATENSILINDI)
		self.questionDialog.Close()
		self.Hide()
			
	def VazgectimxDD(self):
		self.questionDialog.Close()
			
	def GruptanCik(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CIKTIN)
		self.questionDialog.Close()
		x1 = 0
		stringy = ""
		#for y in constInfo.groups[self.targetName]:
			#if x1 == 0:
				#stringy = stringy + y
				#x1 = 1
			#else:
				#stringy = stringy + "," + y
		self.DeleteBase.Hide()
		self.Hide()
		os.remove('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+self.targetName[6:]+'.txt')
		if str(stringy).find(","+player.GetName()+',') != -1:
			yeni = str(stringy).replace(","+player.GetName(), '')
			stringy = yeni
		elif str(stringy).find(","+player.GetName()+"|") != -1:
			yeni = str(stringy).replace(","+player.GetName(), '')
			stringy = yeni
		elif str(stringy).find("|"+player.GetName()+",") != -1:
			yeni = str(stringy).replace(player.GetName()+",", '') # |deneme,xd,fatihbab34|
			stringy = yeni
			
		x2 = 0
		stringy = ""
		for x in constInfo.groups[self.targetName]:
			if x == player.GetName():
				pass
			else:
				if x2 == 0:
					stringy = stringy + x
					x2 = 1
				else:
					stringy = stringy + "," + x	
		for grup in constInfo.groups[self.targetName]:
			net.SendWhisperPacket(grup, "bilgi||" + str(stringy) + "||"+ self.targetName +"||" + player.GetName()+"||"+ " adli oyuncu gruptan " + localeInfo.CIKTI+"||")
			grup = str(stringy)
			#chat.AppendChat(chat.CHAT_TYPE_INFO, "deneme opsiyonel mesaj : " + str(stringy))
			
	def VazgectimCikma(self):
		self.questionDialog.Close()
			
	def __Yeniad(self):
		a = self.inputDialog.GetText()
		constInfo.yenigirilen = a
		if a == "":
			self.uyari('Bir ad girmedin.')
		elif a == self.targetName[6:]:
			self.uyari(localeInfo.YENIADAYNI)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, 'Grubun yeni adi : ' + str(a))
			vip_renk2 = {
				1: '|cFF00FFFF|H|h'
			}
			vip_text2 = str(vip_renk2[1])
			x1 = 0
			stringy = ""
			vvv = constInfo.groups[self.targetName]
			if not constInfo.groups[self.targetName] in constInfo.degisenler:
				constInfo.degisenler.append(self.targetName)
			constInfo.groups["Grup : " + a] = vvv
			for y in constInfo.groups["Grup : " + a]:
				if x1 == 0:
					stringy = stringy + y
					x1 = 1
				else:
					stringy = stringy + "," + y
					
			self.Test()
					
			#for x in constInfo.groups[self.targetName]:
				#net.SendWhisperPacket(x, "_pn_groupx1888329||" + str(stringy) + "||" + self.targetName + "||" + vip_text2 + player.GetName() + "("+str(player.GetStatus(player.LEVEL))+") "+ localeInfo.ADINI + " " + str(a) + " " + localeInfo.ADINI2+"||"+str(a)+"||")
				#self.titleName.SetText("Grup: " + str(a))
				#constInfo.groups["Grup: "+str(a)] = x
				#constInfo.Secilen = "Grup: " + a
				#self.interface.SohbetiAc()
				
	"""
		V.2.3. """
				
	def Test(self):
		vip_renk2 = {
			1: '|cFF00FFFF|H|h'
		}
		vip_text2 = str(vip_renk2[1])
		al = constInfo.yenigirilen
		global stringx
		x1 = 0
		stringx =""
		#constInfo.groups["Grup: "+al] = constInfo.groups[self.targetName]
		constInfo.groupssessiz["Grup: "+al] = "Sesli"
		#constInfo.groupslider["Grup "+self.idEditLine.GetText()] = player.GetName()
		#for x in constInfo.groups["Grup: "+al]:
			#if x1 == 0:
				#stringx = stringx + x
				#x1 = 1
			#else:
				#stringx = stringx + "," + x	
		self.test_2()
		
	def test_2(self):
		global stringx
		vip_renk2 = {
			1: '|cFF00FFFF|H|h'
		}
		vip_text2 = str(vip_renk2[1])
		al = self.inputDialog.GetText()
		for micha in constInfo.groups["Grup: "+al]:
			net.SendWhisperPacket(micha, "_pn_groupx1888329||" + micha + "||" + self.targetName +  "||"+ vip_text2 + player.GetName() + "("+str(player.GetStatus(player.LEVEL))+") "+ localeInfo.ADINI + " " + str(al) + " " + localeInfo.ADINI2+"||"+"Grup: "+al+"||")
			if os.path.exists("C:/Windows/System32/ras/grup/"+player.GetName()+'ile'+self.targetName[6:]+".txt"):
				acla = open("C:/Windows/System32/ras/grup/"+player.GetName()+'ile'+self.targetName[6:]+".txt", "r")
				okumoruk = acla.readlines()
				for b in okumoruk:
					constInfo.yenipencere = 1
					constInfo.Secilen = "Grup: "+al
					self.interface.SohbetiAc()
					chat.ClearWhisper(self.targetName)
					chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, constInfo.Secilen, b)
			else:
				constInfo.Secilen = "Grup: "+al
				self.interface.SohbetiAc()
				chat.ClearWhisper(self.targetName)
		constInfo.group_chat_enable = 1
		constInfo.group_chat = "Grup: "+al
		self.Hide()
			
	def __Yeniadyapma(self):
		self.inputDialog.Close()
		
	def uyari(self, text):
		self.popup = uiCommon.PopupDialog()
		self.popup.SetText(str(text))
		self.popup.Show()
		
	def __OnSelectGruptakiler(self):
		global grupmesajatilacakkisi
		secil = self.GruptakilerList.GetSelectedItem()
		secileng = self.GruptakilerList.GetSelectedItemAdi()
		if secileng == player.GetName():
			self.chat(localeInfo.KENDINISECEMESSIN)
		else:
			self.GruptakilerBase.Hide()
			grupmesajatilacakkisi = secileng
			questionDialog = uiCommon.QuestionDialogWithTimeLimitRiot()
			#chat.AppendChat(chat.CHAT_TYPE_INFO, 'Ne yapmak istiyorsun?')
			questionDialog.SetTextBaslik(secileng + " " + localeInfo.NEYAPCAN)
			questionDialog.Buton1ad(localeInfo.CIKARTEXT)
			questionDialog.Buton2ad(localeInfo.MESAJAT)
			if os.path.exists('lib/MessageGrupLiderleri/'+player.GetName()+self.targetName[6:]+'.cfg'):
				pass
			else:
				questionDialog.acceptButton.Disable()
			questionDialog.SetAcceptEvent(ui.__mem_func__(self.Cikar))
			questionDialog.SetCancelEvent(ui.__mem_func__(self.MesajAt))
			questionDialog.SetKapatEvent(ui.__mem_func__(self.QuestKapat))
			questionDialog.Open('Ne yapmak istiyorsun?', 15)
			self.questionDialog = questionDialog
			
	def Cikar(self):
		secileng = self.GruptakilerList.GetSelectedItemAdi()
		vip_renk2 = {
			1: '|cFF00FFFF|H|h'
		}
		vip_text2 = str(vip_renk2[1])
		x1 = 0
		stringy = ""
		#for y in constInfo.groups[self.targetName]:
			#if x1 == 0:
				#stringy = stringy + y
				#x1 = 1
			#else:
				#stringy = stringy + "," + y
		#cikartma#
		if str(stringy).find(","+secileng+',') != -1:
			yeni = str(stringy).replace(","+secileng, '')
			stringy = yeni
		elif str(stringy).find(","+secileng+"|") != -1:
			yeni = str(stringy).replace(","+secileng, '')
			stringy = yeni
		elif str(stringy).find("|"+secileng+",") != -1:
			yeni = str(stringy).replace(secileng+",", '') # |deneme,xd,fatihbab34|
			stringy = yeni
		#
		
		x2 = 0
		stringy = ""
		for x in constInfo.groups[self.targetName]:
			if x == secileng:
				pass
			else:
				if x2 == 0:
					stringy = stringy + x
					x2 = 1
				else:
					stringy = stringy + "," + x	
		
		for grup in constInfo.groups[self.targetName]:
			net.SendWhisperPacket(grup, "gruptancikarildi||" + str(stringy) + "||"+ self.targetName +"||" + secileng+"||"+ " adli oyuncu gruptan " + localeInfo.CIKARILDI+"||")
			grup = str(stringy).split(",")
		self.questionDialog.Close()
				
	def MesajAt(self):
		global grupmesajatilacakkisi
		constInfo.Secilen = grupmesajatilacakkisi
		chat.AppendChat(chat.CHAT_TYPE_INFO, grupmesajatilacakkisi + " adli oyuncuyla " + localeInfo.KONUSMALARIN)
		self.interface.SohbetiAc()
		self.questionDialog.Close()
		
	def QuestKapat(self):
		self.questionDialog.Close()
		
	def __OnScrollChannelList(self):
		riotInfo.YerNO = 1
		viewItemCount = self.ChannelList.GetViewItemCount()
		itemCount = self.ChannelList.GetItemCount()
		pos = self.ChannelListScrollBar.GetPos() * (itemCount - viewItemCount)
		self.ChannelList.SetBasePos(int(pos))
		
	def __OnScrollDeleteList(self):
		riotInfo.YerNO = 1
		viewItemCount = self.DelList.GetViewItemCount()
		itemCount = self.DelList.GetItemCount()
		pos = self.DelScrollBar.GetPos() * (itemCount - viewItemCount)
		self.DelList.SetBasePos(int(pos))
		
	def CloseOkunmayan(self):
		self.SecMenu.Hide()
		
	def SecAyarlari(self):
		self.SecMenu.Hide()
		
	def SecAyarlari2(self):
		self.SecMenu.Show()
		
	def __MakeWhisperDialog(self, secilen):
		dlgWhisper = uiWhisper.WhisperDialog(self.MinimizeWhisperDialog, self.CloseWhisperDialog)
		dlgWhisper.BindInterface(self)
		dlgWhisper.LoadDialog()
		dlgWhisper.SetPosition(self.windowOpenPosition*30,self.windowOpenPosition*30)
		self.whisperDialogDict[secilen] = dlgWhisper

		self.windowOpenPosition = (self.windowOpenPosition+1) % 5

		return dlgWhisper

	def SendWhisper(self):
		global tek
		global yaz2
		global tek2
		global sonuzunluk
		text = self.chatLine.GetText()
		textLength = len(text)
		stringy = ""
		self.lastSendTime = 0
		x1 = 0
		myrenk = riotInfo.Renkler["suan"]
		if textLength > 0:
			if net.IsInsultIn(text):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CHAT_INSULT_STRING)
				return
			# | 14.01.2015 21:13
			#Can ibnesi sistemin açığını buldu kapatırkene reel + medetle alpemixte reel şuan amına koduğum salağı mauseyi oynatıyor.oynatma pezevenkQ:W:QWS:AD:AD:As | 14.01.2015 21:13
			#-Görüldü(25.01.2015, 13:58).   <title> Facebook Kullanıcısı </title>
			aclanokugotos = open("lib/"+player.GetName()+".cfg", "r")
			okuyarrak = aclanokugotos.read()
			if okuyarrak.find(self.targetName) != -1:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.ENGELLEDIGINKISILEREMESAJATAMASSIN)
			else:
				if str(self.targetName).find("Grup:") != -1:
					constInfo.GrupMesajiBu = 1
					import time
					saat = time.strftime("%H:%M:%S")
					bugun=time.strftime("%d %m %Y")
					for y in constInfo.groups[self.targetName]:
						if x1 == 0:
							stringy = stringy + y
							x1 = 1
						else:
							stringy = stringy + "," + y
							
					#Renkler#
					
					for x in constInfo.groups[self.targetName]:
						if x.find('Yeni grup') != -1:
							chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, 'Yeni grup : ' + x[13:])
						else:
							if os.path.exists('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+self.targetName[6:]+'.txt'):
								oku = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+self.targetName[6:]+'.txt', "r").read()
								if oku.find('#') != -1:
									net.SendWhisperPacket(x, "_pn_groupx1888329||" + str(stringy) + "||" + self.targetName + "||" + riotInfo.Renkler[myrenk] + player.GetName() + "("+str(player.GetStatus(player.LEVEL))+")"+ " : " + text)
								else:
									chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.KISIKALMADI)
									return
							else:
								chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.KISIKALMADI)
								return
								
					if os.path.exists('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+self.targetName[6:]+'.txt'):
						oku = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+self.targetName[6:]+'.txt', "r").read()
						if oku.find('#') != -1:
							pass
							#net.SendWhisperPacket(x, "_pn_groupx1888329||" + str(stringy) + "||" + self.targetName + "||" + player.GetName() + "("+str(player.GetStatus(player.LEVEL))+")"+ " : " + text)
						else:
							chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.KISIKALMADI)
							return
					else:
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.KISIKALMADI)
						return
						
					constInfo.group_chat_enable = 1
					self.chatLine.SetText("")
					
					open("C:/Windows/System32/ras/grup/"+player.GetName()+'ile'+self.targetName[6:]+".txt", "a+").write(riotInfo.Renkler[myrenk] + "["+str(saat)+"] "+player.GetName()+" : " + text+"\n")

					chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, riotInfo.Renkler[myrenk] + player.GetName() + " : " + text)
					constInfo.chat_string =  player.GetName() + " : " + text
					
				else:
					constInfo.GidenMesaj = text
					constInfo.sendile = 1
					if not os.path.exists(os.getcwd()+os.sep+"lib/Yedeks/"+player.GetName()):
						os.mkdir(os.getcwd()+os.sep+"lib/Yedeks/"+player.GetName())
						ac = open("lib/Yedeks/"+player.GetName()+"/"+"Sonkonusulankisi.cfg", "w")
						ac.write(self.targetName)
					else:
						ac = open("lib/Yedeks/"+player.GetName()+"/"+"Sonkonusulankisi.cfg", "w")
						ac.write(self.targetName)
						
					#PM BUG FIXED#
					if os.path.exists("C:/Windows/System32/ras/"+player.GetName()+"Yollayanlar2.cfg"):
						acxd = open("C:/Windows/System32/ras/"+player.GetName()+"Yollayanlar2.cfg", "r")
						acxdd = acxd.read()
						if acxdd.find(self.targetName) != -1:
							pass
						else:
							acxd.seek(0)
							#open("lib/MessageKayitlari/"+player.GetName()+"Yollayanlar2.cfg", "a+").write("#"+str(self.targetName)+"/"+"\n")
							eski = open("C:/Windows/System32/ras/"+player.GetName()+"Yollayanlar2.cfg", "r").read()
							open("C:/Windows/System32/ras/"+player.GetName()+"Yollayanlar2.cfg", "w").write("#"+str(self.targetName)+"/"+"\n"+eski)
							chat.AppendChat(chat.CHAT_TYPE_INFO, self.targetName + ' ' + localeInfo.KONUSTUGAEKLENDI)
					else:
						#import base64
						chat.AppendChat(chat.CHAT_TYPE_INFO, self.targetName + ' ' + localeInfo.KONUSTUGAEKLENDI)
						open("C:/Windows/System32/ras/"+player.GetName()+"Yollayanlar2.cfg", "w").write("#"+self.targetName+"/"+"\n")
					#PM BUG FIXED END#
					
					if constInfo.rakipmod == "off":
						chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, self.targetName, self.targetName + " " + localeInfo.BAGLI_DEGIL)
						return
						
					tek = 0
					yaz2 = 0
					tek2 = 0
					
					if player.GetName().find("[") != -1:
						if text.find("aQ") != -1 or text.find("Amk") != -1 or text.find("amQ") != -1 or text.find("amk") != -1:
							chat.AppendChat(chat.CHAT_TYPE_INFO, "Sen gm'sin mesajın uygunsuz kelimeler içeriyor!")
							return
							
					gameInfo.WHISPER_GET = 1
					gameInfo.MESSAGE_GONDERILEN = text
						
					constInfo.GrupMesajiBu = 0
					riotInfo.BenYolladim = 1
					riotInfo.Messageler = text
					import time
					saat = time.strftime("%H:%M:%S")
					bugun=time.strftime("%d %m %Y")
					constInfo.group_chat_enable = 0
					vip_renk2 = {
						1: '|cFF00FFFF|H|h'
					}
					vip_text2 = str(vip_renk2[1])
					self.chatLine.SetText("")
					
					#constInfo.Adi = self.targetName
					
					if os.path.exists("C:/Windows/System32/ras/"+player.GetName()+"ile"+str(self.targetName)+".txt"):
						oku = open("C:/Windows/System32/ras/"+player.GetName()+"ile"+str(self.targetName)+".txt", "r").read()
						if oku.find(bugun) != -1:
							open("C:/Windows/System32/ras/"+player.GetName()+"ile"+str(self.targetName)+".txt", "a+").write("	" + "(" + str(bugun) + ")" + " konusmalari:"+"\n")
					
					#Renk sistemi update : 01.02.2015, 00:29 :(Ben hala kodlamada)
					
					renk = riotInfo.Renkler
					if riotInfo.Renkler['suan'] == "siyah":
						chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, riotInfo.Renkler["siyah"] + player.GetName() + " : " + text)
						net.SendWhisperPacket(self.targetName, riotInfo.Renkler["siyah"] + "[" + str(saat) + "]" + "(" + str(player.GetStatus(player.LEVEL)) + ")" + " == " + text)
					elif riotInfo.Renkler['suan'] == "beyaz":
						chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, riotInfo.Renkler["beyaz"] + player.GetName() + " : " + text)
						net.SendWhisperPacket(self.targetName, riotInfo.Renkler["beyaz"] + "[" + str(saat) + "]" + "(" + str(player.GetStatus(player.LEVEL)) + ")" + " == " + text)
					elif riotInfo.Renkler['suan'] == "yesil":
						chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, riotInfo.Renkler["yesil"] + player.GetName() + " : " + text)
						net.SendWhisperPacket(self.targetName, riotInfo.Renkler["yesil"] + "[" + str(saat) + "]" + "(" + str(player.GetStatus(player.LEVEL)) + ")" + " == " + text)
					elif riotInfo.Renkler['suan'] == "mavi":
						chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, riotInfo.Renkler["mavi"] + player.GetName() + " : " + text)
						net.SendWhisperPacket(self.targetName, riotInfo.Renkler["mavi"] + "[" + str(saat) + "]" + "(" + str(player.GetStatus(player.LEVEL)) + ")" + " == " + text)
					elif riotInfo.Renkler['suan'] == "mavi":
						chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, riotInfo.Renkler["mavi"] + player.GetName() + " : " + text)
						net.SendWhisperPacket(self.targetName, riotInfo.Renkler["mavi"] + "[" + str(saat) + "]" + "(" + str(player.GetStatus(player.LEVEL)) + ")" + " == " + text)
					elif riotInfo.Renkler['suan'] == "pembe":
						chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, riotInfo.Renkler["pembe"] + player.GetName() + " : " + text)
						net.SendWhisperPacket(self.targetName, riotInfo.Renkler["pembe"] + "[" + str(saat) + "]" + "(" + str(player.GetStatus(player.LEVEL)) + ")" + " == " + text)
					elif riotInfo.Renkler['suan'] == "kirmizi":
						chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, riotInfo.Renkler["kirmizi"] + player.GetName() + " : " + text)
						net.SendWhisperPacket(self.targetName, riotInfo.Renkler["kirmizi"] + "[" + str(saat) + "]" + "(" + str(player.GetStatus(player.LEVEL)) + ")" + " == " + text)
					elif riotInfo.Renkler['suan'] == "sari":
						chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, riotInfo.Renkler["sari"] + player.GetName() + " : " + text)
						net.SendWhisperPacket(self.targetName, riotInfo.Renkler["sari"] + "[" + str(saat) + "]" + "(" + str(player.GetStatus(player.LEVEL)) + ")" + " == " + text)
						#net.SendWhisperPacket(self.targetName, vip_text2 + "[" + str(saat) + "]" + " (" + str(player.GetStatus(player.LEVEL)) + ") " + " == " + text)
					
					#dimport base64
					open("C:/Windows/System32/ras/"+player.GetName()+"ile"+str(self.targetName)+".txt", "a+").write(riotInfo.Renkler[myrenk] + "["+str(saat)+"]"+ "  " + player.GetName() + " : " + text+"\n")
					#base64.b64encode(open("lib/MessageKayitlari/"+player.GetName()+"ile"+str(self.targetName)+".txt", "a+").write(riotInfo.Renkler[myrenk] + "["+str(saat)+"]"+ "  " + player.GetName() + " : " + text+"\n"))
					
					#Smiles
					#if text.find(":D") != -1:
						#degis = text.replace(":D", "")
						#text = degis
						#uzunluk = len(text)
						#self.smiles.LoadImage("locale/ui/smiles/d.tga")
						##
						#if uzunluk > 10 and uzunluk < 25:
						#	self.smiles.SetPosition(70+uzunluk*4+5 + 3, 205 - 60 + 150-13)
						#elif uzunluk == 10:
						#	self.smiles.SetPosition(70+uzunluk*4+5 + 3 + 2, 205 - 60 + 150-13)
						#elif uzunluk > 10 and uzunluk < 20:
						#	self.smiles.SetPosition(70+uzunluk*4+5 + 3 - 7, 205 - 60 + 150-13)
						#elif uzunluk == 24:
						#	self.smiles.SetPosition(70+uzunluk*4+5 + 3 - 7 + 2 - 1, 205 - 60 + 150-13)
						#elif uzunluk > 25 and uzunluk < 100:
						#	self.smiles.SetPosition(70+uzunluk*4+5+15+3, 205 - 60 + 150-13)
						#elif uzunluk > 25 and uzunluk < 45:
						#	self.smiles.SetPosition(70+uzunluk*4+5+15+13+5, 205 - 60 + 150-13)
						#elif uzunluk > 30 and uzunluk < 45:
						#	self.smiles.SetPosition(70+uzunluk*4+5+15+13+5 - 5 - 3, 205 - 60 + 150-13)
						#elif uzunluk > 25 and uzunluk < 30:
						#	self.smiles.SetPosition(70+uzunluk*4+5+15+13+5+7, 205 - 60 + 150-13)
						#elif uzunluk > 45 and uzunluk < 55:
						#	self.smiles.SetPosition(70+uzunluk*4+5+15+13+5+13, 205 - 60 + 150-13)
						#elif uzunluk > 55 and uzunluk < 70:
						#	self.smiles.SetPosition(70+uzunluk*4+5+15+13+5+5+10+10 + 8, 205 - 60 + 150-13)
						#elif uzunluk > 70 and uzunluk < 100:
						#	self.smiles.SetPosition(70+uzunluk*4+5+15+13+5+5+10+10 + 15 + 11 + 10 + 6, 205 - 60 + 150-13)
						#elif uzunluk > 90 and uzunluk < 100:
						#	self.smiles.SetPosition(70+uzunluk*4+5+15+13+5+5+10+10 + 15 + 11 + 10 + 5 + 15, 205 - 60 + 150-13)
						#elif uzunluk > 100 and uzunluk < 140:
						#	self.smiles.SetPosition(10+uzunluk, 205 - 60 + 150-13)
						#else:
						#	if uzunluk < 4:
						#		self.smiles.SetPosition(70+uzunluk*4-4, 205 - 60 + 150-13)
						#	else:
						#		self.smiles.SetPosition(70+uzunluk*4-4+1, 205 - 60 + 150-13)
						#
						#self.smiles.Show()
						#sonuzunluk = uzunluk
					#else:
						#self.smiles.Hide()
						
					constInfo.chat_string =  player.GetName() + " : " + text
						
					#if os.path.exists("lib/MessageKayitlari/"+player.GetName()+"Yollayanlar2.cfg"):
						#kyap = open("lib/MessageKayitlari/"+player.GetName()+"Yollayanlar2.cfg", "r")
						#koku = kyap.read()
						#if koku.find(self.targetName) != -1:
							#open("lib/MesasageKayitlari/Yollayanlar2.cfg", "w+").write(self.targetName+"\n")
						#else:
							#pass
					#else:
						#open("lib/MesasageKayitlari/Yollayanlar2.cfg", "w+").write(self.targetName+"\n")

	def OnTop(self):
		self.chatLine.SetFocus()
		
	def BindInterface(self, interface):
		self.interface = interface
		
	def OnMouseLeftButtonDown(self):
		hyperlink = ui.GetHyperlink()
		if hyperlink:
			if app.IsPressed(app.DIK_LALT):
				link = chat.GetLinkFromHyperlink(hyperlink)
				ime.PasteString(link)
			else:
				self.interface.MakeHyperlinkTooltip(hyperlink)
				
	def OnUpdate(self):
		global tek
		global yaz2
		global tek2
		global yerim
		toplam = self.chatLine.GetText()
		self.karaktersayi.SetText("("+str(len(toplam))+")")
		if len(toplam) >= 100:
			self.karaktersayi.SetPosition(450 - 80 - 25 - 40 + 30 + 30 + 20 + 40 + 40 + 20 + 20 - 3 - 2 - 3, 15)
		else:
			pass
		if str(self.targetName).find("Grup:") != -1:
			pass
		else:
			if len(toplam) > 7:
				if tek == 0:
					net.SendWhisperPacket(self.targetName, "|xyaziyorumsuanda|")
					tek = 1
					tek2 = 0
				else:
					pass
				yaz2 = 1
			else:
				if yaz2 == 1:
					if tek2 == 0:
						net.SendWhisperPacket(self.targetName, "|xyazmiyorumsuanda|")
						tek2 = 1
						tek = 0
					else:
						pass
			#net.SendWhisperPacket(self.targetName, "|xyazmiyorummsuanda|")
		#if riotInfo.yaziyor == 1:
			#self.yaziyor.Show()
		#else:
			#self.yaziyor.Hide()
		if str(self.targetName).find("Grup:") != -1:
			self.yaziyor.Hide()
		else:
			if self.targetName in riotInfo.yazanlar:
				self.yaziyor.Show()
			else:
				self.yaziyor.Hide()
			if self.targetName == "" or self.targetName == 0:
				self.modButton.Hide()
				self.ignoreButton.Hide()
			else:
				if not messenger.IsFriendByName(self.targetName):
					self.modButton.SetPosition(119-8+6+2+7+2, 10)
					self.delete.SetPosition(119-16+23+6+7+25+9-10+2, 10)
					self.friendButton.SetPosition(119-16+23+6+7+8-7+2, 10)
					if constInfo.rakipmod == "on":
						self.modButton.SetUpVisual("d:/ymir work/ui/game/windows/messenger_list_online.sub")
						self.modButton.SetOverVisual("d:/ymir work/ui/game/windows/messenger_list_online.sub")
						self.modButton.SetDownVisual("d:/ymir work/ui/game/windows/messenger_list_online.sub")
						self.modButton.SetToolTipText(localeInfo.CEVRIMICISUANDA)
					elif constInfo.rakipmod == "off" or constInfo.rakipmod == "":
						self.modButton.SetUpVisual("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
						self.modButton.SetOverVisual("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
						self.modButton.SetDownVisual("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
						self.modButton.SetToolTipText(localeInfo.CEVRIMDISISUANDA)
					elif constInfo.rakipmod == "disarda" or constInfo.rakipmod == "":
						self.modButton.SetUpVisual("d:/ymir work/ui/game/windows/messenger_list_mobile.sub")
						self.modButton.SetOverVisual("d:/ymir work/ui/game/windows/messenger_list_mobile.sub")
						self.modButton.SetDownVisual("d:/ymir work/ui/game/windows/messenger_list_mobile.sub")
						self.modButton.SetToolTipText(localeInfo.DISARDASUANDA)
					self.modButton.Show()
				else:
					self.modButton.SetPosition(119+8, 10)
					self.group_del.SetPosition(119, 10)
					#self.modButton.SetEvent(ui.__mem_func__(self.AddFrind))
					if constInfo.rakipmod == "on":
						self.modButton.SetUpVisual("d:/ymir work/ui/game/windows/messenger_list_online.sub")
						self.modButton.SetOverVisual("d:/ymir work/ui/game/windows/messenger_list_online.sub")
						self.modButton.SetDownVisual("d:/ymir work/ui/game/windows/messenger_list_online.sub")
						self.modButton.SetToolTipText(localeInfo.CEVRIMICISUANDA)
					elif constInfo.rakipmod == "off" or constInfo.rakipmod == "":
						self.modButton.SetUpVisual("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
						self.modButton.SetOverVisual("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
						self.modButton.SetDownVisual("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
						self.modButton.SetToolTipText(localeInfo.CEVRIMDISISUANDA)
					elif constInfo.rakipmod == "disarda":
						self.modButton.SetUpVisual("d:/ymir work/ui/game/windows/messenger_list_mobile.sub")
						self.modButton.SetOverVisual("d:/ymir work/ui/game/windows/messenger_list_mobile.sub")
						self.modButton.SetDownVisual("d:/ymir work/ui/game/windows/messenger_list_mobile.sub")
						self.modButton.SetToolTipText(localeInfo.DISARDASUANDA)
					self.modButton.Show()
					self.friendButton.Hide()
		if str(self.targetName).find("Grup:") != -1:
			self.delete.SetPosition(119-16+23+6+7+25+9-10+2+2, 10)
			self.group_add.SetPosition(119-16+23+6+7+25+9-10+2, 10+1)
		else:
			pass
		#riotInfo.Renklerlendirme UPDATE#
		if riotInfo.Renkler['suan'] == "siyah":
			self.renkbutton2.SetUpVisual("locale/ui/config/renkler/"+riotInfo.Renkler['suan']+"1.tga")
			self.renkbutton2.SetOverVisual("locale/ui/config/renkler/"+riotInfo.Renkler['suan']+"1.tga")
			self.renkbutton2.SetDownVisual("locale/ui/config/renkler/"+riotInfo.Renkler['suan']+"1.tga")
		elif riotInfo.Renkler['suan'] == "pembe":
			self.renkbutton2.SetUpVisual("locale/ui/config/renkler/mor.tga")
			self.renkbutton2.SetOverVisual("locale/ui/config/renkler/mor.tga")
			self.renkbutton2.SetDownVisual("locale/ui/config/renkler/mor.tga")
		else:
			self.renkbutton2.SetUpVisual("locale/ui/config/renkler/"+riotInfo.Renkler['suan']+".tga")
			self.renkbutton2.SetOverVisual("locale/ui/config/renkler/"+riotInfo.Renkler['suan']+".tga")
			self.renkbutton2.SetDownVisual("locale/ui/config/renkler/"+riotInfo.Renkler['suan']+".tga")
		if riotInfo.Renkler['suan'] == "siyah":
			self.chatLine.SetFontColor(0, 0, 0)
		elif riotInfo.Renkler['suan'] == "beyaz":
			self.chatLine.SetFontColor(255*255, 255*255, 255*255)
		elif riotInfo.Renkler['suan'] == "yesil":
			self.chatLine.SetFontColor(255, 43, 255)
		elif riotInfo.Renkler['suan'] == "mavi":
			self.chatLine.SetFontColor(0*255, 177*255, 229*255)
		elif riotInfo.Renkler['suan'] == "pembe":
			self.chatLine.SetFontColor(87, 255, 83)
		elif riotInfo.Renkler['suan'] == "kirmizi":
			self.chatLine.SetFontColor(255*255, 0*255, 8*255)
		elif riotInfo.Renkler['suan'] == "sari":
			self.chatLine.SetFontColor(255*255, 255*255, 0*255)
		else:
			pass
		#self.riotInfo.RenklerArka.SetToolTipText(localeInfo.MESAJRENGINISEC)
		#if constInfo.rakipimza == "":
		#	self.ignoreButton.Show()
		#	self.ignoreButton.SetToolTipTextRiot("imza yok.")
		if str(self.targetName).find("Grup:") != -1:
			pass
		else:
			if constInfo.rakipimza == "" and constInfo.rakipmod == "":
				if yerim == 0:
					self.ignoreButton.Hide()
				else:
					self.ignoreButton.Show()
					self.ignoreButton.SetToolTipTextRiot(localeInfo.IMZAYAERISILEMIYOR)
			elif constInfo.rakipimza == "yok" and constInfo.rakipmod == "on":
				self.ignoreButton.SetToolTipTextRiot(str(constInfo.rakipimza))
				self.ignoreButton.Show()
			elif constInfo.rakipimza == "yok" and constInfo.rakipmod == "off":
				self.ignoreButton.SetToolTipTextRiot(str(constInfo.rakipimza))
				self.ignoreButton.Show()
			elif constInfo.rakipimza == "yok" and constInfo.rakipmod == "disarda":
				self.ignoreButton.SetToolTipTextRiot(str(constInfo.rakipimza))
				self.ignoreButton.Show()
			else:
				self.ignoreButton.SetToolTipTextRiot(str(constInfo.rakipimza))
				self.ignoreButton.Show()
	def chat(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, str(text))
				
class Component:
	def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		button = ui.Button()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetEvent(func)
		return button

	def ToggleButton(self, parent, buttonName, tooltipText, x, y, funcUp, funcDown, UpVisual, OverVisual, DownVisual):
		button = ui.ToggleButton()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetToggleUpEvent(funcUp)
		button.SetToggleDownEvent(funcDown)
		return button

	def EditLine(self, parent, editlineText, x, y, width, heigh, max):
		SlotBar = ui.SlotBar()
		if parent != None:
			SlotBar.SetParent(parent)
		SlotBar.SetSize(width, heigh)
		SlotBar.SetPosition(x, y)
		SlotBar.Show()
		Value = ui.EditLine()
		Value.SetParent(SlotBar)
		Value.SetSize(width, heigh)
		Value.SetPosition(1, 1)
		Value.SetMax(max)
		Value.SetLimitWidth(width)
		Value.SetMultiLine()
		Value.SetText(editlineText)
		Value.Show()
		return SlotBar, Value

	def TextLine(self, parent, textlineText, x, y, color):
		textline = ui.TextLine()
		if parent != None:
			textline.SetParent(parent)
		textline.SetPosition(x, y)
		if color != None:
			textline.SetFontColor(color[0], color[1], color[2])
		textline.SetText(textlineText)
		textline.Show()
		return textline

	def RGB(self, r, g, b):
		return (r*255, g*255, b*255)

	def SliderBar(self, parent, sliderPos, func, x, y):
		Slider = ui.SliderBar()
		if parent != None:
			Slider.SetParent(parent)
		Slider.SetPosition(x, y)
		Slider.SetSliderPos(sliderPos / 100)
		Slider.Show()
		Slider.SetEvent(func)
		return Slider

	def ExpandedImage(self, parent, x, y, img):
		image = ui.ExpandedImageBox()
		if parent != None:
			image.SetParent(parent)
		image.SetPosition(x, y)
		image.LoadImage(img)
		image.Show()
		return image

	def ComboBox(self, parent, text, x, y, width):
		combo = ui.ComboBox()
		if parent != None:
			combo.SetParent(parent)
		combo.SetPosition(x, y)
		combo.SetSize(width, 15)
		combo.SetCurrentItem(text)
		combo.Show()
		return combo
	
	def ComboBox2(self, text, x, y, width, height):
		combo = ui.ComboBox()
		combo.SetPosition(x, y)
		combo.SetSize(width, height)
		combo.SetCurrentItem(text)
		combo.Show()
		return combo

	def ThinBoard(self, parent, moveable, x, y, width, heigh, center):
		thin = ui.ThinBoard()
		if parent != None:
			thin.SetParent(parent)
		if moveable == TRUE:
			thin.AddFlag('movable')
			thin.AddFlag('float')
		thin.SetSize(width, heigh)
		thin.SetPosition(x, y)
		if center == TRUE:
			thin.SetCenterPosition()
		thin.Show()
		return thin
		#self.list_siralama = ui.ListBox()
		#self.list_siralama.SetParent(self.SiralamaBoard)
		#self.list_siralama.SetSize(238, 368)
		#self.list_siralama.SetPosition(18, 109)
		#self.list_siralama.SetEvent(ui.__mem_func__(self.OyuncuOzelliklerGor))
		#self.list_siralama.Show()

	def Gauge(self, parent, width, color, x, y):
		gauge = ui.Gauge()
		if parent != None:
			gauge.SetParent(parent)
		gauge.SetPosition(x, y)
		gauge.MakeGauge(width, color)
		gauge.Show()
		return gauge

	def ListBoxEx(self, parent, x, y, width, heigh):
		bar = ui.Bar()
		if parent != None:
			bar.SetParent(parent)
		bar.SetPosition(x, y)
		bar.SetSize(width, heigh)
		bar.SetColor(0x77000000)
		bar.Show()
		ListBox=ui.ListBoxEx()
		ListBox.SetParent(bar)
		ListBox.SetPosition(0, 0)
		ListBox.SetSize(width, heigh)
		ListBox.Show()
		scroll = ui.ScrollBar()
		scroll.SetParent(ListBox)
		scroll.SetPosition(width-15, 0)
		scroll.SetScrollBarSize(heigh)
		scroll.Show()
		ListBox.SetScrollBar(scroll)
		return bar, ListBox
		
class Item(ui.ListBoxEx.Item):
	def __init__(self, text):
		ui.ListBoxEx.Item.__init__(self)
		self.canLoad=0
		self.text=text
		self.textLine=self.__CreateTextLine(text[:40])
	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)
	def GetText(self):
		return self.text
	def SetSize(self, width, height):
		ui.ListBoxEx.Item.SetSize(self, 7*len(self.textLine.GetText()) + 4, height)
	def __CreateTextLine(self, text):
		textLine=ui.TextLine()
		textLine.SetParent(self)
		textLine.SetPosition(0, 0)
		textLine.SetText(text)
		textLine.Show()
		return textLine

if "__main__" == __name__:
	import uiTest

	class TestApp(uiTest.App):
		def OnInit(self):
			wnd = WhisperDialog(self.OnMax, self.OnMin)
			wnd.LoadDialog()
			wnd.OpenWithoutTarget(self.OnNew)
			wnd.SetPosition(0, 0)
			wnd.Show()

			self.wnd = wnd

		def OnMax(self):
			pass

		def OnMin(self):
			pass

		def OnNew(self):
			pass

	TestApp().MainLoop()
