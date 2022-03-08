import riotInfo
import guild		

		elif Type == "resimlistbox":
				parent.Children[Index] = ImageListBox()
				parent.Children[Index].SetParent(parent)
				self.LoadElementListBox(parent.Children[Index], ElementValue, parent)
				
			elif Type == "listboxsiralama":
				parent.Children[Index] = ListBoxSiralama()
				parent.Children[Index].SetParent(parent)
				self.LoadElementListBox(parent.Children[Index], ElementValue, parent)
				
			elif Type == "listbox_scroll":
				parent.Children[Index] = ListBoxScroll()
				parent.Children[Index].SetParent(parent)
				self.LoadElementListBox(parent.Children[Index], ElementValue, parent)
				
			elif Type == "listbox_scrollt":
				parent.Children[Index] = ListBoxScrollTest()
				parent.Children[Index].SetParent(parent)
				self.LoadElementListBox(parent.Children[Index], ElementValue, parent)

			elif Type == "titlebaralisveris":
				parent.Children[Index] = TitleBar()
				parent.Children[Index].SetParent(parent)
				self.LoadElementTitleBar(parent.Children[Index], ElementValue, parent)

			elif Type == "listbox_scrollitem":
				parent.Children[Index] = ListBoxScrollItemEkleme()
				parent.Children[Index].SetParent(parent)
				self.LoadElementListBox(parent.Children[Index], ElementValue, parent)

			elif Type == "alisveris_system":
				parent.Children[Index] = Alisveris_System()
				parent.Children[Index].SetParent(parent)
				self.LoadElementListBox(parent.Children[Index], ElementValue, parent)
				
#button-deðiþtir#
class Button(Window):
	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)

		self.eventFunc = None
		self.eventArgs = None

		self.ButtonText = None
		self.ToolTipText = None

		self.toolTipType = 0 

		import uiToolTip
		self.toolTipAlignment = uiToolTip.ToolTip(130)

	def __del__(self):
		Window.__del__(self)

		self.eventFunc = None
		self.eventArgs = None

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterButton(self, layer)

	def SetUpVisual(self, filename):
		wndMgr.SetUpVisual(self.hWnd, filename)

	def SetOverVisual(self, filename):
		wndMgr.SetOverVisual(self.hWnd, filename)

	def SetDownVisual(self, filename):
		wndMgr.SetDownVisual(self.hWnd, filename)

	def SetDisableVisual(self, filename):
		wndMgr.SetDisableVisual(self.hWnd, filename)

	def GetUpVisualFileName(self):
		return wndMgr.GetUpVisualFileName(self.hWnd)

	def GetOverVisualFileName(self):
		return wndMgr.GetOverVisualFileName(self.hWnd)

	def GetDownVisualFileName(self):
		return wndMgr.GetDownVisualFileName(self.hWnd)

	def GetText(self):
		if not self.ButtonText:
			return
		return self.ButtonText.GetText()

	def Flash(self):
		wndMgr.Flash(self.hWnd)

	def Enable(self):
		wndMgr.Enable(self.hWnd)

	def Disable(self):
		wndMgr.Disable(self.hWnd)

	def Down(self):
		wndMgr.Down(self.hWnd)

	def SetUp(self):
		wndMgr.SetUp(self.hWnd)

	def SAFE_SetEvent(self, func, *args):
		self.eventFunc = __mem_func__(func)
		self.eventArgs = args
		
	def SetEvent(self, func, *args):
		self.eventFunc = func
		self.eventArgs = args

	def SetTextColor(self, color):
		if not self.ButtonText:
			return
		self.ButtonText.SetPackedFontColor(color)

	def SetText(self, text, height = 4):

		if not self.ButtonText:
			textLine = TextLine()
			textLine.SetParent(self)
			textLine.SetPosition(self.GetWidth()/2, self.GetHeight()/2)
			textLine.SetVerticalAlignCenter()
			textLine.SetHorizontalAlignCenter()
			textLine.Show()
			self.ButtonText = textLine

		self.ButtonText.SetText(text)

	def SetFormToolTipText(self, type, text, x, y):
		if not self.ToolTipText:		
			toolTip=createToolTipWindowDict[type]()
			toolTip.SetParent(self)
			toolTip.SetSize(0, 0)
			toolTip.SetHorizontalAlignCenter()
			toolTip.SetOutline()
			toolTip.Hide()
			toolTip.SetPosition(x + self.GetWidth()/2, y)
			self.ToolTipText=toolTip

		self.ToolTipText.SetText(text)
		self.toolTipType = 0

	def SetFormToolTipTextGame(self, type, text, x, y):
		self.toolTipAlignment.ClearToolTip()
		self.toolTipAlignment.AutoAppendTextLine(text)
		self.toolTipAlignment.AlignHorizonalCenter()
		self.toolTipAlignment.SetPosition(x + self.GetWidth()/2, y)
		self.toolTipType = 1

	def SetToolTipWindow(self, toolTip):		
		self.ToolTipText=toolTip		
		self.ToolTipText.SetParentProxy(self)

	def SetToolTipText(self, text, x=0, y = -19):
		self.SetFormToolTipText("TEXT", text, x, y)

	def SetToolTipTextRiot(self, text, x=0-29, y = -29):
		self.SetFormToolTipTextGame("TEXT", text, x, y)

	def SetRotation(self, rotation):
		wndMgr.SetRotation(self.hWnd, rotation)

	def CallEvent(self):
		snd.PlaySound("sound/ui/click.wav")

		if self.eventFunc:
			apply(self.eventFunc, self.eventArgs)

	def ShowToolTip(self):
		#if self.GetText() == "Duyurular Acýk" or self.GetText() == "Duyurular Kapalý":
		if self.toolTipType == 1:
			self.toolTipAlignment.ShowToolTip()
		else:
			if self.ToolTipText:
				self.ToolTipText.Show()

	def HideToolTip(self):
		#if self.GetText() == "Duyurular Acýk" or self.GetText() == "Duyurular Kapalý":
		if self.toolTipType == 1:
			self.toolTipAlignment.HideToolTip()
		else:
			if self.ToolTipText:
				self.ToolTipText.Hide()
			
	def IsDown(self):
		return wndMgr.IsDown(self.hWnd)

class ListBox(Window):

	TEMPORARY_PLACE = 3

	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)
		self.overLine = -1
		self.selectedLine = -1
		self.width = 0
		self.height = 0
		self.stepSize = 17
		self.basePos = 0
		self.showLineCount = 0
		self.itemCenterAlign = TRUE
		self.itemList = []
		self.itemList2 = []
		self.keyDict = {}
		self.textDict = {}
		self.text = ""
		self.event = lambda *arg: None
	def __del__(self):
		Window.__del__(self)

	def SetWidth(self, width):
		self.SetSize(width, self.height)

	def SetSize(self, width, height):
		Window.SetSize(self, width, height)
		self.width = width
		self.height = height

	def SetTextCenterAlign(self, flag):
		self.itemCenterAlign = flag

	def SetBasePos(self, pos):
		import riotInfo
		self.basePos = pos
		if riotInfo.YerNO == 1:
			riotInfo.yerNO = 0
			return
		else:
			self._LocateItem()

	def ClearItem(self):
		self.keyDict = {}
		self.textDict = {}
		self.itemList = []
		self.overLine = -1
		self.selectedLine = -1

	def InsertItem(self, number, text):
		self.keyDict[len(self.itemList)] = number
		self.textDict[len(self.itemList)] = text

		textLine = TextLine()
		textLine.SetParent(self)
		textLine.SetText(text)
		textLine.Show()
		
		self.text = text
		
		if self.itemCenterAlign:
			textLine.SetWindowHorizontalAlignCenter()
			textLine.SetHorizontalAlignCenter()

		self.itemList.append(textLine)

		self._LocateItem()
		
	def GetText(self):
		return self.text
		
	def InsertItem3(self, number, text):
		self.keyDict[len(self.itemList)] = number
		self.textDict[len(self.itemList)] = text

		textLine2 = TextLine()
		textLine2.SetParent(self)
		textLine2.SetText(text)
		textLine2.Show()
		
		self.text = text
		
		if self.itemCenterAlign:
			textLine2.SetWindowHorizontalAlignCenter()
			textLine2.SetHorizontalAlignCenter()

		self.itemList.append(textLine2)

		self._LocateItem3()
	
	def InsertItem2(self, number, text, tooltipText, textlineText, arg):
		self.keyDict[len(self.itemList)] = number
		self.textDict[len(self.itemList)] = text + tooltipText + textLineText + arg

		textLine = TextLine()
		textLine.SetParent(self)
		textLine.SetPosition(0, 3)
		textLine.SetText(text)
		textLine.Show()
		
		textLine2 = TextLine()
		textLine2.SetParent(self)
		textLine2.SetPosition(20, 3)
		textLine2.SetText(tooltipText)
		textLine2.Show()
		
		textLine3 = TextLine()
		textLine3.SetParent(self)
		textLine3.SetPosition(20+20, 3)
		textLine3.SetText(textlineText)
		textLine3.Show()
		
		textLine4 = TextLine()
		textLine4.SetParent(self)
		textLine4.SetPosition(20+20+20, 3)
		textLine4.SetText(arg)
		textLine4.Show()
		
		if self.itemCenterAlign:
			textLine.SetWindowHorizontalAlignCenter()
			textLine.SetHorizontalAlignCenter()

		self.itemList.append(textLine + textLine2 + textLine3 + textLine4)

		self._LocateItem2()

	def ChangeItem(self, number, text):
		for key, value in self.keyDict.items():
			if value == number:
				self.textDict[key] = text

				if number < len(self.itemList):
					self.itemList[key].SetText(text)

				return

	def LocateItem(self):
		self._LocateItem()

	def _LocateItem(self):

		skipCount = self.basePos
		yPos = 0
		self.showLineCount = 0

		for textLine in self.itemList:
			textLine.Hide()

			if skipCount > 0:
				skipCount -= 1
				continue

			if localeInfo.IsARABIC():
				w, h = textLine.GetTextSize()
				textLine.SetPosition(w+10, yPos + 3)
			else:
				textLine.SetPosition(0, yPos + 3)

			import constInfo
			if constInfo.modduzenle == 1:
				yPos += self.stepSize
			else:
				yPos += self.stepSize
			
			
			if yPos <= self.GetHeight():
				self.showLineCount += 1
				textLine.Show()
				
			Thin = ThinBoard()
			Thin.SetPosition(150, 100)
			Thin.SetSize(100, 150)
			Thin.Show()
			
			Thin = ThinBoard()
			Thin.SetPosition(150, 100)
			Thin.SetSize(100, 150)
			Thin.Show()
			
	def _LocateItem3(self):

		skipCount = self.basePos
		yPos = 0
		self.showLineCount = 0

		for textLine in self.itemList:
			textLine.Hide()

			if skipCount > 0:
				skipCount -= 1
				continue

			if localeInfo.IsARABIC():
				w, h = textLine.GetTextSize()
				textLine.SetPosition(w+10, yPos + 3)
			else:
				textLine.SetPosition(0, yPos + 3)

			yPos += self.stepSize

			if yPos <= self.GetHeight():
				self.showLineCount += 1
				textLine.Show()
				
			Thin = ThinBoard()
			Thin.SetPosition(150, 100)
			Thin.SetSize(100, 150)
			Thin.Show()
			
			Thin = ThinBoard()
			Thin.SetPosition(150, 100)
			Thin.SetSize(100, 150)
			Thin.Show()
			
	def _LocateItem2(self):

		skipCount = self.basePos
		yPos = 0
		self.showLineCount = 0

		for textLine in self.itemList:
			textLine.Hide()

			if skipCount > 0:
				skipCount -= 1
				continue

			if localeInfo.IsARABIC():
				w, h = textLine.GetTextSize()
				textLine.SetPosition(w+10, yPos + 3)
			else:
				textLine.SetPosition(0, yPos + 3)

			yPos += self.stepSize

			if yPos <= self.GetHeight():
				self.showLineCount += 1
				textLine.Show()

	def ArrangeItem(self):
		self.SetSize(self.width)
		self.SetSize(self.width, len(self.itemList) * 17)
		self._LocateItem()

	def GetViewItemCount(self):
		return int(self.GetHeight() / self.stepSize)

	def GetItemCount(self):
		return len(self.itemList)

	def SetEvent(self, event):
		self.event = event

	def SelectItem(self, line):

		if not self.keyDict.has_key(line):
			return

		if line == self.selectedLine:
			return

		self.selectedLine = line
		self.event(self.keyDict.get(line, 0), self.textDict.get(line, "None"))
		
		x, y = self.GetGlobalPosition()
		
		Thin = ThinBoard()
		Thin.SetPosition(150, 100)
		Thin.SetSize(100, 150)
		Thin.Show()
		
		Thin = ThinBoard()
		Thin.SetPosition(150, 100)
		Thin.SetSize(100, 150)
		Thin.Show()

	def GetSelectedItem(self):
		return self.keyDict.get(self.selectedLine, 0)
		
	def GetSelectedItemAdi(self):
		secilen = self.textDict.get(self.selectedLine, 0)
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
		return secilen

	def OnMouseLeftButtonDown(self):
		if self.overLine < 0:
			return

	def OnMouseLeftButtonUp(self):
		if self.overLine >= 0:
			self.SelectItem(self.overLine+self.basePos)
	def OnUpdate(self):

		self.overLine = -1

		if self.IsIn():
			self.SelectItem(self.overLine+self.basePos)
			x, y = self.GetGlobalPosition()
			height = self.GetHeight()
			xMouse, yMouse = wndMgr.GetMousePosition()

			if yMouse - y < height - 1:
				self.overLine = (yMouse - y) / self.stepSize

				if self.overLine < 0:
					self.overLine = -1
				if self.overLine >= len(self.itemList):
					self.overLine = -1
					
			elif yMouse - y < height - 1:
				self.overLine = (yMouse - y) / self.stepSize

				if self.overLine < 0:
					self.overLine = -1
				if self.overLine >= len(self.itemList2):
					self.overLine = -1
					
			Thin = ThinBoard()
			Thin.SetPosition(150, 100)
			Thin.SetSize(100, 150)
			Thin.Show()
			
			Thin = ThinBoard()
			Thin.SetPosition(150, 100)
			Thin.SetSize(100, 150)
			Thin.Show()

	def OnRender(self):
		xRender, yRender = self.GetGlobalPosition()
		yRender -= self.TEMPORARY_PLACE
		widthRender = self.width
		heightRender = self.height + self.TEMPORARY_PLACE*2

		if localeInfo.IsCIBN10:
			if -1 != self.overLine and self.keyDict[self.overLine] != -1:
				grp.SetColor(HALF_WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + self.overLine*self.stepSize + 4, self.width - 3, self.stepSize)				

			if -1 != self.selectedLine and self.keyDict[self.selectedLine] != -1:
				if self.selectedLine >= self.basePos:
					if self.selectedLine - self.basePos < self.showLineCount:
						grp.SetColor(SELECT_COLOR)
						grp.RenderBar(xRender + 2, yRender + (self.selectedLine-self.basePos)*self.stepSize + 4, self.width - 3, self.stepSize)

		else:		
			if -1 != self.overLine:
				grp.SetColor(HALF_WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + self.overLine*self.stepSize + 4, self.width - 3, self.stepSize)				

			if -1 != self.selectedLine:
				if self.selectedLine >= self.basePos:
					if self.selectedLine - self.basePos < self.showLineCount:
						grp.SetColor(SELECT_COLOR)
						grp.RenderBar(xRender + 2, yRender + (self.selectedLine-self.basePos)*self.stepSize + 4, self.width - 3, self.stepSize)
			
			Thin = ThinBoard()
			Thin.SetPosition(150, 100)
			Thin.SetSize(100, 150)
			Thin.Show()
			
			Thin = ThinBoard()
			Thin.SetPosition(150, 100)
			Thin.SetSize(100, 150)
			Thin.Show()

