#ifndef FORMPAGO_H
#define FORMPAGO_H

#include <QWidget>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlQueryModel>
#include <QSqlError>
#include <QDebug>

namespace Ui {
class FormPago;
}

class FormPago : public QWidget
{
    Q_OBJECT

public:
    explicit FormPago(QWidget *parent = nullptr);
    ~FormPago();

private slots:
    void on_Mostrar_clicked();

private:
    Ui::FormPago *ui;
};

#endif // FORMPAGO_H
