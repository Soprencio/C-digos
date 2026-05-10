#include "formsimon.h"
#include "ui_formsimon.h"

void esperas(int);

FormSimon::FormSimon(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::FormSimon)
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
    qDebug() << "Error al Conectar: <descripción del error>";
    db.close();
    QPixmap image(":/ruta/a/la/imagen.jpg");
    ui->Rojo->setPalette(Qt::red);
    ui->Verde->setPalette(Qt::green);
    ui->Azul->setPalette(Qt::blue);
    ui->Amarillo->setPalette(Qt::yellow);
    QPalette palette = ui->Amarillo->palette();
    palette.setColor(QPalette::Button, qRgba(170, 170, 255, 0));
    ui->Amarillo->setPalette(palette);
    QPalette palette2 = ui->Rojo->palette();
    palette2.setColor(QPalette::Button, qRgba(170, 170, 255, 0));
    ui->Rojo->setPalette(palette2);
    QPalette palette3 = ui->Azul->palette();
    palette3.setColor(QPalette::Button, qRgba(170, 170, 255, 0));
    ui->Azul->setPalette(palette3);
    QPalette palette4 = ui->Verde->palette();
    palette4.setColor(QPalette::Button, qRgba(170, 170, 255, 0));
    ui->Verde->setPalette(palette4);
}

FormSimon::~FormSimon()
{
    delete ui;
}


void FormSimon::on_Comenzar_clicked()
{
    srand(time(NULL));
    for(int verif = 0; verif<cont-1; verif++)
    {
        if(vec[verif]!=resp[verif] || cont-1 != aux)
        {
            aux2 = 1;
        }
    }
    aux = 0;
    if(aux2 == 0)
    {
        int num;
        num = rand() % 4;
        vec[cont-1] = num;
        for(int sim = 0; sim<cont; sim++)
        {
            ui->Rojo->setAutoFillBackground(true);
            ui->Verde->setAutoFillBackground(true);
            ui->Azul->setAutoFillBackground(true);
            ui->Amarillo->setAutoFillBackground(true);
            ui->Comenzar->setEnabled(false);
            ui->Rojo->setEnabled(false);
            ui->Verde->setEnabled(false);
            ui->Azul->setEnabled(false);
            ui->Amarillo->setEnabled(false);
            if(vec[sim] == 0)
            {
                ui->Rojo->setPalette(Qt::red);
            }
            else if(vec[sim] == 1)
            {
                ui->Verde->setPalette(Qt::green);
            }
            else if(vec[sim] == 2)
            {
                ui->Azul->setPalette(Qt::blue);
            }
            else
            {
                ui->Amarillo->setPalette(Qt::yellow);
            }
            esperas(tem);
            QPalette palette = ui->Amarillo->palette();
            palette.setColor(QPalette::Button, qRgba(170, 170, 255, 0));
            ui->Amarillo->setPalette(palette);
            QPalette palette2 = ui->Rojo->palette();
            palette2.setColor(QPalette::Button, qRgba(170, 170, 255, 0));
            ui->Rojo->setPalette(palette2);
            QPalette palette3 = ui->Azul->palette();
            palette3.setColor(QPalette::Button, qRgba(170, 170, 255, 0));
            ui->Azul->setPalette(palette3);
            QPalette palette4 = ui->Verde->palette();
            palette4.setColor(QPalette::Button, qRgba(170, 170, 255, 0));
            ui->Verde->setPalette(palette4);
            esperas(200);
        }
        cont++;
        if(tem>400)
        {
            tem-=100;
        }
        ui->Comenzar->setEnabled(true);
        ui->Rojo->setEnabled(true);
        ui->Verde->setEnabled(true);
        ui->Azul->setEnabled(true);
        ui->Amarillo->setEnabled(true);
    }
    else
    {
        int i = ui->comboBox->currentIndex()+1;
        if(!db.open())
        {
            qDebug() << "Error al Conectar: " << db.lastError().text();
        }
        else
        {
            QSqlQuery consulta(db);
            consulta.prepare("INSERT INTO SimonSays(iDusr, puntaje) values(:idu, :pun)");
            consulta.bindValue(":idu",i);
            consulta.bindValue(":pun",cont-2);
            consulta.exec();
        }
        QMessageBox msgbox;
        msgbox.setWindowTitle("Haz perdido");
        msgbox.setText("Puntaje: "+QString::number(cont-2)+" Rondas ganadas");
        msgbox.setStandardButtons(QMessageBox::Ok);
        msgbox.setIcon(QMessageBox::Information);
        msgbox.setGeometry(100,100,200,200);
        msgbox.exec();
        db.close();
        ui->Comenzar->setEnabled(false);
    }
}

void esperas(int mil)
{
    QEventLoop loop;
    QTimer::singleShot(mil,&loop,SLOT(quit()));
    loop.exec();
}

void FormSimon::on_Rojo_clicked()
{
    ui->Rojo->setPalette(Qt::red);
    ui->Rojo->setEnabled(false);
    ui->Verde->setEnabled(false);
    ui->Azul->setEnabled(false);
    ui->Amarillo->setEnabled(false);
    esperas(300);
    QPalette palette = ui->Rojo->palette();
    palette.setColor(QPalette::Button, qRgba(170, 170, 255, 0));
    ui->Rojo->setPalette(palette);
    ui->Rojo->setEnabled(true);
    ui->Verde->setEnabled(true);
    ui->Azul->setEnabled(true);
    ui->Amarillo->setEnabled(true);
    verifica(0);
}
void FormSimon::on_Verde_clicked()
{
    ui->Verde->setPalette(Qt::green);
    ui->Rojo->setEnabled(false);
    ui->Verde->setEnabled(false);
    ui->Azul->setEnabled(false);
    ui->Amarillo->setEnabled(false);
    esperas(300);
    QPalette palette = ui->Verde->palette();
    palette.setColor(QPalette::Button, qRgba(170, 170, 255, 0));
    ui->Verde->setPalette(palette);
    ui->Rojo->setEnabled(true);
    ui->Verde->setEnabled(true);
    ui->Azul->setEnabled(true);
    ui->Amarillo->setEnabled(true);
    verifica(1);
}
void FormSimon::on_Azul_clicked()
{
    ui->Azul->setPalette(Qt::blue);
    ui->Rojo->setEnabled(false);
    ui->Verde->setEnabled(false);
    ui->Azul->setEnabled(false);
    ui->Amarillo->setEnabled(false);
    esperas(300);
    QPalette palette = ui->Azul->palette();
    palette.setColor(QPalette::Button, qRgba(170, 170, 255, 0));
    ui->Azul->setPalette(palette);
    ui->Rojo->setEnabled(true);
    ui->Verde->setEnabled(true);
    ui->Azul->setEnabled(true);
    ui->Amarillo->setEnabled(true);
    verifica(2);
}
void FormSimon::on_Amarillo_clicked()
{
    ui->Amarillo->setPalette(Qt::yellow);
    ui->Rojo->setEnabled(false);
    ui->Verde->setEnabled(false);
    ui->Azul->setEnabled(false);
    ui->Amarillo->setEnabled(false);
    esperas(300);
    QPalette palette = ui->Amarillo->palette();
    palette.setColor(QPalette::Button, qRgba(170, 170, 255, 0));
    ui->Amarillo->setPalette(palette);
    ui->Rojo->setEnabled(true);
    ui->Verde->setEnabled(true);
    ui->Azul->setEnabled(true);
    ui->Amarillo->setEnabled(true);
    verifica(3);
}

void FormSimon::verifica(int res)
{
    resp[aux]=res;
    aux++;
}
