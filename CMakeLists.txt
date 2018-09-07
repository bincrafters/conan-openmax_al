cmake_minimum_required(VERSION 2.8.11)

project(openmax_al)

include(conanbuildinfo.cmake)
conan_basic_setup()

add_library(omxal OpenMAXAL_IID.c)
