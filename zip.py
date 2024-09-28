from pathlib import Path
import os

names = [
    ["simplified-water-polygons-split-3857", "simplified_water_polygons"],
    ["water-polygons-split-3857", "water_polygons"],
    ["antarctica-icesheet-polygons-3857", "icesheet_polygons"],
    ["antarctica-icesheet-outlines-3857", "icesheet_outlines"],
    ["", "ne_110m_admin_0_boundary_lines_land"]
]

for name in names:
    path = name[0] if name[0] else name[1]
    Path(path).mkdir(parents=True, exist_ok=True)
    for ext in ['cpg', 'dbf', 'prj', 'shp', 'shx']:
        os.system(f'cp empty.{ext} {path}/{name[1]}.{ext}')
    os.system(f'zip -r{"" if name[0] else " -j"} {name[1]}.zip {path}')