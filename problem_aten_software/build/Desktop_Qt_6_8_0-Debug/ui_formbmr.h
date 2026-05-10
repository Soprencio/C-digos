/********************************************************************************
** Form generated from reading UI file 'formbmr.ui'
**
** Created by: Qt User Interface Compiler version 6.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FORMBMR_H
#define UI_FORMBMR_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_FormBMR
{
public:
    QTextEdit *textEdit;
    QLabel *label;
    QLabel *label_2;
    QPushButton *adivinar;
    QPlainTextEdit *plainTextEdit;
    QPushButton *generar;
    QLineEdit *lineEdit_2;
    QComboBox *comboBox;
    QLabel *label_4;
    QLabel *label_5;
    QLineEdit *lineEdit;
    QLabel *label_3;

    void setupUi(QWidget *FormBMR)
    {
        if (FormBMR->objectName().isEmpty())
            FormBMR->setObjectName("FormBMR");
        FormBMR->resize(500, 500);
        FormBMR->setMinimumSize(QSize(500, 500));
        textEdit = new QTextEdit(FormBMR);
        textEdit->setObjectName("textEdit");
        textEdit->setEnabled(false);
        textEdit->setGeometry(QRect(270, 50, 201, 421));
        textEdit->setStyleSheet(QString::fromUtf8("background:rgb(170, 170, 255)"));
        label = new QLabel(FormBMR);
        label->setObjectName("label");
        label->setGeometry(QRect(60, 90, 161, 21));
        label->setStyleSheet(QString::fromUtf8("color:rgb(198, 70, 0)"));
        label_2 = new QLabel(FormBMR);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(60, 110, 151, 20));
        label_2->setStyleSheet(QString::fromUtf8("color:rgb(198, 70, 0)"));
        adivinar = new QPushButton(FormBMR);
        adivinar->setObjectName("adivinar");
        adivinar->setEnabled(false);
        adivinar->setGeometry(QRect(70, 170, 131, 26));
        adivinar->setStyleSheet(QString::fromUtf8("background:rgba(70, 10, 120, 0)"));
        plainTextEdit = new QPlainTextEdit(FormBMR);
        plainTextEdit->setObjectName("plainTextEdit");
        plainTextEdit->setEnabled(false);
        plainTextEdit->setGeometry(QRect(3, 219, 256, 121));
        plainTextEdit->setStyleSheet(QString::fromUtf8("background:rgba(191, 64, 64, 0);\n"
"color:rgb(198, 70, 0)"));
        generar = new QPushButton(FormBMR);
        generar->setObjectName("generar");
        generar->setGeometry(QRect(110, 60, 151, 25));
        generar->setStyleSheet(QString::fromUtf8("background:rgba(70, 10, 120, 0)"));
        lineEdit_2 = new QLineEdit(FormBMR);
        lineEdit_2->setObjectName("lineEdit_2");
        lineEdit_2->setGeometry(QRect(183, 265, 20, 20));
        lineEdit_2->setStyleSheet(QString::fromUtf8("background:rgba(191, 64, 64, 0)"));
        comboBox = new QComboBox(FormBMR);
        comboBox->setObjectName("comboBox");
        comboBox->setGeometry(QRect(10, 60, 86, 25));
        comboBox->setStyleSheet(QString::fromUtf8("background:rgba(70, 10, 120, 0)"));
        label_4 = new QLabel(FormBMR);
        label_4->setObjectName("label_4");
        label_4->setGeometry(QRect(0, 40, 121, 17));
        label_4->setStyleSheet(QString::fromUtf8("color:rgb(198, 70, 0)"));
        label_5 = new QLabel(FormBMR);
        label_5->setObjectName("label_5");
        label_5->setGeometry(QRect(50, 0, 401, 41));
        label_5->setStyleSheet(QString::fromUtf8("color:rgb(51, 209, 122);\n"
"font: 800 italic 20pt \"Ubuntu\";"));
        lineEdit = new QLineEdit(FormBMR);
        lineEdit->setObjectName("lineEdit");
        lineEdit->setGeometry(QRect(80, 140, 113, 26));
        lineEdit->setStyleSheet(QString::fromUtf8("background:rgb(170, 170, 255)"));
        label_3 = new QLabel(FormBMR);
        label_3->setObjectName("label_3");
        label_3->setGeometry(QRect(0, -10, 501, 511));
        label_3->setPixmap(QPixmap(QString::fromUtf8(":/new/prefix1/img123")));
        label_3->raise();
        lineEdit_2->raise();
        textEdit->raise();
        label->raise();
        label_2->raise();
        adivinar->raise();
        plainTextEdit->raise();
        generar->raise();
        comboBox->raise();
        label_4->raise();
        label_5->raise();
        lineEdit->raise();

        retranslateUi(FormBMR);

        QMetaObject::connectSlotsByName(FormBMR);
    } // setupUi

    void retranslateUi(QWidget *FormBMR)
    {
        FormBMR->setWindowTitle(QCoreApplication::translate("FormBMR", "Form", nullptr));
        label->setText(QCoreApplication::translate("FormBMR", "Ingrese un n\303\272mero de", nullptr));
        label_2->setText(QCoreApplication::translate("FormBMR", "4 Caracteres distintos", nullptr));
        adivinar->setText(QCoreApplication::translate("FormBMR", "Adivinar", nullptr));
#if QT_CONFIG(whatsthis)
        plainTextEdit->setWhatsThis(QCoreApplication::translate("FormBMR", "<html><head/><body><p align=\"justify\">Este juego trata de adivinar un n\303\272mero de 4 digitos al azar sin repetirse, al adivinar se muestran que n\303\272meros est\303\241n en su posici\303\263n, cuales no est\303\241n y cuales est\303\241n pero en otro sitio.</p></body></html>", nullptr));
#endif // QT_CONFIG(whatsthis)
        plainTextEdit->setPlainText(QCoreApplication::translate("FormBMR", "Este juego trata de adivinar un n\303\272mero de 4 digitos al azar sin repetirse, al adivinar se muestran que n\303\272meros est\303\241n en su posici\303\263n, cuales no est\303\241n y cuales est\303\241n pero en otro sitio.", nullptr));
        generar->setText(QCoreApplication::translate("FormBMR", "Generar N\303\272mero", nullptr));
        label_4->setText(QCoreApplication::translate("FormBMR", "Usuario Jugando", nullptr));
        label_5->setText(QCoreApplication::translate("FormBMR", "BUENOS, MALOS y REGULARES", nullptr));
        label_3->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class FormBMR: public Ui_FormBMR {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FORMBMR_H
