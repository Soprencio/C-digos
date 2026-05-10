/********************************************************************************
** Form generated from reading UI file 'formpago.ui'
**
** Created by: Qt User Interface Compiler version 6.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FORMPAGO_H
#define UI_FORMPAGO_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTableView>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_FormPago
{
public:
    QTableView *tableView;
    QPushButton *Mostrar;

    void setupUi(QWidget *FormPago)
    {
        if (FormPago->objectName().isEmpty())
            FormPago->setObjectName("FormPago");
        FormPago->resize(450, 450);
        FormPago->setMinimumSize(QSize(450, 450));
        tableView = new QTableView(FormPago);
        tableView->setObjectName("tableView");
        tableView->setGeometry(QRect(0, 90, 441, 231));
        Mostrar = new QPushButton(FormPago);
        Mostrar->setObjectName("Mostrar");
        Mostrar->setGeometry(QRect(0, 40, 121, 41));

        retranslateUi(FormPago);

        QMetaObject::connectSlotsByName(FormPago);
    } // setupUi

    void retranslateUi(QWidget *FormPago)
    {
        FormPago->setWindowTitle(QCoreApplication::translate("FormPago", "Form", nullptr));
        Mostrar->setText(QCoreApplication::translate("FormPago", "Mostrar Viajes", nullptr));
    } // retranslateUi

};

namespace Ui {
    class FormPago: public Ui_FormPago {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FORMPAGO_H
