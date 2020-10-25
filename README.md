# Rhino-Batch-Processor
Loop-walks trough directories, opening rhino files, removing instances, saving and exporting it to FBX.

For Rhino 6 (Win)

# Usage
- open new Rhino scene (cm)
- Rhino Python Editor
- ctrl + O,  then choose Script
- script must be at the same location as Rhino files, or you can edit CWD variable to point to Rhino files directory
- to start Debugging press [F5]

# Output
```
/file_name/file_name.3dm  # 3dm with exploded instances
/file_name/file_name.fbx
```
