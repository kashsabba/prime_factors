# prime_factors
prime factorization processor

clone the repository including "test_output" and "sql_questions" directories

prime_factor_processor.py
- run within a python virtual environment in command line
- python prime_factor_processor.py 100 
- run creates a directory called "saved_output" in the location where the code is
- writes text files for each value inputted through command line
- checks if a value inputted has already been processed and retrieves from the "saved_output" files if already processed
- prints out a list of prime factors in command line
- writes out a log file in the same location where the code is
- code can be run multiple times and will check the "saved_output" before writing/reading from saved

prime_factor_tester.py
- python prime_factor_tester.py
- unit tests leverage the "test_output" directory files to test two functions

sql_questions
- has the solutions to two questions
- written in postgresql
