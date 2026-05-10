#ifndef FORMALTAS_H
#define FORMALTAS_H

#include <QWidget>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlQueryModel>
#include <QSqlError>
#include <QDebug>
#include <QMessageBox>

namespace Ui {
class FormAltas;
}

class FormAltas : public QWidget
{
    Q_OBJECT

public:
    explicit FormAltas(QWidget *parent = nullptr);
    ~FormAltas();

private slots:
    void on_Alta_clicked();

private:
    Ui::FormAltas *ui;
};

#endif // FORMALTAS_H
