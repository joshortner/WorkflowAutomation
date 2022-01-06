[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

# Workflow Automation Package 

This package contains programs to automate some of the things I find myself doing often.

### Installation

Use the package manager pip to install the workflow-automation package

```bash
pip install -i https://test.pypi.org/simple/ workflow-automation-pkg-joshortner
```

## cmake-man

cmake-man is a CLI program to manage CMake projects without having to hand-edit a CMakeLists.txt. Its based off of my personal experience using CMake. The functionaality and project structure is defined below.

### Usage

Create a CMake Project

```bash
mkdir <project_name>
cd <project_name>
cmake-man --init --lang c
```

Project Structure:

```bash
C:/path/to/my_project
│   CMakeLists.txt
│
├───lib
└───src
    │   main.<lang>
    │   my_project.h
    │
    └───my_project
```

Build a CMake Project. This will add a "build" directory and generate files for the system's default compilation tools.

```bash
cmake-man --build
```

## Current Issues:
- default project header define macro is lower case, should be upper
- init without lang causes error