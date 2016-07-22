#!/usr/bin/env python
# -*- coding: utf-8 -*-


# def parse_task(func):
#     def handle_args(*args, **kwargs):
#         print args
#         print args[0]
#         print args[0]['aaa']
#         func (*args, **kwargs)
#     return handle_args


def parse_task(func):
    def handle_args(*args, **kwargs):
        print args
        print args[0]
        print args[0]['aaa']
        func (*args, aaa=args[0]['aaa'])
    return handle_args


@parse_task
def foo(task, **kwargs):
    print task
    print kwargs


def main():
    task = {"aaa": 111, "bbb": 222}
    foo(task)

if __name__ == '__main__':
    main()