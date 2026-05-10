#include "formlistado.h"
#include "ui_formlistado.h"

FormListado::FormListado(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::FormListado)
{
    ui->setupUi(this);
}

FormListado::~FormListado()
{
    delete ui;
}

void FormListado::on_Mostrar_clicked()
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
        QSqlQuery consulta("SELECT * FROM usuario",db);
        QSqlQueryModel *modelo = new QSqlQueryModel;
        modelo->setQuery(consulta);
        ui->tableView->setModel(modelo);
    }
    db.close();
}

