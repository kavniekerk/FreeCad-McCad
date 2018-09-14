#!/usr/bin/env python
# -*- coding: utf-8 -*-

import FreeCAD,FreeCADGui
import sys
import TestApp

class MyTool:
        "My tool object"
        def Activated(self):
            TestApp.TestText("Menu.MenuDeleteCases")

        def GetResources(self):
            return {'Pixmap'  : 'Std_Tool1',
                    'MenuText': 'Remove menu',
                    'ToolTip' : 'Test the menu stuff of FreeCAD'}


FreeCADGui.addCommand("MyCommand1",MyTool())
