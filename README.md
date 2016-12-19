## Git Relay Race
---  

### Overview  
Student teams (3) must collaborate using Git to write code to translate ‘Hello World’


### Instructions 

Teacher contains repo with the following:

* `countries.csv`  
*  `hello_world_translations` - ‘Hello world’ translations in several languages taken from [Webucator](https://www.webucator.com/blog/2010/03/saying-hello-world-in-your-language-using-javascript/)   
*  `language_dict` - dictionary of country : language pairs taken from [CIA Factbook](https://www.cia.gov/library/publications/the-world-factbook/fields/2098.html)    
*  `languages.csv` - list of available languages (identical to languages from language_dict)    
*  `shakespeare.txt` - Shakespeare corpus taken from [Project Gutenberg Shakespeare text](https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt)    
*  `target_country` - unique for each student team
*  `answer_key_dict` - allows teacher to check for student accuracy

All students clone repo, then collaborate on tasks below:

*  Student1 - write code to find index and number of instances of 'Hello world' from `shakespeare.txt`   
*  Student2 - write code to identify correct language to extract from l`anguages.csv` based on `target_country`    
*  Student3 - write code to translate 'Hello world' into language for `target_country` & write output & # of instances of ‘Hello world’ to new `answer.txt` in repo    
*  Any student - writes `function.py` that takes input `answer.txt` and outputs correct translation x times for # of instances of 'Hello world' using `answer_key_dict `   
*  Students run comparison `function.py` output to teacher version of function

### To-do

* Write `answer_key_dict`, include teamIDs. Will eventually add the following for each team: target_country, # of instances of 'Hello world', and correct translation.   
* Write randomizer function that allows teacher to randomly select country from `countries.csv`. Possible countries must be restricted to languages included in `hello_world_translations` Output will be unique `target_country` for each team and updated `answer_key_dict` with `target_country`
* Write function that randomly imports x +/- y instances of 'Hello world' into `shakespeare.txt`. Ideally, includes multiple versions, e.g., 'hello world', 'HELLO WORLD', 'Hello World', etc. Output should include new text file with teamID and updated `answer_key_dict` with # of instances of 'Hello world'    
