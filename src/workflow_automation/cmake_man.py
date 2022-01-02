#from workflow_automation import example

'''
Source: 
    - https://packaging.python.org/en/latest/tutorials/packaging-projects/
'''

# TO DO: --build option

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Initialize a CMake project directory")
    parser.add_argument("--lang", type=str, required=True, help="Project language (options: c, cpp)")
    parser.add_argument("--dir", type=str, required=True, help="Project directory")

    args = parser.parse_args()

    initializeCMakeProject(args.dir, args.lang)



def initializeCMakeProject(directory: str, language: str):
    directory = Path(directory)
    if language in SUPPORTED_LANGUAGES:
        if not directory.is_dir():
            project_name = directory.name.lower()

            directory.mkdir()

            lib_dir = directory.joinpath("lib")
            src_dir = directory.joinpath("src")
            src_project_dir = src_dir.joinpath(project_name)
            default_module_dir = src_project_dir.joinpath("default")

            cmake_lists_path = directory.joinpath("CMakeLists.txt")
            #build_script     = directory.joinpath("run_build.sh")

            entry_point_path  = src_dir.joinpath(f'main.{language}')
            main_include_path = src_dir.joinpath(f'{project_name}.h')

            # Make directories
            lib_dir.mkdir()
            src_dir.mkdir()
            src_project_dir.mkdir()
            default_module_dir.mkdir()

            # Write default files
            with cmake_lists_path.open("w") as f:
                f.write(cmake_lists_contents(project_name, language))

            with entry_point_path.open("w") as f:
                f.write(main_c_contents(project_name))

            with main_include_path.open("w") as f:
                f.write(main_include_c_contents(project_name.upper()))

        else:
            print(f'Directory {directory} already exisits!')
            return

    else:
        print(f'Language not supported. Choose one of the following: {SUPPORTED_LANGUAGES}')
        return


SUPPORTED_LANGUAGES = [
    "c", "cpp"
]

cmake_lists_contents = lambda project_name, language: \
    (
        f'cmake_minimum_required(VERSION 3.7.1)\n' +
        f'set(CMAKE_C_STANDARD 99)\n\n' +
        f'project({project_name})\n\n' +
        f'set(SRC_DIR ${{CMAKE_CURRENT_SOURCE_DIR}}/src)\n\n' +
        f'include_directories(\n\t${{SRC_DIR}}\n)\n\n' +
        f'file(\n\tGLOB SOURCES\n\t${{SRC_DIR}}/main.{language}\n)\n\n' +
        f'add_executable(\n\t${{PROJECT_NAME}}\n\t${{SOURCES}}\n)\n\n' +
        f'#target_link_libraries(\n#\t${{PROJECT_NAME}}\n#\t<lib>\n#)'
    )

main_c_contents = lambda project_name: \
    (
        f'#include <{project_name}.h>\n\n' +
        "#include <stdio.h>\n" +
        f'int main(int argc, char **argv)\n' +
        "{\n" +
        '\tprintf("Hello World\\n");\n' +
        f'\treturn 0;\n'
        "}\n"
    )

main_include_c_contents = lambda project_name: \
    (
        f'#ifndef {project_name}_H\n' +
        f'#define {project_name}_H\n\n' +
        f'#endif'
    )

if __name__ == "__main__":
    main()