class ImageListBox(Window):

	TEMPORARY_PLACE = 3

	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)
		self.overLine = -1
		self.selectedLine = -1
		self.width = 0
		self.height = 0
		self.stepSize = 17
		self.basePos = 0
		self.showLineCount = 0
		self.itemCenterAlign = FALSE
		self.itemList = []
		self.subItemList = []
		self.imageList = []
		self.keyDict = {}
		self.textDict = {}
		self.subTextDict = {}
		self.event = None
		self.eventMouseDoubleClick = None
		self.eventMouseOver = None

	def __del__(self):
		Window.__del__(self)

	def SetWidth(self, width):
		self.SetSize(width, self.height)

	def SetSize(self, width, height):
		Window.SetSize(self, width, height)
		self.width = width
		self.height = height

	def SetTextCenterAlign(self, flag):
		self.itemCenterAlign = flag

	def SetBasePos(self, pos):
		self.overLine = None
		self.basePos = pos
		self._LocateItem()

	def GetBasePos(self):
		return self.basePos

	def ClearItem(self):
		self.keyDict = {}
		self.textDict = {}
		self.subTextDict = {}
		self.itemList = []
		self.subItemList = []
		self.imageList = []
		self.overLine = -1
		self.selectedLine = -1
		self.basePos = 0
		self.showLineCount = 0

	def InsertItem(self, number, text, image):
		self.keyDict[len(self.itemList)] = number
		self.textDict[len(self.itemList)] = text

		imageLine = ImageBox()
		imageLine.SetParent(self)
		imageLine.LoadImage(image)
		imageLine.SetMouseButtonUpEvent(self.OnMouseLeftButtonUp)
		imageLine.SetMouseDoubleClickEvent(self.OnMouseLeftButtonDoubleClick)
		imageLine.Show()

		textLine = TextLine()
		textLine.SetParent(self)
		textLine.SetText(text)
		textLine.Show()

		if self.itemCenterAlign:
			textLine.SetWindowHorizontalAlignCenter()
			textLine.SetHorizontalAlignCenter()

		self.itemList.append(textLine)
	
		self._LocateItem()

	def UpdateSubText(self, number, new_text):
		for key, value in self.keyDict.items():
			if value == number:
				self.subTextDict[key] = new_text

				if key < len(self.itemList):
					self.subItemList[key].SetText(new_text)

				return

	def ChangeItem(self, number, text, subtext, image):
		for key, value in self.keyDict.items():
			if value == number:
				self.textDict[key] = text
				self.subTextDict[key] = subtext

				if number < len(self.itemList):
					self.itemList[key].SetText(text)
					self.subItemList[key].SetText(subtext)
					self.imageList[key].LoadImage(image)

				return

	def LocateItem(self):
		self._LocateItem()

	def _LocateItem(self):
		if len(self.imageList) > 0:
			self.stepSize = max(self.stepSize, self.imageList[0].GetHeight()+4)

		skipCount = self.basePos
		yPos = 0
		self.showLineCount = 0

		for i in xrange(0, len(self.itemList)):
			image = self.imageList[i]
			textLine = self.itemList[i]

			image.Hide()
			textLine.Hide()
			if skipCount > 0:
				skipCount -= 1
				continue

			image.SetPosition(2, yPos + 3)
			w, h = textLine.GetTextSize()
			textLine.SetPosition(2 + 8 + image.GetWidth(), yPos + image.GetHeight() / 2 - h / 2)
			w, h = subTextLine.GetTextSize()

			yPos += self.stepSize

			if yPos <= self.GetHeight():
				self.showLineCount += 1
				image.Show()
				textLine.Show()
				
	def ArrangeItem(self):
		self.SetSize(self.width, len(self.itemList) * self.stepSize)
		self._LocateItem()

	def GetViewItemCount(self):
		return self.showLineCount

	def GetItemCount(self):
		return len(self.itemList)

	def SetEvent(self, event):
		self.event = event

	def SetMouseDoubleClickEvent(self, event):
		self.eventMouseDoubleClick = __mem_func__(event)

	def OnMouseLeftButtonDoubleClick(self):
		if self.eventMouseDoubleClick:
			self.eventMouseDoubleClick(self.keyDict.get(self.selectedLine, 0))

	def SelectItem(self, line):

		if not self.keyDict.has_key(line):
			return

		self.selectedLine = line
		if self.event:
			self.event(self.keyDict.get(line, 0), self.textDict.get(line, "None"))

	def GetSelectedItem(self):
		return self.keyDict.get(self.selectedLine, -1)

	def GetSelectedItemText(self):
		return self.textDict.get(self.selectedLine, "")

	def GetSelectedItemSubText(self):
		return self.subTextDict.get(self.selectedLine, "")

	def GetItemText(self, index):
		return self.textDict.get(index, "")

	def OnMouseLeftButtonDown(self):
		if self.overLine < 0:
			return

	def OnMouseLeftButtonUp(self):
		if self.overLine >= 0:
			self.SelectItem(self.overLine+self.basePos)

	def SetMouseOverEvent(self, event):
		self.eventMouseOver = __mem_func__(event)

	def IsInImage(self):
		for img in self.imageList:
			if img.IsIn():
				return TRUE
		return FALSE

	def OnUpdate(self):

		oldOverLine = self.overLine
		self.overLine = -1

		if self.IsIn() or self.IsInImage():
			x, y = self.GetGlobalPosition()
			height = self.GetHeight()
			xMouse, yMouse = wndMgr.GetMousePosition()

			if yMouse - y < height - 1:
				self.overLine = (yMouse - y) / self.stepSize

				if self.overLine < 0:
					self.overLine = -1
				if self.overLine >= len(self.itemList):
					self.overLine = -1

		if self.overLine != oldOverLine:
			if self.eventMouseOver:
				self.eventMouseOver(self.overLine)

	def OnRender(self):
		xRender, yRender = self.GetGlobalPosition()
		yRender -= self.TEMPORARY_PLACE
		widthRender = self.width
		heightRender = self.height + self.TEMPORARY_PLACE*2

		if localeInfo.IsCIBN10:
			if -1 != self.overLine and self.keyDict[self.overLine] != -1:
				grp.SetColor(HALF_WHITE_COLOR)
				grp.RenderBar(xRender, yRender + self.overLine*self.stepSize + 4, self.width - 1, self.stepSize)				

			if -1 != self.selectedLine and self.keyDict[self.selectedLine] != -1:
				if self.selectedLine >= self.basePos:
					if self.selectedLine - self.basePos < self.showLineCount:
						grp.SetColor(SELECT_COLOR)
						grp.RenderBar(xRender, yRender + int(self.selectedLine-self.basePos)*self.stepSize + 4, self.width - 1, self.stepSize)

