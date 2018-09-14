# PythonTest gui init module
# (c) 2001 Juergen Riegel LGPL

class PythonTest ( Workbench ):
        "My workbench object"
        def __init__(self):
            self.__class__.Icon = FreeCAD.getResourceDir() + "Mod/PythonTest/Resources/PythonTest.svg"
            self.__class__.MenuText = "PythonTest"
            self.__class__.ToolTip = "This is workbench for testing the python programming"

        def Initialize(self):
                import CreatBox
                list = ["MyCommand1","MyCommand2"]
                self.appendToolbar("My Tools", list)
                self.appendMenu("My Tools", list)
                Log ("Loading MyModule... done\n")

        def Activated(self):
                # do something here if needed...
                Msg ("MyWorkbench.Activated()\n")

        def Deactivated(self):
                # do something here if needed...
                Msg ("MyWorkbench.Deactivated()\n")

        def GetClassName(self):
                return "Gui::PythonWorkbench"

FreeCADGui.addWorkbench(PythonTest)
