#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "formuser.h"
#include "formlista.h"
#include "formestbmr.h"
#include "formestmemo.h"
#include "formestsimon.h"
#include "formbmr.h"
#include "formsimon.h"
#include "formmemo.h"
#include <QMdiSubWindow>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    qDebug() << QSqlDatabase::drivers();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_actionUsuarios_triggered()
{
    loadSubWindows(new FormUser (this), 1);
}

void MainWindow::loadSubWindows(QWidget *qwidget, int i)
{
    auto window = ui->mdiArea->addSubWindow(qwidget);
    if(i == 1)
    {
        window->setWindowTitle("Cargar Usuario");
    }
    else if(i == 2)
    {
        window->setWindowTitle("Mostrar Usuario");
    }
    else if(i == 3)
    {
        window->setWindowTitle("Estadísticas BMR");
    }
    else if(i == 4)
    {
        window->setWindowTitle("Estadísticas Memotest");
    }
    else if(i == 5)
    {
        window->setWindowTitle("Estadísticas SimonSays");
    }
    else if(i == 6)
    {
        window->setWindowTitle("Buenos, Malos y Regulares");
    }
    else if(i == 7)
    {
        window->setWindowTitle("Simon Says");
    }
    else if(i == 8)
    {
        window->setWindowTitle("Memotest");
    }
    window->setWindowIcon(qwidget->windowIcon());
    window->setWindowFlags(qwidget->windowFlags() & ~Qt::WindowMinimizeButtonHint & ~Qt::WindowMaximizeButtonHint);
    window->show();
}

void MainWindow::on_actionMostrar_Usuarios_triggered()
{
    loadSubWindows(new FormLista (this), 2);
}


void MainWindow::on_actionEst_Bue_Mal_y_Reg_triggered()
{
    loadSubWindows(new FormEstBMR (this), 3);
}


void MainWindow::on_actionEst_MemoTest_triggered()
{
    loadSubWindows(new FormEstMemo (this), 4);
}


void MainWindow::on_actionEst_Simon_Says_triggered()
{
    loadSubWindows(new FormEstSimon (this), 5);
}


void MainWindow::on_actionBuenos_Malos_y_Regulares_triggered()
{
    loadSubWindows(new FormBMR (this), 6);
}


void MainWindow::on_actionSimon_Says_triggered()
{
    loadSubWindows(new FormSimon (this), 7);
}


void MainWindow::on_actionMemoTest_triggered()
{
    loadSubWindows(new FormMemo (this), 8);
}

