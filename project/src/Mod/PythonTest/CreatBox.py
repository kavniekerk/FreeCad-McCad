#!/usr/bin/env python
# -*- coding: utf-8 -*-

import FreeCAD,FreeCADGui
import PythonTest_rc

from pivy import coin

class SaveBox:
       "My tool object"

       def GetResources(self):
               return {"MenuText": "Save box",
                       "Accel": "Ctrl+M",
                       "ToolTip": "My extraordinary command",
                       "Pixmap"  : ":/Save_Box"}

       def IsActive(self):
               if FreeCAD.ActiveDocument == None:
                       return False
               else:
                       return True

       def Activated(self):
           import Part
           shapes=[]

           sel = FreeCADGui.Selection.getSelection()
           objs = FreeCAD.ActiveDocument.Objects
           if len(sel) == 0:
               for obj in objs:
                   if (obj.ViewObject.Visibility == True ):
                       shapes.append(obj)
           else:
               for obj in sel:
                   shapes.append(obj)

           Part.export(shapes,"2610172.stp")
           #for obj in FreeCAD.ActiveDocument.Objects:
               #obj.Shape.exportStep("261017.stp")
               #__objs__.append(obj)


class CreateBox:
      "My tool object"

      def GetResources(self):
              return {"MenuText": "My Command",
                      "Accel": "Ctrl+M",
                      "ToolTip": "My extraordinary command",
                      "Pixmap"  : ":/Create_Box"}

      def IsActive(self):
               if FreeCAD.ActiveDocument == None:
                       return False
               else:
                       return True      

      def Activated(self):
          import Part
          doc = FreeCAD.activeDocument()

          length = 10
          width  = 20
          hight  = 40
          box = Part.makeBox(length,width,hight)

          shapeobj = doc.addObject("Part::Feature","MyShape")
          shapeobj.Shape = box

          doc.recompute()
          FreeCADGui.SendMsgToActiveView("ViewFit")

          import Observer
          #obs=Observer.SelectionObserver()
          #FreeCADGui.Selection.addObserver(obs)

          v = FreeCADGui.activeDocument().activeView()
          o = Observer.ViewObserver()
          c = v.addEventCallback("SoMouseButtonEvent",o.logPosition)
          #mouse_over = v.addEventCallbackPivy( coin.SoLocation2Event.getClassTypeId(), o.mouse_over_cb )

FreeCADGui.addCommand('MyCommand1',SaveBox())
FreeCADGui.addCommand('MyCommand2',CreateBox())
