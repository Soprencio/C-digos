#ifndef FORMPAGAR_H
#define FORMPAGAR_H

#include <QWidget>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlQueryModel>
#include <QSqlError>
#include <QDebug>
#include <QMessageBox>

namespace Ui {
class FormPagar;
}

class FormPagar : public QWidget
{
    Q_OBJECT

public:
    explicit FormPagar(QWidget *parent = nullptr);
    ~FormPagar();

private slots:
    void on_Cofirm_ram_us_clicked();

    void on_Mostrar_precio_clicked();

    void on_pagar_viaje_clicked();

    void on_ramal_currentIndexChanged(int index);

    void on_usuario_currentIndexChanged(int index);

    void on_parada1_currentIndexChanged(int index);

    void on_parada2_currentIndexChanged(int index);

    void on_linea_currentIndexChanged(int index);

private:
    Ui::FormPagar *ui;
    QSqlDatabase qdb = QSqlDatabase::addDatabase("QMYSQL");
    int user;
    double sald;
    QString pri, seg, ram;
};

#endif // FORMPAGAR_H
