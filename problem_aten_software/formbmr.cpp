#include "formbmr.h"
#include "ui_formbmr.h"

QString cargaNum();
int numeroesta(QString, int, int);
QString parecidos(QString, QString);

FormBMR::FormBMR(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::FormBMR)
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
}

FormBMR::~FormBMR()
{
    delete ui;
}

void FormBMR::on_adivinar_clicked()
{
    if((ui->lineEdit->text()).size()==4)
    {
        contador += 1;
        QString aux = "4B0R0M";
        QString a = ui->lineEdit->text();
        QString b = ui->lineEdit_2->text();
        QString aux2 = parecidos(a,b);
        QString c = aux2.at(0);
        c = c+aux2.at(1)+"-"+aux2.at(2)+aux2.at(3)+"-"+aux2.at(4)+aux2.at(5);
        if(aux2 == aux)
        {
            ui->adivinar->setEnabled(false);
            if(!db.open())
            {
                qDebug() << "Error al Conectar: " << db.lastError().text();
            }
            else
            {
                QSqlQuery consulta(db);
                consulta.prepare("INSERT INTO BuenMalReg(iDusr, acciones) values(:idr, :acc)");
                consulta.bindValue(":idr",ui->comboBox->currentIndex()+1);
                consulta.bindValue(":acc",contador);
                consulta.exec();
            }
            ui->textEdit->insertPlainText(c+"  Intento: "+QString::number(contador)+"  "+a+'\n');
            QMessageBox msgbox;
            msgbox.setWindowTitle("Haz adivinado");
            msgbox.setText("Puntaje: "+QString::number(contador)+" intentos");
            msgbox.setStandardButtons(QMessageBox::Ok);
            msgbox.setIcon(QMessageBox::Information);
            msgbox.setGeometry(100,100,200,200);
            msgbox.exec();
        }
        if(aux!=aux2)
        {
            ui->textEdit->insertPlainText(c+"  Intento: "+QString::number(contador)+"  "+a+'\n');

        }
    }
    else
    {
        QMessageBox msgbox;
        msgbox.setWindowTitle("Error");
        msgbox.setText("Ingresa un número de 4 cifras");
        msgbox.setStandardButtons(QMessageBox::Ok);
        msgbox.setIcon(QMessageBox::Information);
        msgbox.setGeometry(100,100,200,200);
        msgbox.exec();
    }
}

void FormBMR::on_generar_clicked()
{
    srand(time(NULL));
    QString num = cargaNum();
    ui->lineEdit_2->setText(num);
    ui->textEdit->clear();
    ui->adivinar->setEnabled(true);
    QMessageBox msgbox;
    msgbox.setWindowTitle("Generado");
    msgbox.setText("Has generado un nuevo número para adivinar");
    msgbox.setStandardButtons(QMessageBox::Ok);
    msgbox.setIcon(QMessageBox::Information);
    msgbox.setGeometry(100,100,200,200);
    msgbox.exec();
}
QString cargaNum()
{
    QString n = "";
    for(int cont = 0; cont<4; cont++)
    {
        int num = rand() % 10;
        while(numeroesta(n,num,cont)==0)
        {
            num = rand() % 10;
        }
        n.append(QString::number(num));
    }
    return(n);
}

int numeroesta(QString n, int num, int c)
{
    for(int cont = 0; cont<c; cont++)
    {
        if(QString::number(num)==QString(n.at(cont)))
        {
            return(0);
        }
    }
    return(1);
}

QString parecidos(QString a, QString b)
{
    int e = 0, f = 0, g = 0, j = 0;
    QString aux = "";
    for(int cont = 0; cont<4; cont++)
    {
        j = 0;
        while(a.at(cont)!=b.at(j) && j<3)
        {
            j+=1;
        }
        if(a.at(cont)==b.at(j))
        {
            if(cont==j)
            {
                e+=1;
            }
            else
            {
                f+=1;
            }
        }
        else
        {
            g+=1;
        }
    }
    aux.append(QString::number(e));
    aux.append('B');
    aux.append(QString::number(f));
    aux.append('R');
    aux.append(QString::number(g));
    aux.append('M');
    return(aux);
}
