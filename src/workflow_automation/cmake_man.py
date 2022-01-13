#from workflow_automation import example

'''
Source: 
    - https://packaging.python.org/en/latest/tutorials/packaging-projects/
'''

# TO DO: --build option

import argparse
import shutil
import subprocess
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Initialize a CMake project directory")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-i", "--init", action="store_true", help="Initialize a directory with a CMake project template")
    group.add_argument("-b", "--build", action="store_true", help="Build an existing CMake project")

    parser.add_argument("-l", "--lang", type=str, help="Project language (options: c, cpp)")
    
    args = parser.parse_args()

    if args.init:
        initProject(Path.cwd(), args.lang)
    elif args.build:
        buildProject(Path.cwd())


def buildProject(directory: Path):
    # Check for CMakeLists file
    check_file = directory.joinpath("CMakeLists.txt")
    if check_file.is_file():
        # Check for existing build path
        build_path = directory.joinpath("build")
        if build_path.is_dir():
            shutil.rmtree(build_path)

        subprocess.call("mkdir build", shell=True)
        subprocess.run("cd build && cmake ..", shell=True)

    else:
        print(f'Directory {directory} doesn\'t contain a CMakeLists.txt!')


def initProject(directory: Path, language: str):
    if language in LANGUAGE_FILES.keys():
        # Check for existing CMakeLists file
        check_file = directory.joinpath("CMakeLists.txt")
        if not check_file.is_file():
            project_name = directory.name.lower()

            lib_dir = directory.joinpath("lib")
            src_dir = directory.joinpath("src")
            src_project_dir = src_dir.joinpath(project_name)

            cmake_lists_path = directory.joinpath("CMakeLists.txt")

            entry_point_path  = src_dir.joinpath(f'main.{language}')
            main_include_path = src_dir.joinpath(f'{project_name}.h')

            # Make directories
            lib_dir.mkdir()
            src_dir.mkdir()
            src_project_dir.mkdir()

            # Write default files
            with cmake_lists_path.open("w") as f:
                f.write(LANGUAGE_FILES[language]["cmake_lists"](project_name, language)) 

            with entry_point_path.open("w") as f:
                f.write(LANGUAGE_FILES[language]["main"](project_name))

            with main_include_path.open("w") as f:
                f.write(LANGUAGE_FILES[language]["main_include"](project_name))

        else:
            print(f'Directory {directory} already contains a CMakeLists.txt!')
            return

    else:
        print(f'Language not supported. Choose one of the following: {SUPPORTED_LANGUAGES}')
        return


LANGUAGE_FILES = {
    "c": {
        "cmake_lists": lambda project_name, language: \
            (
                f'cmake_minimum_required(VERSION 3.7.1)\n' +
                f'set(CMAKE_C_STANDARD 99)\n\n' +
                f'project({project_name})\n\n' +
                f'set(SRC_DIR ${{CMAKE_CURRENT_SOURCE_DIR}}/src)\n\n' +
                f'include_directories(\n\t${{SRC_DIR}}\n)\n\n' +
                f'file(\n\tGLOB SOURCES\n\t${{SRC_DIR}}/main.{language}\n)\n\n' +
                f'add_executable(\n\t${{PROJECT_NAME}}\n\t${{SOURCES}}\n)\n\n' +
                f'#target_link_libraries(\n#\t${{PROJECT_NAME}}\n#\t<lib>\n#)'
            ),

        "main": lambda project_name: \
            (
                f'#include <{project_name}.h>\n\n' +
                "#include <stdio.h>\n" +
                f'int main(int argc, char **argv)\n' +
                "{\n" +
                '\tprintf("Hello World\\n");\n' +
                f'\treturn 0;\n'
                "}\n"
            ),

        "main_include": lambda project_name: \
            (
                f'#ifndef {project_name.upper()}_H\n' +
                f'#define {project_name.upper()}_H\n\n' +
                f'#endif'
            )
    }
}

#main_c_contents = lambda project_name: \

#main_include_c_contents = lambda project_name: \

if __name__ == "__main__":
    main()
