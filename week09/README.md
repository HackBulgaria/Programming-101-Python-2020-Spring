# Introduction to Databases and SQL

Presentation: https://slides.com/hackbulgaria/python-101-9th-sql/

## Task 1: Tables, tables everywhere! SELECT, UPDATE, INSERT, DELETE

Now, we know that our languages table looks like this:

| id      | language  | answer  | answered | guide |
| ------------- |:-------------:| --- | --- |-----:|
1|Python|google|0|A folder named Python was created. Go there and fight with program.py!
2|Go|200 OK|0|A folder named Go was created. Go there and try to make Google Go run.
3|Java|object oriented programming|0|A folder named Java was created. Can you handle the class?
4|Haskell|Lambda|0|Something pure has landed. Go to Haskell folder and see it!
5|C#|NDI=|0|Do you see sharp? Go to the C# folder and check out.
6|Ruby|https://www.ruby-lang.org/bg/|0|Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!
7|C++|header files|0|Here be dragons! It's C++ time. Go to the C++ folder.
8|JavaScript|Douglas Crockford|0|NodeJS time. Go to JavaScript folder and Node your way!

Your task is to write queries for:

* Create database
* Create table `Languages` with columns and attributes with the correct types
* Insert data
* Add new column `rating` which is number from 1 to 9. Insert values for every language.
* For few languages (`Python` and `Go`) update answered value from 0 to 1
* Select languages which answer is `200 OK` or `Lambda`.
