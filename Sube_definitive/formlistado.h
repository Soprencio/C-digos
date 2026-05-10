#ifndef FORMLISTADO_H
#define FORMLISTADO_H

#include <QWidget>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlQueryModel>
#include <QSqlError>
#include <QDebug>

namespace Ui {
class FormListado;
}

class FormListado : public QWidget
{
    Q_OBJECT

public:
    explicit FormListado(QWidget *parent = nullptr);
    ~FormListado();

private slots:
    void on_Mostrar_clicked();

private:
    Ui::FormListado *ui;
};

#endif // FORMLISTADO_H
