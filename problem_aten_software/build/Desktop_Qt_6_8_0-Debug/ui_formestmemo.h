/********************************************************************************
** Form generated from reading UI file 'formestmemo.ui'
**
** Created by: Qt User Interface Compiler version 6.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FORMESTMEMO_H
#define UI_FORMESTMEMO_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTableView>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_FormEstMemo
{
public:
    QTableView *tableView;
    QPushButton *pushButton;
    QLabel *label;

    void setupUi(QWidget *FormEstMemo)
    {
        if (FormEstMemo->objectName().isEmpty())
            FormEstMemo->setObjectName("FormEstMemo");
        FormEstMemo->resize(400, 250);
        FormEstMemo->setMinimumSize(QSize(400, 250));
        tableView = new QTableView(FormEstMemo);
        tableView->setObjectName("tableView");
        tableView->setGeometry(QRect(10, 70, 381, 171));
        tableView->setStyleSheet(QString::fromUtf8("background:rgb(98, 160, 234)"));
        pushButton = new QPushButton(FormEstMemo);
        pushButton->setObjectName("pushButton");
        pushButton->setGeometry(QRect(10, 20, 251, 41));
        pushButton->setStyleSheet(QString::fromUtf8("background:rgb(98, 160, 234)"));
        label = new QLabel(FormEstMemo);
        label->setObjectName("label");
        label->setGeometry(QRect(-20, -30, 431, 321));
        label->setPixmap(QPixmap(QString::fromUtf8(":/new/prefix1/Captura desde 2024-11-13 15-36-59.png")));
        label->raise();
        tableView->raise();
        pushButton->raise();

        retranslateUi(FormEstMemo);

        QMetaObject::connectSlotsByName(FormEstMemo);
    } // setupUi

    void retranslateUi(QWidget *FormEstMemo)
    {
        FormEstMemo->setWindowTitle(QCoreApplication::translate("FormEstMemo", "Form", nullptr));
        pushButton->setText(QCoreApplication::translate("FormEstMemo", "Mostrar Estad\303\255sticas de Memotest", nullptr));
        label->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class FormEstMemo: public Ui_FormEstMemo {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FORMESTMEMO_H
