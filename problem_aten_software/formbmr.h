#ifndef FORMBMR_H
#define FORMBMR_H

#include <QWidget>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlQueryModel>
#include <QSqlError>
#include <QDebug>
#include <time.h>
#include <QMessageBox>

namespace Ui {
class FormBMR;
}

class FormBMR : public QWidget
{
    Q_OBJECT

public:
    explicit FormBMR(QWidget *parent = nullptr);
    ~FormBMR();

private slots:
    void on_adivinar_clicked();

    void on_generar_clicked();

private:
    Ui::FormBMR *ui;
    QSqlDatabase db = QSqlDatabase::addDatabase("QMYSQL");
    int contador = 0;
};

#endif // FORMBMR_H
