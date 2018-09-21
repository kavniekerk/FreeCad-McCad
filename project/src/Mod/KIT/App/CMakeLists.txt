
include_directories(
    ${Boost_INCLUDE_DIRS}
    ${OCC_INCLUDE_DIR}
    ${PYTHON_INCLUDE_DIRS}
    ${ZLIB_INCLUDE_DIR}
    ${XercesC_INCLUDE_DIRS}
)

set(KIT_LIBS
    FreeCADApp
)

SET(KIT_SRCS
    AppKIT.cpp
    PreCompiled.cpp
    PreCompiled.h
)

add_library(KIT SHARED ${KIT_SRCS})
target_link_libraries(KIT ${KIT_LIBS})


fc_target_copy_resource(KIT 
    ${CMAKE_SOURCE_DIR}/src/Mod/KIT
    ${CMAKE_BINARY_DIR}/Mod/KIT
    Init.py)

SET_BIN_DIR(KIT KIT /Mod/KIT)
SET_PYTHON_PREFIX_SUFFIX(KIT)

install(TARGETS KIT DESTINATION ${CMAKE_INSTALL_LIBDIR})
