#!/usr/bin/env python

###### 
from PyQt4 import QtCore, QtGui

if __name__ == '__main__':

    import sys
    from quixcel.ui.MainWindow import MainWindow
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-c", "--config", dest="configfile",default='quickexcel.ini',
                      help="Configuration File", metavar="FILE")
    parser.add_option("-l", "--log", dest="logpath",default='quickexcel.log',
                      help="Logging File", metavar="FILE")
    (options, args) = parser.parse_args()
    app = QtGui.QApplication(sys.argv)
    window = MainWindow(config=options.configfile if options.configfile else 'quickexcel.ini')
    window.resize(1024, 680)
    window.show()
    sys.exit(app.exec_())