class ListBoxScrollVeSiralamaBiyolog(Window):

	TEMPORARY_PLACE = 3

	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)
		self.overLine = -1
		self.selectedLine = -1
		self.width = 0
		self.height = 0
		self.stepSize = 20 #15
		self.basePos = 0
		self.showLineCount = 0
		self.itemCenterAlign = TRUE
		self.butonarttir = 0
		self.ilk = 0
		#Biyolog LISTELERI
		self.biyologGerekenItem = []
		self.biyologGerekenItem2 = []
		self.itemadeti = []
		self.leveli = []
		self.canavar = []
		self.canavaryeri = []
		self.gorevdurumu = []
		self.baslaveyabitir = []
		self.dahafazlaList = []
		self.yatayList = []
		self.arkaplan = []
		self.list = []
		self.gerekenitemler = []

		self.keyDict = {}
		self.textDict = {}
		self.nameDict = {}
		self.levelDict = {}
		self.bayrakDict = {}
		self.istatistikDict = {}
		self.kriterDict = {}
		self.yatayDict = {}
		import uiToolTip
		self.toolTip = uiToolTip.ItemToolTip()
		self.event = lambda *arg: None
		
	def __del__(self):
		Window.__del__(self)

	def SetWidth(self, width):
		self.SetSize(width, self.height)

	def SetSize(self, width, height):
		Window.SetSize(self, width, height)
		self.width = width
		self.height = height

	def SetTextCenterAlign(self, flag):
		self.itemCenterAlign = flag

	def SetBasePos(self, pos):
		self.basePos = pos
		self._LocateItem()

	def ClearItem(self):
		self.keyDict = {}
		self.textDict = {}
		self.nameDict = {}
		self.levelDict = {}
		self.bayrakDict = {}
		self.istatistikDict = {}
		self.kriterDict = {}
		self.yatayDict = {}
		self.biyologGerekenItem = []
		self.biyologGerekenItem2 = []
		self.itemadeti = []
		self.leveli = []
		self.canavaryeri = []
		self.canavar = []
		self.gorevdurumu = []
		self.baslaveyabitir = []
		self.list = []
		self.dahafazlaList = []
		self.yatayList = []
		self.arkaplan = []
		self.gerekenitemler = []
		self.ilk = 0
		self.overLine = -1
		self.selectedLine = -1
	
	def InsertItem(self, number, gerekenitem, gerekenitem2, adeti, leveli, canavar, canavaryeri, gorevdurumu):
		import item
		self.keyDict[len(self.biyologGerekenItem)] = number
		self.textDict[len(self.biyologGerekenItem)] = gerekenitem
		self.textDict[len(self.biyologGerekenItem2)] = gerekenitem2
		self.nameDict[len(self.itemadeti)] = adeti
		self.levelDict[len(self.leveli)] = leveli
		self.bayrakDict[len(self.canavaryeri)] = canavaryeri
		self.istatistikDict[len(self.canavar)] = canavar
		self.kriterDict[len(self.gorevdurumu)] = gorevdurumu
		
		self.list.append("ekle")
		
		arkaplan = ImageBox()
		arkaplan.SetParent(self)
		arkaplan.SetPosition(5, 6)
		arkaplan.LoadImage("KFDevelopers/server_fb34_kf/images/thinboard.tga")
		arkaplan.Show()
		self.arkaplan.append(arkaplan)
		
		item.SelectItem(gerekenitem)
		iconu = item.GetIconImageFileName()
		
		imageLine = ImageBox()
		imageLine.SetParent(arkaplan)
		imageLine.LoadImage(iconu)
		imageLine.Show()
		
		item.SelectItem(gerekenitem2)
		iconu2 = item.GetIconImageFileName()
		
		imageLine2 = ImageBox()
		imageLine2.SetParent(arkaplan)
		imageLine2.LoadImage(iconu2)
		imageLine2.Show()
		
		import player
		
		self.gerekenitemler.append(gerekenitem)
		
		self.biyologGerekenItem.append(imageLine)
		self.biyologGerekenItem2.append(imageLine2)
		
		textLine = TextLine()
		textLine.SetParent(arkaplan)
		textLine.SetPosition(30, 6)
		textLine.SetText(gerekenitem)
		textLine.Show()
		
		textLine2 = TextLine()
		textLine2.SetParent(arkaplan)
		textLine2.SetPosition(30+106, 6)
		textLine2.SetText(adeti)
		textLine2.Show()
		
		textLine3 = TextLine()
		textLine3.SetParent(arkaplan)
		textLine3.SetPosition(30+106+106, 6)
		textLine3.SetText(leveli)
		textLine3.Show()
		
		textLine4 = TextLine()
		textLine4.SetParent(arkaplan)
		textLine4.SetPosition(30+106+106+106, 6)
		textLine4.SetText(canavar)
		textLine4.Show()
		
		textLine5 = TextLine()
		textLine5.SetParent(arkaplan)
		textLine5.SetPosition(30+106+106, 6)
		textLine5.SetText(canavaryeri)
		textLine5.Show()
		
		self.Basla = Button()
		self.Basla.SetParent(arkaplan)
		self.Basla.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
		self.Basla.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
		self.Basla.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
		self.Basla.SetText("M")
		self.Basla.SetToolTipText("")
		self.Basla.SetPosition(20+110+110+110+110+87+87+15, 6)
		
		if gorevdurumu == "bitti":
			self.Basla.SetText("Bitti")
			self.Basla.Disable()
			self.Basla.SetToolTipText("G?ev tamamland?")
			self.Basla.SetEvent(lambda: self.Basla2("bitti", leveli))
		elif gorevdurumu == "devamediyor":
			self.Basla.SetText("Devam..")
			self.Basla.Disable()
			self.Basla.SetToolTipText("G?ev devam ediyor...")
			self.Basla.SetEvent(lambda: self.Basla2("devamediyor", leveli))
		else:
			self.Basla.SetText("Baþla")
			self.Basla.SetToolTipText("G?eve baþla ve daha fazla bilgi al!")
			self.Basla.SetEvent(lambda: self.Basla2("basla", leveli))
			
		self.itemadeti.append(textLine2)
		self.leveli.append(textLine3)
		self.canavar.append(textLine4)
		self.canavaryeri.append(textLine5)
		self.baslaveyabitir.append(self.Basla)
		self.gorevdurumu.append(self.Basla)
		
		self._LocateItem()
		

	def Basla2(self, text):
		if str(text) == "bitti":
			return
			
		if str(text) == "devamediyor":
			import chat
			chat.AppendChat(chat.CHAT_TYPE_INFO, 'G?ev devam ediyor...')
			return
		
		import event
		import riotInfo
		riotInfo.BiyologDurum = "basla"+str(leveli)
		event.QuestButtonClick(riotInfo.BiyologSystem)
		
	def Uzerinde(self, gerekenitem):
		import player
		itemkodu = int(gerekenitem)
		self.toolTip.ClearToolTip()
		metinSlot = [player.GetItemMetinSocket(itemkodu, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
		attrSlot = [player.GetItemAttribute(itemkodu, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]
		self.toolTip.AddRefineItemData(itemkodu, metinSlot, attrSlot)
		self.toolTip.AppendSpace(3)
		
	def NoUzerinde(self):
		self.toolTip.Hide()
		
	def ChangeItem(self, number, text, tooltipText, textlineText, width):
		for key, value in self.keyDict.items():
			if value == number:
				self.textDict[key] = text + tooltipText + textlineText + width

				if number < len(self.biyologGerekenItem):
					self.biyologGerekenItem[key].SetText(text)

				return

	def LocateItem(self):
		self._LocateItem()
		
	def MesajGonderOna(self, text):
		import interfaceModule
		import constInfo
		import player
		if str(text) == player.GetName():
			import chat
			chat.AppendChat(chat.CHAT_TYPE_INFO, 'Kendine mesaj atamassýn.')
		else:
			constInfo.Secilen = str(text)
			constInfo.mesajat = 1

	def _LocateItem(self):

		skipCount = self.basePos
		yPos = 0
		yPos2 = 0
		self.showLineCount = 0

		for i in xrange(0, len(self.list)):
			textLine = self.biyologGerekenItem[i]
			textLine2 = self.biyologGerekenItem2[i]
			nameTextLine = self.itemadeti[i]
			levelTextLine = self.leveli[i]
			bayrakResim = self.canavaryeri[i]
			istatistikler = self.canavar[i]
			kriterler = self.gorevdurumu[i]
			arkaplan = self.arkaplan[i]
				
			textLine.Hide()
			textLine2.Hide()
			nameTextLine.Hide()
			levelTextLine.Hide()		
			bayrakResim.Hide()
			istatistikler.Hide()
			kriterler.Hide()
			arkaplan.Hide()
			
			if skipCount > 0:
				skipCount -= 1
				continue
			
			arkaplan.SetPosition(-3, yPos2 + 6)
			textLine.SetPosition(32 - 22 + 8 - 9, yPos + 11 + 9 - 30 + 8 + 10)
			textLine2.SetPosition(32 - 22 + 8 + 10, yPos + 11 + 9 - 30 + 8 + 10)#2.gereken item
			nameTextLine.SetPosition(125 - 11 - 30 + 40, yPos + 14 + 9 - 2 - 2)
			levelTextLine.SetPosition(211 - 22 + 9, yPos + 14 + 9 - 2 - 2)#g?ev leveli
			istatistikler.SetPosition(211 - 22 + 95, yPos + 14 + 9 - 2 - 2)#canavar ad?
			bayrakResim.SetPosition(282+37 + 45, yPos + 14 + 9 - 2 - 2)#canavar yeri
			kriterler.SetPosition(370 - 10 + 93, yPos + 6 + 8 + 1)

			yPos += 0
			yPos2 += 50

			if yPos <= self.GetHeight():
				arkaplan.Show()
				textLine.Show()
				textLine2.Show()
				nameTextLine.Show()
				levelTextLine.Show()
				bayrakResim.Show()
				istatistikler.Show()
				kriterler.Show()

	def ArrangeItem(self):
		self.SetSize(self.width)
		self.SetSize(self.width, len(self.biyologGerekenItem) * 17)
		self._LocateItem()

	def GetViewItemCount(self):
		return self.showLineCount

	def GetItemCount(self):
		return len(self.biyologGerekenItem)

	def SetEvent(self, event):
		self.event = event

	def SelectItem(self, line):

		if not self.keyDict.has_key(line):
			return

		if line == self.selectedLine:
			return

		self.selectedLine = line
		self.event(self.keyDict.get(line, 0), self.textDict.get(line, "None"))
		
		x, y = self.GetGlobalPosition()

	def GetSelectedItem(self):
		return self.keyDict.get(self.selectedLine, 0)

	def OnMouseLeftButtonDown(self):
		if self.overLine < 0:
			return

	def OnMouseLeftButtonUp(self):
		if self.overLine >= 0:
			self.SelectItem(self.overLine+self.basePos)
	def OnUpdate(self):

		self.overLine = -1

		if self.IsIn():
			self.SelectItem(self.overLine+self.basePos)
			x, y = self.GetGlobalPosition()
			height = self.GetHeight()
			xMouse, yMouse = wndMgr.GetMousePosition()

			if yMouse - y < height - 1:
				self.overLine = (yMouse - y) / self.stepSize

				if self.overLine < 0:
					self.overLine = -1
				if self.overLine >= len(self.biyologGerekenItem):
					self.overLine = -1

	def OnRender(self):
		xRender, yRender = self.GetGlobalPosition()
		yRender -= self.TEMPORARY_PLACE
		widthRender = self.width
		heightRender = self.height + self.TEMPORARY_PLACE*2 + 25 - 6

		if localeInfo.IsCIBN10 and 50 > 100:
			if -1 != self.overLine and self.keyDict[self.overLine] != -1:
				grp.SetColor(HALF_WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + self.overLine*self.stepSize + 4, self.width - 3 + 25 - 6 - 8, self.stepSize + 25 - 6  - 10)

			if -1 != self.selectedLine and self.keyDict[self.selectedLine] != -1:
				if self.selectedLine >= self.basePos:
					if self.selectedLine - self.basePos < self.showLineCount:
						grp.SetColor(SELECT_COLOR)
						grp.RenderBar(xRender + 2, yRender + (self.selectedLine-self.basePos)*self.stepSize + 4, self.width - 3 + 25 - 6 - 8, self.stepSize + 25 - 6 - 8)

		else:
			if 50 > 100:
				if -1 != self.overLine:
					grp.SetColor(HALF_WHITE_COLOR)
					grp.RenderBar(xRender + 2, yRender + self.overLine*self.stepSize + 4 + 25, self.width - 3 + 20 - 6 - 8, self.stepSize + 20) #+20				

				if -1 != self.selectedLine:
					if self.selectedLine >= self.basePos:
						if self.selectedLine - self.basePos < self.showLineCount:
							grp.SetColor(SELECT_COLOR)
							grp.RenderBar(xRender + 2, yRender + (self.selectedLine-self.basePos)*self.stepSize + 4 + 25 - 6 - 8, self.width - 3 + 25 - 6 - 8, self.stepSize + 30)
		
class ListBoxScrollTestBiyolog(ListBoxScrollVeSiralamaBiyolog):
	def __init__(self):
		ListBoxScrollVeSiralamaBiyolog.__init__(self)
		
		self.viewItemCount=15
		self.basePos=0
		self.itemHeight=15
		self.itemStep=20
		self.scrollBar = ScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetScrollEvent(self.__OnScroll)
		self.scrollBar.Hide()

	def SetSize(self, width, height):
		ListBoxScrollVeSiralamaBiyolog.SetSize(self, width - ScrollBar.SCROLLBAR_WIDTH, height)
		Window.SetSize(self, width, height)
		
		self.scrollBar.SetPosition(width - ScrollBar.SCROLLBAR_WIDTH + 5, 0)
		self.scrollBar.SetScrollBarSize(height)

	def ClearItem(self):
		ListBoxScrollVeSiralamaBiyolog.ClearItem(self)
		self.scrollBar.SetPos(0)

	def _LocateItem(self):
		ListBoxScrollVeSiralamaBiyolog._LocateItem(self)
		
		if self.showLineCount < len(self.biyologGerekenItem):
			self.scrollBar.SetMiddleBarSize(float(self.GetViewItemCount())/self.GetItemCount())
			self.scrollBar.Show()
		else:
			self.scrollBar.Hide()
		
	def SetScrollBar(self, scrollBar):
		scrollBar.SetScrollEvent(__mem_func__(self.__OnScroll))
		self.scrollBar=scrollBar
		
	def __OnScroll(self):
		scrollLen = self.GetItemCount()-self.GetViewItemCount()
		if scrollLen < 0:
			scrollLen = 0
		self.SetBasePos(int(self.scrollBar.GetPos()*scrollLen))
		ListBoxScrollVeSiralamaBiyolog._LocateItem(self)

	def __GetScrollLen(self):
		scrollLen=self.__GetItemCount()-self.__GetViewItemCount()
		if scrollLen<0:
			return 0

		return scrollLen
		

	def __GetViewItemCount(self):
		return self.viewItemCount

	def __GetItemCount(self):
		return len(self.biyologGerekenItem)

	def GetItemViewCoord(self, pos, itemWidth):
		if localeInfo.IsARABIC():
			return (self.GetWidth()-itemWidth-15, (pos-self.basePos)*self.itemStep)
		else:
			return (0, (pos-self.basePos)*self.itemStep)
			
	def __IsInViewRange(self, pos):
		if pos<self.basePos:
			return 0
		if pos>=self.basePos+self.viewItemCount:
			return 0
		return 1						
					
class ListBoxScrollVeSiralamaLonca(Window):

	TEMPORARY_PLACE = 3

	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)
		self.overLine = -1
		self.selectedLine = -1
		self.width = 0
		self.height = 0
		self.stepSize = 20 #15
		self.basePos = 0
		self.showLineCount = 0
		self.itemCenterAlign = TRUE
		self.butonarttir = 0
		self.ilk = 0
		self.loncaNameList = []
		self.tanitanNameList = []
		self.sonuyesayisiList = []
		self.loncaIstatistikleriList = []
		self.bayrakResimList = []
		self.loncaKriterleriList = []
		self.mesajatList = []
		self.dahafazlaList = []
		self.yatayList = []
		self.keyDict = {}
		self.textDict = {}
		self.nameDict = {}
		self.levelDict = {}
		self.bayrakDict = {}
		self.istatistikDict = {}
		self.kriterDict = {}
		self.yatayDict = {}
		self.event = lambda *arg: None
		
	def __del__(self):
		Window.__del__(self)

	def SetWidth(self, width):
		self.SetSize(width, self.height)

	def SetSize(self, width, height):
		Window.SetSize(self, width, height)
		self.width = width
		self.height = height

	def SetTextCenterAlign(self, flag):
		self.itemCenterAlign = flag

	def SetBasePos(self, pos):
		self.basePos = pos
		self._LocateItem()

	def ClearItem(self):
		self.keyDict = {}
		self.textDict = {}
		self.nameDict = {}
		self.levelDict = {}
		self.bayrakDict = {}
		self.istatistikDict = {}
		self.kriterDict = {}
		self.yatayDict = {}
		self.loncaNameList = []
		self.tanitanNameList = []
		self.sonuyesayisiList = []
		self.bayrakResimList = []
		self.loncaIstatistikleriList = []
		self.loncaKriterleriList = []
		self.mesajatList = []
		self.dahafazlaList = []
		self.yatayList = []
		self.ilk = 0
		self.overLine = -1
		self.selectedLine = -1
	
	def InsertItem(self, number, loncaadi, tanitan, sonuye, bayrak, istatistik, kriterler):
		self.keyDict[len(self.loncaNameList)] = number
		self.textDict[len(self.loncaNameList)] = loncaadi
		self.nameDict[len(self.tanitanNameList)] = tanitan
		self.levelDict[len(self.sonuyesayisiList)] = sonuye
		self.bayrakDict[len(self.bayrakResimList)] = bayrak
		self.istatistikDict[len(self.loncaIstatistikleriList)] = istatistik
		self.kriterDict[len(self.loncaKriterleriList)] = kriterler
		
		textLine = TextLine()
		textLine.SetParent(self)
		textLine.SetPosition(30, 6)
		textLine.SetText(loncaadi)
		textLine.Show()
		
		textLine2 = TextLine()
		textLine2.SetParent(self)
		textLine2.SetPosition(30+106, 6)
		textLine2.SetText(tanitan)
		textLine2.Show()
		
		textLine3 = TextLine()
		textLine3.SetParent(self)
		textLine3.SetPosition(30+106+106, 6)
		textLine3.SetText(sonuye)
		textLine3.Show()
		
		textLine4 = TextLine()
		textLine4.SetParent(self)
		textLine4.SetPosition(30+106+106+106, 6)
		textLine4.SetText(istatistik)
		textLine4.Show()
		
		textLine5 = TextLine()
		textLine5.SetParent(self)
		textLine5.SetPosition(30+106+106+106, 6)
		textLine5.SetText(kriterler)
		textLine5.Show()
		
		textLine5_2 = TextLine()
		textLine5_2.SetParent(self)
		textLine5_2.SetPosition(30+106+106+106, 6)
		textLine5_2.SetText(kriterler[:26])
		textLine5_2.Show()

		self.loncaNameList.append(textLine)
		self.tanitanNameList.append(textLine2)
		self.sonuyesayisiList.append(textLine3)
		self.loncaIstatistikleriList.append(textLine4)
		if len(kriterler) < 15:
			self.loncaKriterleriList.append(textLine5)
		else:	
			self.loncaKriterleriList.append(textLine5_2)
		
		self.KriterlerDahaFazla = Button()
		self.KriterlerDahaFazla.SetParent(self)
		self.KriterlerDahaFazla.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
		self.KriterlerDahaFazla.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
		self.KriterlerDahaFazla.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
		self.KriterlerDahaFazla.SetText(">>>")
		self.KriterlerDahaFazla.SetToolTipTextRiot("Kriterlerin devam?: " + str(kriterler[26:]))
		self.KriterlerDahaFazla.SetPosition(20+110+110+110+110+87+87+15, 6+self.butonarttir)
		
		self.MesajAt = Button()
		self.MesajAt.SetParent(self)
		self.MesajAt.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
		self.MesajAt.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
		self.MesajAt.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
		self.MesajAt.SetText("M")
		self.MesajAt.SetToolTipText("Mesaj g?der")
		self.MesajAt.SetPosition(20+110+110+110+110+87+87+15, 6+self.butonarttir+19)
		self.MesajAt.SetEvent(lambda: self.MesajGonderOna(tanitan))
		
		self.mesajatList.append(self.MesajAt)
		self.dahafazlaList.append(self.KriterlerDahaFazla)
		
		self.butonarttir += 24
		
		import riotInfo
		if riotInfo.BuNP == 1:
			textLine4 = TextLine()
			textLine4.SetParent(self)
			textLine4.SetPosition(20+20+20, 3)
			textLine4.SetText(bayrak)
			textLine4.Show()
			self.bayrakResimList.append(textLine4)
		else:
			if bayrak == "Mavi" or str(bayrak) == "Mavi" or bayrak == "3" or bayrak == 3:
				imageLine = ImageBox()
				imageLine.SetParent(self)
				imageLine.LoadImage("KFDevelopers/server_fb34_kf/images/mavi.jpg")
				imageLine.Show()
				self.bayrakResimList.append(imageLine)
			elif bayrak == "Kirmizi" or str(bayrak) == "Kirmizi" or bayrak == "1" or bayrak == 1:
				imageLine = ImageBox()
				imageLine.SetParent(self)
				imageLine.LoadImage("KFDevelopers/server_fb34_kf/images/kirmizi.jpg")
				imageLine.Show()
				self.bayrakResimList.append(imageLine)
			elif bayrak == "Sari" or str(bayrak) == "Sari" or bayrak == "2" or bayrak == 2:
				imageLine = ImageBox()
				imageLine.SetParent(self)
				imageLine.LoadImage("KFDevelopers/server_fb34_kf/images/kirmizi.jpg") #oyunda sar?olmadýð?i?n k?m??oldu.
				imageLine.Show()
				self.bayrakResimList.append(imageLine)
				
		yatay = ImageBox()
		yatay.SetParent(self)
		yatay.LoadImage("KFDevelopers/server_fb34_kf/images/yatay.tga")
		yatay.Show()
		
		self.yatayList.append(yatay)

		self._LocateItem()
		

	def ChangeItem(self, number, text, tooltipText, textlineText, width):
		for key, value in self.keyDict.items():
			if value == number:
				self.textDict[key] = text + tooltipText + textlineText + width

				if number < len(self.loncaNameList):
					self.loncaNameList[key].SetText(text)

				return

	def LocateItem(self):
		self._LocateItem()
		
	def MesajGonderOna(self, text):
		import interfaceModule
		import constInfo
		import player
		if str(text) == player.GetName():
			import chat
			chat.AppendChat(chat.CHAT_TYPE_INFO, 'Kendine mesaj atamassýn.')
		else:
			constInfo.Secilen = str(text)
			constInfo.mesajat = 1

	def _LocateItem(self):

		skipCount = self.basePos
		yPos = 0
		yPos2 = 0
		self.showLineCount = 0

		for i in xrange(0, len(self.loncaNameList)):
			textLine = self.loncaNameList[i]
			nameTextLine = self.tanitanNameList[i]
			levelTextLine = self.sonuyesayisiList[i]
			bayrakResim = self.bayrakResimList[i]
			istatistikler = self.loncaIstatistikleriList[i]
			kriterler = self.loncaKriterleriList[i]
			mesajat = self.mesajatList[i]
			dahafazla = self.dahafazlaList[i]
			yatay = self.yatayList[i]
				
			textLine.Hide()
			nameTextLine.Hide()
			levelTextLine.Hide()		
			bayrakResim.Hide()
			istatistikler.Hide()
			kriterler.Hide()
			mesajat.Hide()
			dahafazla.Hide()
			yatay.Hide()
			
			if skipCount > 0:
				skipCount -= 1
				continue
			
			textLine.SetPosition(20, yPos + 6)
			nameTextLine.SetPosition(20+110, yPos + 6)
			levelTextLine.SetPosition(20+110+110, yPos + 6)
			istatistikler.SetPosition(20+110+110+110-18-12, yPos + 6)
			bayrakResim.SetPosition(20+110+110+110+110-20, yPos + 1 + 4)
			kriterler.SetPosition(20+110+110+110+110+87-24, yPos + 6)
			yatay.SetPosition(20-14-14-11, yPos2 + 6 - 2)
			
			mesajat.SetPosition(20+110+110+110+110+87+87+15+30+20-28, yPos + 4+1)
			dahafazla.SetPosition(20+110+110+110+110+87+87+15+30+20+5+11-4, yPos + 4+1)
		
			yPos += 24
			yPos2 += 23 - 4

			if yPos <= self.GetHeight() + 20:
				textLine.Show()
				nameTextLine.Show()
				levelTextLine.Show()
				bayrakResim.Show()
				istatistikler.Show()
				kriterler.Show()
				mesajat.Show()
				dahafazla.Show()
				yatay.Hide()

	def ArrangeItem(self):
		self.SetSize(self.width)
		self.SetSize(self.width, len(self.loncaNameList) * 17)
		self._LocateItem()

	def GetViewItemCount(self):
		return self.showLineCount

	def GetItemCount(self):
		return len(self.loncaNameList)

	def SetEvent(self, event):
		self.event = event

	def SelectItem(self, line):

		if not self.keyDict.has_key(line):
			return

		if line == self.selectedLine:
			return

		self.selectedLine = line
		self.event(self.keyDict.get(line, 0), self.textDict.get(line, "None"))
		
		x, y = self.GetGlobalPosition()

	def GetSelectedItem(self):
		return self.keyDict.get(self.selectedLine, 0)

	def OnMouseLeftButtonDown(self):
		if self.overLine < 0:
			return

	def OnMouseLeftButtonUp(self):
		if self.overLine >= 0:
			self.SelectItem(self.overLine+self.basePos)
	def OnUpdate(self):

		self.overLine = -1

		if self.IsIn():
			self.SelectItem(self.overLine+self.basePos)
			x, y = self.GetGlobalPosition()
			height = self.GetHeight()
			xMouse, yMouse = wndMgr.GetMousePosition()

			if yMouse - y < height - 1:
				self.overLine = (yMouse - y) / self.stepSize

				if self.overLine < 0:
					self.overLine = -1
				if self.overLine >= len(self.loncaNameList):
					self.overLine = -1

	def OnRender(self):
		xRender, yRender = self.GetGlobalPosition()
		yRender -= self.TEMPORARY_PLACE
		widthRender = self.width
		heightRender = self.height + self.TEMPORARY_PLACE*2 + 25 - 6

		if localeInfo.IsCIBN10:
			if -1 != self.overLine and self.keyDict[self.overLine] != -1:
				grp.SetColor(HALF_WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + self.overLine*self.stepSize + 4, self.width - 3 + 25 - 6 - 8, self.stepSize + 25 - 6  - 10)

			if -1 != self.selectedLine and self.keyDict[self.selectedLine] != -1:
				if self.selectedLine >= self.basePos:
					if self.selectedLine - self.basePos < self.showLineCount:
						grp.SetColor(SELECT_COLOR)
						grp.RenderBar(xRender + 2, yRender + (self.selectedLine-self.basePos)*self.stepSize + 4, self.width - 3 + 25 - 6 - 8, self.stepSize + 25 - 6 - 8)

		else:		
			if -1 != self.overLine:
				grp.SetColor(HALF_WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + self.overLine*self.stepSize + 4 + 25, self.width - 3 + 20 - 6 - 8, self.stepSize + 20) #+20				

			if -1 != self.selectedLine:
				if self.selectedLine >= self.basePos:
					if self.selectedLine - self.basePos < self.showLineCount:
						grp.SetColor(SELECT_COLOR)
						grp.RenderBar(xRender + 2, yRender + (self.selectedLine-self.basePos)*self.stepSize + 4 + 25 - 6 - 8, self.width - 3 + 25 - 6 - 8, self.stepSize + 30)
		
class ListBoxScrollTestLonca(ListBoxScrollVeSiralamaLonca):
	def __init__(self):
		ListBoxScrollVeSiralamaLonca.__init__(self)
		
		self.viewItemCount=15
		self.basePos=0
		self.itemHeight=15
		self.itemStep=20
		self.scrollBar = ScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetScrollEvent(self.__OnScroll)
		self.scrollBar.Hide()

	def SetSize(self, width, height):
		ListBoxScrollVeSiralamaLonca.SetSize(self, width - ScrollBar.SCROLLBAR_WIDTH, height)
		Window.SetSize(self, width, height)
		
		self.scrollBar.SetPosition(width - ScrollBar.SCROLLBAR_WIDTH + 5, 0)
		self.scrollBar.SetScrollBarSize(height)

	def ClearItem(self):
		ListBoxScrollVeSiralamaLonca.ClearItem(self)
		self.scrollBar.SetPos(0)

	def _LocateItem(self):
		ListBoxScrollVeSiralamaLonca._LocateItem(self)
		
		if self.showLineCount < len(self.loncaNameList):
			self.scrollBar.SetMiddleBarSize(float(self.GetViewItemCount())/self.GetItemCount())
			self.scrollBar.Show()
		else:
			self.scrollBar.Hide()

	def SetScrollBar(self, scrollBar):
		scrollBar.SetScrollEvent(__mem_func__(self.__OnScroll))
		self.scrollBar=scrollBar
		
	def __OnScroll(self):
		scrollLen = self.GetItemCount()-self.GetViewItemCount()
		if scrollLen < 0:
			scrollLen = 0
		self.SetBasePos(int(self.scrollBar.GetPos()*scrollLen))
		ListBoxScrollVeSiralamaLonca._LocateItem(self)

	def __GetScrollLen(self):
		scrollLen=self.__GetItemCount()-self.__GetViewItemCount()
		if scrollLen<0:
			return 0

		return scrollLen
		

	def __GetViewItemCount(self):
		return self.viewItemCount

	def __GetItemCount(self):
		return len(self.loncaNameList)

	def GetItemViewCoord(self, pos, itemWidth):
		if localeInfo.IsARABIC():
			return (self.GetWidth()-itemWidth-15, (pos-self.basePos)*self.itemStep)
		else:
			return (0, (pos-self.basePos)*self.itemStep)
			
	def __IsInViewRange(self, pos):
		if pos<self.basePos:
			return 0
		if pos>=self.basePos+self.viewItemCount:
			return 0
		return 1
						
class TitleBarAlisveris(Window):

	BLOCK_WIDTH = 32
	BLOCK_HEIGHT = 23

	def __init__(self):
		Window.__init__(self)
		self.AddFlag("attach")

	def __del__(self):
		Window.__del__(self)

	def MakeTitleBar(self, width, color):

		width = max(64, width)

		imgLeft = ImageBox()
		imgCenter = ExpandedImageBox()
		imgRight = ImageBox()
		imgLeft.AddFlag("not_pick")
		imgCenter.AddFlag("not_pick")
		imgRight.AddFlag("not_pick")
		imgLeft.SetParent(self)
		imgCenter.SetParent(self)
		imgRight.SetParent(self)

		if localeInfo.IsARABIC():
			imgLeft.LoadImage("locale/ae/ui/pattern/titlebar_left.tga")
			imgCenter.LoadImage("locale/ae/ui/pattern/titlebar_center.tga")
			imgRight.LoadImage("locale/ae/ui/pattern/titlebar_right.tga")
		else:
			imgLeft.LoadImage("d:/ymir work/ui/pattern/titlebar_left.tga")
			imgCenter.LoadImage("d:/ymir work/ui/pattern/titlebar_center.tga")
			imgRight.LoadImage("d:/ymir work/ui/pattern/titlebar_right.tga")

		imgLeft.Show()
		imgCenter.Show()
		imgRight.Show()

		self.imgLeft = imgLeft
		self.imgCenter = imgCenter
		self.imgRight = imgRight
		self.btnClose = btnClose

		self.SetWidth(width)

	def SetWidth(self, width):
		self.imgCenter.SetRenderingRect(0.0, 0.0, float((width - self.BLOCK_WIDTH*2) - self.BLOCK_WIDTH) / self.BLOCK_WIDTH, 0.0)
		self.imgCenter.SetPosition(self.BLOCK_WIDTH, 0)
		self.imgRight.SetPosition(width - self.BLOCK_WIDTH, 0)
			
		self.SetSize(width, self.BLOCK_HEIGHT)

class ListBoxScrollVeSiralama2(Window):

	TEMPORARY_PLACE = 3

	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)
		self.overLine = -1
		self.selectedLine = -1
		self.width = 0
		self.height = 0
		self.stepSize = 100
		self.basePos = 0
		self.showLineCount = 0
		self.itemCenterAlign = TRUE
		self.itemList = []
		self.itemlerList = []
		self.itemThinList = []
		self.itemSlotList = []
		self.itemSlotList2 = []
		self.itemResimList = []
		self.itemNameList = []
		self.fiyatList = []
		self.satanNameList = []
		self.satinalList = []
		self.gerialList = []
		
		self.keyDict = {}
		self.textDict = {}
		self.event = lambda *arg: None
		
	def __del__(self):
		Window.__del__(self)

	def SetWidth(self, width):
		self.SetSize(width, self.height)

	def SetSize(self, width, height):
		Window.SetSize(self, width, height)
		self.width = width
		self.height = height

	def SetTextCenterAlign(self, flag):
		self.itemCenterAlign = flag

	def SetBasePos(self, pos):
		self.basePos = pos
		self._LocateItem()

	def ClearItem(self):
		self.keyDict = {}
		self.textDict = {}
		self.itemList = []
		self.itemThinList = []
		self.itemSlotList = []
		self.itemSlotList2 = []
		self.itemResimList = []
		self.itemNameList = []
		self.fiyatList = []
		self.satanNameList = []
		self.satinalList = []
		self.gerialList = []
		self.overLine = -1
		self.selectedLine = -1
	
	def InsertItem(self, number, kodu, itemadi, itemfiyati, itemisatan, uzerinegelince):
		self.keyDict[len(self.itemList)] = number
		self.textDict[len(self.itemList)] = itemadi + itemfiyati + itemisatan + uzerinegelince
		self.textDict[len(self.itemNameList)] = itemadi
		self.textDict[len(self.fiyatList)] = itemfiyati
		self.textDict[len(self.satanNameList)] = itemisatan
		
		thin = ThinBoard()
		thin.SetParent(self)
		thin.SetPosition(6, 40)
		thin.SetSize(744+15+15, 72)
		thin.Show()
		
		slotLine = ImageBox()
		slotLine.SetParent(thin)
		slotLine.SetPosition(30, 5-1)
		slotLine.LoadImage("d:/ymir work/ui/Public/Slot_Base.sub")
		slotLine.Show()
		
		slotLine.SAFE_SetStringEvent("MOUSE_OVER_IN", self.Uzerinde(kodu, uzerinegelince))
		slotLine.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.NoUzerinde)
		
		slotLine2 = ImageBox()
		slotLine2.SetParent(thin)
		slotLine2.SetPosition(30, 20+20-5)
		slotLine2.LoadImage("d:/ymir work/ui/Public/Slot_Base.sub")
		slotLine2.Show()
		
		item.SelectItem(kodu)
		iconu = item.GetIconImageFileName()
		
		resimLine = ImageBox()
		resimLine.SetParent(thin)
		resimLine.SetPosition(30-2, 10-3-1)
		resimLine.LoadImage(iconu)
		resimLine.Show()
		
		itemAdiLine = TextLine()
		itemAdiLine.SetParent(thin)
		itemAdiLine.SetPosition(200-10, 25+2)
		itemAdiLine.SetText(itemadi)
		itemAdiLine.Show()
		
		itemFiyatLine = TextLine()
		itemFiyatLine.SetParent(thin)
		itemFiyatLine.SetPosition(190+180+75-10, 25+2)
		itemFiyatLine.SetText(itemfiyati)
		itemFiyatLine.Show()
		
		itemSatanLine = TextLine()
		itemSatanLine.SetParent(thin)
		itemSatanLine.SetPosition(190+180+80+160-50+10, 25+2)
		itemSatanLine.SetText(itemisatan)
		itemSatanLine.Show()
		
		satinal = Button()
		satinal.SetParent(thin)
		satinal.SetPosition(190+180+80+160+30+10, 25+2-5+1)
		satinal.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		satinal.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		satinal.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		satinal.SetText("Satin Al")
		satinal.SetToolTipText("Itemi satin al")
		satinal.Show()

		self.itemList.append(itemAdiLine)
		self.itemThinList.append(thin)
		self.itemSlotList.append(slotLine)
		self.itemSlotList2.append(slotLine2)
		self.itemResimList.append(resimLine)
		self.itemNameList.append(itemAdiLine)
		self.fiyatList.append(itemFiyatLine)
		self.satanNameList.append(itemSatanLine)
		self.satinalList.append(satinal)

		self._LocateItem()
		
	def InsertItemMy(self, number, kodu, itemadi, itemfiyati, itemisatan, uzerinegelince):
		self.keyDict[len(self.itemList)] = number
		self.textDict[len(self.itemList)] = itemadi + itemfiyati + itemisatan + uzerinegelince
		self.textDict[len(self.itemNameList)] = itemadi
		self.textDict[len(self.fiyatList)] = itemfiyati
		self.textDict[len(self.satanNameList)] = itemisatan
		
		thin = ThinBoard()
		thin.SetParent(self)
		thin.SetPosition(6, 40)
		thin.SetSize(744+15+15, 72)
		thin.Show()
		
		slotLine = ImageBox()
		slotLine.SetParent(thin)
		slotLine.SetPosition(30, 5-1)
		slotLine.LoadImage("d:/ymir work/ui/Public/Slot_Base.sub")
		slotLine.Show()
		
		slotLine.SAFE_SetStringEvent("MOUSE_OVER_IN", self.Uzerinde(kodu, uzerinegelince))
		slotLine.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.NoUzerinde)
		
		slotLine2 = ImageBox()
		slotLine2.SetParent(thin)
		slotLine2.SetPosition(30, 20+20-5)
		slotLine2.LoadImage("d:/ymir work/ui/Public/Slot_Base.sub")
		slotLine2.Show()
		
		item.SelectItem(kodu)
		iconu = item.GetIconImageFileName()
		
		resimLine = ImageBox()
		resimLine.SetParent(thin)
		resimLine.SetPosition(30-2, 10-3-1)
		resimLine.LoadImage(iconu)
		resimLine.Show()
		
		itemAdiLine = TextLine()
		itemAdiLine.SetParent(thin)
		itemAdiLine.SetPosition(200-10, 25+2)
		itemAdiLine.SetText(itemadi)
		itemAdiLine.Show()
		
		itemFiyatLine = TextLine()
		itemFiyatLine.SetParent(thin)
		itemFiyatLine.SetPosition(190+180+75-10, 25+2)
		itemFiyatLine.SetText(itemfiyati)
		itemFiyatLine.Show()
		
		itemSatanLine = TextLine()
		itemSatanLine.SetParent(thin)
		itemSatanLine.SetPosition(190+180+80+160-50+10, 25+2)
		itemSatanLine.SetText(itemisatan)
		itemSatanLine.Show()
		
		gerial = Button()
		gerial.SetParent(thin)
		gerial.SetPosition(190+180+80+160+30+10, 25+2-5+1)
		gerial.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		gerial.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		gerial.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		gerial.SetText("Kald?")
		gerial.SetToolTipText("Itemi alisveristen kaldir.")
		gerial.Show()

		self.itemList.append(itemAdiLine)
		self.itemThinList.append(thin)
		self.itemSlotList.append(slotLine)
		self.itemSlotList2.append(slotLine2)
		self.itemResimList.append(resimLine)
		self.itemNameList.append(itemAdiLine)
		self.fiyatList.append(itemFiyatLine)
		self.satanNameList.append(itemSatanLine)
		self.gerialList.append(gerial)

		self._LocateItemMy()
		
	def Uzerinde(self, itemkod, text):
		self.toolTip.ClearToolTip()
		items = text.split("#")
		self.toolTip.AddRefineItemData(itemkod, [items[1],items[2],items[3],items[4],items[5],items[6]], [(items[8],items[9]),(items[10],items[11]),(items[12],items[13]),(items[14],items[15]),(items[16],items[17]),(items[18],items[19]),(items[20],items[21])])
		
	def NoUzerinde(self):
		self.toolTip.Hide()

	def ChangeItem(self, number, text, tooltipText, textlineText, width):
		for key, value in self.keyDict.items():
			if value == number:
				self.textDict[key] = text + tooltipText + textlineText + width

				if number < len(self.itemList):
					self.itemList[key].SetText(text)

				return

	def LocateItem(self):
		self._LocateItem()

	def _LocateItem(self):

		skipCount = self.basePos
		yPos = 0
		self.showLineCount = 0

		for i in xrange(0, len(self.itemList)):
			thin = self.itemThinList[i]
			slot = self.itemSlotList[i]
			slot2 = self.itemSlotList2[i]
			itemresim = self.itemResimList[i]
			itemadi = self.itemNameList[i]
			itemfiyati = self.fiyatList[i]
			itemisatan = self.satanNameList[i]
			satinal = self.satinalList[i]

			if skipCount > 0:
				skipCount -= 1
				continue

			if localeInfo.IsARABIC():
				w, h = textLine.GetTextSize()
				textLine.SetPosition(w+10, yPos + 3)
			else:
				thin.SetPosition(6, yPos + 40-18+2)

			yPos += 75

			if yPos <= self.GetHeight():
				thin.Show()
				slot.Show()
				slot2.Show()
				itemresim.Show()
				itemadi.Show()
				itemfiyati.Show()
				itemisatan.Show()
				satinal.Show()
			else:
				thin.Hide()
				slot.Hide()
				slot2.Hide()
				itemresim.Hide()
				itemadi.Hide()
				itemfiyati.Hide()
				itemisatan.Hide()
				satinal.Hide()
				
	def _LocateItemMy(self):

		skipCount = self.basePos
		yPos = 0
		self.showLineCount = 0

		for i in xrange(0, len(self.itemList)):
			thin = self.itemThinList[i]
			slot = self.itemSlotList[i]
			slot2 = self.itemSlotList2[i]
			itemresim = self.itemResimList[i]
			itemadi = self.itemNameList[i]
			itemfiyati = self.fiyatList[i]
			itemisatan = self.satanNameList[i]
			gerial = self.gerialList[i]

			if skipCount > 0:
				skipCount -= 1
				continue

			if localeInfo.IsARABIC():
				w, h = textLine.GetTextSize()
				textLine.SetPosition(w+10, yPos + 3)
			else:
				thin.SetPosition(6, yPos + 40-18+2)

			yPos += 75

			if yPos <= self.GetHeight():
				thin.Show()
				slot.Show()
				slot2.Show()
				itemresim.Show()
				itemadi.Show()
				itemfiyati.Show()
				itemisatan.Show()
				gerial.Show()
			else:
				thin.Hide()
				slot.Hide()
				slot2.Hide()
				itemresim.Hide()
				itemadi.Hide()
				itemfiyati.Hide()
				itemisatan.Hide()
				gerial.Hide()

	def ArrangeItem(self):
		self.SetSize(self.width)
		self.SetSize(self.width, len(self.itemList) * 17)
		self._LocateItem()

	def GetViewItemCount(self):
		return self.showLineCount

	def GetItemCount(self):
		return len(self.itemList)

	def SetEvent(self, event):
		self.event = event

	def SelectItem(self, line):

		if not self.keyDict.has_key(line):
			return

		if line == self.selectedLine:
			return

	def GetSelectedItem(self):
		return self.keyDict.get(self.selectedLine, 0)

	def OnMouseLeftButtonDown(self):
		if self.overLine < 0:
			return

	def OnMouseLeftButtonUp(self):
		if self.overLine >= 0:
			pass

	def OnUpdate(self):

		if self.IsIn():
			pass

	def OnRender(self):
		xRender, yRender = self.GetGlobalPosition()
		yRender -= self.TEMPORARY_PLACE
		widthRender = self.width
		heightRender = self.height + self.TEMPORARY_PLACE*2

		if localeInfo.IsCIBN10:
			if -1 != self.overLine and self.keyDict[self.overLine] != -1:
				grp.SetColor(HALF_WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + self.overLine*self.stepSize + 4, self.width - 3, self.stepSize)

			if -1 != self.selectedLine and self.keyDict[self.selectedLine] != -1:
				if self.selectedLine >= self.basePos:
					if self.selectedLine - self.basePos < self.showLineCount:
						grp.SetColor(SELECT_COLOR)
						grp.RenderBar(xRender + 2 - 50, yRender + (self.selectedLine-self.basePos)*self.stepSize + 4, self.width - 3, self.stepSize - 50)

		else:		
			if -1 != self.overLine:
				pass

			if -1 != self.selectedLine:
				pass
						
