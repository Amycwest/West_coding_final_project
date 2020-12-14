# West_coding_final_project

Amy West - amycwest7@gmail.com

Mark is a Program that can easily conduct the statistics for mark-recapture data. However, it can only read .inp files. The .inp file required by Mark is a text file that contains a single string of letters or numbers that act as dummy variables. The .inp files produced by this program contains rows something like this:

000000000ABCA0000000000000000000 1;

H0H00000000000000000000000000000 1;

0000D0E0F00000000000000000000000 1;

The purpose of this project is to examine the effect of weight on year-to-year survival in CLSW. As such, we want the elements in the .inp string representing the weight of each bird for each year of the study followed by a count of how many times that sequence appears in the data. The resulting file will contain strings of numbers representing each bird's weight at the time of capture and will be able to be opened in Mark.

This python script is designed to transform the data from the document CLSW_cut.txt into an INPUT (.inp) file for Mark. the file CLSW_cut.txt is required to run the script.

CLSW_cut.txt contains the weights of Cliff Swallows(CLSW) from 32 years of recapture studies as well as the age, band number, and year the bird was first captured. Each row also contains a string of numbers that could be used in an .inp file, but only represents captures of the bird with no information regarding the bird's weight.
  
The program first clears out unnecessary data: birds that were juveniles when first captured and birds for which we have no late-weight data. Late weight refers to the weight of birds when captured late in the season and is more likely to effect survival than weights taken early in the breeding season. Next the program turns the continuous late weight data into discrete variables, and merges the columns from each year into a single string. Finally, the strings are written to a .inp file.  

Github Repository contents:

Data file: CLSW_cut.txt.gz
	-File will need to be unnzipped using command 'gunzip CLSW_cut.txt.gz' on command line
	-Contains 35 columns and 216,477 rows
	-Opens in Excel (at the risk of slowing down your computer)
	-You can view it on the command line, but you should not
	-Jupyter notebook will not print the whole doc, but you can get an idea of what it looks like if you just print the first couple rows

Python script:  West_coding_final_python.py
	-Runs from the command line 
	-Runtime: 10-30 seconds

Jupyter notebook file: West_coding_final_jupyter_notebook.ipynb
	-Contains code with markdown and annotations
	-Opens in jupyter notebook

Mark Input file: recap.inp
	-What the resulting output file should look like
	-Opens in text editors and Program:Mark

Readme file: README_West_final.txt
	-README file
	-Opens in text editors
