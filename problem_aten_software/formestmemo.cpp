#include "formestmemo.h"
#include "ui_formestmemo.h"

FormEstMemo::FormEstMemo(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::FormEstMemo)
{
    ui->setupUi(this);
}

FormEstMemo::~FormEstMemo()
{
    delete ui;
}

void FormEstMemo::on_pushButton_clicked()
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
        QSqlQuery consulta("SELECT u.nombre, m.* FROM Memotest m INNER JOIN Usuario u ON m.iDusr = u.iDusr ORDER BY m.pasos",db);
        QSqlQueryModel *modelo = new QSqlQueryModel;
        modelo->setQuery(consulta);
        ui->tableView->setModel(modelo);
    }
    db.close();
}

