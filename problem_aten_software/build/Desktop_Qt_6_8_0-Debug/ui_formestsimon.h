/********************************************************************************
** Form generated from reading UI file 'formestsimon.ui'
**
** Created by: Qt User Interface Compiler version 6.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FORMESTSIMON_H
#define UI_FORMESTSIMON_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTableView>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_FormEstSimon
{
public:
    QTableView *tableView;
    QPushButton *pushButton;
    QLabel *label;

    void setupUi(QWidget *FormEstSimon)
    {
        if (FormEstSimon->objectName().isEmpty())
            FormEstSimon->setObjectName("FormEstSimon");
        FormEstSimon->resize(400, 250);
        FormEstSimon->setMinimumSize(QSize(400, 250));
        tableView = new QTableView(FormEstSimon);
        tableView->setObjectName("tableView");
        tableView->setGeometry(QRect(10, 70, 381, 171));
        tableView->setStyleSheet(QString::fromUtf8("background:rgb(98, 160, 234)"));
        pushButton = new QPushButton(FormEstSimon);
        pushButton->setObjectName("pushButton");
        pushButton->setGeometry(QRect(10, 20, 251, 41));
        pushButton->setStyleSheet(QString::fromUtf8("background:rgba(191, 64, 64, 190)"));
        label = new QLabel(FormEstSimon);
        label->setObjectName("label");
        label->setGeometry(QRect(-30, -70, 431, 421));
        label->setPixmap(QPixmap(QString::fromUtf8(":/new/prefix1/Captura desde 2024-11-13 15-36-59.png")));
        label->raise();
        tableView->raise();
        pushButton->raise();

        retranslateUi(FormEstSimon);

        QMetaObject::connectSlotsByName(FormEstSimon);
    } // setupUi

    void retranslateUi(QWidget *FormEstSimon)
    {
        FormEstSimon->setWindowTitle(QCoreApplication::translate("FormEstSimon", "Form", nullptr));
        pushButton->setText(QCoreApplication::translate("FormEstSimon", "Mostrar Estad\303\255sticas de Simon Says", nullptr));
        label->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class FormEstSimon: public Ui_FormEstSimon {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FORMESTSIMON_H
