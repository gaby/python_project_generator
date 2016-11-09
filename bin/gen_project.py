#!/usr/bin/env python

from python_project_generator import ProjectGenerator, get_parser_args


def main():
    gen = ProjectGenerator(**get_parser_args())
    gen.generate()


if __name__ == '__main__':
    main()
