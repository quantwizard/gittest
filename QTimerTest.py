#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PyQt4.QtCore import QTimer, QObject, SIGNAL

class timerTest:
    def __init__(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerfunc)
        #QObject.connect(self.timer, SIGNAL("timeout()"), self.timerfunc)
        
    def timerfunc(self):
        print "lalalala"

    def starTimer(self):
        self.timer.start(1000)

    def doNothing(self):
        pass
        
if __name__ == "__main__":
    import sys
    #from datetime import datetime
    from PyQt4.QtCore import QCoreApplication

    # 必须通过app的event loop才能让QTimer工作，否则QTimer无效
    app = QCoreApplication(sys.argv)
    
    tt = timerTest()
    
    tt.starTimer()
    
    app.exec_()