class ListBoxScrollItemEkleme(ListBoxScrollVeSiralama2):
	def __init__(self):
		ListBoxScrollVeSiralama2.__init__(self)
		
		self.viewItemCount=15
		self.basePos=0
		self.itemHeight=15
		self.itemStep=20
		self.showLineCount = 0
		self.scrollBar = ScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetScrollEvent(self.__OnScroll)
		self.scrollBar.Hide()

	def SetSize(self, width, height):
		ListBoxScrollVeSiralama2.SetSize(self, width - ScrollBar.SCROLLBAR_WIDTH, height)
		Window.SetSize(self, width, height)
		
		self.scrollBar.SetPosition(width - ScrollBar.SCROLLBAR_WIDTH - 8 - 3 - 9, 0)
		self.scrollBar.SetScrollBarSize(height)

	def ClearItem(self):
		ListBoxScrollVeSiralama2.ClearItem(self)
		self.scrollBar.SetPos(0)

	def _LocateItem(self):
		ListBoxScrollVeSiralama2._LocateItem(self)
		
		if self.showLineCount < len(self.itemList):
			self.scrollBar.SetMiddleBarSize(float(self.GetViewItemCount())/self.GetItemCount())
			self.scrollBar.Show()
		else:
			self.scrollBar.Hide()
		
	def SetScrollBar(self, scrollBar):
		scrollBar.SetScrollEvent(__mem_func__(self.__OnScroll))
		self.scrollBar=scrollBar
		
	def __OnScroll(self):
		scrollLineCount = len(self.showingItemList) - (self.showingPageSize/20)
		startLine = int(scrollLineCount * self.scrollBar.GetPos())

		if startLine != self.startLine:
			self.startLine = startLine
			self._LocateItem()

	def __GetScrollLen(self):
		scrollLen=self.__GetItemCount()-self.__GetViewItemCount()
		if scrollLen<0:
			return 0

		return scrollLen

	def __GetViewItemCount(self):
		return self.viewItemCount

	def __GetItemCount(self):
		return len(self.itemList)

	def GetItemViewCoord(self, pos, itemWidth):
		if localeInfo.IsARABIC():
			return (self.GetWidth()-itemWidth-10, (pos-self.basePos)*self.itemStep)
		else:
			return (0, (pos-self.basePos)*self.itemStep)
			
	def __IsInViewRange(self, pos):
		if pos<self.basePos:
			return 0
		if pos>=self.basePos+self.viewItemCount:
			return 0
		return 1
						
