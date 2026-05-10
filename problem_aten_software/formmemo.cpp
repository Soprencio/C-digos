#include "formmemo.h"
#include "ui_formmemo.h"

void espera(int);

FormMemo::FormMemo(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::FormMemo)
{
    ui->setupUi(this);
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
        QSqlQuery consulta("SELECT nombre FROM Usuario",db);
        QSqlQueryModel *modelo = new QSqlQueryModel;
        modelo->setQuery(consulta);
        ui->comboBox->setModel(modelo);
    }
    db.close();
    ui->lineEdit->setText(QString::number(pasos));
}

FormMemo::~FormMemo()
{
    delete ui;
}

void FormMemo::on_generar_clicked()
{
    srand(time(NULL));
    pasos = 0;
    aux = 0;
    turno = 0;
    for(int cont = 0; cont<8; cont++)
    {
        numer[cont] = cont;
        numer[cont+8] = cont;
    }
    ui->lineEdit->setText(QString::number(pasos));
    for(int cont = 0; cont<16; cont++)
    {
        if(cont == 0)
        {
            ui->pushButton_2->setEnabled(true);
            ui->pushButton_2->setText("");
        }
        else if(cont == 1)
        {
            ui->pushButton_3->setEnabled(true);
            ui->pushButton_3->setText("");
        }
        else if(cont == 2)
        {
            ui->pushButton_4->setEnabled(true);
            ui->pushButton_4->setText("");
        }
        else if(cont == 3)
        {
            ui->pushButton_5->setEnabled(true);
            ui->pushButton_5->setText("");
        }
        else if(cont == 4)
        {
            ui->pushButton_6->setEnabled(true);
            ui->pushButton_6->setText("");
        }
        else if(cont == 5)
        {
            ui->pushButton_7->setEnabled(true);
            ui->pushButton_7->setText("");
        }
        else if(cont == 6)
        {
            ui->pushButton_8->setEnabled(true);
            ui->pushButton_8->setText("");
        }
        else if(cont == 7)
        {
            ui->pushButton_9->setEnabled(true);
            ui->pushButton_9->setText("");
        }
        else if(cont == 8)
        {
            ui->pushButton_10->setEnabled(true);
            ui->pushButton_10->setText("");
        }
        else if(cont == 9)
        {
            ui->pushButton_11->setEnabled(true);
            ui->pushButton_11->setText("");
        }
        else if(cont == 10)
        {
            ui->pushButton_12->setEnabled(true);
            ui->pushButton_12->setText("");
        }
        else if(cont == 11)
        {
            ui->pushButton_13->setEnabled(true);
            ui->pushButton_13->setText("");
        }
        else if(cont == 12)
        {
            ui->pushButton_14->setEnabled(true);
            ui->pushButton_14->setText("");
        }
        else if(cont == 13)
        {
            ui->pushButton_15->setEnabled(true);
            ui->pushButton_15->setText("");
        }
        else if(cont == 14)
        {
            ui->pushButton_16->setEnabled(true);
            ui->pushButton_16->setText("");
        }
        else
        {
            ui->pushButton_17->setEnabled(true);
            ui->pushButton_17->setText("");
        }
    }
    int num, aux2, contador = 0;
    for(int j = 0; j<3; j++)
    {
        for(int i = 0; i<16; i++)
        {
            num = rand() % 16;
            aux2 = numer[i];
            numer[i] = numer[num];
            numer[num] = aux2;
        }
    }
    for(int f = 0; f<4; f++)
    {
        for(int c = 0; c<4; c++)
        {
            mat(f, c) = numer[contador];
            contador++;
        }
    }
    QMessageBox msgbox;
    msgbox.setWindowTitle("Generado");
    msgbox.setText("Nuevo Memotest Generado");
    msgbox.setStandardButtons(QMessageBox::Ok);
    msgbox.setIcon(QMessageBox::Information);
    msgbox.setGeometry(100,100,200,200);
    msgbox.exec();
}


void FormMemo::on_pushButton_2_clicked()
{
    ui->pushButton_2->setText(QString::number(mat(0, 0)));
    ui->pushButton_2->setEnabled(false);
    if(turno == 1)
    {
        espera(1000);
        aux3[1] = mat(0, 0);
        aux3[3] = 0;
        ui->pushButton_2->setText("");
        ui->pushButton_2->setEnabled(true);
        confirmar(aux3[0], aux3[1], aux3[2], aux3[3]);
        turno = 0;
    }
    else
    {
        aux3[0] = mat(0, 0);
        aux3[2] = 0;
        turno = 1;
    }
}


