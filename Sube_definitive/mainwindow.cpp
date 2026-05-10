#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "formaltas.h"
#include "formlistado.h"
#include "formcarga.h"
#include "formpagar.h"
#include "formpago.h"
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

void MainWindow::on_actionAlta_triggered()
{
    loadSubWindows(new FormAltas(this));
}


void MainWindow::on_actionslair_triggered()
{
    exit(0);
}


void MainWindow::on_actionListado_triggered()
{
    loadSubWindows(new FormListado(this));
}

void MainWindow::loadSubWindows(QWidget *qwidget)
{
    auto window = ui->mdiArea->addSubWindow(qwidget);
    window->setWindowTitle(qwidget->windowTitle());
    window->setWindowIcon(qwidget->windowIcon());
    window->show();
}

void MainWindow::on_actionCargar_Saldo_triggered()
{
    loadSubWindows(new FormCarga(this));
}


void MainWindow::on_actionPagar_Boleto_triggered()
{
    loadSubWindows(new FormPagar(this));
}


void MainWindow::on_actionListado_Viajes_triggered()
{
    loadSubWindows(new FormPago(this));
}

