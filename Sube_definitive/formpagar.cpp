#include "formpagar.h"
#include "ui_formpagar.h"

FormPagar::FormPagar(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::FormPagar)
{
    ui->setupUi(this);
    qdb.setHostName("localhost");
    qdb.setUserName("root");
    qdb.setPassword("12341234");
    qdb.setDatabaseName("LAMIBE");
    if(!qdb.open())
    {
        qDebug() << "Error al Conectar: " << qdb.lastError().text();
    }
    else
    {
        QSqlQuery consulta("SELECT nom_lin FROM linea",qdb);
        QSqlQueryModel *modelo = new QSqlQueryModel;
        modelo->setQuery(consulta);
        ui->linea->setModel(modelo);
    }
    qdb.close();
}

FormPagar::~FormPagar()
{
    delete ui;
}

void FormPagar::on_Cofirm_ram_us_clicked()
{
    ui->ramal_sel->setText(ui->ramal->currentText());
    ui->usuario_sel->setText(ui->usuario->currentText());
    user = ui->usuario->currentIndex()+1;
    ram = QString::number(ui->ramal->currentIndex()+1);
    if(!qdb.open())
    {

        qDebug() << "Error al Conectar: " << qdb.lastError().text();
    }
    else
    {
        QSqlQuery consulta(qdb);
        consulta.prepare("SELECT e.nom_est FROM parada p INNER JOIN estacion e ON p.id_est = e.id_est WHERE id_ram = :ram");
        consulta.bindValue(":ram",int((ui->ramal->currentIndex())+1));
        consulta.exec();
        QSqlQueryModel *modelo = new QSqlQueryModel;
        modelo->setQuery(consulta);
        ui->parada1->setModel(modelo);
        ui->parada2->setModel(modelo);
        QSqlQuery consulta2(qdb);
        consulta2.prepare("SELECT saldo_sube FROM usuario WHERE id_usr = :sal");
        consulta2.bindValue(":sal",user);
        consulta2.exec();
        QSqlQueryModel *modelo2 = new QSqlQueryModel;
        modelo2->setQuery(consulta2);
        QSqlQuery consulta3(qdb);
        consulta3.prepare("SELECT tarifa FROM usuario WHERE id_usr = :tar");
        consulta3.bindValue(":tar",user);
        consulta3.exec();
        QSqlQueryModel *modelo3 = new QSqlQueryModel;
        modelo3->setQuery(consulta3);
        ui->saldo->setModel(modelo2);
        ui->tarifa->setModel(modelo3);
        ui->parada1->setEnabled(true);
        ui->parada2->setEnabled(true);
        ui->Mostrar_precio->setEnabled(true);
        ui->pagar_viaje->setEnabled(false);
    }
    qdb.close();
}

void FormPagar::on_Mostrar_precio_clicked()
{
    pri = ui->parada1->currentText();
    seg = ui->parada2->currentText();
    sald = ui->saldo->currentText().toInt();
    QString tar = ui->tarifa->currentText();
    int prim = ui->parada1->currentIndex()+1;
    int ult = ui->parada2->currentIndex()+1;
    if(prim == ult)
    {
        QMessageBox msgbox;
        msgbox.setWindowTitle("Error");
        msgbox.setText("No se puede seleccionar la misma parada");
        msgbox.setStandardButtons(QMessageBox::Ok);
        msgbox.setIcon(QMessageBox::Information);
        msgbox.setGeometry(100,100,200,200);
        msgbox.exec();
    }
    else
    {
        ui->pagar_viaje->setEnabled(true);
        if(tar == QString("No"))
        {
            if(ult-prim<5 && ult-prim>-5)
            {
                ui->precio->setText("280");
            }
            else if((ult-prim>=5 && ult-prim<10) || (ult-prim<=-5 && ult-prim>-10))
            {
                ui->precio->setText("360");
            }
            else
            {
                ui->precio->setText("450");
            }
        }
        else
        {
            if(ult-prim<5 && ult-prim>-5)
            {
                ui->precio->setText("154");
            }
            else if((ult-prim>=5 && ult-prim<10) || (ult-prim<=-5 && ult-prim>-10))
            {
                ui->precio->setText("198");
            }
            else
            {
                ui->precio->setText("247.50");
            }
        }
    }
}


