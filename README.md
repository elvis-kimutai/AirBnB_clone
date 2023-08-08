# 0x00. AirBnB clone - The console

![AirBnB](https://lh3.googleusercontent.com/OZLwRNCRCb07jKwoYk1m0CCbPEg2UR0q5qtcwhMKnneaZGLXWE9OAb9fOZG2JOvIgZEfYaBkcWkw81Ozv9exRIZyxTGDzjRlccS1rBhrqo7VyQ)

## Descreption
AirBnB is a web application composed by:
- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Objectives
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## command interpreter
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Execution
Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  nothing  quit  show  update

(hbnb)
(hbnb) 
(hbnb)quit
$ 
```
But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  nothing  quit  show  update
(hbnb) 
$
```

All tests should also pass in non-interactive mode: 

> $ echo "python3 -m unittest discover tests" | bash

