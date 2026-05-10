#ifndef FORMESTSIMON_H
#define FORMESTSIMON_H

#include <QWidget>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlQueryModel>
#include <QSqlError>
#include <QDebug>

namespace Ui {
class FormEstSimon;
}

class FormEstSimon : public QWidget
{
    Q_OBJECT

public:
    explicit FormEstSimon(QWidget *parent = nullptr);
    ~FormEstSimon();

private slots:
    void on_pushButton_clicked();

private:
    Ui::FormEstSimon *ui;
};

#endif // FORMESTSIMON_H
