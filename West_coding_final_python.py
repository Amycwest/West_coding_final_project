#!/usr/bin/env python
# coding: utf-8

# # Part 1: 
# ## Make a file Python can read

# Python does not know how to read files, we have to tell it how to do it

# In[2]:


#### Open CLSW_cut.txt file ####

# Provide file name
filename='CLSW_cut.txt'

# Open file and make each line an element in a list
with open (filename) as file_object:
    CLSW_cut=file_object.readlines()


# In[3]:


#### Make CLSW_cut into a nested list ####

## Make a list of empty lists: 
    #This prevents us from having to append 30+ rows of data individually

# Make an empty nest to put the empty lists in
CLSW_cut_nest=[] 

# Create a variable that counts the number of rows we need
    # Python is currently reading each row as a single string, so we can't count the number of rows
       # Instead we count the number of tabs in the first string and then add 1
n = (CLSW_cut[0].count('\t'))+1  

# Add all the empty lists to the empty list
for i in range(n): # Loop through the 'n' count
    CLSW_cut_nest.append([]) # Add an empty list for every row in the dataset

    
## Divide each row into a separate list and append to the nest
 
# Fill the empty nest
for row in CLSW_cut: # Loop through each row in CLSW_cut 
    counter=0 # Make a counter: it has to be in the loop so it resets for each row
    if counter < 36: # DO NOT continue this loop when we run out of rows 
        stripped_CLSW=row.rstrip() # Take out extra characters
        split_CLSW=stripped_CLSW.split('\t') # Split the cells along the tab key
        for num in CLSW_cut_nest: # Loop through each empty list 
            num.append(split_CLSW[counter]) # Add that string we split
            counter=counter+1 # Increase the counter so the next element can be added


# # Part 2:
# ## Remove baby birds

# The question we're trying to answer is about weight, and baby birds (J=juvenile) do not weigh the same as adult birds, so we need to remove them from the dataset.

# In[4]:


### Remove juvenile birds ###

#A count of the rows we need, but now, we can use the len command
rows=len(CLSW_cut_nest[0]) 

# Create an empty_list
no_J=[] 

# Put all the adult birds into the new list
for x in range (0,rows): # Loop through each row of the nest
    if CLSW_cut_nest[0][x] != 'J': # If the first row does not contain a J...
        for y in range (0,n): #(loop through columns)
            no_J.append(CLSW_cut_nest[y][x]) #... append the whole row to the no_J list


# In[5]:


### Turn the data back into a nest ###

## Note: this is a bit different than in part 1. 
    # Before all our elements weren't separated. Now they are but they aren't in rows, 
    # Concept is the same but the code's a bit different

# Make an empty list
no_J_nest=[]

# Create a list of empty lists
n2 = int((len(no_J))/(n)) # Calculate the number of rows we need in the list, 
                                # Because we did math we end up with a float(ing integer), which don't work in range lists
                                # Change it into an integer using int

for i in range(0,n2): # Fill the empty list with empty lists
    no_J_nest.append([])

## Put No_J into nested list 

# Make a counter
counter=0 

# Append each line of the no_J data
for g in no_J_nest: # Loop through each line of our nest
    if (counter+n) > (len(no_J)):  # Create a condition with some math
            break  # End the loop 
    for y in range (counter,counter+n): #Loop through each element
        g.append(no_J[y]) #Append each element to a row of the nest
    counter=counter+n #Increase the counter

    
#Note the output of this nest is actually flipped from the previous nest we made; this doesn't matter 


# # Part 3:
# ## Remove NA's

# We are trying to answer a question about year to year survival.  What a bird weighs at the beginning of the season is irrelevant to this question and could scew the data.  If we have no Late Weight data, we don't need that bird.  However, we have 32 years to sort though.  We need to look at the Late Weight measurements for each year, so only if all 32 cells have NA's can we eliminate the bird from the data set.

# In[6]:


### Remove the NA's ### 

# Make an empty list
no_NA=[]

# Put rows with all NA's for Late Weights into new list
for rows in no_J_nest: # Loop through each row in our old nest
    if any (rows[x] != 'NA' for x in range (4,36)): # Fulfill multiple conditions with if any command and reverse search
                                                        # Rows 4-35 contain the Late Weights 
        no_NA.append(rows) # Add the rows that fulfill requirement to new list


# # Part 4: 
# ## Weight Categories

