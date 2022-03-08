import ui
import localeInfo
import net
import constInfo
import chat
import interfacemodule
import player
import uiCommon
import dbg

class GroupDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadDialog()
		self.interface = interfacemodule.Interface()
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.Hide()
		return TRUE

	def LoadDialog(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "group.py")
		except:
			import exception
			exception.Abort("ConnectingDialog.LoadDialog.BindObject")
		GetObject=self.GetChild	
		self.idEditLine				= GetObject("ID_EditLine")
		self.pwdEditLine			= GetObject("PW_EditLine")
		
		self.idEditLine.SetReturnEvent(ui.__mem_func__(self.pwdEditLine.SetFocus))
		self.idEditLine.SetTabEvent(ui.__mem_func__(self.pwdEditLine.SetFocus))
		self.pwdEditLine.SetReturnEvent(ui.__mem_func__(self.create))
		self.pwdEditLine.SetTabEvent(ui.__mem_func__(self.idEditLine.SetFocus))
		self.GetChild("titlebar").SetCloseEvent(ui.__mem_func__(self.Close))
		self.GetChild("Gamemasta1").SetEvent(ui.__mem_func__(self.create))
		self.idEditLine.SetFocus()
		
	def Test(self):
		global stringx
		names_x = self.pwdEditLine.GetText() + "," + player.GetName()
		x1 = 0
		stringx =""
		constInfo.groups["Grup: "+self.idEditLine.GetText()] = names_x.split(",")
		constInfo.groupssessiz["Grup: "+self.idEditLine.GetText()] = "Sesli"
		ac = open('lib/MessageGrupLiderleri/'+player.GetName()+self.idEditLine.GetText()+'.cfg', "w")
		ac.write("Lider benim")
		constInfo.groupslider["Grup : " + self.idEditLine.GetText()] = player.GetName()
		#constInfo.groupslider["Grup "+self.idEditLine.GetText()] = player.GetName()
		for x in constInfo.groups["Grup: "+self.idEditLine.GetText()]:
			if x1 == 0:
				stringx = stringx + x
				x1 = 1
			else:
				stringx = stringx + "," + x	
		self.test_2()
		
	def test_2(self):
		for micha in constInfo.groups["Grup: "+self.idEditLine.GetText()]:
			net.SendWhisperPacket(micha, "_pn_groupx1888329||" + str(stringx) + "||" + "Grup: "+self.idEditLine.GetText() + "||"+"Grup kuruldu!||"+player.GetName()+"||")
			net.SendWhisperPacket(micha, "_pn_groupx1888329||" + str(stringx) + "||" + "Grup: "+self.idEditLine.GetText() + "||"+player.GetName() + " grubu kurdu.||"+player.GetName()+"||")
			net.SendWhisperPacket(micha, "_pn_groupx1888329||" + str(stringx) + "||" + "Grup: "+self.idEditLine.GetText() + "||" + player.GetName() + "|| gruba katıldı.")
			constInfo.Secilen = micha
		constInfo.group_chat_enable = 1
		constInfo.group_chat = "Grup: "+self.idEditLine.GetText()
		self.Close()
		
	def create(self):
		if str(self.idEditLine.GetText()) == "":
			self.uyari(localeInfo.GRUPADIGIRIN)
		elif str(self.pwdEditLine.GetText()) == "":
			self.uyari(localeInfo.GRUPUYESIGIRIN)
		elif str(self.pwdEditLine.GetText()).find(player.GetName()+",") != -1:
			self.uyari(localeInfo.GRUPKENDINIEKLIYEMESSIN)	
		else:
			self.Test()
		
	def Show(self):
		ui.ScriptWindow.Show(self)
		
	def uyari(self, text):
		self.popup = uiCommon.PopupDialog()
		self.popup.SetText(str(text))
		self.popup.Show()
		
	def Close(self):
		self.Hide()
		return TRUE
		
	def OnPressEscapeKey(self):
		self.Close()
