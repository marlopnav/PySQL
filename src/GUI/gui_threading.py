
from PySide2.QtCore import QThread, Signal

from ReePlexos.Engine.Merge.merge_plexos_split_run import merge_all, merge_unziped_xml
from core.sqlHandler import DataBase

class MergeThread(QThread):
    progress_signal = Signal(float)
    progress_text = Signal(str)
    progress_text_2 = Signal(str)
    done_signal = Signal()

    def __init__(self, folder, is_local=False):
        """

        :param folder:
        """
        QThread.__init__(self)

        self.folder = folder

        self.is_local = is_local

        header1 = ['Step', 'Sample', 'Contingency', 'Period', 'Line', 'Flow', 'Shadow Price', 'Date', 'tag', 'Index']
        header2 = ['Step', 'Sample', 'Iteration', 'Zone', 'Period', 'Constraint', 'Line/Node',
                   'Flow/Angle', 'Coefficient', 'Shadow price', 'PTDF', 'LMP Part', 'Date', 'tag', 'Index']
        header3 = ['Region', 'Node', 'Step', 'Sample', 'Period', 'Load', 'Generation',
                   'Unserved Energy', 'Dump Energy', 'Net Injection', 'Date', 'tag', 'Index']

        self.xml_file_list = [('BindingContingencies Diagnostics.xml', header1)]
                              # ('CongestionCharges Diagnostics.xml', header2),
                              # ('UnservedEnergy Diagnostics.xml', header3)]

    def run(self):
        """

        :return:
        """

        allowed_subdirs = ['Interval', 'Year']
        merge_all(main_folder=self.folder,
                  allowed_subdirs=allowed_subdirs,
                  xml_file_list=self.xml_file_list,
                  text_func=self.progress_text.emit,
                  prog_func=self.progress_signal.emit,
                  text_func2=self.progress_text_2.emit,
                  is_local=self.is_local)

        self.progress_text_2.emit('Done!')
        self.progress_text.emit('Done!')
        self.progress_signal.emit(0)