# Program mark cannot read continus variables, so we are making them all discrete, by changing our weight measurements into letters.  Weight categories are based on standard deviation from the mean.

# In[7]:


### Put first four rows into separate list ### 

# Make a new list
pop_catch=[]

# Use pop fuunction to remove the rows and put them somewhere else
for x in no_NA: # Loop through each row in no_NA nest
    for counter in range (0,4): # For each of the first four rows
        popcorn=x.pop(0) # Remove the elment and make it a variable called popcorn (lol)
        pop_catch.append(popcorn) # Put the popcorn into the pop_catch list 


# In[8]:


### Make pop-catch into a nest so it can be indexed into later ###

# Change pop_catch into nested list 
pop_catch_nest=[]

# Create a nest of empty lists

n2 =int(len(pop_catch)/4)

for i in range(0,n2):
    pop_catch_nest.append([])

# Create a counter
counter=0

# Append pop_catch to the new list
for g in pop_catch_nest: # For each row in the empty nest
    if (counter+4) > len((pop_catch)): # Do not continue this loop when you get to the end of the list
        break
    for y in range (counter,counter+4): # Loop through the first four elements
        g.append(pop_catch[y]) # Append to a nest
    counter=counter+4 # Increase the counter to the next four elements


# In[9]:


### Make nested list into a list ###
flatList = [item for elem in no_NA for item in elem]


# In[10]:


### Make all the numbers readable ###

# As it stands all the numbers are being read as a mix of strings, integers, and floats, we need them all to be strings with a float format

# Make a new list
flatList_float=[]

# Turn all the numbers into floats
for line in flatList: # Loop through each line in our list
    if line >= '13' and line <= '34': # If the element is a number in this range (the weight range for CLSW's)...
        floating=float(line) # ...turn the number into a float
        flatList_float.append(floating) # Put the float in our new list
    else: # If the element is not a CLSW weight... 
        flatList_float.append(line) # ...Just leave it as is and add it to the new list

# Now that we have your decimals turn your floating integers back into strings because python refuses to replace numbers with letters 
flatList_string=[] # Make a new list
for line in flatList_float: # Loop through the list
        floating=str(line) # Turn everything into a string
        flatList_string.append(floating) # Add it to the new list
   


# In[11]:


### Replace all the weights with discrete variables ###

# Make a new list
inp_con=[]

# Change numbers into letters#
for line in flatList_string: # Loop through each line in the string
    if line == 'NA': # Replace remaining NA's with 0's
        inp_con.append(0)
    elif line >= '14.0' and line <= '19.0': # Replace each weight range with a different letter
        inp_con.append('A')
    elif line >= '19.1' and line <= '20.6': 
        inp_con.append('B')
    elif line >= '20.7' and line <= '21.9':
        inp_con.append('C')
    elif line == '22.0':
        inp_con.append('D')
    elif line >= '22.1' and line <= '23.7':
        inp_con.append('E')
    elif line >= '23.8' and line <= '25.4':
        inp_con.append('F')
    elif line >= '25.5' and line <= '27.0':
        inp_con.append('G')
    elif line >= '27.1' and line <= '33.5':
        inp_con.append('H')
    else: # if the line is not a CLSW weight or an NA just leave it as is
        inp_con.append(line)
        


# In[12]:


### Change back into a nested list ###

# Make an empty list
inp_con_nest=[] 

# Create a list of empty lists
n2 =len(no_NA) # Number of lines in our last nested list 
n3 =n-4 # Number of rows except that we popped the first 4 

# Add empty lists to empty nest
for i in range(0,n2):
    inp_con_nest.append([]) 

# Make a counter
counter=0 

# Append data to empty nest
for g in inp_con_nest: # Loop through each row in the nest
    if (counter+n3) > (len(inp_con)): # Once the counter reaches the last row stop
           break
    for y in range (counter,counter+n3): # For elements in range 0-36 for example...
        g.append(inp_con[y]) # ...add elements to the row in the nest
    counter=counter+n3 # Increase the counter to go to the next set of numbers


# # Part 5: 
# ## Make a single string of Late Weights

# .inp files are just a string of numbers separated by semicolons, so we need to get rid of all the extra stuff

# In[13]:


### Merge all weight data into single string ###

# Create an empty list
inp_strings=[] 

