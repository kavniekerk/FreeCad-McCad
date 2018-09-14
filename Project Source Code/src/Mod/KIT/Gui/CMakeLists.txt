
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

set(KITGui_LIBS
    KIT
    FreeCADGui
)

qt4_add_resources(KIT_QRC_SRCS Resources/KIT.qrc)

SET(KITGui_SRCS
    ${KIT_QRC_SRCS}
    AppKITGui.cpp
    Command.cpp
    PreCompiled.cpp
    PreCompiled.h
    Workbench.cpp
    Workbench.h
)

add_library(KITGui SHARED ${KITGui_SRCS})
target_link_libraries(KITGui ${KITGui_LIBS})

fc_target_copy_resource(KITGui 
    ${CMAKE_SOURCE_DIR}/src/Mod/KIT
    ${CMAKE_BINARY_DIR}/Mod/KIT
    InitGui.py)

SET_BIN_DIR(KITGui KITGui /Mod/KIT)
SET_PYTHON_PREFIX_SUFFIX(KITGui)
    
install(TARGETS KITGui DESTINATION ${CMAKE_INSTALL_LIBDIR})
