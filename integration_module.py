import pyautocad
import pyrevit
import sketchup

def integrate_with_autocad(rendering):
    acad = pyautocad.Autocad()
    acad.doc.ActiveSpace.AddPolyline(rendering)

def integrate_with_revit(rendering):
    revit = pyrevit.Revit()
    revit.doc.Create.NewFamilyInstance(rendering)

def integrate_with_sketchup(rendering):
    sketchup = sketchup.Sketchup()
    sketchup.model.entities.add_group(rendering)
