/********************************************************************************
** Form generated from reading UI file 'formuser.ui'
**
** Created by: Qt User Interface Compiler version 6.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FORMUSER_H
#define UI_FORMUSER_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_FormUser
{
public:
    QLabel *label;
    QLabel *label_2;
    QLineEdit *lineEdit;
    QLineEdit *lineEdit_2;
    QPushButton *pushButton;
    QLabel *label_3;

    void setupUi(QWidget *FormUser)
    {
        if (FormUser->objectName().isEmpty())
            FormUser->setObjectName("FormUser");
        FormUser->resize(200, 200);
        FormUser->setMinimumSize(QSize(200, 200));
        label = new QLabel(FormUser);
        label->setObjectName("label");
        label->setGeometry(QRect(60, 10, 66, 18));
        label->setStyleSheet(QString::fromUtf8("color:rgb(198, 70, 0);\n"
"font: 700 11pt \"Ubuntu\";"));
        label_2 = new QLabel(FormUser);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(60, 70, 66, 18));
        label_2->setStyleSheet(QString::fromUtf8("color:rgb(198, 70, 0);\n"
"font: 700 11pt \"Ubuntu\";"));
        lineEdit = new QLineEdit(FormUser);
        lineEdit->setObjectName("lineEdit");
        lineEdit->setGeometry(QRect(40, 40, 111, 26));
        lineEdit->setMinimumSize(QSize(0, 0));
        lineEdit->setStyleSheet(QString::fromUtf8("background:rgba(142, 233, 44, 190)"));
        lineEdit_2 = new QLineEdit(FormUser);
        lineEdit_2->setObjectName("lineEdit_2");
        lineEdit_2->setGeometry(QRect(40, 90, 113, 26));
        lineEdit_2->setStyleSheet(QString::fromUtf8("background:rgba(142, 233, 44, 190)"));
        pushButton = new QPushButton(FormUser);
        pushButton->setObjectName("pushButton");
        pushButton->setGeometry(QRect(40, 130, 111, 26));
        pushButton->setStyleSheet(QString::fromUtf8("background:rgb(246, 97, 81)"));
        label_3 = new QLabel(FormUser);
        label_3->setObjectName("label_3");
        label_3->setGeometry(QRect(-4, -14, 211, 221));
        label_3->setPixmap(QPixmap(QString::fromUtf8(":/new/prefix1/Captura desde 2024-11-13 15-36-59.png")));
        label_3->raise();
        label->raise();
        label_2->raise();
        lineEdit->raise();
        lineEdit_2->raise();
        pushButton->raise();

        retranslateUi(FormUser);

        QMetaObject::connectSlotsByName(FormUser);
    } // setupUi

    void retranslateUi(QWidget *FormUser)
    {
        FormUser->setWindowTitle(QCoreApplication::translate("FormUser", "Form", nullptr));
        label->setText(QCoreApplication::translate("FormUser", "Nombre:", nullptr));
        label_2->setText(QCoreApplication::translate("FormUser", "Apellido:", nullptr));
        pushButton->setText(QCoreApplication::translate("FormUser", "Cargar Usuario", nullptr));
        label_3->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class FormUser: public Ui_FormUser {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FORMUSER_H