void FormMemo::on_pushButton_3_clicked()
{
    ui->pushButton_3->setText(QString::number(mat(0, 1)));
    ui->pushButton_3->setEnabled(false);
    if(turno == 1)
    {
        espera(1000);
        aux3[1] = mat(0, 1);
        aux3[3] = 1;
        ui->pushButton_3->setText("");
        ui->pushButton_3->setEnabled(true);
        confirmar(aux3[0], aux3[1], aux3[2], aux3[3]);
        turno = 0;
    }
    else
    {
        aux3[0] = mat(0, 1);
        aux3[2] = 1;
        turno = 1;
    }
}


void FormMemo::on_pushButton_4_clicked()
{
    ui->pushButton_4->setText(QString::number(mat(0, 2)));
    ui->pushButton_4->setEnabled(false);
    if(turno == 1)
    {
        espera(1000);
        aux3[1] = mat(0, 2);
        aux3[3] = 2;
        ui->pushButton_4->setText("");
        ui->pushButton_4->setEnabled(true);
        confirmar(aux3[0], aux3[1], aux3[2], aux3[3]);
        turno = 0;
    }
    else
    {
        aux3[0] = mat(0, 2);
        aux3[2] = 2;
        turno = 1;
    }
}


void FormMemo::on_pushButton_5_clicked()
{
    ui->pushButton_5->setText(QString::number(mat(0, 3)));
    ui->pushButton_5->setEnabled(false);
    if(turno == 1)
    {
        espera(1000);
        aux3[1] = mat(0, 3);
        aux3[3] = 3;
        ui->pushButton_5->setText("");
        ui->pushButton_5->setEnabled(true);
        confirmar(aux3[0], aux3[1], aux3[2], aux3[3]);
        turno = 0;
    }
    else
    {
        aux3[0] = mat(0, 3);
        aux3[2] = 3;
        turno = 1;
    }
}


void FormMemo::on_pushButton_6_clicked()
{
    ui->pushButton_6->setText(QString::number(mat(1, 0)));
    ui->pushButton_6->setEnabled(false);
    if(turno == 1)
    {
        espera(1000);
        aux3[1] = mat(1, 0);
        aux3[3] = 4;
        ui->pushButton_6->setText("");
        ui->pushButton_6->setEnabled(true);
        confirmar(aux3[0], aux3[1], aux3[2], aux3[3]);
        turno = 0;
    }
    else
    {
        aux3[0] = mat(1, 0);
        aux3[2] = 4;
        turno = 1;
    }
}


void FormMemo::on_pushButton_7_clicked()
{
    ui->pushButton_7->setText(QString::number(mat(1, 1)));
    ui->pushButton_7->setEnabled(false);
    if(turno == 1)
    {
        espera(1000);
        aux3[1] = mat(1, 1);
        aux3[3] = 5;
        ui->pushButton_7->setText("");
        ui->pushButton_7->setEnabled(true);
        confirmar(aux3[0], aux3[1], aux3[2], aux3[3]);
        turno = 0;
    }
    else
    {
        aux3[0] = mat(1, 1);
        aux3[2] = 5;
        turno = 1;
    }
}


void FormMemo::on_pushButton_8_clicked()
{
    ui->pushButton_8->setText(QString::number(mat(1, 2)));
    ui->pushButton_8->setEnabled(false);
    if(turno == 1)
    {
        espera(1000);
        aux3[1] = mat(1, 2);
        aux3[3] = 6;
        ui->pushButton_8->setText("");
        ui->pushButton_8->setEnabled(true);
        confirmar(aux3[0], aux3[1], aux3[2], aux3[3]);
        turno = 0;
    }
    else
    {
        aux3[0] = mat(1, 2);
        aux3[2] = 6;
        turno = 1;
    }
}


void FormMemo::on_pushButton_9_clicked()
{
    ui->pushButton_9->setText(QString::number(mat(1, 3)));
    ui->pushButton_9->setEnabled(false);
    if(turno == 1)
    {
        espera(1000);
        aux3[1] = mat(1, 3);
        aux3[3] = 7;
        ui->pushButton_9->setText("");
        ui->pushButton_9->setEnabled(true);
        confirmar(aux3[0], aux3[1], aux3[2], aux3[3]);
        turno = 0;
    }
    else
    {
        aux3[0] = mat(1, 3);
        aux3[2] = 7;
        turno = 1;
    }
}


