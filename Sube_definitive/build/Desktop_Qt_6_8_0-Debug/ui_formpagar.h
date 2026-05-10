/********************************************************************************
** Form generated from reading UI file 'formpagar.ui'
**
** Created by: Qt User Interface Compiler version 6.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FORMPAGAR_H
#define UI_FORMPAGAR_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_FormPagar
{
public:
    QComboBox *ramal;
    QLabel *label;
    QComboBox *parada1;
    QLabel *label_2;
    QPushButton *Mostrar_precio;
    QPushButton *Cofirm_ram_us;
    QComboBox *parada2;
    QLabel *label_3;
    QComboBox *usuario;
    QLabel *label_5;
    QLabel *label_6;
    QComboBox *saldo;
    QLabel *label_7;
    QPushButton *pagar_viaje;
    QLineEdit *precio;
    QComboBox *tarifa;
    QLabel *label_8;
    QLabel *label_9;
    QLabel *label_10;
    QLineEdit *ramal_sel;
    QLineEdit *usuario_sel;
    QComboBox *linea;
    QLabel *label_4;
    QLabel *label_11;
    QLabel *label_12;
    QLabel *label_13;
    QLineEdit *contrase;
    QLabel *label_14;
    QComboBox *comboBox;

    void setupUi(QWidget *FormPagar)
    {
        if (FormPagar->objectName().isEmpty())
            FormPagar->setObjectName("FormPagar");
        FormPagar->resize(550, 550);
        FormPagar->setMinimumSize(QSize(550, 550));
        ramal = new QComboBox(FormPagar);
        ramal->setObjectName("ramal");
        ramal->setEnabled(false);
        ramal->setGeometry(QRect(10, 80, 201, 21));
        label = new QLabel(FormPagar);
        label->setObjectName("label");
        label->setGeometry(QRect(10, 60, 121, 18));
        parada1 = new QComboBox(FormPagar);
        parada1->setObjectName("parada1");
        parada1->setEnabled(false);
        parada1->setGeometry(QRect(10, 170, 201, 21));
        label_2 = new QLabel(FormPagar);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(10, 150, 131, 18));
        Mostrar_precio = new QPushButton(FormPagar);
        Mostrar_precio->setObjectName("Mostrar_precio");
        Mostrar_precio->setEnabled(false);
        Mostrar_precio->setGeometry(QRect(10, 200, 391, 31));
        Mostrar_precio->setStyleSheet(QString::fromUtf8("background: lime"));
        Cofirm_ram_us = new QPushButton(FormPagar);
        Cofirm_ram_us->setObjectName("Cofirm_ram_us");
        Cofirm_ram_us->setEnabled(false);
        Cofirm_ram_us->setGeometry(QRect(10, 110, 391, 26));
        Cofirm_ram_us->setStyleSheet(QString::fromUtf8("background: lime"));
        parada2 = new QComboBox(FormPagar);
        parada2->setObjectName("parada2");
        parada2->setEnabled(false);
        parada2->setGeometry(QRect(220, 170, 181, 21));
        label_3 = new QLabel(FormPagar);
        label_3->setObjectName("label_3");
        label_3->setGeometry(QRect(240, 150, 141, 18));
        usuario = new QComboBox(FormPagar);
        usuario->setObjectName("usuario");
        usuario->setEnabled(false);
        usuario->setGeometry(QRect(220, 80, 181, 21));
        label_5 = new QLabel(FormPagar);
        label_5->setObjectName("label_5");
        label_5->setGeometry(QRect(240, 60, 141, 18));
        label_6 = new QLabel(FormPagar);
        label_6->setObjectName("label_6");
        label_6->setGeometry(QRect(430, 120, 121, 20));
        saldo = new QComboBox(FormPagar);
        saldo->setObjectName("saldo");
        saldo->setEnabled(false);
        saldo->setGeometry(QRect(450, 140, 91, 31));
        saldo->setStyleSheet(QString::fromUtf8("background: lightgrey"));
        label_7 = new QLabel(FormPagar);
        label_7->setObjectName("label_7");
        label_7->setGeometry(QRect(220, 250, 81, 20));
        pagar_viaje = new QPushButton(FormPagar);
        pagar_viaje->setObjectName("pagar_viaje");
        pagar_viaje->setEnabled(false);
        pagar_viaje->setGeometry(QRect(10, 270, 151, 26));
        pagar_viaje->setStyleSheet(QString::fromUtf8("background: lime"));
        precio = new QLineEdit(FormPagar);
        precio->setObjectName("precio");
        precio->setEnabled(false);
        precio->setGeometry(QRect(200, 270, 131, 31));
        precio->setStyleSheet(QString::fromUtf8("background: lightgrey"));
        tarifa = new QComboBox(FormPagar);
        tarifa->setObjectName("tarifa");
        tarifa->setEnabled(false);
        tarifa->setGeometry(QRect(450, 60, 91, 31));
        tarifa->setStyleSheet(QString::fromUtf8("background: lightgrey"));
        label_8 = new QLabel(FormPagar);
        label_8->setObjectName("label_8");
        label_8->setGeometry(QRect(450, 40, 91, 20));
        label_9 = new QLabel(FormPagar);
        label_9->setObjectName("label_9");
        label_9->setGeometry(QRect(450, 190, 91, 20));
        label_10 = new QLabel(FormPagar);
        label_10->setObjectName("label_10");
        label_10->setGeometry(QRect(450, 250, 91, 20));
        ramal_sel = new QLineEdit(FormPagar);
        ramal_sel->setObjectName("ramal_sel");
        ramal_sel->setEnabled(false);
        ramal_sel->setGeometry(QRect(410, 210, 131, 31));
        ramal_sel->setStyleSheet(QString::fromUtf8("background: lightgrey"));
        usuario_sel = new QLineEdit(FormPagar);
        usuario_sel->setObjectName("usuario_sel");
        usuario_sel->setEnabled(false);
        usuario_sel->setGeometry(QRect(410, 270, 131, 31));
        usuario_sel->setStyleSheet(QString::fromUtf8("background: lightgrey"));
        linea = new QComboBox(FormPagar);
        linea->setObjectName("linea");
        linea->setEnabled(true);
        linea->setGeometry(QRect(10, 30, 391, 21));
        label_4 = new QLabel(FormPagar);
        label_4->setObjectName("label_4");
        label_4->setGeometry(QRect(10, 10, 121, 18));
        label_11 = new QLabel(FormPagar);
        label_11->setObjectName("label_11");
        label_11->setGeometry(QRect(200, 300, 181, 31));
        label_12 = new QLabel(FormPagar);
        label_12->setObjectName("label_12");
        label_12->setGeometry(QRect(200, 320, 161, 31));
        label_13 = new QLabel(FormPagar);
        label_13->setObjectName("label_13");
        label_13->setGeometry(QRect(200, 340, 161, 31));
        contrase = new QLineEdit(FormPagar);
        contrase->setObjectName("contrase");
        contrase->setGeometry(QRect(10, 330, 151, 25));
        label_14 = new QLabel(FormPagar);
        label_14->setObjectName("label_14");
        label_14->setGeometry(QRect(10, 300, 161, 31));
        comboBox = new QComboBox(FormPagar);
        comboBox->setObjectName("comboBox");
        comboBox->setEnabled(false);
        comboBox->setGeometry(QRect(460, 280, 20, 20));
        comboBox->setStyleSheet(QString::fromUtf8("background:rgba(191, 64, 64, 0)"));
        comboBox->raise();
        ramal->raise();
        label->raise();
        parada1->raise();
        label_2->raise();
        Mostrar_precio->raise();
        Cofirm_ram_us->raise();
        parada2->raise();
        label_3->raise();
        usuario->raise();
        label_5->raise();
        label_6->raise();
        saldo->raise();
        label_7->raise();
        pagar_viaje->raise();
        precio->raise();
        tarifa->raise();
        label_8->raise();
        label_9->raise();
        label_10->raise();
        ramal_sel->raise();
        usuario_sel->raise();
        linea->raise();
        label_4->raise();
        label_11->raise();
        label_12->raise();
        label_13->raise();
        contrase->raise();
        label_14->raise();

        retranslateUi(FormPagar);

        QMetaObject::connectSlotsByName(FormPagar);
    } // setupUi

    void retranslateUi(QWidget *FormPagar)
    {
        FormPagar->setWindowTitle(QCoreApplication::translate("FormPagar", "Form", nullptr));
        label->setText(QCoreApplication::translate("FormPagar", "Selecciona Ramal", nullptr));
        label_2->setText(QCoreApplication::translate("FormPagar", "Estaci\303\263n de Partida", nullptr));
        Mostrar_precio->setText(QCoreApplication::translate("FormPagar", "Mostrar Precio del trayecto", nullptr));
        Cofirm_ram_us->setText(QCoreApplication::translate("FormPagar", "Confirmar Ramal y Usuario", nullptr));
        label_3->setText(QCoreApplication::translate("FormPagar", "Estaci\303\263n de Llegada", nullptr));
        label_5->setText(QCoreApplication::translate("FormPagar", "Selecciona Usuario", nullptr));
        label_6->setText(QCoreApplication::translate("FormPagar", "Saldo Disponible", nullptr));
        label_7->setText(QCoreApplication::translate("FormPagar", "Precio Final ", nullptr));
        pagar_viaje->setText(QCoreApplication::translate("FormPagar", "Confirmar Trayecto", nullptr));
        label_8->setText(QCoreApplication::translate("FormPagar", "Tarifa Social", nullptr));
        label_9->setText(QCoreApplication::translate("FormPagar", "Ramal Selec.", nullptr));
        label_10->setText(QCoreApplication::translate("FormPagar", "User Selec.", nullptr));
        label_4->setText(QCoreApplication::translate("FormPagar", "Selecciona l\303\255nea", nullptr));
        label_11->setText(QCoreApplication::translate("FormPagar", "Saldo m\303\255nimo para viajar:", nullptr));
        label_12->setText(QCoreApplication::translate("FormPagar", "Sin tarifa: $50", nullptr));
        label_13->setText(QCoreApplication::translate("FormPagar", "Con tarifa: $-152.50", nullptr));
        label_14->setText(QCoreApplication::translate("FormPagar", "Contrase\303\261a:", nullptr));
    } // retranslateUi

};

namespace Ui {
    class FormPagar: public Ui_FormPagar {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FORMPAGAR_H
