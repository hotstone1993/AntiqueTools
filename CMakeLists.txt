cmake_minimum_required(VERSION 3.10.2)

project("AntiqueTools"  
        LANGUAGES   CXX   
        VERSION     0.0.1
)

set (CMAKE_CXX_STANDARD 17)

add_compile_options( -g -Wall )

set (PATH ${CMAKE_CURRENT_SOURCE_DIR}/src)

add_executable( ${PROJECT_NAME} ${PATH}/main.cpp )

set_target_properties( ${PROJECT_NAME} PROPERTIES 
                RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/output)

target_include_directories( ${PROJECT_NAME} PUBLIC 
                    ${PATH}/include )