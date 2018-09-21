#!/usr/bin/env python
# -*- coding: utf-8 -*-

import FreeCAD,FreeCADGui

class SelectionObserver:
    def addSelection(self,doc,obj,sub,pos):
        FreeCAD.Console.PrintMessage("Document: %s, Object: %s, Element: %s, Pos: (%d,%d,%d)\n" % (doc,obj,sub, pos[0], pos[1], pos[2]))

    #def setPreselection(self,doc,obj,sub):
        #FreeCAD.Console.PrintMessage("Document: %s, Object: %s, Element: %s\n" % (doc,obj,sub))

class ViewObserver:
    def logPosition(self, info):
        down = (info["State"] == "DOWN")
        pos = info["Position"]
        if (down):
            FreeCAD.Console.PrintMessage("Clicked on position: ("+str(pos[0])+", "+str(pos[1])+")\n")
            #obs = SelectionObserver()
            #FreeCADGui.Selection.addObserver(obs)
        up = (info["Button"] == "BUTTON1")
        if (up):
            sel = FreeCADGui.Selection.getSelection()
            FreeCAD.Console.PrintMessage("Clicked on position: ("+str(len(sel))+")\n")

class ViewObserver2:
      def mouse_over_cb( event_callback):
          event = event_callback.getEvent()
          pos = event.getPosition().getValue()
          listObjects = FreeCADGui.activeDocument().activeView().getObjectsInfo((int(pos[0]),int(pos[1])))
          obj = []
          if listObjects:
              FreeCAD.Console.PrintMessage("\n *** Objects under mouse pointer ***")
              for o in listObjects:
                 label = str(o["Object"])
                 if not label in obj:
                    obj.append(label)
          FreeCAD.Console.PrintMessage("\n"+str(obj))
