#include "formuser.h"
#include "ui_formuser.h"

FormUser::FormUser(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::FormUser)
{
    ui->setupUi(this);
}

FormUser::~FormUser()
{
    delete ui;
}

void FormUser::on_pushButton_clicked()
{
    QSqlDatabase db = QSqlDatabase::addDatabase("QMYSQL");
    db.setHostName("localhost");
    db.setUserName("root");
    db.setPassword("12341234");
    db.setDatabaseName("Problem_aten");

    if(!db.open())
    {
        qDebug() << "Error al Conectar: " << db.lastError().text();
    }
    else
    {
        QString aux = ui->lineEdit->text();
        QString aux2 = ui->lineEdit_2->text();
        if(aux != "" && aux2 != "")
        {
            if(aux.size()<=40 && aux2.size()<=40)
            {
                QSqlQuery consulta(db);
                consulta.prepare("INSERT INTO Usuario(nombre, apellido) values(:nom, :ape)");
                consulta.bindValue(":nom",ui->lineEdit->text());
                consulta.bindValue(":ape",ui->lineEdit_2->text());
                consulta.exec();
                qDebug() << ui->lineEdit->text();
                QMessageBox msgbox;
                msgbox.setWindowTitle("Usuario Cargado");
                msgbox.setText("Se ha cargado un nuevo usuario");
                msgbox.setStandardButtons(QMessageBox::Ok);
                msgbox.setIcon(QMessageBox::Information);
                msgbox.setGeometry(100,100,200,200);
                msgbox.exec();
                ui->lineEdit->clear();
                ui->lineEdit_2->clear();
            }
            else
            {
                QMessageBox error2;
                error2.setWindowTitle("Error al cargar");
                error2.setText("No puedes escribir más de 40 caracteres");
                error2.setStandardButtons(QMessageBox::Ok);
                error2.setIcon(QMessageBox::Information);
                error2.setGeometry(100,100,200,200);
                error2.exec();
            }
        }
        else
        {
            QMessageBox error;
            error.setWindowTitle("Error al cargar");
            error.setText("No puedes dejar los campos nombre y apellido vacíos");
            error.setStandardButtons(QMessageBox::Ok);
            error.setIcon(QMessageBox::Information);
            error.setGeometry(100,100,200,200);
            error.exec();
        }
    }
    db.close();
}

