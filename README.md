##File Zipper

This is a command-line application built using Python and Click. It makes available to the user two commands, `zip` and `unzip`, to create an archive of an arbitrary number of files and to extract files from an archive respectively.

The user has options such as saving the archive/extracted files to any directory of their choice, giving the archive a specific name, selecting a compression method, etc. The user can also use the `verbose` optional to get a progress bar of the operation being performed. 

Four modules have been used: 
* `click`
* `zipfile`
* `os`
* `progressbar2`

##**Installing the commands**

Before these can be used in the command line, they need to be installed to your current environment. To do this, in your terminal, navigate to the directory where the files have been saved and type the following command:

`pip install --editable .`

##**Using the commands**

The help text for the `zip` command:

![zip-help](/images/zip-help.png)

The help text for the `unzip` command:

![unzip-help](/images/unzip-help.png)

###Using `zip`

By default, the `zip` command saves a new archive to the cwd under the name, 'my-zipfile.zip' and uses the `ZIP_STORED` compression available in the `zipfile` module. 

To create an archive in the cwd of files, `file1.txt` and `file2.txt`:

`zip file1.txt file2.txt`

To create an archive in `directory` of the same files:

`zip -d directory file1.txt file2.txt`

To create an archive named, `archive.zip` in `directory` of the same files:

`zip -d directory -n archive.zip file1.txt file2.txt`

To change the compression used to `compression`:

`zip -d directory -n archive.zip -c compression file1.txt file2.txt`

To get a progress bar of any operation:

`zip -v <other options>`

###Using `unzip`

To extract all the files to the cwd from an archive named, `archive.zip` present in the cwd:

`unzip archive.zip`

To extract files, `file1.txt` and `file2.txt`, present in the archive to the cwd:

`unzip archive.zip file1.txt file2.txt`

To extract all the files to some other directory, `directory`:

`unzip -d directory archive.zip`

To extract specific files to some other directory:

`unzip -d directory archive.zip file1.txt file2.txt`

To get more details about the operation:

`unzip -v <other options>`