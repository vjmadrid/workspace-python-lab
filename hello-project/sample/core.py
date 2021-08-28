# -*- coding: utf-8 -*-


from . import helper


def get_hello_world_msg():
    return 'Hello World'


def hello():
    if helper.get_answer():
        print(get_hello_world_msg())
