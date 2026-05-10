#include "formestbmr.h"
#include "ui_formestbmr.h"

FormEstBMR::FormEstBMR(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::FormEstBMR)
{
    ui->setupUi(this);
}

FormEstBMR::~FormEstBMR()
{
    delete ui;
}

void FormEstBMR::on_pushButton_clicked()
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
        QSqlQuery consulta("SELECT u.nombre, b.* FROM BuenMalReg b INNER JOIN Usuario u ON b.iDusr = u.iDusr ORDER BY b.acciones",db);
        QSqlQueryModel *modelo = new QSqlQueryModel;
        modelo->setQuery(consulta);
        ui->tableView->setModel(modelo);
    }
    db.close();
}

