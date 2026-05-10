#ifndef FORMESTMEMO_H
#define FORMESTMEMO_H

#include <QWidget>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlQueryModel>
#include <QSqlError>
#include <QDebug>

namespace Ui {
class FormEstMemo;
}

class FormEstMemo : public QWidget
{
    Q_OBJECT

public:
    explicit FormEstMemo(QWidget *parent = nullptr);
    ~FormEstMemo();

private slots:
    void on_pushButton_clicked();

private:
    Ui::FormEstMemo *ui;
};

#endif // FORMESTMEMO_H
