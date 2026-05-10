#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlQueryModel>
#include <QSqlError>
#include <QDebug>

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_actionAlta_triggered();

    void on_actionslair_triggered();

    void on_actionListado_triggered();

    void on_actionCargar_Saldo_triggered();

    void on_actionPagar_Boleto_triggered();

    void on_actionListado_Viajes_triggered();

private:
    Ui::MainWindow *ui;
    void loadSubWindows(QWidget * qwidget);
};
#endif // MAINWINDOW_H
