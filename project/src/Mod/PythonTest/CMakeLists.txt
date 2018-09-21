IF(BUILD_GUI)
    PYSIDE_WRAP_RC(PythonTest_QRC_SRCS Resources/PythonTest.qrc)
ENDIF(BUILD_GUI)

SET(${PythonTest_SRCS}
    PythonTest_SRCS
    Init.py    
    PyGui.py
    InitGui.py
    CreatBox.py
    Observer.py
)
SOURCE_GROUP("" FILES ${PythonTest_SRCS})

ADD_CUSTOM_TARGET(PythonTest ALL
   SOURCES ${all_files} ${PythonTest_SRCS}
)

qt4_add_resources(PythonTest_QRC_SRCS Resources/PythonTest.qrc)

fc_copy_sources(PythonTest "${CMAKE_BINARY_DIR}/Mod/PythonTest" ${PythonTest_SRCS})

INSTALL(
    FILES
        ${PythonTest_SRCS}
        ${PythonTest_QRC_SRCS}
    DESTINATION
        Mod/PythonTest
)

SET(PythonTestGuiIcon_SVG
    Resources/PythonTest.svg
)

fc_copy_sources(PythonTest "${CMAKE_BINARY_DIR}/${CMAKE_INSTALL_DATADIR}/Mod/PythonTest" ${PythonTestGuiIcon_SVG})

INSTALL(FILES ${PythonTestGuiIcon_SVG} DESTINATION "${CMAKE_INSTALL_DATADIR}/Mod/PythonTest/Resources")