class ScrollBarAlisveris(Window):

	SCROLLBAR_WIDTH = 35
	SCROLLBAR_MIDDLE_HEIGHT = 9
	SCROLLBAR_BUTTON_WIDTH = 35
	SCROLLBAR_BUTTON_HEIGHT = 35
	MIDDLE_BAR_POS = 5
	MIDDLE_BAR_UPPER_PLACE = 3
	MIDDLE_BAR_DOWNER_PLACE = 4
	TEMP_SPACE = MIDDLE_BAR_UPPER_PLACE + MIDDLE_BAR_DOWNER_PLACE

	class MiddleBar(DragButton):
		def __init__(self):
			DragButton.__init__(self)
			self.AddFlag("movable")

		def MakeImage(self):
			top = ImageBox()
			top.SetParent(self)
			top.LoadImage("d:/ymir work/ui/pattern/ScrollBar_Top.tga")
			top.SetPosition(0, 0)
			top.AddFlag("not_pick")
			top.Show()
			bottom = ImageBox()
			bottom.SetParent(self)
			bottom.LoadImage("d:/ymir work/ui/pattern/ScrollBar_Bottom.tga")
			bottom.AddFlag("not_pick")
			bottom.Show()

			middle = ExpandedImageBox()
			middle.SetParent(self)
			middle.LoadImage("d:/ymir work/ui/pattern/ScrollBar_Middle.tga")
			middle.SetPosition(0, 4)
			middle.AddFlag("not_pick")
			middle.Show()

			self.top = top
			self.bottom = bottom
			self.middle = middle

		def SetSize(self, height):
			height = max(12, height)
			DragButton.SetSize(self, 10, height)
			self.bottom.SetPosition(0, height-4)

			height -= 4*3
			self.middle.SetRenderingRect(0, 0, 0, float(height)/4.0)

	def __init__(self):
		Window.__init__(self)

		self.pageSize = 1
		self.curPos = 0.0
		self.eventScroll = lambda *arg: None
		self.lockFlag = FALSE
		self.scrollStep = 0.20


		self.CreateScrollBar()

	def __del__(self):
		Window.__del__(self)

	def CreateScrollBar(self):
		barSlot = Bar3D()
		barSlot.SetParent(self)
		barSlot.AddFlag("not_pick")
		barSlot.Show()

		middleBar = self.MiddleBar()
		middleBar.SetParent(self)
		middleBar.SetMoveEvent(__mem_func__(self.OnMove))
		middleBar.Show()
		middleBar.MakeImage()
		middleBar.SetSize(12)

		upButton = Button()
		upButton.SetParent(self)
		upButton.SetEvent(__mem_func__(self.OnUp))
		upButton.SetUpVisual("d:/ymir work/ui/public/scrollbar_up_button_01.sub")
		upButton.SetOverVisual("d:/ymir work/ui/public/scrollbar_up_button_02.sub")
		upButton.SetDownVisual("d:/ymir work/ui/public/scrollbar_up_button_03.sub")
		upButton.Show()

		downButton = Button()
		downButton.SetParent(self)
		downButton.SetEvent(__mem_func__(self.OnDown))
		downButton.SetUpVisual("d:/ymir work/ui/public/scrollbar_down_button_01.sub")
		downButton.SetOverVisual("d:/ymir work/ui/public/scrollbar_down_button_02.sub")
		downButton.SetDownVisual("d:/ymir work/ui/public/scrollbar_down_button_03.sub")
		downButton.Show()

		self.upButton = upButton
		self.downButton = downButton
		self.middleBar = middleBar
		self.barSlot = barSlot

		self.SCROLLBAR_WIDTH = self.upButton.GetWidth()
		self.SCROLLBAR_MIDDLE_HEIGHT = self.middleBar.GetHeight()
		self.SCROLLBAR_BUTTON_WIDTH = self.upButton.GetWidth()
		self.SCROLLBAR_BUTTON_HEIGHT = self.upButton.GetHeight()

	def Destroy(self):
		self.middleBar = None
		self.upButton = None
		self.downButton = None
		self.eventScroll = lambda *arg: None

	def SetScrollEvent(self, event):
		self.eventScroll = event

	def SetMiddleBarSize(self, pageScale):
		realHeight = self.GetHeight() - self.SCROLLBAR_BUTTON_HEIGHT*2
		self.SCROLLBAR_MIDDLE_HEIGHT = int(pageScale * float(realHeight))
		self.middleBar.SetSize(self.SCROLLBAR_MIDDLE_HEIGHT)
		self.pageSize = (self.GetHeight() - self.SCROLLBAR_BUTTON_HEIGHT*2) - self.SCROLLBAR_MIDDLE_HEIGHT - (self.TEMP_SPACE)

	def SetScrollBarSize(self, height):
		self.pageSize = (height - self.SCROLLBAR_BUTTON_HEIGHT*2) - self.SCROLLBAR_MIDDLE_HEIGHT - (self.TEMP_SPACE)
		self.SetSize(self.SCROLLBAR_WIDTH, height)
		self.upButton.SetPosition(0, 0)
		self.downButton.SetPosition(0, height - self.SCROLLBAR_BUTTON_HEIGHT)
		self.middleBar.SetRestrictMovementArea(self.MIDDLE_BAR_POS, self.SCROLLBAR_BUTTON_HEIGHT + self.MIDDLE_BAR_UPPER_PLACE, self.MIDDLE_BAR_POS+2, height - self.SCROLLBAR_BUTTON_HEIGHT*2 - self.TEMP_SPACE)
		self.middleBar.SetPosition(self.MIDDLE_BAR_POS, 0)

		self.UpdateBarSlot()

	def UpdateBarSlot(self):
		self.barSlot.SetPosition(0, self.SCROLLBAR_BUTTON_HEIGHT)
		self.barSlot.SetSize(self.GetWidth() - 2, self.GetHeight() - self.SCROLLBAR_BUTTON_HEIGHT*2 - 2)

	def GetPos(self):
		return self.curPos

	def SetPos(self, pos):
		pos = max(0.0, pos)
		pos = min(1.0, pos)

		newPos = float(self.pageSize) * pos
		self.middleBar.SetPosition(self.MIDDLE_BAR_POS, int(newPos) + self.SCROLLBAR_BUTTON_HEIGHT + self.MIDDLE_BAR_UPPER_PLACE)
		self.OnMove()

	def SetScrollStep(self, step):
		self.scrollStep = step
	
	def GetScrollStep(self):
		return self.scrollStep
		
	def OnUp(self):
		self.SetPos(self.curPos-self.scrollStep)

	def OnDown(self):
		self.SetPos(self.curPos+self.scrollStep)

	def OnMove(self):

		if self.lockFlag:
			return

		if 0 == self.pageSize:
			return

		(xLocal, yLocal) = self.middleBar.GetLocalPosition()
		self.curPos = float(yLocal - self.SCROLLBAR_BUTTON_HEIGHT - self.MIDDLE_BAR_UPPER_PLACE) / float(self.pageSize)

		self.eventScroll()

	def OnMouseLeftButtonDown(self):
		(xMouseLocalPosition, yMouseLocalPosition) = self.GetMouseLocalPosition()
		pickedPos = yMouseLocalPosition - self.SCROLLBAR_BUTTON_HEIGHT - self.SCROLLBAR_MIDDLE_HEIGHT/2
		newPos = float(pickedPos) / float(self.pageSize)
		self.SetPos(newPos)

	def LockScroll(self):
		self.lockFlag = TRUE

	def UnlockScroll(self):
		self.lockFlag = FALSE

