# Workflow Automation Package 

This package contains scripts to automate some of the things I find myself doing often.

## cmake-man

cmake-man is a CLI program to manage CMake projects without having to hand-edit a CMakeLists. Its based off of my personal CMake Project setup which is described below.

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

|---<project_name>
	|--- CMakeLists.txt
	|--- lib
	|--- src
		|--- main.<lang>
		|--- <project_name>.h
		|--- <project_name>


Build a CMake Project. This will add a "build" directory and generate files for the systems default compilation tools.

```bash
cmake-man --build
```
