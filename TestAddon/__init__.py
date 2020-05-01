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
    "name" : "AddonName",
    "author" : "Adam Makiewicz",
    "description" : "test description",
    "blender" : (2, 82, 0),
    "version" : (0, 0, 3),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from . test_panel import LayoutDemoPanel
from . Test import GeneratePCB
import addon_utils
addon_utils.enable("io_import_images_as_planes", default_set = True, persistent = True)
classes = (LayoutDemoPanel, GeneratePCB)

register, unregister = bpy.utils.register_classes_factory(classes)