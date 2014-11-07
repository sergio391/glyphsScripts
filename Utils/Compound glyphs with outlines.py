#MenuTitle: Compound glyphs with outlines
# -*- coding: utf-8 -*-
__doc__="""
Based con mekablue's "New Edit tab with compound glyphs". Opens a new Edit tab with all glyphs which contain the currently selected glyphs as a component and also have outlines
"""

import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font
FontMaster = Font.selectedFontMaster
selectedLayers = Font.selectedLayers

editString = ""
Output = ""

for thisLayer in selectedLayers:
	thisGlyphName = thisLayer.parent.name
	compoundList = [ g.name for g in Font.glyphs if thisGlyphName in [ c.componentName for c in g.layers[ FontMaster.id ].components ] and len(g.layers[ FontMaster.id ].paths) > 0 ]
	if len(compoundList) > 1 :
		Output += "Compounds with %s: " % thisGlyphName + " ".join( compoundList ) + "\n"
		editString += "\n/" + thisGlyphName + "/space/" + "/".join( compoundList )
	else :
		Output += "No compound glyphs with %s and outlines" % thisGlyphName + "\n"

editString = editString.lstrip()
print Output

Doc.windowController().performSelectorOnMainThread_withObject_waitUntilDone_( "addTabWithString:", editString, True )