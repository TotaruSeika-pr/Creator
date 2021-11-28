# Creator 1.0.1.0 / Documentation
###### *I apologize in advance for any possible incorrect translation. I ask you to interpret the text as accurately and clearly as possible.*


**Creator** - Creator is a spammer program that creates a large number of files. It can be useful for checking long-term storage media for writing, storing, deleting data, as well as checking the security of the OS for spam attacks.

The program receives keys, which we will now analyze

## -p || --path `-p [PATH]`

Required argument that takes the path to the folder where the files will be written. The path can be either full *(C: \\ projects \\ Creator \\ test)* or to the following folder *(test \\)*. If the path is incorrect, it will be written in the console (*"Invalid path specified!"*)

### Example:

`-p C:\projects\Creator\test_dir`

##### The files are created in a folder located in the utility folder. Enter the folder path carefully. Otherwise, you can clog up the folders you need.

## -os || --operating-system `-os [Linux, Win]`

Required argument that takes a specific operating system value. In this version, these are: **"Win"** or **"Linux"**. Different separators (*"/" or "\\"*) are used for the OS. If you enter incorrectly, you will be asked to run the utility with the -h switch, which displays a list of available switches `./Creator.py -h`

### Example:

`$ ./Creator.py -p test -os Linux`

##### If you run the utility on a **Linux** distribution and the path is correct, then the program will work. If you want to use this utility on an android device, then in this parameter, select Linux, since their file system is similar. And in general, Android and Linux are almost the same thing.

## -DocN || --document-name `-DocN [NAME]`

Optional argument. Accepts text, which is the new filename (not counting its number). If not used, the file name will be **"doc"** + *number*

### Example:

`$ ./Creator.py -p test -os Linux -DocN new_file`

##### Specify the name of the file, not its type!

## -DocT || --document-type `-DocT [FILE_TYPE]`

Optional argument. Accepts text, which is a dotted file type. Attaches to the file itself. If not used, the type will be **.txt**

### Example:

`$ ./Creator.py -p test -os Linux -DocT .py`

##### Enter the types correctly in terms of both syntax and data storage. You can't enter a string into the table, can you?

## -r || --range `-r [INT1 INT2]`

Optional argument. The arguments are two numbers, and the first must be greater than the second. The numbers represent the range of numbers for the ultimate file name generation. To avoid exclusion when the file name is repeated, such unique numbers are used.

### Example:

`$ ./Creator.py -p test -os Linux --range 0 100000000`

##### The larger the range you specify, the more files the program can create.

## -ctf || --copy-text-file `-ctf [PATH]`

Optional argument. Takes the path of the file, the text of which will be copied

### Example:

```
$ ./Creator.py -p test -os Linux -cf copy_file.png
```

##### Make sure that the text in the file is adequate and appropriate for you.

## -cf || --copy-file `-cf [PATH]`

Optional argument. Accepts the path to the file to be copied.

### Example:

```
$ ./Creator.py -p test -os Linux -cf copy_file.png
```

##### Note the `-ctf` and` -cf`. `-ctf` only copies the contents of the file when` -ctf` copies the file itself.

## -q || --quantity

Optional argument. Takes one number. The number is the number of files to create. If all files are created, the job ends. If no argument is specified, it will create files indefinitely.



`$ ./Creator.py -p test -os Linux -q 1000`

##### In this case, the utility will create 1000 files and exit.

## -d || --delay `-d [FLOAT]`

Optional argument. Accepts a floating point value. Delay between file creation.

### Example:

`$ ./Creator.py -p test -os Linux -d 2.5`

##### In this case, the program creates one file every 2.5 seconds.

## -t || --text `-t [TEXT]`

Optional argument. Accepts text to be written to files.

### Example:

`$ ./Creator.py -p test -os Linux -t Thanks to Create for the job!`

##### This function is useful if you need to write short text. If you want to write large texts, then write it to a file and use `-cf`

## -a || --about

Argument for getting information. Used to get information about the project and its author.

##### Unfortunately, the key does not work without required arguments. Therefore, we raise an error for the key to work :)

`$ ./Creator.py -p text -os Mac -a`

### Author's comment:

Thanks for using my utility! I hope you enjoy it. If you are active (leave reviews, put stars on the repository, tell others about it), then I will actively engage in this project! I have tons of ideas that I will add as you get active.

#### I'm on social networks

- [Twitter](https://twitter.com/TotaruS)
- [GitHub](https://github.com/TotaruSeika-pr)

###### Where is the donate link? The point is, I think this is wrong. I can't ask for money for a crude project. Perhaps, if the project begins to gain recognition little by little, then I can understand that people really like the project. And in this case, you can get a small reward from those who want to help.
