/********************************************************************************
** Form generated from reading UI file 'formlista.ui'
**
** Created by: Qt User Interface Compiler version 6.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FORMLISTA_H
#define UI_FORMLISTA_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTableView>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_FormLista
{
public:
    QTableView *tableView;
    QPushButton *pushButton;
    QLabel *label;

    void setupUi(QWidget *FormLista)
    {
        if (FormLista->objectName().isEmpty())
            FormLista->setObjectName("FormLista");
        FormLista->resize(300, 300);
        FormLista->setMinimumSize(QSize(300, 300));
        tableView = new QTableView(FormLista);
        tableView->setObjectName("tableView");
        tableView->setGeometry(QRect(10, 90, 281, 201));
        tableView->setStyleSheet(QString::fromUtf8("background:rgb(98, 160, 234)"));
        pushButton = new QPushButton(FormLista);
        pushButton->setObjectName("pushButton");
        pushButton->setGeometry(QRect(20, 30, 191, 41));
        pushButton->setStyleSheet(QString::fromUtf8("background:rgb(246, 97, 81)"));
        label = new QLabel(FormLista);
        label->setObjectName("label");
        label->setGeometry(QRect(-24, -14, 341, 321));
        label->setPixmap(QPixmap(QString::fromUtf8(":/new/prefix1/Captura desde 2024-11-13 15-36-59.png")));
        label->raise();
        tableView->raise();
        pushButton->raise();

        retranslateUi(FormLista);

        QMetaObject::connectSlotsByName(FormLista);
    } // setupUi

    void retranslateUi(QWidget *FormLista)
    {
        FormLista->setWindowTitle(QCoreApplication::translate("FormLista", "Form", nullptr));
        pushButton->setText(QCoreApplication::translate("FormLista", "Mostrar usuarios", nullptr));
        label->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class FormLista: public Ui_FormLista {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FORMLISTA_H
