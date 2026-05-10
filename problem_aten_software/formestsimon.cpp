#include "formestsimon.h"
#include "ui_formestsimon.h"

FormEstSimon::FormEstSimon(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::FormEstSimon)
{
    ui->setupUi(this);
}

FormEstSimon::~FormEstSimon()
{
    delete ui;
}

void FormEstSimon::on_pushButton_clicked()
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
        QSqlQuery consulta("SELECT u.nombre, s.* FROM SimonSays s INNER JOIN Usuario u ON s.iDusr = u.iDusr ORDER BY s.puntaje DESC",db);
        QSqlQueryModel *modelo = new QSqlQueryModel;
        modelo->setQuery(consulta);
        ui->tableView->setModel(modelo);
    }
    db.close();
}

