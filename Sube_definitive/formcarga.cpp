#include "formcarga.h"
#include "ui_formcarga.h"

FormCarga::FormCarga(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::FormCarga)
{
    ui->setupUi(this);
    db.setHostName("localhost");
    db.setUserName("root");
    db.setPassword("12341234");
    db.setDatabaseName("LAMIBE");

    if(!db.open())
    {
        qDebug() << "Error al Conectar: " << db.lastError().text();
    }
    else
    {
        QSqlQuery consulta("SELECT nombre FROM usuario",db);
        QSqlQueryModel *modelo = new QSqlQueryModel;
        modelo->setQuery(consulta);
        ui->Usuario->setModel(modelo);
    }
    db.close();
}

FormCarga::~FormCarga()
{
    delete ui;
}

void FormCarga::on_Carga_clicked()
{
    sald = ui->Cuenta->currentText().toDouble();
    user = ui->Usuario->currentIndex()+1;
    if(!db.open())
    {
        qDebug() << "Error al Conectar: " << db.lastError().text();
    }
    else
    {
        QSqlQuery consulta(db);
        consulta.prepare("UPDATE usuario SET saldo_sube = :sal WHERE id_usr = :num");
        double aux = ui->Aument->text().toDouble();
        aux = aux + sald;
        if(aux>9999)
        {
            ui->label_5->setText("Saldo máximo de 9999");
            aux = 9999.0;
        }
        consulta.bindValue(":sal",aux);
        consulta.bindValue(":num",user);
        consulta.exec();
    }
    QMessageBox msgbox;
    msgbox.setWindowTitle("Carga Exitosa");
    msgbox.setText("Has cargado saldo a usuario "+ui->Usuario->itemText(user-1));
    msgbox.setStandardButtons(QMessageBox::Ok);
    msgbox.setIcon(QMessageBox::Information);
    msgbox.setGeometry(100,100,200,200);
    msgbox.exec();
    db.close();

}
void FormCarga::on_Mostrar_clicked()
{
    if(!db.open())
    {
        qDebug() << "Error al Conectar: " << db.lastError().text();
    }
    else
    {
        QSqlQuery consulta2(db);
        consulta2.prepare("SELECT saldo_sube FROM usuario WHERE id_usr = :sal");
        consulta2.bindValue(":sal",int((ui->Usuario->currentIndex())+1));
        consulta2.exec();
        QSqlQueryModel *modelo = new QSqlQueryModel;
        modelo->setQuery(consulta2);
        ui->Cuenta->setModel(modelo);
    }
    db.close();
}
