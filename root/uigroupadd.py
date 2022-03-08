import ui
import localeInfo
import net
import constInfo
import chat
import interfacemodule
import uiCommon
import player
import dbg

class GroupADDDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadDialog()
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.Hide()
		return TRUE

	def LoadDialog(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "groupadd.py")
		except:
			import exception
			exception.Abort("ConnectingDialog.LoadDialog.BindObject")
		GetObject=self.GetChild	
		self.pwdEditLine				= GetObject("ID_EditLine")
		
		self.pwdEditLine.SetReturnEvent(ui.__mem_func__(self.create))
		self.pwdEditLine.SetTabEvent(ui.__mem_func__(self.create))
		self.GetChild("titlebar").SetCloseEvent(ui.__mem_func__(self.Close))
		self.GetChild("Gamemasta1").SetEvent(ui.__mem_func__(self.create))
		self.pwdEditLine.SetFocus()
		
	def Test(self):
		global stringx
		import os
		if os.path.exists('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+constInfo.group_add[6:]+'.txt'):
			ac = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+constInfo.group_add[6:]+'.txt', "r")
			aco = ac.read()
			ac.close()
			if aco.find('#'+self.pwdEditLine.GetText()+'/') != -1:
				chat.AppendChat(chat.CHAT_TYPE_INFO, 'Bu oyuncu zaten grupta.')
				return
		elif self.pwdEditLine.GetText().find(',') != -1:
			self.uyari('Sadece 1 oyuncu ekleyebilirsin.')
			return
		string_old = ""
		for p in constInfo.groups[constInfo.group_add]:
			string_old = string_old + p + ","
		names_x = string_old + self.pwdEditLine.GetText()
		x1 = 0
		stringx =""
		constInfo.groups[constInfo.group_add] = names_x.split(",")
		for x in constInfo.groups[constInfo.group_add]:
			if x1 == 0:
				stringx = stringx + x
				x1 = 1
			else:
				stringx = stringx + "," + x	
		self.test_2()
		
	def test_2(self):
		constInfo.GrupMesajiBu = 0
		for micha in constInfo.groups[constInfo.group_add]:
			net.SendWhisperPacket(micha, "_pn_groupx1888329||" + str(stringx) + "||" + constInfo.group_add + "||" + self.pwdEditLine.GetText() + " adli oyuncu " + player.GetName() + " " + localeInfo.TARAFINDAN + " gruba eklendi.||"+player.GetName()+"||"+self.pwdEditLine.GetText()+"||")
			net.SendWhisperPacket(micha, "_pn_groupx1888329||" + str(stringx) + "||" + constInfo.group_add + "||" + "xdddddddd23252133132131")
			constInfo.GrupMesajiBu = 1
			
		constInfo.group_new_name = self.pwdEditLine.GetText() + " ekledi."
		constInfo.group_chat_enable = 1
		ac = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+constInfo.group_add[6:]+'.txt', "a+")
		ac.write("#"+self.pwdEditLine.GetText()+"/"+"\n")
		
		yc = open('lib/MessageKayitlariGrupUyeleri/'+player.GetName()+'ile'+constInfo.group_add[6:]+'.txt', "r")
		yco = yc.readlines()
		yc.close()
		constInfo.yeniad = self.pwdEditLine.GetText()
		for i in yco:
			if i.find("#") != -1:
				bol = i.split("#")[1].split("/")[0]
				net.SendWhisperPacket(self.pwdEditLine.GetText(), 'eklelistene||'+bol+'||'+constInfo.group_add[6:]+"||")
		
		self.Close()
		
	def create(self):
		if str(self.pwdEditLine.GetText()) == "":
			self.popup = uiCommon.PopupDialog()
			self.popup.SetText(localeInfo.LUTFENOYUNCUADIGIRIN)
			self.popup.Show()
		elif str(self.pwdEditLine.GetText()).find(player.GetName() + ",") != -1:
			self.uyari(localeInfo.KENDINIEKLIYEMESSIN)
		else:
			self.Test()
			
	def uyari(self, text):
		self.popup = uiCommon.PopupDialog()
		self.popup.SetText(str(text))
		self.popup.Show()
		
	def Show(self):
		ui.ScriptWindow.Show(self)
		
	def Close(self):
		self.Hide()
		return TRUE
		
	def OnPressEscapeKey(self):
		self.Close()
