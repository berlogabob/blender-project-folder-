# import zone
import os
import pathlib
#
# def zone
#
#
# script zone
#
# path of this script
project_name = input("Enter filename: ")
directory = ""
# files to create:
ext_png = ".png"
ext_svg = ".svg"
folder_list = ["ref", "textures", "render"]

file_list = ["000.blend"]

file_list_ref = ["ref.000"+ext_png, "ref.side.000" +
                 ext_png, "ref.front.000"+ext_png, "ref.iso.000"+ext_png]

file_list_render = ["render.000.000"+ext_png, "render.000.999"+ext_png]
file_list_textures = ["UV.part.000" + ext_svg, "UV.part.000" +
                      ext_png, "material.part.000"+ext_png, "textures.part.000"+ext_png]

# get fileName from user
filepath = directory + project_name
filepath_ref = filepath + "ref"
pathlib.Path.mkdir(project_name)
# create common folders
for folders in folder_list:
    project_name = project_name
    full_folders = project_name+"."+folders
    pathlib.Path.mkdir(project_name+"/"+full_folders)

# create files in folders

# create main blend file in project folder
s = "/" + project_name
for i in file_list:
    file_new = (s + "." + i)
    # To create a file
    pathlib.Path(filepath+file_new).touch()

# create files in common folders
# in ref folder
for i in file_list_ref:
    file_new = (s + "." + i)
    # To create a file
    pathlib.Path(filepath + "/" + project_name+"."+"ref" + file_new).touch()


# in textures folder
for i in file_list_textures:
    file_new = (s + "." + i)
    # To create a file
    pathlib.Path(filepath + "/" + project_name +
                 "."+"textures" + file_new).touch()

# in render folder
for i in file_list_render:
    file_new = (s + "." + i)
    # To create a file
    pathlib.Path(filepath + "/" + project_name +
                 "." + "render" + file_new).touch()


# print(input("press any key"))
