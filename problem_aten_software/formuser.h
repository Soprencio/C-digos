#ifndef FORMUSER_H
#define FORMUSER_H

#include <QWidget>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlQueryModel>
#include <QSqlError>
#include <QDebug>
#include <QMessageBox>

namespace Ui {
class FormUser;
}

class FormUser : public QWidget
{
    Q_OBJECT

public:
    explicit FormUser(QWidget *parent = nullptr);
    ~FormUser();

private slots:
    void on_pushButton_clicked();

private:
    Ui::FormUser *ui;
};

#endif // FORMUSER_H
