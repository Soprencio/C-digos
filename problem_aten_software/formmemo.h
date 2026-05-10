#ifndef FORMMEMO_H
#define FORMMEMO_H

#include <QWidget>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlQueryModel>
#include <QSqlError>
#include <QDebug>
#include <QGenericMatrix>
#include <QMessageBox>
#include <time.h>
#include <unistd.h>
#include <QTimer>
#include <QThread>

namespace Ui {
class FormMemo;
}

class FormMemo : public QWidget
{
    Q_OBJECT

public:
    explicit FormMemo(QWidget *parent = nullptr);
    ~FormMemo();

private slots:
    void on_generar_clicked();

    void on_pushButton_2_clicked();

    void on_pushButton_3_clicked();

    void on_pushButton_4_clicked();

    void on_pushButton_5_clicked();

    void on_pushButton_6_clicked();

    void on_pushButton_7_clicked();

    void on_pushButton_8_clicked();

    void on_pushButton_9_clicked();

    void on_pushButton_10_clicked();

    void on_pushButton_11_clicked();

    void on_pushButton_12_clicked();

    void on_pushButton_13_clicked();

    void on_pushButton_14_clicked();

    void on_pushButton_15_clicked();

    void on_pushButton_16_clicked();

    void on_pushButton_17_clicked();

    void confirmar(int, int, int, int);

private:
    Ui::FormMemo *ui;
    QSqlDatabase db = QSqlDatabase::addDatabase("QMYSQL");
    int aux = 0, turno = 0, pasos = 0;
    int *aux3 = (int*)malloc(sizeof(int*)*4);
    int *numer = (int*)malloc(sizeof(int*)*16);
    QGenericMatrix<4,4,int> mat;
};

#endif // FORMMEMO_H
