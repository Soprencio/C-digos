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
    void on_actionUsuarios_triggered();

    void on_actionMostrar_Usuarios_triggered();

    void on_actionEst_Bue_Mal_y_Reg_triggered();

    void on_actionBuenos_Malos_y_Regulares_triggered();

    void on_actionEst_MemoTest_triggered();

    void on_actionEst_Simon_Says_triggered();

    void on_actionSimon_Says_triggered();

    void on_actionMemoTest_triggered();

private:
    Ui::MainWindow *ui;
    void loadSubWindows(QWidget * qwidget, int);
};
#endif // MAINWINDOW_H
