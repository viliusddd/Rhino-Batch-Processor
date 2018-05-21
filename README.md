# Rhino-Batch-Processor
Loops Walks trough directories opening rhino file, removing instances, saving and exporting to FBX.

Used on Rhino 6 (Win)
# Usage
- Open new Rhino scene (cm);
- Rhino Python Editor;
- Ctrl + O -> Choose Script;
- Script must be in with the rhino files,
  or you can edit cwd variable to point to rhino files directory;
- Start Debugging [F5];
- Thats it!
# Output
	/file_name/file_name.3dm -> 3dm su exploded instances
	/file_name/file_name.fbx
