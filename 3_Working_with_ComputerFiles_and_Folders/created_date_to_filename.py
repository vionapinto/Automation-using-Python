""" Files are:
Pathlib_Library-new-abc.txt
Pathlib_Library-new-def.txt
Pathlib_Library-new-ghi.txt
"""

from pathlib import Path
from datetime import datetime

root_dir = Path('Pathlib_Library')

for path in root_dir.glob("**/*"):
  if path.is_file():
    created_date = datetime.fromtimestamp(path.stat().st_ctime)
    created_date_str = created_date.strftime("%Y-%m-%d_%H:%M:%S")
    new_filename = created_date_str + '_' + path.name
    print(new_filename)
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)

"""
Files are now renamed to :
2023-05-30_23:00:01_2023-05-30_22:56:42_Pathlib_Library-new-abc.txt
2023-05-30_23:00:01_2023-05-30_22:56:42_Pathlib_Library-new-def.txt
2023-05-30_23:00:01_2023-05-30_22:56:42_Pathlib_Library-new-ghi.txt
"""