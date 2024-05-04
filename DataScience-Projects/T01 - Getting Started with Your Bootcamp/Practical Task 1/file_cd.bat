@echo off
rem Create three new folders
mkdir "folder1"
mkdir "folder2"
mkdir "folder3"

rem Navigate inside "folder1" and create three new subfolders
cd "folder1"
mkdir "subfolder1"
mkdir "subfolder2"
mkdir "subfolder3"

rem Remove "subfolder2" and "subfolder3" from "folder1"
rmdir /s /q "subfolder2"
rmdir /s /q "subfolder3"

rem Navigate back to the parent folder
cd ..
