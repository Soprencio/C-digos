#include "formlista.h"
#include "ui_formlista.h"

FormLista::FormLista(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::FormLista)
{
    ui->setupUi(this);
}

FormLista::~FormLista()
{
    delete ui;
}


void FormLista::on_pushButton_clicked()
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
        QSqlQuery consulta("SELECT * FROM Usuario",db);
        QSqlQueryModel *modelo = new QSqlQueryModel;
        modelo->setQuery(consulta);
        ui->tableView->setModel(modelo);
    }
    db.close();
}

