import os
import pprint
import rhinoscriptsyntax as rs


def explode_blocks():
    # Explode object instances
    objs = rs.AllObjects()
    for obj in objs:
        try:
            rs.ExplodeBlockInstance(obj, explode_nested_instances=False)
        except:
            pass

# Gets Rhino file-list
cwd = os.getcwd()
print("CWD: " + cwd)

file_list = []
for root, dirs, files in os.walk(cwd):
    for file in files:
        if file.endswith(".3dm"):
             file_list.append(os.path.join(root, file))
pprint.pprint(file_list)

for file in file_list:
    # Open .3dm file
    rs.Command('_-Open ' + file)

    explode_blocks()

    path = rs.DocumentPath()  # C:\foo\
    name = rs.DocumentName()  # 001.3dm
    filename, file_extension = os.path.splitext(name) # 001, 3dm
    fbx = filename + ".fbx"  # 001.fbx
    save_path = os.path.join(path, filename)  # C:\foo\001\
    save_name = os.path.join(path, filename, name)  # C:\foo\001\001.3dm
    fbx_name = os.path.join(path, filename, fbx)  # C:\foo\001\001.fbx

    # Make new folder
    try:
        os.makedirs(save_path)
    except OSError:
        pass

    # Export .fbx file
    rs.AllObjects(bool) #selects all geometry
    command = "-_Export {} Enter Enter".format(fbx_name)
    rs.Command(command, True)

    # Save .3dm file
    command = "-_SaveAs {} Scheme Default Enter".format(save_name)
    rs.Command(command, True)
    
    print(save_name + " - completed!")

print("Success!")


