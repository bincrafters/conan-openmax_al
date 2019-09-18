#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools, CMake


class OpenMAXALConan(ConanFile):
    name = "openmax_al"
    version = "1.1"
    url = "https://github.com/bincrafters/conan-openmax_al"
    author = "Bincrafters <bincrafters@gmail.com>"
    description = "OpenMAX AL is a royalty-free, cross platform open standard for accelerating the capture, and " \
                  "presentation of audio, video, and images in multimedia applications on embedded and mobile devices"
    license = "Khronos"
    exports = ["LICENSE.md"]
    generators = 'cmake'
    exports_sources = ['CMakeLists.txt']
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {'shared': False, 'fPIC': True}

    def configure(self):
        del self.settings.compiler.libcxx

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        for file in ['OpenMAXAL.h', 'OpenMAXAL_Platform.h', 'OpenMAXAL_IID.c']:
            tools.download('https://www.khronos.org/registry/OpenMAX-AL/api/1.1/%s' % file, file)

    def build(self):
        cmake = CMake(self)
        cmake.definitions['CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS'] = True
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy(pattern="*.h", dst="include")
        self.copy(pattern="*.dll", dst="bin", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", keep_path=False)
        self.copy(pattern="*.dylib*", dst="lib", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", keep_path=False)
        self.copy(pattern="*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['omxal']
