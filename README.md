# How to use this script

## Install Python:

Windows 10

https://www.python.org/downloads/

MacOS X

https://www.python.org/downloads/mac-osx/

## Open a terminal:

Check that Python is installed correctly

Windows 10

1. Press "Windows Key"
2. Type "PowerShell"
3. Select "Windows PowerShell" App
4. At the prompt, type:

    `python --version`

    Output should be something like `Python 3.8.5`

MacOS X

1. Open "Terminal" App
2. At the prompt, type:

    `python --version`

    Output should be something like `Python 3.8.5`

## Download .zip file with lab report submissions

Extract the folder wherever you want. I would also rename it to something simpler,
like 'Tue_Exp15-Alum' or something.

Copy the `rename.py` file into the same directory as your extracted file.

Open the `rename.py` file and edit the variables as-needed:

```python
...
# VARIABLES (EDIT ME!)
REPORT_FOLDER='./Tue_Exp15-Alum'  # this is the name of the root folder that contains all submission folders
GRADED_FOLDER='./graded/'         # change this if you want to specify a different output folder
EXP_NUM = '15-alum'               # change this to the current experiment number
```

Open a new PowerShell or Terminal in this folder.

In Windows 10, you can just type `powershell` into the address bar of File Explorer.

<img src="https://media.giphy.com/media/IdBwW0P6st1naXZSbV/giphy.gif" height="300" />

Once you are sure the variables have been named correctly, run the python file from the terminal.

```bash
> python rename.py
```

If working correctly, you should see output like:

```
Writing ./graded/....
Success!
...
```

Check that the PDFs in the "graded" folder have been successfully renamed.
