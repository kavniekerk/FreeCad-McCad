# KIT gui init module
# (c) 2001 Juergen Riegel LGPL

class KITWorkbench ( Workbench ):
	"KIT workbench object"
	MenuText = "KIT"
	ToolTip = "KIT workbench"
	def Initialize(self):
		# load the module
		import KITGui
	def GetClassName(self):
		return "KITGui::Workbench"

Gui.addWorkbench(KITWorkbench())
