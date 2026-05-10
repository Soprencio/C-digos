/********************************************************************************
** Form generated from reading UI file 'formestbmr.ui'
**
** Created by: Qt User Interface Compiler version 6.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FORMESTBMR_H
#define UI_FORMESTBMR_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTableView>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_FormEstBMR
{
public:
    QTableView *tableView;
    QPushButton *pushButton;
    QLabel *label;

    void setupUi(QWidget *FormEstBMR)
    {
        if (FormEstBMR->objectName().isEmpty())
            FormEstBMR->setObjectName("FormEstBMR");
        FormEstBMR->resize(400, 250);
        FormEstBMR->setMinimumSize(QSize(400, 250));
        tableView = new QTableView(FormEstBMR);
        tableView->setObjectName("tableView");
        tableView->setGeometry(QRect(10, 70, 381, 171));
        tableView->setStyleSheet(QString::fromUtf8("background:rgb(98, 160, 234)"));
        pushButton = new QPushButton(FormEstBMR);
        pushButton->setObjectName("pushButton");
        pushButton->setGeometry(QRect(10, 20, 351, 41));
        pushButton->setStyleSheet(QString::fromUtf8("background:rgb(143, 240, 164)"));
        label = new QLabel(FormEstBMR);
        label->setObjectName("label");
        label->setGeometry(QRect(-4, -4, 411, 311));
        label->setPixmap(QPixmap(QString::fromUtf8(":/new/prefix1/Captura desde 2024-11-13 15-36-59.png")));
        label->raise();
        tableView->raise();
        pushButton->raise();

        retranslateUi(FormEstBMR);

        QMetaObject::connectSlotsByName(FormEstBMR);
    } // setupUi

    void retranslateUi(QWidget *FormEstBMR)
    {
        FormEstBMR->setWindowTitle(QCoreApplication::translate("FormEstBMR", "Form", nullptr));
        pushButton->setText(QCoreApplication::translate("FormEstBMR", "Mostrar Estad\303\255sticas de Buenos, Malos y Regulares", nullptr));
        label->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class FormEstBMR: public Ui_FormEstBMR {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FORMESTBMR_H
