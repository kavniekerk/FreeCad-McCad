
include_directories(
    ${Boost_INCLUDE_DIRS}
    ${OCC_INCLUDE_DIR}
    ${PYTHON_INCLUDE_DIRS}
    ${ZLIB_INCLUDE_DIR}
    ${XercesC_INCLUDE_DIRS}
)

set(PythonTest_LIBS
    FreeCADApp
)

SET(PythonTest_SRCS
    AppPythonTest.cpp
    PreCompiled.cpp
    PreCompiled.h
)

add_library(PythonTest SHARED ${PythonTest_SRCS})
target_link_libraries(PythonTest ${PythonTest_LIBS})


fc_target_copy_resource(PythonTest 
    ${CMAKE_SOURCE_DIR}/src/Mod/PythonTest
    ${CMAKE_BINARY_DIR}/Mod/PythonTest
    Init.py)

SET_BIN_DIR(PythonTest PythonTest /Mod/PythonTest)
SET_PYTHON_PREFIX_SUFFIX(PythonTest)

install(TARGETS PythonTest DESTINATION ${CMAKE_INSTALL_LIBDIR})
