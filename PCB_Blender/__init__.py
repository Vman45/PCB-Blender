# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "PCB-Blender",
    "author" : "Adam Makiewicz",
    "description" : "Addon for generating models of PCB from Gerber files",
    "blender" : (2, 80, 0),
    "version" : (0, 1, 4),
    "category" : "Generic",
    "location" : "Scene Properties > PCB Renderer"
}

import bpy
from . PCB_Blender_panel import PCB_LayoutPanel
from . PCB_Blender import PCB_Generate
classes = (PCB_LayoutPanel, PCB_Generate)
register, unregister = bpy.utils.register_classes_factory(classes)