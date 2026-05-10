/********************************************************************************
** Form generated from reading UI file 'formlistado.ui'
**
** Created by: Qt User Interface Compiler version 6.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FORMLISTADO_H
#define UI_FORMLISTADO_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTableView>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_FormListado
{
public:
    QTableView *tableView;
    QPushButton *Mostrar;

    void setupUi(QWidget *FormListado)
    {
        if (FormListado->objectName().isEmpty())
            FormListado->setObjectName("FormListado");
        FormListado->resize(450, 507);
        FormListado->setMinimumSize(QSize(450, 450));
        FormListado->setMaximumSize(QSize(1000, 1000));
        tableView = new QTableView(FormListado);
        tableView->setObjectName("tableView");
        tableView->setGeometry(QRect(0, 90, 400, 300));
        tableView->setMinimumSize(QSize(200, 100));
        tableView->setMaximumSize(QSize(400, 400));
        tableView->setBaseSize(QSize(200, 200));
        Mostrar = new QPushButton(FormListado);
        Mostrar->setObjectName("Mostrar");
        Mostrar->setGeometry(QRect(0, 20, 111, 41));

        retranslateUi(FormListado);

        QMetaObject::connectSlotsByName(FormListado);
    } // setupUi

    void retranslateUi(QWidget *FormListado)
    {
        FormListado->setWindowTitle(QCoreApplication::translate("FormListado", "Form", nullptr));
        Mostrar->setText(QCoreApplication::translate("FormListado", "Listado", nullptr));
    } // retranslateUi

};

namespace Ui {
    class FormListado: public Ui_FormListado {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FORMLISTADO_H