# Merge elements and add them to a new list
for line in inp_con_nest: # For each line of the nest
    inp_string=' '.join([str(elem) for elem in line]) # Collaspe elements in each row into a string
    no_space=inp_string.replace(" ","" ) # Take out extra spaces in the file
    inp_strings.append(no_space) # Add merged and spaceless string to a list


# # Part 6:
# ## Fill in some 1's

# We caught birds. Sometimes we caught a bird late in the season (so we have a Late Weight), and sometimes we caught that bird again, but not late in the year.  We want Mark to know that those birds were recaught but don't want Mark to consider the weight.  Thus, these birds get their own code (a '1'), but they are currently coded as 0's (meaning we didn't catch the bird).
# Previously, someone also working with this dataset, made an .inp looking at just bird survival (a string of 1's and 0's that tell us nothing about the birds other than whether or not they were captured).  They then left these strings in the CLSW_cut.txt file we're working from, and we're going to take advantage of it. These .inp strings are referred to as the ch number.

# Example of filling in the 1's
# 
# Ch number:    ['10100000000000000000000000000000', '01100000000000000000000000000000']
# 
# inp_strings:  ['00E00000000000000000000000000000', '0FD00000000000000000000000000000']
# 
# final product:['10E00000000000000000000000000000', '0FD00000000000000000000000000000']
# 
# In the first column the first number in the string gets replaced because the bird was captured without collecting late weight data.    
# 
# The second string remains the same beause whenever bird was captured there was a late weight.  

# In[14]:


### Just grab the Ch numbers ###

ch_nums=[] # Make an empty list

for line in pop_catch_nest: # Append each of the ch numbers from pop_catch to ch_nums
     ch_nums.append(line[3])


# In[15]:


### Remove headers as we don't need them for this, or the final product ###
ch_nums.pop(0)
inp_strings.pop(0)


# In[16]:


### Fill in the 1's and put them in a new list ###

# Create some empty lists
recap=[]
recap_string=[]

# Fill in 1's and add a merged string to new list
for g in range (0, len(inp_strings)): # Give some ranges to index into in this case the rows for each of our two lists 
    for x in range (0,n3): # This is the number of columns
        if ch_nums[g][x] == '1' and inp_strings[g][x] == '0': # If the ch_num is a 1 and the inp_string is a 0... 
            recap.append('1') # ...append a 1 to the list 
        else: # If not...
            recap.append(inp_strings[g][x]) # ...append the inp_string element
    inp_string=''.join(recap) # Merge the appended numbers
    recap_string.append(inp_string) # Add the appended number to a new list
    recap=[] # Clear out the first list for the next loop


# # Part 7:
# ## Add some counts and semicolons

# We have all our strings! Now for Mark to read the strings, we need to add a little blip to each string that says how many times the string appears and then put a semicolon so Mark knows it's a different bird.  We could count each time a sequence appears and put that on the end, but for data with more than 0's and 1's such as this, Mark wants to read each one at a time, so we'll just put ' 1;' on the end of each.

# In[17]:


### Turning into nest ###
  
# Create an empty file
recap_nest=[] 

# Create a nest of empty lists
n4 =int(len(recap_string)) # Want the same number of rows as recap_string

for i in range(0,n4):
    recap_nest.append([]) # Add empty lists

#Fill the empty lists
for y in range (0,n4): 
    recap_nest[y].append(recap_string[y]) # Put each of the strings into a nest


# In[18]:


### Add ' 1;' to each line ###
for line in recap_nest: # For each row in the nest 
    line.append(' 1 ;')  # The space is necessary for the file to be read, semicolon indicates new bird


# In[19]:


### Turn nest into a list

# Make an empty list
recap_string_count=[] 

# Collaspe nest into a list
for line in recap_nest: # Loop through each row in the nest
    inp_string=''.join(line) # Collaspe each line
    recap_string_count.append(inp_string) # Append each line to a string


# # Part 8:
# ## Export the file

# OMG We did it! Now, we just have to export our work. File can be opened with textedit (and presumably other text editors), viewed on the terminal command (though use head or less commands), and most importantly Mark!

# In[20]:


### Create file and add data to it ###
with open("recap.inp", "w") as file: #Create a file, name and open it so we can write data to it
    for line in recap_string_count: #Loop through each line
        file.write(f'{line}\n') #Add each list element to file.  
                                #We don't need the new line but it makes it look nicer
    


# In[21]:


print("\nYou have sucessfully created an .inp file! File is located in working directory as (recap.inp) and is ready to run in Mark\n\nThank you for using my program\n")