class Alisveris_System(Window):

	TEMPORARY_PLACE = 3

	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)
		self.overLine = -1
		self.selectedLine = -1
		self.width = 0
		self.height = 0
		self.stepSize = 20
		self.basePos = 0
		self.showLineCount = 0
		self.itemCenterAlign = TRUE
		self.butonarttir = 0
		self.ilk = 0

		self.arkaplan = []
		self.itemicon = []
		self.itemadi = []
		self.itemfiyati = []
		self.satinal = []
		self.kod = ""

		self.keyDict = {}
		self.textDict = {}

		import player
		import uiToolTip
		
		self.toolTip = uiToolTip.ItemToolTip()
		self.event = lambda *arg: None
		
	def __del__(self):
		Window.__del__(self)

	def SetWidth(self, width):
		self.SetSize(width, self.height)

	def SetSize(self, width, height):
		Window.SetSize(self, width, height)
		self.width = width
		self.height = height

	def SetTextCenterAlign(self, flag):
		self.itemCenterAlign = flag

	def SetBasePos(self, pos):
		self.basePos = pos
		self._LocateItem()

	def ClearItem(self):
		self.arkaplan = []
		self.itemicon = []
		self.itemadi = []
		self.itemfiyati = []
		self.satinal = []
		self.keyDict = {}
		self.textDict = {}
		self.ilk = 0
		self.overLine = -1
		self.selectedLine = -1
	
	def InsertItem(self, number, itemkodu, adeti, fiyati):
		
		self.kod = str(itemkodu)
	
		arkaplan = ImageBox()
		arkaplan.SetParent(self)
		arkaplan.SetPosition(5, 6)
		arkaplan.LoadImage("KFDevelopers/server_fb34_kf/images/thinboard.tga")
		arkaplan.Show()
		
		item.SelectItem(int(itemkodu))
		iconu = item.GetIconImageFileName()
		adi = item.GetItemName()
		
		imageLine = ImageBox()
		imageLine.SetParent(arkaplan)
		imageLine.LoadImage(iconu)
		imageLine.Show()

		itemAdi = TextLine()
		itemAdi.SetParent(arkaplan)
		itemAdi.SetText(str(adi))
		itemAdi.Show()

		itemFiyati = TextLine()
		itemFiyati.SetParent(arkaplan)
		itemFiyati.SetText(str(fiyati) + " EP")
		itemFiyati.Show()
		
		self.SatinAl = Button()
		self.SatinAl.SetParent(arkaplan)
		self.SatinAl.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.SatinAl.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.SatinAl.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.SatinAl.SetText("Sat? Al")
		self.SatinAl.SetToolTipText("?emi sat? al!")
		
		imageLine.SAFE_SetStringEvent("MOUSE_OVER_IN", self.Uzerinde)
		imageLine.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.NoUzerinde)

		self.arkaplan.append(arkaplan)
		self.itemicon.append(imageLine)
		self.itemadi.append(itemAdi)
		self.itemfiyati.append(itemFiyati)
		self.satinal.append(self.SatinAl)
	
		self._LocateItem()
		
	def Uzerinde(self):
		import player
		self.toolTip.ClearToolTip()
		metinSlot = [player.GetItemMetinSocket(int(self.kod), i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
		attrSlot = [player.GetItemAttribute(int(self.kod), i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]
		self.toolTip.AddRefineItemData(int(self.kod), metinSlot, attrSlot)
		self.toolTip.AppendSpace(3)
		
	def NoUzerinde(self):
		self.toolTip.Hide()
		
	def ChangeItem(self, number, text, tooltipText, textlineText, width):
		for key, value in self.keyDict.items():
			if value == number:
				self.textDict[key] = text + tooltipText + textlineText + width

				return

	def LocateItem(self):
		self._LocateItem()

	def _LocateItem(self):

		skipCount = self.basePos
		yPos = 0
		yPos2 = 0
		self.showLineCount = 0

		for i in xrange(0, len(self.arkaplan)):
			arkaplan = self.arkaplan[i]
			itemicon = self.itemicon[i]
			itemadi = self.itemadi[i]
			itemfiyati = self.itemfiyati[i]
			satinal = self.satinal[i]

			arkaplan.Hide()
			itemicon.Hide()
			itemadi.Hide()
			itemfiyati.Hide()
			satinal.Hide()

			if skipCount > 0:
				skipCount -= 1
				continue
			
			arkaplan.SetPosition(60-30, yPos2 + 8)
			itemicon.SetPosition(30, yPos + 0)
			itemadi.SetPosition(125, yPos + 16)
			itemfiyati.SetPosition(320, yPos + 16)
			satinal.SetPosition(400, yPos + 11)

			yPos += 0
			yPos2 += 50
			

			if yPos <= self.GetHeight():
				self.showLineCount += 1
				arkaplan.Show()
				itemicon.Show()
				itemadi.Show()
				itemfiyati.Show()
				satinal.Show()

	def ArrangeItem(self):
		self.SetSize(self.width)
		self.SetSize(self.width, len(self.biyologGerekenItem) * 17)
		self._LocateItem()

	def GetViewItemCount(self):
		return int(self.GetHeight() / self.stepSize)

	def GetItemCount(self):
		return len(self.biyologGerekenItem)

	def SetEvent(self, event):
		self.event = event

	def SelectItem(self, line):

		if not self.keyDict.has_key(line):
			return

		if line == self.selectedLine:
			return

		self.selectedLine = line
		self.event(self.keyDict.get(line, 0), self.textDict.get(line, "None"))
		
		x, y = self.GetGlobalPosition()

	def GetSelectedItem(self):
		return self.keyDict.get(self.selectedLine, 0)

	def OnMouseLeftButtonDown(self):
		if self.overLine < 0:
			return

	def OnMouseLeftButtonUp(self):
		if self.overLine >= 0:
			self.SelectItem(self.overLine+self.basePos)
	def OnUpdate(self):

		self.overLine = -1

		if self.IsIn():
			self.SelectItem(self.overLine+self.basePos)
			x, y = self.GetGlobalPosition()
			height = self.GetHeight()
			xMouse, yMouse = wndMgr.GetMousePosition()

			if yMouse - y < height - 1:
				self.overLine = (yMouse - y) / self.stepSize

				if self.overLine < 0:
					self.overLine = -1
				if self.overLine >= len(self.arkaplan):
					self.overLine = -1

	def OnRender(self):
		xRender, yRender = self.GetGlobalPosition()
		yRender -= self.TEMPORARY_PLACE
		widthRender = self.width
		heightRender = self.height + self.TEMPORARY_PLACE*2 + 25 - 6

		if localeInfo.IsCIBN10 and 50 > 100:
			if -1 != self.overLine and self.keyDict[self.overLine] != -1:
				grp.SetColor(HALF_WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + self.overLine*self.stepSize + 4, self.width - 3 + 25 - 6 - 8, self.stepSize + 25 - 6  - 10)

			if -1 != self.selectedLine and self.keyDict[self.selectedLine] != -1:
				if self.selectedLine >= self.basePos:
					if self.selectedLine - self.basePos < self.showLineCount:
						grp.SetColor(SELECT_COLOR)
						grp.RenderBar(xRender + 2, yRender + (self.selectedLine-self.basePos)*self.stepSize + 4, self.width - 3 + 25 - 6 - 8, self.stepSize + 25 - 6 - 8)

		else:
			if 50 > 100:
				if -1 != self.overLine:
					grp.SetColor(HALF_WHITE_COLOR)
					grp.RenderBar(xRender + 2, yRender + self.overLine*self.stepSize + 4 + 25, self.width - 3 + 20 - 6 - 8, self.stepSize + 20) #+20				

				if -1 != self.selectedLine:
					if self.selectedLine >= self.basePos:
						if self.selectedLine - self.basePos < self.showLineCount:
							grp.SetColor(SELECT_COLOR)
							grp.RenderBar(xRender + 2, yRender + (self.selectedLine-self.basePos)*self.stepSize + 4 + 25 - 6 - 8, self.width - 3 + 25 - 6 - 8, self.stepSize + 30)
		
class Alisveris_System_AlTaban(Alisveris_System):
	def __init__(self):
		Alisveris_System.__init__(self)
		
		self.viewItemCount=15
		self.basePos=0
		self.itemHeight=15
		self.itemStep=20
		self.scrollBar = ScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetScrollEvent(self.__OnScroll)
		self.scrollBar.Hide()

	def SetSize(self, width, height):
		Alisveris_System.SetSize(self, width - ScrollBar.SCROLLBAR_WIDTH, height)
		Window.SetSize(self, width, height)
		
		self.scrollBar.SetPosition(width - ScrollBar.SCROLLBAR_WIDTH + 5, 0)
		self.scrollBar.SetScrollBarSize(height)

	def ClearItem(self):
		Alisveris_System.ClearItem(self)
		self.scrollBar.SetPos(0)

	def _LocateItem(self):
		Alisveris_System._LocateItem(self)
		
		if self.showLineCount < len(self.biyologGerekenItem):
			self.scrollBar.SetMiddleBarSize(float(self.GetViewItemCount())/self.GetItemCount())
			self.scrollBar.Show()
		else:
			self.scrollBar.Hide()

	def SetScrollBar(self, scrollBar):
		scrollBar.SetScrollEvent(__mem_func__(self.__OnScroll))
		self.scrollBar=scrollBar
		
	def __OnScroll(self):
		scrollLen = self.GetItemCount()-self.GetViewItemCount()
		if scrollLen < 0:
			scrollLen = 0
		self.SetBasePos(int(self.scrollBar.GetPos()*scrollLen))
		Alisveris_System._LocateItem(self)

	def __GetScrollLen(self):
		scrollLen=self.__GetItemCount()-self.__GetViewItemCount()
		if scrollLen<0:
			return 0

		return scrollLen

	def __GetViewItemCount(self):
		return self.viewItemCount

	def __GetItemCount(self):
		return len(self.biyologGerekenItem)

	def GetItemViewCoord(self, pos, itemWidth):
		if localeInfo.IsARABIC():
			return (self.GetWidth()-itemWidth-15, (pos-self.basePos)*self.itemStep)
		else:
			return (0, (pos-self.basePos)*self.itemStep)
			
	def __IsInViewRange(self, pos):
		if pos<self.basePos:
			return 0
		if pos>=self.basePos+self.viewItemCount:
			return 0
		return 1						

class ListBoxSiralama(Window):

	TEMPORARY_PLACE = 3

	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)
		self.overLine = -1
		self.selectedLine = -1
		self.width = 0
		self.height = 0
		self.stepSize = 17
		self.basePos = 0
		self.showLineCount = 0
		self.itemCenterAlign = TRUE
		self.itemList = []
		self.keyDict = {}
		self.textDict = {}
		self.event = lambda *arg: None
	def __del__(self):
		Window.__del__(self)

	def SetWidth(self, width):
		self.SetSize(width, self.height)

	def SetSize(self, width, height):
		Window.SetSize(self, width, height)
		self.width = width
		self.height = height

	def SetTextCenterAlign(self, flag):
		self.itemCenterAlign = flag

	def SetBasePos(self, pos):
		self.basePos = pos
		self._LocateItem()

	def ClearItem(self):
		self.keyDict = {}
		self.textDict = {}
		self.itemList = []
		self.overLine = -1
		self.selectedLine = -1
		
	def InsertItem(self, number, text, arg, idx):
		self.keyDict[len(self.itemList)] = number
		self.textDict[len(self.itemList)] = text, arg, idx

		textLine = TextLine()
		textLine.SetParent(self)
		textLine.SetText(text)
		textLine.SetPosition(10, 3)
		textLine.Show()
		
		textLine2 = TextLine()
		textLine2.SetParent(self)
		textLine2.SetText(arg)
		textLine.SetPosition(30, 3)
		textLine2.Show()
		
		textLine3 = TextLine()
		textLine3.SetParent(self)
		textLine3.SetText(idx)
		textLine.SetPosition(50, 3)
		textLine3.Show()

		if self.itemCenterAlign:
			textLine.SetWindowHorizontalAlignCenter()
			textLine.SetHorizontalAlignCenter()

		self.itemList.append(textLine, textLine2, textLine3)

		self._LocateItem()

	def ChangeItem(self, number, text):
		for key, value in self.keyDict.items():
			if value == number:
				self.textDict[key] = text

				if number < len(self.itemList):
					self.itemList[key].SetText(text)

				return

	def LocateItem(self):
		self._LocateItem()

	def _LocateItem(self):

		skipCount = self.basePos
		yPos = 0
		self.showLineCount = 0
		pass

	def ArrangeItem(self):
		self.SetSize(self.width, len(self.itemList) * self.stepSize)
		self._LocateItem()

	def GetViewItemCount(self):
		return int(self.GetHeight() / self.stepSize)

	def GetItemCount(self):
		return len(self.itemList)

	def SetEvent(self, event):
		self.event = event

	def SelectItem(self, line):

		if not self.keyDict.has_key(line):
			return

		if line == self.selectedLine:
			return

		self.selectedLine = line
		self.event(self.keyDict.get(line, 0), self.textDict.get(line, "None"))

	def GetSelectedItem(self):
		return self.keyDict.get(self.selectedLine, 0)

	def OnMouseLeftButtonDown(self):
		if self.overLine < 0:
			return

	def OnMouseLeftButtonUp(self):
		if self.overLine >= 0:
			self.SelectItem(self.overLine+self.basePos)
	def OnUpdate(self):

		self.overLine = -1

		if self.IsIn():
			self.SelectItem(self.overLine+self.basePos)
			x, y = self.GetGlobalPosition()
			height = self.GetHeight()
			xMouse, yMouse = wndMgr.GetMousePosition()

			if yMouse - y < height - 1:
				self.overLine = (yMouse - y) / self.stepSize

				if self.overLine < 0:
					self.overLine = -1
				if self.overLine >= len(self.itemList):
					self.overLine = -1

	def OnRender(self):
		xRender, yRender = self.GetGlobalPosition()
		yRender -= self.TEMPORARY_PLACE
		widthRender = self.width
		heightRender = self.height + self.TEMPORARY_PLACE*2

		if localeInfo.IsCIBN10:
			if -1 != self.overLine and self.keyDict[self.overLine] != -1:
				grp.SetColor(HALF_WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + self.overLine*self.stepSize + 4, self.width - 3, self.stepSize)				

			if -1 != self.selectedLine and self.keyDict[self.selectedLine] != -1:
				if self.selectedLine >= self.basePos:
					if self.selectedLine - self.basePos < self.showLineCount:
						grp.SetColor(SELECT_COLOR)
						grp.RenderBar(xRender + 2, yRender + (self.selectedLine-self.basePos)*self.stepSize + 4, self.width - 3, self.stepSize)

		else:		
			if -1 != self.overLine:
				grp.SetColor(HALF_WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + self.overLine*self.stepSize + 4, self.width - 3, self.stepSize)				

			if -1 != self.selectedLine:
				if self.selectedLine >= self.basePos:
					if self.selectedLine - self.basePos < self.showLineCount:
						grp.SetColor(SELECT_COLOR)
						grp.RenderBar(xRender + 2, yRender + (self.selectedLine-self.basePos)*self.stepSize + 4, self.width - 3, self.stepSize)
						
class ListBox_Scroll(ListBox):
	def __init__(self):
		ListBox.__init__(self)
		
		self.scrollBar = ScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetScrollEvent(self.__OnScroll)
		self.scrollBar.Hide()

	def SetSize(self, width, height):
		ListBox.SetSize(self, width - ScrollBar.SCROLLBAR_WIDTH, height)
		Window.SetSize(self, width, height)
		
		self.scrollBar.SetPosition(width - ScrollBar.SCROLLBAR_WIDTH, 0)
		self.scrollBar.SetScrollBarSize(height)

	def ClearItem(self):
		ListBox.ClearItem(self)
		self.scrollBar.SetPos(0)

	def _LocateItem(self):
		ListBox._LocateItem(self)
		
		if self.showLineCount < len(self.itemList):
			self.scrollBar.SetMiddleBarSize(float(self.GetViewItemCount())/self.GetItemCount())
			self.scrollBar.Show()
		else:
			self.scrollBar.Hide()

	def __OnScroll(self):
		scrollLen = self.GetItemCount()-self.GetViewItemCount()
		if scrollLen < 0:
			scrollLen = 0
		self.SetBasePos(int(self.scrollBar.GetPos()*scrollLen))
		
class ListBoxScroll(ListBox):
	def __init__(self):
		ListBox.__init__(self)
		
		self.scrollBar = ScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetScrollEvent(self.__OnScroll)
		self.scrollBar.Hide()

	def SetSize(self, width, height):
		ListBox.SetSize(self, width - ScrollBar.SCROLLBAR_WIDTH, height)
		Window.SetSize(self, width, height)
		
		self.scrollBar.SetPosition(width - ScrollBar.SCROLLBAR_WIDTH + 5+15-6-3, 0)
		self.scrollBar.SetScrollBarSize(height)

	def ClearItem(self):
		ListBox.ClearItem(self)
		self.scrollBar.SetPos(0)

	def _LocateItem(self):
		import riotInfo
		import constInfo
		ListBox._LocateItem(self)
		
		self.scrollBar.SetMiddleBarSize(float(self.GetViewItemCount())/self.GetItemCount())
		if riotInfo.ScrollKapat == 1:
			riotInfo.ScrollKapat = 0
			self.scrollBar.Hide()
		else:
			self.scrollBar.Show()
			
		if constInfo.listkapat == 1:
			self.scrollBar.Hide()
		else:
			self.scrollBar.Show()

	def __OnScroll(self):
		scrollLen = self.GetItemCount()-self.GetViewItemCount()
		if scrollLen < 0:
			scrollLen = 0
		self.SetBasePos(int(self.scrollBar.GetPos()*scrollLen))
		
class ListBoxScrollVeSiralama(Window):

	TEMPORARY_PLACE = 3

	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)
		self.overLine = -1
		self.selectedLine = -1
		self.width = 0
		self.height = 0
		self.stepSize = 15
		self.basePos = 0
		self.showLineCount = 0
		self.itemCenterAlign = TRUE
		self.itemList = []
		self.itemNameList = []
		self.levelNameList = []
		self.bayrakResimList = []
		self.npNameList = []
		self.keyDict = {}
		self.textDict = {}
		self.nameDict = {}
		self.levelDict = {}
		self.bayrakDict = {}
		self.event = lambda *arg: None
		
	def __del__(self):
		Window.__del__(self)

	def SetWidth(self, width):
		self.SetSize(width, self.height)

	def SetSize(self, width, height):
		Window.SetSize(self, width, height)
		self.width = width
		self.height = height

	def SetTextCenterAlign(self, flag):
		self.itemCenterAlign = flag

	def SetBasePos(self, pos):
		self.basePos = pos
		self._LocateItem()

	def ClearItem(self):
		self.keyDict = {}
		self.textDict = {}
		self.nameDict = {}
		self.levelDict = {}
		self.bayrakDict = {}
		self.itemList = []
		self.itemNameList = []
		self.levelNameList = []
		self.bayrakResimList = []
		self.npNameList = []
		self.overLine = -1
		self.selectedLine = -1
	
	def InsertItem(self, number, text, tooltipText, arg, line):
		self.keyDict[len(self.itemList)] = number
		self.textDict[len(self.itemList)] = text
		self.nameDict[len(self.itemNameList)] = tooltipText
		self.levelDict[len(self.levelNameList)] = arg
		self.bayrakDict[len(self.npNameList)] = line

		
		textLine = TextLine()
		textLine.SetParent(self)
		textLine.SetText(text)
		textLine.Show()
		
		textLine2 = TextLine()
		textLine2.SetParent(self)
		textLine2.SetPosition(20, 3)
		textLine2.SetText(tooltipText)
		textLine2.Show()
		
		textLine3 = TextLine()
		textLine3.SetParent(self)
		textLine3.SetPosition(20+20, 3)
		textLine3.SetText(arg)
		textLine3.Show()

		self.itemList.append(textLine)
		self.itemNameList.append(textLine2)
		self.levelNameList.append(textLine3)
		
		import riotInfo
		if riotInfo.BuNP == 1:
			textLine4 = TextLine()
			textLine4.SetParent(self)
			textLine4.SetPosition(20+20+20, 3)
			textLine4.SetText(line)
			textLine4.Show()
			self.npNameList.append(textLine4)
		else:
			if line == "Mavi" or str(line) == "Mavi" or line == "3" or line == 3:
				imageLine = ImageBox()
				imageLine.SetParent(self)
				imageLine.LoadImage("KFDevelopers/server_fb34_kf/22.jpg")
				imageLine.Show()
				self.bayrakResimList.append(imageLine)
			elif line == "Kirmizi" or str(line) == "Kirmizi" or line == "1" or line == 1:
				imageLine = ImageBox()
				imageLine.SetParent(self)
				imageLine.LoadImage("KFDevelopers/server_fb34_kf/20.jpg")
				imageLine.Show()
				self.bayrakResimList.append(imageLine)
			elif line == "Sari" or str(line) == "Sari" or line == "2" or line == 2:
				imageLine = ImageBox()
				imageLine.SetParent(self)
				imageLine.LoadImage("KFDevelopers/server_fb34_kf/21.jpg")
				imageLine.Show()
				self.bayrakResimList.append(imageLine)

		self._LocateItem()

	def ChangeItem(self, number, text, tooltipText, textlineText, width):
		for key, value in self.keyDict.items():
			if value == number:
				self.textDict[key] = text + tooltipText + textlineText + width

				if number < len(self.itemList):
					self.itemList[key].SetText(text)

				return

	def LocateItem(self):
		self._LocateItem()

	def _LocateItem(self):

		skipCount = self.basePos
		yPos = 0
		self.showLineCount = 0

		for i in xrange(0, len(self.itemList)):
			textLine = self.itemList[i]
			nameTextLine = self.itemNameList[i]
			levelTextLine = self.levelNameList[i]
			if riotInfo.BuNP == 1:
				npTextLine = self.npNameList[i]
			else:
				bayrakResim = self.bayrakResimList[i]

			textLine.Hide()
			nameTextLine.Hide()
			levelTextLine.Hide()			
			if riotInfo.BuNP == 1:
				npTextLine.Hide()
			else:
				bayrakResim.Hide()
			
			if skipCount > 0:
				skipCount -= 1
				continue

			if localeInfo.IsARABIC():
				w, h = textLine.GetTextSize()
				textLine.SetPosition(w+10, yPos + 3)
			else:
				textLine.SetPosition(3+5, yPos + 3)
				nameTextLine.SetPosition(20+20+5+5, yPos + 3)
				levelTextLine.SetPosition(20+20+5+25+40+25+15+3-8-2, yPos + 3)
				if riotInfo.BuNP == 1:
					npTextLine.SetPosition(20+20+5+25+40+30+25+5+13-3 + 6 + 4, yPos + 3)
				else:
					bayrakResim.SetPosition(20+20+5+25+40+30+25+5+13-3, yPos + 2)

			yPos += self.stepSize

			if yPos <= self.GetHeight():
				textLine.Show()
				nameTextLine.Show()
				levelTextLine.Show()
				if riotInfo.BuNP == 1:
					npTextLine.Show()
				else:
					bayrakResim.Show()
	def ArrangeItem(self):
		self.SetSize(self.width)
		self.SetSize(self.width, len(self.itemList) * 17)
		self._LocateItem()

	def GetViewItemCount(self):
		return self.showLineCount

	def GetItemCount(self):
		return len(self.itemList)

	def SetEvent(self, event):
		self.event = event

	def SelectItem(self, line):

		if not self.keyDict.has_key(line):
			return

		if line == self.selectedLine:
			return

		self.selectedLine = line
		self.event(self.keyDict.get(line, 0), self.textDict.get(line, "None"))
		
		x, y = self.GetGlobalPosition()

	def GetSelectedItem(self):
		return self.keyDict.get(self.selectedLine, 0)

	def OnMouseLeftButtonDown(self):
		if self.overLine < 0:
			return

	def OnMouseLeftButtonUp(self):
		if self.overLine >= 0:
			self.SelectItem(self.overLine+self.basePos)
	def OnUpdate(self):

		self.overLine = -1

		if self.IsIn():
			self.SelectItem(self.overLine+self.basePos)
			x, y = self.GetGlobalPosition()
			height = self.GetHeight()
			xMouse, yMouse = wndMgr.GetMousePosition()

			if yMouse - y < height - 1:
				self.overLine = (yMouse - y) / self.stepSize

				if self.overLine < 0:
					self.overLine = -1
				if self.overLine >= len(self.itemList):
					self.overLine = -1

	def OnRender(self):
		xRender, yRender = self.GetGlobalPosition()
		yRender -= self.TEMPORARY_PLACE
		widthRender = self.width
		heightRender = self.height + self.TEMPORARY_PLACE*2

		if localeInfo.IsCIBN10:
			if -1 != self.overLine and self.keyDict[self.overLine] != -1:
				grp.SetColor(HALF_WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + self.overLine*self.stepSize + 4, self.width - 3, self.stepSize)

			if -1 != self.selectedLine and self.keyDict[self.selectedLine] != -1:
				if self.selectedLine >= self.basePos:
					if self.selectedLine - self.basePos < self.showLineCount:
						grp.SetColor(SELECT_COLOR)
						grp.RenderBar(xRender + 2, yRender + (self.selectedLine-self.basePos)*self.stepSize + 4, self.width - 3, self.stepSize)

		else:		
			if -1 != self.overLine:
				grp.SetColor(HALF_WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + self.overLine*self.stepSize + 4, self.width - 3, self.stepSize)				

			if -1 != self.selectedLine:
				if self.selectedLine >= self.basePos:
					if self.selectedLine - self.basePos < self.showLineCount:
						grp.SetColor(SELECT_COLOR)
						grp.RenderBar(xRender + 2, yRender + (self.selectedLine-self.basePos)*self.stepSize + 4, self.width - 3, self.stepSize)
		
class ListBoxScrollTest(ListBoxScrollVeSiralama):
	def __init__(self):
		ListBoxScrollVeSiralama.__init__(self)
		
		self.viewItemCount=15
		self.basePos=0
		self.itemHeight=15
		self.itemStep=20
		self.scrollBar = ScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetScrollEvent(self.__OnScroll)
		self.scrollBar.Hide()

	def SetSize(self, width, height):
		ListBoxScrollVeSiralama.SetSize(self, width - ScrollBar.SCROLLBAR_WIDTH, height)
		Window.SetSize(self, width, height)
		
		self.scrollBar.SetPosition(width - ScrollBar.SCROLLBAR_WIDTH + 5, 0)
		self.scrollBar.SetScrollBarSize(height)

	def ClearItem(self):
		ListBoxScrollVeSiralama.ClearItem(self)
		self.scrollBar.SetPos(0)

	def _LocateItem(self):
		ListBoxScrollVeSiralama._LocateItem(self)
		
		if self.showLineCount < len(self.itemList):
			self.scrollBar.SetMiddleBarSize(float(self.GetViewItemCount())/self.GetItemCount())
			self.scrollBar.Show()
		else:
			self.scrollBar.Hide()

	def SetScrollBar(self, scrollBar):
		scrollBar.SetScrollEvent(__mem_func__(self.__OnScroll))
		self.scrollBar=scrollBar
		
	def __OnScroll(self):
		scrollLen = self.GetItemCount()-self.GetViewItemCount()
		if scrollLen < 0:
			scrollLen = 0
		self.SetBasePos(int(self.scrollBar.GetPos()*scrollLen))
		ListBoxScrollVeSiralama._LocateItem(self)

	def __GetScrollLen(self):
		scrollLen=self.__GetItemCount()-self.__GetViewItemCount()
		if scrollLen<0:
			return 0

		return scrollLen
		

	def __GetViewItemCount(self):
		return self.viewItemCount

	def __GetItemCount(self):
		return len(self.itemList)

	def GetItemViewCoord(self, pos, itemWidth):
		if localeInfo.IsARABIC():
			return (self.GetWidth()-itemWidth-15, (pos-self.basePos)*self.itemStep)
		else:
			return (0, (pos-self.basePos)*self.itemStep)
			
	def __IsInViewRange(self, pos):
		if pos<self.basePos:
			return 0
		if pos>=self.basePos+self.viewItemCount:
			return 0
		return 1