

# Docker Image for Eggplants


## Intro

The scope of this chapter is to describe some basics behind my decissions and bullet points of the project

### Documentation
I have chosen markdown as format for documentation.
- It is very easy to write
- It is fast
- Can be fully intergrated with git

Documentation will cover all commands and details as for mid level technician. 

Documentation is written during the course of project.


### Choice of language

I have chosen python since it was the first on the list. I also thought about JavaScript since it would be the most natural choice for this type of application but python application will be smaller and I think it is more important to show my Python skills than JS.
As web server I have chosen Flask as the simplest basic one but enough for this task.
Assitionally, this project gave me the chance to present jinja2 skils which are very useful for work with many DevOps tools.


## Files in the project

- Dockerfile - Docker image configuraiton file used by `docker build` command
- README.md -  This documentation 
- TASK.md - Original task definition. Just for reference.
- app.py - Main Python application file. This file is executed by Python to start the application
- build.sh - building shell script, can be used for build or as example of use
- templates - directory which contains two templates one for GET and the other for POST requests

## How to use this repository

It is required to have installed:
- docker
- python
- flask python library


To build and execute the product simply run:
  ` ./build.sh `

This file serves also as documentation of the process. It is pretty self explanatory but I added some comments for clarity.


### Plan of work 

|----|----|
|Status | Task |
|----|----|
|DONE | Choose base image for container |
|DONE | Choose language |
|DONE | Choose repository |
|DONE | Build the app |
|DONE | Test the app |
|DONE | Add to zip |





