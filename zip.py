from pathlib import Path
import os

names = [
    ["simplified-water-polygons-split-3857", "simplified_water_polygons", "p"],
    ["water-polygons-split-3857", "water_polygons", "p"],
    ["antarctica-icesheet-polygons-3857", "icesheet_polygons", "p"],
    ["antarctica-icesheet-outlines-3857", "icesheet_outlines", "l"],
    ["", "ne_110m_admin_0_boundary_lines_land", "l"]
]

for name in names:
    path = name[0] if name[0] else name[1]
    Path(path).mkdir(parents=True, exist_ok=True)
    for ext in ['cpg', 'dbf', 'prj', 'shp', 'shx']:
        os.system(f'cp empty{"" if name[2]=="p" else "-lines"}.{ext} {path}/{name[1]}.{ext}')
    os.system(f'zip -r{"" if name[0] else " -j"} {path}.zip {path}')