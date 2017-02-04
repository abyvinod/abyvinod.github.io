title: Create bookmarks when including pdfs using pdflatex
Date:2017-01-20
tags: Latex, Python
category: How To
author: Abraham Vinod
summary: Python code to create bookmarks for latex

This is the README file from my [Bitbucket
repository](https://bitbucket.org/abyvinod/createbookmarkincludepdf) for the
code. Do check it out!

## Problem ##
Extract bookmarks from a pdf that has to be included as is into another pdf
created using pdflatex. Includepdf package ignores pdf annotations.

## Solution ##
Use pdftk to fetch the annotations, python to parse through these annotations,
and bookmark package to feed it back to pdflatex.

## How do I get set up? ##

* Tested on Python 3.5 and TexLive 2015 with bookmark package installed
* Requires:
	* re, os, subprocess
	* pdftk

## How do I run the code? ##

* Copy the python script into the folder where the parent tex file resides.
* Edit three variables:
    * filename --- Relative path from the parent tex file to the pdf to be
      included (without the .pdf extension)
    * parentLevel --- Bookmark level at which the pdf is to be included
    * createBookmarkForWholePDF --- Flag for setting a bookmark to the
      to-be-included pdf
* Run the script
```python createBookmarkIncludePdf.py```
* The script creates in the folder where the to-be-included-pdf resides two
  files:
    * filename_Pdfannot.txt --- Annotations as given by the pdftk software
    * filename_TexCommands.tex --- Tex commands that is to be included into the
      parent tex file

## Who do I talk to? ##

* Abraham Vinod (aby[dot]vinod[at]gmail[dot]com)
