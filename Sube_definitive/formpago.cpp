#include "formpago.h"
#include "ui_formpago.h"

FormPago::FormPago(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::FormPago)
{
    ui->setupUi(this);
}

FormPago::~FormPago()
{
    delete ui;
}

void FormPago::on_Mostrar_clicked()
{
    QSqlDatabase db = QSqlDatabase::addDatabase("QMYSQL");
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
        QSqlQuery consulta("SELECT v.*, u.nombre FROM viajes v INNER JOIN usuario u ON v.id_usr = u.id_usr",db);
        QSqlQueryModel *modelo = new QSqlQueryModel;
        modelo->setQuery(consulta);
        ui->tableView->setModel(modelo);
    }
}

