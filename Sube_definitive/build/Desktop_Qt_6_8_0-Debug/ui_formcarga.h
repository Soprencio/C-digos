/********************************************************************************
** Form generated from reading UI file 'formcarga.ui'
**
** Created by: Qt User Interface Compiler version 6.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FORMCARGA_H
#define UI_FORMCARGA_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_FormCarga
{
public:
    QLabel *label;
    QPushButton *Carga;
    QLabel *label_3;
    QLabel *label_2;
    QPushButton *Mostrar;
    QComboBox *Cuenta;
    QComboBox *Usuario;
    QLabel *label_4;
    QLabel *label_5;
    QSpinBox *Aument;

    void setupUi(QWidget *FormCarga)
    {
        if (FormCarga->objectName().isEmpty())
            FormCarga->setObjectName("FormCarga");
        FormCarga->resize(450, 450);
        FormCarga->setMinimumSize(QSize(450, 450));
        label = new QLabel(FormCarga);
        label->setObjectName("label");
        label->setGeometry(QRect(20, 40, 111, 17));
        Carga = new QPushButton(FormCarga);
        Carga->setObjectName("Carga");
        Carga->setGeometry(QRect(10, 250, 131, 31));
        label_3 = new QLabel(FormCarga);
        label_3->setObjectName("label_3");
        label_3->setGeometry(QRect(280, 40, 121, 20));
        label_2 = new QLabel(FormCarga);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(160, 40, 111, 20));
        Mostrar = new QPushButton(FormCarga);
        Mostrar->setObjectName("Mostrar");
        Mostrar->setGeometry(QRect(280, 110, 111, 25));
        Cuenta = new QComboBox(FormCarga);
        Cuenta->setObjectName("Cuenta");
        Cuenta->setEnabled(false);
        Cuenta->setGeometry(QRect(170, 60, 86, 25));
        Usuario = new QComboBox(FormCarga);
        Usuario->setObjectName("Usuario");
        Usuario->setGeometry(QRect(290, 60, 86, 25));
        label_4 = new QLabel(FormCarga);
        label_4->setObjectName("label_4");
        label_4->setGeometry(QRect(150, 260, 181, 18));
        label_5 = new QLabel(FormCarga);
        label_5->setObjectName("label_5");
        label_5->setGeometry(QRect(10, 100, 181, 18));
        Aument = new QSpinBox(FormCarga);
        Aument->setObjectName("Aument");
        Aument->setGeometry(QRect(20, 60, 111, 26));
        Aument->setMinimum(1);
        Aument->setMaximum(9999);

        retranslateUi(FormCarga);

        QMetaObject::connectSlotsByName(FormCarga);
    } // setupUi

    void retranslateUi(QWidget *FormCarga)
    {
        FormCarga->setWindowTitle(QCoreApplication::translate("FormCarga", "Form", nullptr));
        label->setText(QCoreApplication::translate("FormCarga", "Cuanto Cargar", nullptr));
        Carga->setText(QCoreApplication::translate("FormCarga", "Cargar Saldo", nullptr));
        label_3->setText(QCoreApplication::translate("FormCarga", "Usuario a cargar", nullptr));
        label_2->setText(QCoreApplication::translate("FormCarga", "Saldo en cuenta", nullptr));
        Mostrar->setText(QCoreApplication::translate("FormCarga", "Mostrar Saldo", nullptr));
        label_4->setText(QString());
        label_5->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class FormCarga: public Ui_FormCarga {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FORMCARGA_H
