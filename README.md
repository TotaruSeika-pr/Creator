# Creator

###### *I apologize in advance for any possible incorrect translation. I ask you to interpret the text as accurately and clearly as possible.*


Creator - is a utility that allows you to check hard drives for writing and deleting data.

The program receives keys, which we will now analyze

## -p || --path

Required argument that takes the path to the folder where the files will be written. The path can be either full *(C: \\ projects \\ Creator \\ test)* or to the following folder *(test \\)*. If the path is incorrect, it will be written in the console (*"Invalid path specified!"*)

### Example:

`-p C:\projects\Creator\test_dir`

##### The files are created in a folder located in the utility folder. Enter the folder path carefully. Otherwise, you can clog up the folders you need.

## -os || --operating-system

Required argument that takes a specific operating system value. In this version, these are: **"Win"** or **"Linux"**. Different separators (*"/" or "\\"*) are used for the OS. If you enter incorrectly, you will be asked to run the utility with the -h switch, which displays a list of available switches `./Creator.py -h`

### Example:

`./Creator.py -p test -os Linux`

##### If you run the utility on a **Linux** distribution and the path is correct, then the program will work

## -DocN || --document-name

Optional argument. Accepts text, which is the new filename (not counting its number). If not used, the file name will be **"doc"** + *number*

### Example:

`./Creator.py -p test -os Linux -DocN new_file`

##### Specify the name of the file, not its type!

## -DocT || --document-type

Optional argument. Accepts text, which is a dotted file type. Attaches to the file itself. If not used, the type will be **.txt**

### Example:

`./Creator.py -p test -os Linux -DocT .py`

##### Enter the types correctly in terms of both syntax and data storage. You can't enter a string into the table, can you?