void FormPagar::on_pagar_viaje_clicked()
{
    int aux = 0, aux2 = 0;
    if(!qdb.open())
    {
        qDebug() << "Error al Conectar: " << qdb.lastError().text();
    }
    else
    {
        QString tar = ui->tarifa->currentText();
        QSqlQuery contra(qdb);
        contra.prepare("SELECT passw FROM usuario WHERE id_usr = :psw");
        contra.bindValue(":psw",user);
        contra.exec();
        QSqlQueryModel *model = new QSqlQueryModel;
        model->setQuery(contra);
        ui->comboBox->setModel(model);
        if(ui->tarifa->currentText() == "Si")
        {
            sald = sald - 247.5;
        }
        else
        {
            sald = sald - 450.0;
        }
        if(sald>=-400)
        {
            if(QString(ui->contrase->text())==QString(ui->comboBox->currentText()))
            {
                aux = 1;
            }
            else
            {
                QMessageBox msgbox;
                msgbox.setWindowTitle("Error");
                msgbox.setText("Contraseña incorrecta");
                msgbox.setStandardButtons(QMessageBox::Ok);
                msgbox.setIcon(QMessageBox::Information);
                msgbox.setGeometry(100,100,200,200);
                msgbox.exec();
                aux2 = 1;
            }
            if(ui->tarifa->currentText() == "Si")
            {
                sald = sald + 247.5 - ui->precio->text().toDouble();
            }
            else
            {
                sald = sald + 450.0 - ui->precio->text().toDouble();
            }
        }
        if(aux==1)
        {
            QSqlQuery consulta(qdb);
            consulta.prepare("INSERT INTO viajes(pri_est, ult_est, id_ram, costo, id_usr) values(:pes, :ues, :idr, :cos, :idu)");
            consulta.bindValue(":pes",pri);
            consulta.bindValue(":ues",seg);
            consulta.bindValue(":idr",ram);
            consulta.bindValue(":cos",ui->precio->text());
            consulta.bindValue(":idu",user);
            consulta.exec();
            QSqlQuery consulta2(qdb);
            consulta2.prepare("UPDATE usuario SET saldo_sube = :sal WHERE id_usr = :num");
            consulta2.bindValue(":sal",sald);
            consulta2.bindValue(":num",ui->usuario->currentIndex()+1);
            consulta2.exec();
            QMessageBox msgbox;
            msgbox.setWindowTitle("Viaje Exitoso");
            msgbox.setText("Has hecho un viaje");
            msgbox.setStandardButtons(QMessageBox::Ok);
            msgbox.setIcon(QMessageBox::Information);
            msgbox.setGeometry(100,100,200,200);
            msgbox.exec();
        }
        else if(aux2==0)
        {
            QMessageBox msgbox;
            msgbox.setWindowTitle("Error");
            msgbox.setText("Saldo Insuficiente");
            msgbox.setStandardButtons(QMessageBox::Ok);
            msgbox.setIcon(QMessageBox::Information);
            msgbox.setGeometry(100,100,200,200);
            msgbox.exec();
        }
        qdb.close();
    }
}


void FormPagar::on_ramal_currentIndexChanged(int index)
{
    ui->Mostrar_precio->setEnabled(false);
    ui->pagar_viaje->setEnabled(false);
}

void FormPagar::on_usuario_currentIndexChanged(int index)
{
    ui->Mostrar_precio->setEnabled(false);
    ui->pagar_viaje->setEnabled(false);
}

void FormPagar::on_parada1_currentIndexChanged(int index)
{
    ui->pagar_viaje->setEnabled(false);
}

void FormPagar::on_parada2_currentIndexChanged(int index)
{
    ui->pagar_viaje->setEnabled(false);
}

void FormPagar::on_linea_currentIndexChanged(int index)
{
    if(!qdb.open())
    {
        qDebug() << "Error al Conectar: " << qdb.lastError().text();
    }
    else
    {
        QSqlQuery consulta(qdb);
        consulta.prepare("SELECT nom_ramal FROM ramal WHERE id_linea = :lin");
        consulta.bindValue(":lin",index+1);
        consulta.exec();
        QSqlQueryModel *modelo = new QSqlQueryModel;
        modelo->setQuery(consulta);
        ui->ramal->setModel(modelo);
        QSqlQuery consulta2("SELECT nombre FROM usuario",qdb);
        QSqlQueryModel *modelo2 = new QSqlQueryModel;
        modelo2->setQuery(consulta2);
        ui->usuario->setModel(modelo2);
        ui->ramal->setEnabled(true);
        ui->usuario->setEnabled(true);
        ui->Cofirm_ram_us->setEnabled(true);
        ui->Mostrar_precio->setEnabled(false);
        ui->pagar_viaje->setEnabled(false);
    }
    qdb.close();
}

