# -*- coding: utf-8 -*-

import FreeCAD,FreeCADGui,Observer

class MyTool:
        "My tool object"
        def GetResources(self):
             return {'Pixmap'  : 'MyCommand1',
            'MenuText': 'Insert a TestFeauture',
            'ToolTip' : 'Insert a TestFeature in the active Document'}

        #def IsActive(self):
        #        # do something here...

        #def Activated(self):
        #        # do something here...

def SelSurf(self):
    obs = Observer.SelectionObserver()
    FreeCADGui.Selection.addObserver(obs)

FreeCADGui.addCommand('MyCommand1',MyTool())
