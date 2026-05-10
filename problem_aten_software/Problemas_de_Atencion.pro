QT       += core gui sql

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++17

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    formbmr.cpp \
    formestbmr.cpp \
    formestmemo.cpp \
    formestsimon.cpp \
    formlista.cpp \
    formmemo.cpp \
    formsimon.cpp \
    formuser.cpp \
    main.cpp \
    mainwindow.cpp

HEADERS += \
    formbmr.h \
    formestbmr.h \
    formestmemo.h \
    formestsimon.h \
    formlista.h \
    formmemo.h \
    formsimon.h \
    formuser.h \
    mainwindow.h

FORMS += \
    formbmr.ui \
    formestbmr.ui \
    formestmemo.ui \
    formestsimon.ui \
    formlista.ui \
    formmemo.ui \
    formsimon.ui \
    formuser.ui \
    mainwindow.ui

TRANSLATIONS += \
    Problemas_de_Atencion_es_AR.ts
CONFIG += lrelease
CONFIG += embed_translations

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

RESOURCES += \
    fondo1.qrc
