## Git Relay Race
---  

### Overview  
Student teams (3) must collaborate using Git to write code to translate ‘Hello World’

Teacher contains repo with the following:

* __countries.csv__  
*  __hello_world_translations__ - ‘Hello world’ translations in several languages taken from [Webucator](https://www.webucator.com/blog/2010/03/saying-hello-world-in-your-language-using-javascript/)   
*  __language_dict__ - dictionary of country : language pairs taken from [CIA Factbook](https://www.cia.gov/library/publications/the-world-factbook/fields/2098.html)    
*  __languages.csv__ - list of available languages (identical to languages from language_dict)    
*  __shakespeare.txt__ - Shakespeare corpus taken from [Project Gutenberg Shakespeare text](https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt)    
*  __target_country__ - unique for each student team
*  __answer_key_dict__ - allows teacher to check for student accuracy

All students clone repo, then collaborate on tasks below:

*  Student1 - write code to find index and number of instances of 'Hello world' from shakespeare.txt
*  Student2 - write code to identify correct language to extract from [list_of_languages] based on 'target_country'
*  Student3 - write code to translate 'Hello world' into language for 'target_country' & write output & # of instances of ‘Hello world’ to new 'answer.txt' in repo
*  Any student - writes function.py that takes input 'answer.txt' and outputs correct translation x times for # of instances of 'Hello world' using {answer_key_dict}
*  Students run comparison function.py output to teacher version of fuction