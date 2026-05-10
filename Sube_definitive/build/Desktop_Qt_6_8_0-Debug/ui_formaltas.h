/********************************************************************************
** Form generated from reading UI file 'formaltas.ui'
**
** Created by: Qt User Interface Compiler version 6.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FORMALTAS_H
#define UI_FORMALTAS_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_FormAltas
{
public:
    QLineEdit *Nombre;
    QLineEdit *Apellido;
    QLabel *label;
    QLabel *label_2;
    QLabel *label_3;
    QLabel *label_4;
    QPushButton *Alta;
    QComboBox *Tarifa;
    QSpinBox *spinBox;

    void setupUi(QWidget *FormAltas)
    {
        if (FormAltas->objectName().isEmpty())
            FormAltas->setObjectName("FormAltas");
        FormAltas->resize(450, 320);
        FormAltas->setMinimumSize(QSize(450, 320));
        Nombre = new QLineEdit(FormAltas);
        Nombre->setObjectName("Nombre");
        Nombre->setGeometry(QRect(260, 30, 113, 25));
        Apellido = new QLineEdit(FormAltas);
        Apellido->setObjectName("Apellido");
        Apellido->setGeometry(QRect(260, 100, 113, 25));
        label = new QLabel(FormAltas);
        label->setObjectName("label");
        label->setGeometry(QRect(270, 230, 91, 20));
        label_2 = new QLabel(FormAltas);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(290, 10, 67, 17));
        label_3 = new QLabel(FormAltas);
        label_3->setObjectName("label_3");
        label_3->setGeometry(QRect(276, 80, 81, 20));
        label_4 = new QLabel(FormAltas);
        label_4->setObjectName("label_4");
        label_4->setGeometry(QRect(300, 150, 67, 17));
        Alta = new QPushButton(FormAltas);
        Alta->setObjectName("Alta");
        Alta->setGeometry(QRect(0, 250, 141, 41));
        Tarifa = new QComboBox(FormAltas);
        Tarifa->addItem(QString());
        Tarifa->addItem(QString());
        Tarifa->setObjectName("Tarifa");
        Tarifa->setGeometry(QRect(270, 260, 86, 25));
        spinBox = new QSpinBox(FormAltas);
        spinBox->setObjectName("spinBox");
        spinBox->setGeometry(QRect(270, 170, 101, 26));
        spinBox->setMaximum(9999);

        retranslateUi(FormAltas);

        QMetaObject::connectSlotsByName(FormAltas);
    } // setupUi

    void retranslateUi(QWidget *FormAltas)
    {
        FormAltas->setWindowTitle(QCoreApplication::translate("FormAltas", "Alta", nullptr));
        label->setText(QCoreApplication::translate("FormAltas", "Tarifa Social", nullptr));
        label_2->setText(QCoreApplication::translate("FormAltas", "Nombre", nullptr));
        label_3->setText(QCoreApplication::translate("FormAltas", "Contrase\303\261a", nullptr));
        label_4->setText(QCoreApplication::translate("FormAltas", "Saldo", nullptr));
        Alta->setText(QCoreApplication::translate("FormAltas", "Hacer Alta", nullptr));
        Tarifa->setItemText(0, QCoreApplication::translate("FormAltas", "Si", nullptr));
        Tarifa->setItemText(1, QCoreApplication::translate("FormAltas", "No", nullptr));

    } // retranslateUi

};

namespace Ui {
    class FormAltas: public Ui_FormAltas {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FORMALTAS_H
