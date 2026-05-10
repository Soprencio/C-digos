#ifndef FORMLISTA_H
#define FORMLISTA_H

#include <QWidget>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlQueryModel>
#include <QSqlError>
#include <QDebug>

namespace Ui {
class FormLista;
}

class FormLista : public QWidget
{
    Q_OBJECT

public:
    explicit FormLista(QWidget *parent = nullptr);
    ~FormLista();

private slots:
    void on_pushButton_clicked();

private:
    Ui::FormLista *ui;
};

#endif // FORMLISTA_H
