cmake_minimum_required(VERSION 3.20)
project(find_prime C)

set(CMAKE_C_STANDARD 99)

add_library(find_prime library.c)

find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})
target_link_libraries(find_prime PRIVATE ${PYTHON_LIBRARIES} m)