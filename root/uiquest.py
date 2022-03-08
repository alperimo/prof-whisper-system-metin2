import gameInfo
import constInfo

class QuestDialog(ui.ScriptWindow):

	def __init__(self,skin,idx):
		if gameInfo.INPUT == 1:
			return
		if constInfo.INPUT_IGNORE==1:
			return
