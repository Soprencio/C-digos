/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMdiArea>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionslair;
    QAction *actionAlta;
    QAction *actionListado;
    QAction *actionCargar_Saldo;
    QAction *actionPagar_Boleto;
    QAction *actionListado_Viajes;
    QWidget *centralwidget;
    QMdiArea *mdiArea;
    QMenuBar *menubar;
    QMenu *menuArchivo;
    QMenu *menuFunciones;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(800, 600);
        actionslair = new QAction(MainWindow);
        actionslair->setObjectName("actionslair");
        QIcon icon(QIcon::fromTheme(QIcon::ThemeIcon::WindowClose));
        actionslair->setIcon(icon);
        actionAlta = new QAction(MainWindow);
        actionAlta->setObjectName("actionAlta");
        QIcon icon1(QIcon::fromTheme(QIcon::ThemeIcon::ListAdd));
        actionAlta->setIcon(icon1);
        actionListado = new QAction(MainWindow);
        actionListado->setObjectName("actionListado");
        QIcon icon2(QIcon::fromTheme(QIcon::ThemeIcon::FormatJustifyFill));
        actionListado->setIcon(icon2);
        actionCargar_Saldo = new QAction(MainWindow);
        actionCargar_Saldo->setObjectName("actionCargar_Saldo");
        QIcon icon3(QIcon::fromTheme(QIcon::ThemeIcon::DocumentSave));
        actionCargar_Saldo->setIcon(icon3);
        actionPagar_Boleto = new QAction(MainWindow);
        actionPagar_Boleto->setObjectName("actionPagar_Boleto");
        QIcon icon4(QIcon::fromTheme(QIcon::ThemeIcon::GoHome));
        actionPagar_Boleto->setIcon(icon4);
        actionListado_Viajes = new QAction(MainWindow);
        actionListado_Viajes->setObjectName("actionListado_Viajes");
        QIcon icon5(QIcon::fromTheme(QIcon::ThemeIcon::FormatIndentMore));
        actionListado_Viajes->setIcon(icon5);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        mdiArea = new QMdiArea(centralwidget);
        mdiArea->setObjectName("mdiArea");
        mdiArea->setGeometry(QRect(0, 0, 801, 571));
        mdiArea->setStyleSheet(QString::fromUtf8(""));
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName("menubar");
        menubar->setGeometry(QRect(0, 0, 800, 23));
        menuArchivo = new QMenu(menubar);
        menuArchivo->setObjectName("menuArchivo");
        menuFunciones = new QMenu(menubar);
        menuFunciones->setObjectName("menuFunciones");
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName("statusbar");
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menuArchivo->menuAction());
        menubar->addAction(menuFunciones->menuAction());
        menuArchivo->addAction(actionslair);
        menuFunciones->addAction(actionAlta);
        menuFunciones->addAction(actionListado);
        menuFunciones->addAction(actionCargar_Saldo);
        menuFunciones->addAction(actionListado_Viajes);
        menuFunciones->addAction(actionPagar_Boleto);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        actionslair->setText(QCoreApplication::translate("MainWindow", "Salir", nullptr));
        actionAlta->setText(QCoreApplication::translate("MainWindow", "Alta", nullptr));
        actionListado->setText(QCoreApplication::translate("MainWindow", "Listado", nullptr));
        actionCargar_Saldo->setText(QCoreApplication::translate("MainWindow", "Cargar Saldo", nullptr));
        actionPagar_Boleto->setText(QCoreApplication::translate("MainWindow", "Pagar Boleto", nullptr));
        actionListado_Viajes->setText(QCoreApplication::translate("MainWindow", "Listado Viajes", nullptr));
        menuArchivo->setTitle(QCoreApplication::translate("MainWindow", "Archivo", nullptr));
        menuFunciones->setTitle(QCoreApplication::translate("MainWindow", "Funciones", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
