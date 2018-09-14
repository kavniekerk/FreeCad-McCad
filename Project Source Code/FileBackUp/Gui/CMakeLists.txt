
include_directories(
    ${CMAKE_SOURCE_DIR}/src
    ${CMAKE_CURRENT_BINARY_DIR}
    ${Boost_INCLUDE_DIRS}
    ${COIN3D_INCLUDE_DIRS}
    ${QT_INCLUDE_DIR}
    ${ZLIB_INCLUDE_DIR}
    ${PYTHON_INCLUDE_DIRS}
    ${XercesC_INCLUDE_DIRS}
)

set(PythonTestGui_LIBS
    PythonTest
    FreeCADGui
)

qt4_add_resources(PythonTest_QRC_SRCS Resources/PythonTest.qrc)

SET(PythonTestGui_SRCS
    ${PythonTest_QRC_SRCS}
    AppPythonTestGui.cpp
    Command.cpp
    PreCompiled.cpp
    PreCompiled.h
    Workbench.cpp
    Workbench.h
)

add_library(PythonTestGui SHARED ${PythonTestGui_SRCS})
target_link_libraries(PythonTestGui ${PythonTestGui_LIBS})

fc_target_copy_resource(PythonTestGui 
    ${CMAKE_SOURCE_DIR}/src/Mod/PythonTest
    ${CMAKE_BINARY_DIR}/Mod/PythonTest
    InitGui.py)

SET_BIN_DIR(PythonTestGui PythonTestGui /Mod/PythonTest)
SET_PYTHON_PREFIX_SUFFIX(PythonTestGui)
    
install(TARGETS PythonTestGui DESTINATION ${CMAKE_INSTALL_LIBDIR})
