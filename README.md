# Internal data structures

<!-- ABOUT THE PROJECT -->
## About The Project

This project is a practical work of the Big Data course of the EMSE.

## Project participants:

- Caille Maxence - maxence.caille@etu.emse.fr
- Courtois Justin - justin.courtois@etu.emse.fr

## Objective:

Implement  hash functions and compare them on two criteria: the number of collisions and the good distribution. 

## Use the project

Programs to execute : 
- [Main.py](https://github.com/maxant38/big_data_hash_table/blob/main/Main.py)
- launch the main function

## What's in the github repository:

The project is divided in four main components: the main program to launch the project,functions related to file processing, the main functions used (hash,evaluation,...), the  and the front-end interface.

### Main Program 
File : [Main.py](https://github.com/maxant38/big_data_hash_table/blob/main/Main.py)

The Main Program is responsible for:

- Gather the different components of the project. This is the program to run if you want to use the project.
- Call the UI 
### Functions related to file processing 
File : [Lecture_fichier.py](https://github.com/maxant38/big_data_hash_table/blob/main/Lecture_fichier.py)

This component is responsible for:

- Determine which txt file contains the most words (maxline function)

- Determine the size M of our hash table

- Proceed to the hash of a file (hashage_fichier_% functions)

### Main function used
File : [TD.py](https://github.com/maxant38/big_data_hash_table/blob/main/TD.py)

- Define hash functions(Jenkins,Multiplication, ASCII and use_hash)

- Generate a prime number close to the searched one (generate_prime_number)

- Create a TAD and fill it (create_TAD, put_in_TAD)

- A visualization of the data to see if our functions are uniforms (data_viz)
### Front-end interface
File : [GUI.py](https://github.com/maxant38/big_data_hash_table/blob/main/GUI.py)

This component is responsible for:

- Creating a font-end interface for the user
- Create a TAD according custom user input
- Tell the program to display more information (graph, data visualization)

## Built With:

* [Python](https://www.python.org/), [Libraries used](https://github.com/maxant38/big_data_hash_table/tree/main/.venv/Lib/site-packages)
=> To make your life easier, download the .venv file which will allow you to have an environment with all the libraries used in this project. 











