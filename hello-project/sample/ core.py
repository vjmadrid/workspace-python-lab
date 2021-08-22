# -*- coding: utf-8 -*-


from . import helpers


def get_hello_world_msg():
    return 'Hello World'


def hello():
    if helpers.get_answer():
        print(get_hello_world_msg())