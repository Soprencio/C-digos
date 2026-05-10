/********************************************************************************
** Form generated from reading UI file 'formsimon.ui'
**
** Created by: Qt User Interface Compiler version 6.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FORMSIMON_H
#define UI_FORMSIMON_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_FormSimon
{
public:
    QPushButton *Rojo;
    QPushButton *Verde;
    QPushButton *Azul;
    QPushButton *Amarillo;
    QPushButton *Comenzar;
    QComboBox *comboBox;
    QLabel *label;
    QLabel *label_2;
    QTextEdit *textEdit;
    QLabel *label_3;
    QLabel *label_4;

    void setupUi(QWidget *FormSimon)
    {
        if (FormSimon->objectName().isEmpty())
            FormSimon->setObjectName("FormSimon");
        FormSimon->resize(500, 500);
        FormSimon->setMinimumSize(QSize(500, 500));
        Rojo = new QPushButton(FormSimon);
        Rojo->setObjectName("Rojo");
        Rojo->setEnabled(false);
        Rojo->setGeometry(QRect(210, 30, 101, 101));
        Rojo->setStyleSheet(QString::fromUtf8(""));
        Verde = new QPushButton(FormSimon);
        Verde->setObjectName("Verde");
        Verde->setEnabled(false);
        Verde->setGeometry(QRect(310, 30, 101, 101));
        Verde->setStyleSheet(QString::fromUtf8(""));
        Azul = new QPushButton(FormSimon);
        Azul->setObjectName("Azul");
        Azul->setEnabled(false);
        Azul->setGeometry(QRect(210, 130, 101, 101));
        Azul->setStyleSheet(QString::fromUtf8(""));
        Amarillo = new QPushButton(FormSimon);
        Amarillo->setObjectName("Amarillo");
        Amarillo->setEnabled(false);
        Amarillo->setGeometry(QRect(310, 130, 101, 101));
        Amarillo->setStyleSheet(QString::fromUtf8(""));
        Comenzar = new QPushButton(FormSimon);
        Comenzar->setObjectName("Comenzar");
        Comenzar->setGeometry(QRect(50, 150, 101, 41));
        Comenzar->setStyleSheet(QString::fromUtf8("background:rgba(70, 10, 120, 0)"));
        comboBox = new QComboBox(FormSimon);
        comboBox->setObjectName("comboBox");
        comboBox->setGeometry(QRect(60, 110, 86, 26));
        comboBox->setStyleSheet(QString::fromUtf8("background:rgba(70, 10, 120, 0)"));
        label = new QLabel(FormSimon);
        label->setObjectName("label");
        label->setGeometry(QRect(50, 70, 121, 20));
        label->setStyleSheet(QString::fromUtf8("color:rgb(198, 70, 0)"));
        label_2 = new QLabel(FormSimon);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(50, 90, 121, 20));
        label_2->setStyleSheet(QString::fromUtf8("color:rgb(198, 70, 0)"));
        textEdit = new QTextEdit(FormSimon);
        textEdit->setObjectName("textEdit");
        textEdit->setEnabled(false);
        textEdit->setGeometry(QRect(20, 240, 431, 141));
        textEdit->setStyleSheet(QString::fromUtf8("background:rgba(191, 64, 64, 0);\n"
"color:rgb(198, 70, 0)"));
        label_3 = new QLabel(FormSimon);
        label_3->setObjectName("label_3");
        label_3->setGeometry(QRect(10, 20, 191, 31));
        label_3->setStyleSheet(QString::fromUtf8("color:rgb(224, 27, 36);\n"
"font: 800 italic 20pt \"Ubuntu Sans\";"));
        label_3->setLineWidth(1);
        label_4 = new QLabel(FormSimon);
        label_4->setObjectName("label_4");
        label_4->setGeometry(QRect(-10, -10, 511, 511));
        label_4->setPixmap(QPixmap(QString::fromUtf8(":/new/prefix1/img123")));
        label_4->raise();
        Rojo->raise();
        Verde->raise();
        Azul->raise();
        Amarillo->raise();
        Comenzar->raise();
        comboBox->raise();
        label->raise();
        label_2->raise();
        textEdit->raise();
        label_3->raise();

        retranslateUi(FormSimon);

        QMetaObject::connectSlotsByName(FormSimon);
    } // setupUi

    void retranslateUi(QWidget *FormSimon)
    {
        FormSimon->setWindowTitle(QCoreApplication::translate("FormSimon", "Form", nullptr));
        Rojo->setText(QCoreApplication::translate("FormSimon", "Rojo", nullptr));
        Verde->setText(QCoreApplication::translate("FormSimon", "Verde", nullptr));
        Azul->setText(QCoreApplication::translate("FormSimon", "Azul", nullptr));
        Amarillo->setText(QCoreApplication::translate("FormSimon", "Amarillo", nullptr));
        Comenzar->setText(QCoreApplication::translate("FormSimon", "Jugar", nullptr));
        label->setText(QCoreApplication::translate("FormSimon", "\302\277Cu\303\241l usuario", nullptr));
        label_2->setText(QCoreApplication::translate("FormSimon", "Est\303\241 jugando ?", nullptr));
        textEdit->setHtml(QCoreApplication::translate("FormSimon", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu Sans';\">Al darle a jugar, un boton al azar se prender\303\241 de color, debes apretar ese boton y darle devuelta a jugar, si adivinas, al color anterior se le sumar\303\241 uno nuevo teniendo que adivinar 2 colores ahora, y as\303\255 cada ronda, agregando un nuevo color y haci\303\251ndolo cada vez m\303\241s r\303\241pido y dificil!!</span></p></body></html>", nullptr));
        label_3->setText(QCoreApplication::translate("FormSimon", "SIMON SAYS", nullptr));
        label_4->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class FormSimon: public Ui_FormSimon {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FORMSIMON_H
