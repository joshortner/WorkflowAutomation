cmake_minimum_required(VERSION 3.7.1)
set(CMAKE_CXX_STANDARD 17)

project(test)

set(SRC_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src)

include_directories(
	${SRC_DIR}
)

file(
	GLOB SOURCES
	${SRC_DIR}/main.cpp
)

add_executable(
	${PROJECT_NAME}
	${SOURCES}
)

#target_link_libraries(
#	${PROJECT_NAME}
#	<lib>
#)