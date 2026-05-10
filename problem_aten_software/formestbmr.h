#ifndef FORMESTBMR_H
#define FORMESTBMR_H

#include <QWidget>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlQueryModel>
#include <QSqlError>
#include <QDebug>

namespace Ui {
class FormEstBMR;
}

class FormEstBMR : public QWidget
{
    Q_OBJECT

public:
    explicit FormEstBMR(QWidget *parent = nullptr);
    ~FormEstBMR();

private slots:
    void on_pushButton_clicked();

private:
    Ui::FormEstBMR *ui;
};

#endif // FORMESTBMR_H
