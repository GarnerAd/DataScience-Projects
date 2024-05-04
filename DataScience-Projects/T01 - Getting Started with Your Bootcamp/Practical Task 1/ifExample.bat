@echo off
rem Check if the folder named "new_folder" exists
if exist "new_folder\" (
    rem If it exists, create a new folder called "if_folder"
    mkdir "if_folder"
) else (
    rem If it doesn't exist, create a new folder called "new-projects"
    mkdir "new-projects"
)

rem Check if the folder named "if_folder" exists
if exist "if_folder\" (
    rem If it exists, create a new folder called "hyperionDev"
    mkdir "hyperionDev"
) else (
    rem If it doesn't exist, create a new folder called "new-projects"
    mkdir "new-projects"
)
