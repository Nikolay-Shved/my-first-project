#!/usr/bin/env python3
import prompt


def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def welcome_user():
    name = prompt.string('May I have your name? ')
    return (f'Hello, {name}!')
