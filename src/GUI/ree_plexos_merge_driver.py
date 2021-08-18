import sys
import os
import subprocess
import datetime
import pandas as pd
from PySide2.QtWidgets import *
from PySide2 import QtGui
from src.GUI.gui import Ui_DBViewerWindow
# from src.GUI.gui_threading import MergeThread
from src.core.sqlHandler import DataBase
"""
To be stored in: Z:\CORESO tree\18-Projects\16 - D2 SWE\03 - EXPERIMENTATION\KPI DataBase
"""

def find_file(name, path):
    """
    Find file in path
    :param name:
    :param path:
    :return:
    """
    for root, dirs, files in os.walk(path):
        for file in files:
            if name in file:
                return os.path.join(root, file)
    return None


class DBViewerWindow(QMainWindow):

    def __init__(self, parent=None):
        """

        :param parent:
        """
        QMainWindow.__init__(self)
        self.ui = Ui_DBViewerWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Coreso SQLite Viewer')
        self.lock_ui = False

        # variables
        self.split_folder = ''
        self.db_path = r'Z:\CORESO tree\18-Projects\16 - D2 SWE\03 - EXPERIMENTATION\KPI DataBase/CRAC_info.db'
        self.db =DataBase(self.db_path)

        self.sconexion = "Successfuly connected to DB"
        self.bconexion = "It was not possible to connect to DB due to: "

        # action linking
        self.ui.actionReload.triggered.connect(self.refresh_tables)
        self.ui.actionSaveTable.triggered.connect(self.save_table)
        self.ui.actionExportTable.triggered.connect(self.export_to_excel)

        self.ui.LabelStatus.setText("")
        self.ui.ListTables.itemActivated.connect(self.load_table)

        self.refresh_tables()



    def closeEvent(self, event):
        """
        Close and prompt to kill the process
        :param event:
        """

        pass

    def msg(self, text, title="Warning"):
        """
        Message box
        :param text: Text to display
        :param title: Name of the window
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        # msg.setInformativeText("This is additional information")
        msg.setWindowTitle(title)
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def LOCK(self, val=True):
        """
        Lock the interface to prevent new simulation launches
        :param val:
        :return:
        """
        self.lock_ui = val

    def UNLOCK(self):
        """
        Unloack the interface
        @return:
        """
        self.LOCK(False)

    def select_split_folder(self):
        """

        :return:
        """
        folder = str(QFileDialog.getExistingDirectory(self, "Select Output Directory"))
        print(folder)
        if os.path.exists(folder):
            self.ui.plexos_split_folder_label.setText(folder)
            self.split_folder = folder

    def post_merge_run(self):
        pass

    def refresh_tables(self):

        #Clean out all the items in the list
        self.ui.ListTables.clear()

        #Add items to the list, if it is not possible raise the bad conection label
        try:
            table_names = self.db.get_tables_names()
            for t in table_names:
                item = QListWidgetItem(t)
                self.ui.ListTables.addItem(item)
            self.ui.LabelStatus.setText(self.sconexion)
            self.ui.LabelStatus.setStyleSheet("color: green")
        except Exception as e:
            self.ui.LabelStatus.setText(self.bconexion + str(e))
            self.ui.LabelStatus.setStyleSheet("color: red")

    def load_table(self,item=""):

        item = item if item else self.ui.ListTables.selectedItems()[0].text()

        headers, table = self.db.get_table(item.text())

        self.ui.TableViewer.setRowCount(0)
        self.ui.TableViewer.setColumnCount(len(headers))

        self.ui.TableViewer.setHorizontalHeaderLabels(headers)
        for i,row in enumerate(table):
            self.ui.TableViewer.insertRow(i)
            for j,c in enumerate(row):
                self.ui.TableViewer.setItem(i,j, QTableWidgetItem(str(c)))
        t = 0

    def save_table(self):
        fields = []

        for r in range(self.ui.TableViewer.rowCount()):
            row = []
            for c in range(self.ui.TableViewer.columnCount()):
                row.append(self.ui.TableViewer.item(r,c).text())
            fields.append(row)

        table = self.ui.ListTables.selectedItems()[0].text()

        self.db.update_table(table, fields)

        a = 1

    def export_to_excel(self):
        table = self.ui.ListTables.selectedItems()[0].text()

        path = table + '.xlsx'

        self.db.export_table_to_excel(path, table)
        self.ui.LabelStatus.setText(table + " was successfully saved!")
        self.ui.LabelStatus.setStyleSheet("color: blue")


def runDBViewer():
    """

    :return:
    """
    app = QApplication(sys.argv)
    window = DBViewerWindow()
    # window.resize(1.61 * 700.0, 600.0)  # golden ratio
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":

    runDBViewer()
