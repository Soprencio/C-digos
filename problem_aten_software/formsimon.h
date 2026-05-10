#ifndef FORMSIMON_H
#define FORMSIMON_H

#include <QWidget>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlQueryModel>
#include <QSqlError>
#include <QDebug>
#include <unistd.h>
#include <time.h>
#include <QTimer>
#include <QThread>
#include <QMessageBox>
#include <QPixmap>

namespace Ui {
class FormSimon;
}

class FormSimon : public QWidget
{
    Q_OBJECT

public:
    explicit FormSimon(QWidget *parent = nullptr);
    ~FormSimon();

private slots:
    void on_Comenzar_clicked();

    void on_Rojo_clicked();

    void on_Verde_clicked();

    void on_Azul_clicked();

    void on_Amarillo_clicked();

    void verifica(int);

private:
    Ui::FormSimon *ui;
    QSqlDatabase db = QSqlDatabase::addDatabase("QMYSQL");
    int *vec = (int*)malloc(sizeof(int*)*50);
    int *resp = (int*)malloc(sizeof(int*)*50);
    int cont = 1;
    float tem = 1300;
    int aux = 0, aux2= 0;
};

#endif // FORMSIMON_H
