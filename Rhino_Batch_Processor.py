import os
import pprint
import rhinoscriptsyntax as rs


def explode_blocks():
    # explode object instances
    objs = rs.AllObjects()
    for obj in objs:
        # print "Object identifier: ", obj
        try:
            rs.ExplodeBlockInstance(obj, explode_nested_instances=False)
        except:
            pass

# gets rhino file list
cwd = os.getcwd()
print "CWD: " + cwd 

file_list = []
for root, dirs, files in os.walk(cwd):
    for file in files:
        if file.endswith(".3dm"):
             # print(os.path.join(root, file))
             file_list.append(os.path.join(root, file))
pprint.pprint(file_list)

for file in file_list:
    # opens 3dm file
    rs.Command('_-Open ' + file)

    # INSERT YOUR LOGIC FROM HERE
    explode_blocks()

    path = rs.DocumentPath() # D:\Shurik_Test\
    name = rs.DocumentName() # 001.3dm
    filename, file_extension = os.path.splitext(name) # 001, 3dm
    fbx = filename + ".fbx" # 001.fbx
    save_path = os.path.join(path, filename) # D:\Shurik_Test\001\
    save_name = os.path.join(path, filename, name) # D:\Shurik_Test\001\001.3dm
    fbx_name = os.path.join(path, filename, fbx) # D:\Shurik_Test\001\001.fbx

    # makes new folder
    try:
        os.makedirs(save_path)
    except OSError:
        pass

    # exports fbx file
    rs.AllObjects(bool) #selects all geometry
    command = "-_Export {} Enter Enter".format(fbx_name)
    rs.Command(command, True)

    # saves 3dm file
    command = "-_SaveAs {} Scheme Default Enter".format(save_name)
    rs.Command(command, True)
    
    print save_name + " - done!"

print "Success! Process completed."