void FormMemo::on_pushButton_10_clicked()
{
    ui->pushButton_10->setText(QString::number(mat(2, 0)));
    ui->pushButton_10->setEnabled(false);
    if(turno == 1)
    {
        espera(1000);
        aux3[1] = mat(2, 0);
        aux3[3] = 8;
        ui->pushButton_10->setText("");
        ui->pushButton_10->setEnabled(true);
        confirmar(aux3[0], aux3[1], aux3[2], aux3[3]);
        turno = 0;
    }
    else
    {
        aux3[0] = mat(2, 0);
        aux3[2] = 8;
        turno = 1;
    }
}


void FormMemo::on_pushButton_11_clicked()
{
    ui->pushButton_11->setText(QString::number(mat(2, 1)));
    ui->pushButton_11->setEnabled(false);
    if(turno == 1)
    {
        espera(1000);
        aux3[1] = mat(2, 1);
        aux3[3] = 9;
        ui->pushButton_11->setText("");
        ui->pushButton_11->setEnabled(true);
        confirmar(aux3[0], aux3[1], aux3[2], aux3[3]);
        turno = 0;
    }
    else
    {
        aux3[0] = mat(2, 1);
        aux3[2] = 9;
        turno = 1;
    }
}


void FormMemo::on_pushButton_12_clicked()
{
    ui->pushButton_12->setText(QString::number(mat(2, 2)));
    ui->pushButton_12->setEnabled(false);
    if(turno == 1)
    {
        espera(1000);
        aux3[1] = mat(2, 2);
        aux3[3] = 10;
        ui->pushButton_12->setText("");
        ui->pushButton_12->setEnabled(true);
        confirmar(aux3[0], aux3[1], aux3[2], aux3[3]);
        turno = 0;
    }
    else
    {
        aux3[0] = mat(2, 2);
        aux3[2] = 10;
        turno = 1;
    }
}


void FormMemo::on_pushButton_13_clicked()
{
    ui->pushButton_13->setText(QString::number(mat(2, 3)));
    ui->pushButton_13->setEnabled(false);
    if(turno == 1)
    {
        espera(1000);
        aux3[1] = mat(2, 3);
        aux3[3] = 11;
        ui->pushButton_13->setText("");
        ui->pushButton_13->setEnabled(true);
        confirmar(aux3[0], aux3[1], aux3[2], aux3[3]);
        turno = 0;
    }
    else
    {
        aux3[0] = mat(2, 3);
        aux3[2] = 11;
        turno = 1;
    }
}


void FormMemo::on_pushButton_14_clicked()
{
    ui->pushButton_14->setText(QString::number(mat(3, 0)));
    ui->pushButton_14->setEnabled(false);
    if(turno == 1)
    {
        espera(1000);
        aux3[1] = mat(3, 0);
        aux3[3] = 12;
        ui->pushButton_14->setText("");
        ui->pushButton_14->setEnabled(true);
        confirmar(aux3[0], aux3[1], aux3[2], aux3[3]);
        turno = 0;
    }
    else
    {
        aux3[0] = mat(3, 0);
        aux3[2] = 12;
        turno = 1;
    }
}


void FormMemo::on_pushButton_15_clicked()
{
    ui->pushButton_15->setText(QString::number(mat(3, 1)));
    ui->pushButton_15->setEnabled(false);
    if(turno == 1)
    {
        espera(1000);
        aux3[1] = mat(3, 1);
        aux3[3] = 13;
        ui->pushButton_15->setText("");
        ui->pushButton_15->setEnabled(true);
        confirmar(aux3[0], aux3[1], aux3[2], aux3[3]);
        turno = 0;
    }
    else
    {
        aux3[0] = mat(3, 1);
        aux3[2] = 13;
        turno = 1;
    }
}


void FormMemo::on_pushButton_16_clicked()
{
    ui->pushButton_16->setText(QString::number(mat(3, 2)));
    ui->pushButton_16->setEnabled(false);
    if(turno == 1)
    {
        espera(1000);
        aux3[1] = mat(3, 2);
        aux3[3] = 14;
        ui->pushButton_16->setText("");
        ui->pushButton_16->setEnabled(true);
        confirmar(aux3[0], aux3[1], aux3[2], aux3[3]);
        turno = 0;
    }
    else
    {
        aux3[0] = mat(3, 2);
        aux3[2] = 14;
        turno = 1;
    }
}


