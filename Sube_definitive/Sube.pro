QT       += core gui sql

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++17

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    formaltas.cpp \
    formcarga.cpp \
    formlistado.cpp \
    formpagar.cpp \
    formpago.cpp \
    main.cpp \
    mainwindow.cpp

HEADERS += \
    formaltas.h \
    formcarga.h \
    formlistado.h \
    formpagar.h \
    formpago.h \
    mainwindow.h

FORMS += \
    formaltas.ui \
    formcarga.ui \
    formlistado.ui \
    formpagar.ui \
    formpago.ui \
    mainwindow.ui

TRANSLATIONS += \
    Sube_es_AR.ts
CONFIG += lrelease
CONFIG += embed_translations

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target
