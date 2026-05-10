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
#include <QtWidgets/QLabel>
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
    QAction *actionSimon_Says;
    QAction *actionMemoTest;
    QAction *actionBuenos_Malos_y_Regulares;
    QAction *actionUsuarios;
    QAction *actionEst_Simon_Says;
    QAction *actionEst_MemoTest;
    QAction *actionEst_Bue_Mal_y_Reg;
    QAction *actionMostrar_Usuarios;
    QWidget *centralwidget;
    QMdiArea *mdiArea;
    QLabel *label;
    QLabel *label_2;
    QLabel *label_3;
    QMenuBar *menubar;
    QMenu *menuJuegos;
    QMenu *menuBase_de_Datos;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(800, 700);
        MainWindow->setMinimumSize(QSize(700, 700));
        actionSimon_Says = new QAction(MainWindow);
        actionSimon_Says->setObjectName("actionSimon_Says");
        QIcon icon(QIcon::fromTheme(QIcon::ThemeIcon::MediaRecord));
        actionSimon_Says->setIcon(icon);
        actionMemoTest = new QAction(MainWindow);
        actionMemoTest->setObjectName("actionMemoTest");
        QIcon icon1(QIcon::fromTheme(QIcon::ThemeIcon::MailMarkImportant));
        actionMemoTest->setIcon(icon1);
        actionBuenos_Malos_y_Regulares = new QAction(MainWindow);
        actionBuenos_Malos_y_Regulares->setObjectName("actionBuenos_Malos_y_Regulares");
        QIcon icon2(QIcon::fromTheme(QIcon::ThemeIcon::EditSelectAll));
        actionBuenos_Malos_y_Regulares->setIcon(icon2);
        actionUsuarios = new QAction(MainWindow);
        actionUsuarios->setObjectName("actionUsuarios");
        QIcon icon3(QIcon::fromTheme(QIcon::ThemeIcon::ContactNew));
        actionUsuarios->setIcon(icon3);
        actionEst_Simon_Says = new QAction(MainWindow);
        actionEst_Simon_Says->setObjectName("actionEst_Simon_Says");
        actionEst_Simon_Says->setIcon(icon);
        actionEst_MemoTest = new QAction(MainWindow);
        actionEst_MemoTest->setObjectName("actionEst_MemoTest");
        actionEst_MemoTest->setIcon(icon1);
        actionEst_Bue_Mal_y_Reg = new QAction(MainWindow);
        actionEst_Bue_Mal_y_Reg->setObjectName("actionEst_Bue_Mal_y_Reg");
        actionEst_Bue_Mal_y_Reg->setIcon(icon2);
        actionMostrar_Usuarios = new QAction(MainWindow);
        actionMostrar_Usuarios->setObjectName("actionMostrar_Usuarios");
        QIcon icon4(QIcon::fromTheme(QIcon::ThemeIcon::EditCopy));
        actionMostrar_Usuarios->setIcon(icon4);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        mdiArea = new QMdiArea(centralwidget);
        mdiArea->setObjectName("mdiArea");
        mdiArea->setGeometry(QRect(-10, 70, 811, 801));
        label = new QLabel(centralwidget);
        label->setObjectName("label");
        label->setGeometry(QRect(10, 10, 61, 51));
        label->setPixmap(QPixmap(QString::fromUtf8(":/new/prefix1/logo2.png")));
        label_2 = new QLabel(centralwidget);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(70, 10, 281, 18));
        label_3 = new QLabel(centralwidget);
        label_3->setObjectName("label_3");
        label_3->setGeometry(QRect(70, 30, 231, 18));
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName("menubar");
        menubar->setGeometry(QRect(0, 0, 800, 23));
        menuJuegos = new QMenu(menubar);
        menuJuegos->setObjectName("menuJuegos");
        menuBase_de_Datos = new QMenu(menubar);
        menuBase_de_Datos->setObjectName("menuBase_de_Datos");
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName("statusbar");
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menuJuegos->menuAction());
        menubar->addAction(menuBase_de_Datos->menuAction());
        menuJuegos->addAction(actionSimon_Says);
        menuJuegos->addAction(actionMemoTest);
        menuJuegos->addAction(actionBuenos_Malos_y_Regulares);
        menuBase_de_Datos->addAction(actionUsuarios);
        menuBase_de_Datos->addAction(actionMostrar_Usuarios);
        menuBase_de_Datos->addSeparator();
        menuBase_de_Datos->addAction(actionEst_Simon_Says);
        menuBase_de_Datos->addAction(actionEst_MemoTest);
        menuBase_de_Datos->addAction(actionEst_Bue_Mal_y_Reg);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        actionSimon_Says->setText(QCoreApplication::translate("MainWindow", "Simon Says", nullptr));
        actionMemoTest->setText(QCoreApplication::translate("MainWindow", "MemoTest", nullptr));
        actionBuenos_Malos_y_Regulares->setText(QCoreApplication::translate("MainWindow", "Buenos, Malos y Regulares", nullptr));
        actionUsuarios->setText(QCoreApplication::translate("MainWindow", "Usuarios", nullptr));
        actionEst_Simon_Says->setText(QCoreApplication::translate("MainWindow", "Est. Simon Says", nullptr));
        actionEst_MemoTest->setText(QCoreApplication::translate("MainWindow", "Est. MemoTest", nullptr));
        actionEst_Bue_Mal_y_Reg->setText(QCoreApplication::translate("MainWindow", "Est. Bue. Mal. y Reg.", nullptr));
        actionMostrar_Usuarios->setText(QCoreApplication::translate("MainWindow", "Mostrar Usuarios", nullptr));
        label->setText(QString());
        label_2->setText(QCoreApplication::translate("MainWindow", "Software de Problemas de Atenci\303\263n", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "Agust\303\255n Meza y Manuel Ponce", nullptr));
        menuJuegos->setTitle(QCoreApplication::translate("MainWindow", "Juegos", nullptr));
        menuBase_de_Datos->setTitle(QCoreApplication::translate("MainWindow", "Base de Datos", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
