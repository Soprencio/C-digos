#ifndef FORMCARGA_H
#define FORMCARGA_H

#include <QWidget>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlQueryModel>
#include <QSqlError>
#include <QDebug>
#include <QMessageBox>

namespace Ui {
class FormCarga;
}

class FormCarga : public QWidget
{
    Q_OBJECT

public:
    explicit FormCarga(QWidget *parent = nullptr);
    ~FormCarga();

private slots:
    void on_Carga_clicked();

    void on_Mostrar_clicked();

private:
    Ui::FormCarga *ui;
    QSqlDatabase db = QSqlDatabase::addDatabase("QMYSQL");
    double sald;
    int user;
};

#endif // FORMCARGA_H
