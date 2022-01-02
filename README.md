# Workflow Automation Package 

This package contains programs to automate some of the things I find myself doing often.

## cmake-man

cmake-man is a CLI program to manage CMake projects without having to hand-edit a CMakeLists.txt. Its based off of my personal experience using CMake. The project structure is defined below.

### Installation

Use the package manager pip to install cmake-man

```bash
pip install -i https://test.pypi.org/simple/ workflow-automation-pkg-joshortner
```

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
