# Queuing System in JS

This project implements a queuing system in JavaScript using Redis. It covers the implementation of basic queuing operations, job processing, and notification systems.

## Learning Objectives

- How to run a Redis server on your machine
- How to run simple operations with the Redis client
- How to use a Redis client with Node JS for basic operations
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to build a basic Express app interacting with a Redis server and queue

## Requirements

- All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All of your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `js` extension

## Required Files

- `package.json`
- `.babelrc`

## Install Redis on Ubuntu 18.04

```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis-py
```

## Start Redis server

```bash
$ sudo service redis-server start
```

## Verify Redis server is working

```bash
$ redis-cli ping
PONG
```

## Install node_modules

```bash
$ npm install
```

## Tasks

The project consists of multiple tasks that cover different aspects of implementing a queuing system:

1. Node Redis Client
2. Node Redis client and basic operations
3. Node Redis client and async operations
4. Node Redis client and advanced operations
5. Node Redis client publisher and subscriber
6. Create the Job creator
7. Create the Job processor
8. Track progress and errors with Kue: Create the Job creator
9. Track progress and errors with Kue: Create the Job processor
10. Writing the job creation function
11. Writing the test for job creation
12. In stock?

## Author

- ALX SE Student
