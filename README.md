# sobjectizer-conan
This is Conan package for [SObjectizer](https://stiffstream.com/en/products/sobjectizer.html) framework.

# How To Use

## Installing Via Conan

To use SObjectizer via Conan it is necessary to do the following steps:

1. Add the corresponding remote to your conan:

```bash
conan remote add stiffstream https://api.bintray.com/conan/stiffstream/public
```

2. Add SObjectizer to `conanfile.txt` of your project:
```
[requires]
sobjectizer/5.5.24.3@stiffstream/stable
```
It also may be necessary to specify `shared` option for SObjectizer. For example, for build SObjectizer as a static library:
```
[options]
sobjectizer:shared=False
```

3. Install dependencies for your project:
```bash
conan install SOME_PATH --build=missing
```

## Adding SObjectizer To Your CMakeLists.txt

Please note that SObjectizer should be added to your CMakeLists.txt via `find_package` command:
```cmake
...
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(sobjectizer)
...
target_link_libraries(your_target sobjectizer::SharedLib) # Or sobjectizer::StaticLib
```

# Some Notes
If you have any questions about SObjectizer feel free to ask us via `info at stiffstream dot com`.

If you have some problems with SObjectizer or this conan-recipe please open an [issue](https://github.com/Stiffstream/sobjectizer-conan/issues).
