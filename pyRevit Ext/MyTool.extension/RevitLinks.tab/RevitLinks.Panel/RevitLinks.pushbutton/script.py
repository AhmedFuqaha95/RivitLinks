"""Toggles visibility of RevitLinks categories on current view."""

from pyrevit import revit


@revit.carryout('Toggle RevitLinks')
def toggle_RevitLinks():
    aview = revit.active_view
    aview.AreRevitLinksHidden = \
        not aview.AreRevitLinksHidden


toggle_RevitLinks()
