#!/usr/bin/env python

import sys

def open_file(filename):
    f = open(filename, "r")
    file = f.read()
    file = file.split("\n")
    f.close()
    return file

def exo2(file):
    x = 0
    aim = 0
    y = 0
    for line in file:
        command = line.split(" ")
        if command[0] == "forward":
            x += int(command[1])
            y += int(command[1]) * aim
        if command[0] == "up":
            aim -= int(command[1])
        if command[0] == "down":
            aim += int(command[1])
    result = x * y
    print(result)

def exo1(file):
    x = 0
    y = 0
    for line in file:
        command = line.split(" ")
        if command[0] == "forward":
            x += int(command[1])
        if command[0] == "up":
            y -= int(command[1])
        if command[0] == "down":
            y += int(command[1])
    result = x * y
    print(result)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("error ./main.py input.txt");
        exit(-84);
    file = open_file(sys.argv[1])
    exo1(file)
    exo2(file)
    exit(0)