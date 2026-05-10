#include "formaltas.h"
#include "ui_formaltas.h"


FormAltas::FormAltas(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::FormAltas)
{
    ui->setupUi(this);
}

FormAltas::~FormAltas()
{
    delete ui;
}

void FormAltas::on_Alta_clicked()
{
    QSqlDatabase qdb = QSqlDatabase::addDatabase("QMYSQL");
    qdb.setHostName("localhost");
    qdb.setUserName("root");
    qdb.setPassword("12341234");
    qdb.setDatabaseName("LAMIBE");
    if(!qdb.open())
    {
        qDebug() << "Error en la conexión: " << qdb.lastError().text();
    }
    else
    {
        QSqlQuery alta(qdb);
        alta.prepare("INSERT INTO usuario (nombre, passw, saldo_sube, tarifa) values(:nom, :pas, :sal, :tar)");
        alta.bindValue(":nom", ui->Nombre->text());
        alta.bindValue(":pas", ui->Apellido->text());
        alta.bindValue(":sal", ui->spinBox->text());
        alta.bindValue(":tar", ui->Tarifa->currentText());
        alta.exec();
    }
    qdb.close();
    QMessageBox msgbox;
    msgbox.setWindowTitle("Usuario Cargado");
    msgbox.setText("Has cargado un nuevo usuario");
    msgbox.setStandardButtons(QMessageBox::Ok);
    msgbox.setIcon(QMessageBox::Information);
    msgbox.setGeometry(100,100,200,200);
    msgbox.exec();
}