void FormMemo::on_pushButton_17_clicked()
{
    ui->pushButton_17->setText(QString::number(mat(3, 3)));
    ui->pushButton_17->setEnabled(false);
    if(turno == 1)
    {
        espera(1000);
        aux3[1] = mat(3, 3);
        aux3[3] = 15;
        ui->pushButton_17->setText("");
        ui->pushButton_17->setEnabled(true);
        confirmar(aux3[0], aux3[1], aux3[2], aux3[3]);
        turno = 0;
    }
    else
    {
        aux3[0] = mat(3, 3);
        aux3[2] = 15;
        turno = 1;
    }
}

void espera(int mil)
{
    QEventLoop loop;
    QTimer::singleShot(mil,&loop,SLOT(quit()));
    loop.exec();
}

void FormMemo::confirmar(int num1, int num2, int but1, int but2)
{
    pasos++;
    ui->lineEdit->setText(QString::number(pasos));
    if(num1 == num2)
    {
        aux++;
        if(but2 == 0)
        {
            ui->pushButton_2->setEnabled(false);
            ui->pushButton_2->setText(QString::number(mat(0, 0)));
        }
        else if(but2 == 1)
        {
            ui->pushButton_3->setEnabled(false);
            ui->pushButton_3->setText(QString::number(mat(0, 1)));
        }
        else if(but2 == 2)
        {
            ui->pushButton_4->setEnabled(false);
            ui->pushButton_4->setText(QString::number(mat(0, 2)));
        }
        else if(but2 == 3)
        {
            ui->pushButton_5->setEnabled(false);
            ui->pushButton_5->setText(QString::number(mat(0, 3)));
        }
        else if(but2 == 4)
        {
            ui->pushButton_6->setEnabled(false);
            ui->pushButton_6->setText(QString::number(mat(1, 0)));
        }
        else if(but2 == 5)
        {
            ui->pushButton_7->setEnabled(false);
            ui->pushButton_7->setText(QString::number(mat(1, 1)));
        }
        else if(but2 == 6)
        {
            ui->pushButton_8->setEnabled(false);
            ui->pushButton_8->setText(QString::number(mat(1, 2)));
        }
        else if(but2 == 7)
        {
            ui->pushButton_9->setEnabled(false);
            ui->pushButton_9->setText(QString::number(mat(1, 3)));
        }
        else if(but2 == 8)
        {
            ui->pushButton_10->setEnabled(false);
            ui->pushButton_10->setText(QString::number(mat(2, 0)));
        }
        else if(but2 == 9)
        {
            ui->pushButton_11->setEnabled(false);
            ui->pushButton_11->setText(QString::number(mat(2, 1)));
        }
        else if(but2 == 10)
        {
            ui->pushButton_12->setEnabled(false);
            ui->pushButton_12->setText(QString::number(mat(2, 2)));
        }
        else if(but2 == 11)
        {
            ui->pushButton_13->setEnabled(false);
            ui->pushButton_13->setText(QString::number(mat(2, 3)));
        }
        else if(but2 == 12)
        {
            ui->pushButton_14->setEnabled(false);
            ui->pushButton_14->setText(QString::number(mat(3, 0)));
        }
        else if(but2 == 13)
        {
            ui->pushButton_15->setEnabled(false);
            ui->pushButton_15->setText(QString::number(mat(3, 1)));
        }
        else if(but2 == 14)
        {
            ui->pushButton_16->setEnabled(false);
            ui->pushButton_16->setText(QString::number(mat(3, 2)));
        }
        else
        {
            ui->pushButton_17->setEnabled(false);
            ui->pushButton_17->setText(QString::number(mat(3, 3)));
        }
        if(but1 == 0)
        {
            ui->pushButton_2->setEnabled(false);
            ui->pushButton_2->setText(QString::number(mat(0, 0)));
        }
        else if(but1 == 1)
        {
            ui->pushButton_3->setEnabled(false);
            ui->pushButton_3->setText(QString::number(mat(0, 1)));
        }
        else if(but1 == 2)
        {
            ui->pushButton_4->setEnabled(false);
            ui->pushButton_4->setText(QString::number(mat(0, 2)));
        }
        else if(but1 == 3)
        {
            ui->pushButton_5->setEnabled(false);
            ui->pushButton_5->setText(QString::number(mat(0, 3)));
        }
        else if(but1 == 4)
        {
            ui->pushButton_6->setEnabled(false);
            ui->pushButton_6->setText(QString::number(mat(1, 0)));
        }
        else if(but1 == 5)
        {
            ui->pushButton_7->setEnabled(false);
            ui->pushButton_7->setText(QString::number(mat(1, 1)));
        }
        else if(but1 == 6)
        {
            ui->pushButton_8->setEnabled(false);
            ui->pushButton_8->setText(QString::number(mat(1, 2)));
        }
        else if(but1 == 7)
        {
            ui->pushButton_9->setEnabled(false);
            ui->pushButton_9->setText(QString::number(mat(1, 3)));
        }
        else if(but1 == 8)
        {
            ui->pushButton_10->setEnabled(false);
            ui->pushButton_10->setText(QString::number(mat(2, 0)));
        }
        else if(but1 == 9)
        {
            ui->pushButton_11->setEnabled(false);
            ui->pushButton_11->setText(QString::number(mat(2, 1)));
        }
        else if(but1 == 10)
        {
            ui->pushButton_12->setEnabled(false);
            ui->pushButton_12->setText(QString::number(mat(2, 2)));
        }
        else if(but1 == 11)
        {
            ui->pushButton_13->setEnabled(false);
            ui->pushButton_13->setText(QString::number(mat(2, 3)));
        }
        else if(but1 == 12)
        {
            ui->pushButton_14->setEnabled(false);
            ui->pushButton_14->setText(QString::number(mat(3, 0)));
        }
        else if(but1 == 13)
        {
            ui->pushButton_15->setEnabled(false);
            ui->pushButton_15->setText(QString::number(mat(3, 1)));
        }
        else if(but1 == 14)
        {
            ui->pushButton_16->setEnabled(false);
            ui->pushButton_16->setText(QString::number(mat(3, 2)));
        }
        else
        {
            ui->pushButton_17->setEnabled(false);
            ui->pushButton_17->setText(QString::number(mat(3, 3)));
        }
    }
    else
    {
        if(but1 == 0)
        {
            ui->pushButton_2->setText("");
            ui->pushButton_2->setEnabled(true);
        }
        else if(but1 == 1)
        {
            ui->pushButton_3->setText("");
            ui->pushButton_3->setEnabled(true);
        }
        else if(but1 == 2)
        {
            ui->pushButton_4->setText("");
            ui->pushButton_4->setEnabled(true);
        }
        else if(but1 == 3)
        {
            ui->pushButton_5->setText("");
            ui->pushButton_5->setEnabled(true);
        }
        else if(but1 == 4)
        {
            ui->pushButton_6->setText("");
            ui->pushButton_6->setEnabled(true);
        }
        else if(but1 == 5)
        {
            ui->pushButton_7->setText("");
            ui->pushButton_7->setEnabled(true);
        }
        else if(but1 == 6)
        {
            ui->pushButton_8->setText("");
            ui->pushButton_8->setEnabled(true);
        }
        else if(but1 == 7)
        {
            ui->pushButton_9->setText("");
            ui->pushButton_9->setEnabled(true);
        }
        else if(but1 == 8)
        {
            ui->pushButton_10->setText("");
            ui->pushButton_10->setEnabled(true);
        }
        else if(but1 == 9)
        {
            ui->pushButton_11->setText("");
            ui->pushButton_11->setEnabled(true);
        }
        else if(but1 == 10)
        {
            ui->pushButton_12->setText("");
            ui->pushButton_12->setEnabled(true);
        }
        else if(but1 == 11)
        {
            ui->pushButton_13->setText("");
            ui->pushButton_13->setEnabled(true);
        }
        else if(but1 == 12)
        {
            ui->pushButton_14->setText("");
            ui->pushButton_14->setEnabled(true);
        }
        else if(but1 == 13)
        {
            ui->pushButton_15->setText("");
            ui->pushButton_15->setEnabled(true);
        }
        else if(but1 == 14)
        {
            ui->pushButton_16->setText("");
            ui->pushButton_16->setEnabled(true);
        }
        else
        {
            ui->pushButton_17->setText("");
            ui->pushButton_17->setEnabled(true);
        }
    }
    if(aux>=8)
    {
        aux=0;
        if(!db.open())
        {
            qDebug() << "Error al Conectar: " << db.lastError().text();
        }
        else
        {
            QSqlQuery consulta(db);
            consulta.prepare("INSERT INTO Memotest(pasos, iDusr) values(:pas, :idr)");
            consulta.bindValue(":pas",pasos);
            consulta.bindValue(":idr",ui->comboBox->currentIndex()+1);
            consulta.exec();
        }
        db.close();
        QMessageBox msgbox;
        msgbox.setWindowTitle("Haz Ganado");
        msgbox.setText("Cantidad de pasos: "+QString::number(pasos));
        msgbox.setStandardButtons(QMessageBox::Ok);
        msgbox.setIcon(QMessageBox::Information);
        msgbox.setGeometry(100,100,400,400);
        msgbox.exec();
    }
}
