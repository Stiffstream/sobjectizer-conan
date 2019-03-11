from conans import ConanFile, CMake, tools
import os


class SobjectizerConan(ConanFile):
    name = "sobjectizer"
    version = "5.5.24.3"

    license = "BSD 3-Clause"
    url = "https://github.com/Stiffstream/sobjectizer-conan"

    description = (
            "A small framework for simplification of development of "
            "concurrent and event-driven applications in C++ "
            "by using Actor, Publish-Subscribe and CSP models."
    )

    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    options = {"shared": [True, False]}
    default_options = "shared=True"

    source_subfolder = "sobjectizer"

    def source(self):
        source_url = "https://sourceforge.net/projects/sobjectizer/files/sobjectizer/SObjectizer%20Core%20v.5.5"
        tools.get("{0}/so-{1}.zip".format(source_url, self.version))
        extracted_dir = "so-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def build(self):
        cmake = CMake(self)

        cmake.definitions['SOBJECTIZER_BUILD_SHARED'] = self.options.shared
        cmake.definitions['SOBJECTIZER_BUILD_STATIC'] = not self.options.shared

        cmake.configure(source_folder = self.source_subfolder + "/dev")
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*.hpp", dst="include/so_5", src=self.source_subfolder + '/dev/so_5')
        self.copy("*.hpp", dst="include/timertt", src=self.source_subfolder + '/dev/timertt')
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("license*", src=self.source_subfolder, dst="licenses",  ignore_case=True, keep_path=False)
