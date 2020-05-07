#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 20:34:12 2020

I didn't generate any the matplotlib canvas code. I took it from 
some turkish blog/youtube channel

https://yapayzekalabs.blogspot.com/2018/11/pyqt5-gui-qt-designer-matplotlib.html

It was a bit tricky to get matplotlib to work properly.

@author: stephen

TODO:
    Add Alias or description for nodes
    Turn complete graph into object
    Add graph summary statistics
    Enter button for add connection


"""
import pickle
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QInputDialog, QFileDialog



class MplWidget(QWidget):    
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)        
        self.canvas = FigureCanvas(Figure(figsize=(531/100,431/100),dpi=100))        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 773)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.makeGraph = QtWidgets.QPushButton(self.centralwidget)
        self.makeGraph.setGeometry(QtCore.QRect(430, 690, 111, 23))
        self.makeGraph.setObjectName("makeGraph")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 540, 121, 61))
        self.label_6.setObjectName("label_6")
        self.addNode = QtWidgets.QPushButton(self.centralwidget)
        self.addNode.setGeometry(QtCore.QRect(180, 660, 75, 23))
        self.addNode.setObjectName("addNode")
        self.clearGraph = QtWidgets.QPushButton(self.centralwidget)
        self.clearGraph.setGeometry(QtCore.QRect(880, 700, 75, 23))
        self.clearGraph.setObjectName("clearGraph")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 340, 381, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 400, 271, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nodeName = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.nodeName.setObjectName("nodeName")
        self.horizontalLayout.addWidget(self.nodeName)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 440, 371, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.nodeHiddenUnits = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.nodeHiddenUnits.setProperty("value", 20)
        self.nodeHiddenUnits.setObjectName("nodeHiddenUnits")
        self.horizontalLayout_2.addWidget(self.nodeHiddenUnits)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.internConnectStrength = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.internConnectStrength.setMaximum(1.0)
        self.internConnectStrength.setSingleStep(0.05)
        self.internConnectStrength.setProperty("value", 0.4)
        self.internConnectStrength.setObjectName("internConnectStrength")
        self.horizontalLayout_2.addWidget(self.internConnectStrength)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 470, 411, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.connectToName = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.connectToName.setObjectName("connectToName")
        self.horizontalLayout_3.addWidget(self.connectToName)
        self.connectStrength = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_3)
        self.connectStrength.setMaximum(1.0)
        self.connectStrength.setSingleStep(0.05)
        self.connectStrength.setProperty("value", 0.15)
        self.connectStrength.setObjectName("connectStrength")
        self.horizontalLayout_3.addWidget(self.connectStrength)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.addConnection = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.addConnection.setObjectName("addConnection")
        self.horizontalLayout_3.addWidget(self.addConnection)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(560, 469, 371, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.nodeList = QtWidgets.QListWidget(self.centralwidget)
        self.nodeList.setGeometry(QtCore.QRect(40, 530, 261, 111))
        self.nodeList.setObjectName("nodeList")
        self.graphSummary = QtWidgets.QListWidget(self.centralwidget)
        self.graphSummary.setGeometry(QtCore.QRect(560, 530, 371, 151))
        self.graphSummary.setObjectName("graphSummary")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(430, 30, 531, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.MplWidget_summary = MplWidget(self.tab)
        self.MplWidget_summary.setGeometry(QtCore.QRect(0, 0, 521, 411))
        self.MplWidget_summary.setObjectName("MplWidget_summary")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.MplWidget_adj = MplWidget(self.tab_2)
        self.MplWidget_adj.setGeometry(QtCore.QRect(0, 0, 521, 411))
        self.MplWidget_adj.setObjectName("MplWidget_adj")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 521, 401))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab_3, "")
        self.saveB = QtWidgets.QPushButton(self.centralwidget)
        self.saveB.setGeometry(QtCore.QRect(720, 700, 75, 23))
        self.saveB.setObjectName("saveB")
        self.loadB = QtWidgets.QPushButton(self.centralwidget)
        self.loadB.setGeometry(QtCore.QRect(800, 700, 75, 23))
        self.loadB.setObjectName("loadB")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1010, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.makeGraph.setText(_translate("MainWindow", "Generate Graph!"))
        self.label_6.setText(_translate("MainWindow", "Please pick a stregnth \n"
"between 0 and 1"))
        self.addNode.setText(_translate("MainWindow", "Add Node!"))
        self.clearGraph.setText(_translate("MainWindow", "Clear Data"))
        self.label_2.setText(_translate("MainWindow", "Add Node"))
        self.label.setText(_translate("MainWindow", "Node Name"))
        self.label_3.setText(_translate("MainWindow", "# Hidden Units"))
        self.label_7.setText(_translate("MainWindow", "Connection Strength"))
        self.label_4.setText(_translate("MainWindow", "Connect To:"))
        self.addConnection.setText(_translate("MainWindow", "Add Connection"))
        self.label_8.setText(_translate("MainWindow", "Graph Summary"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Graph Summary"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Connection Matrix"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2,sans-serif\'; font-size:14pt; font-weight:600;\">NOTES:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2,sans-serif\'; font-size:8.5pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2,sans-serif\'; font-size:12pt;\">This is a little GUI I wrote to design Artificial Neural Networks. These are some pointers</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2,sans-serif\'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2,sans-serif\'; font-size:12pt;\">  * There is no \'redo\' but you </span><span style=\" font-family:\'MS Shell Dlg 2,sans-serif\'; font-size:12pt; font-style:italic; text-decoration: underline;\">CAN</span><span style=\" font-family:\'MS Shell Dlg 2,sans-serif\'; font-size:12pt;\"> overwrite nodes and connections (just add another entry)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2,sans-serif\'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2,sans-serif\'; font-size:12pt;\">  * When saving, do not specify file type (it will be written as a binary file)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2,sans-serif\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2,sans-serif\'; font-size:12pt;\">  * If you specify a connection to a node that doesn\'t exist, you must then create the node. It does </span><span style=\" font-family:\'MS Shell Dlg 2,sans-serif\'; font-size:12pt; font-weight:600;\">not</span><span style=\" font-family:\'MS Shell Dlg 2,sans-serif\'; font-size:12pt;\"> auto-create nodes</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2,sans-serif\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2,sans-serif\'; font-size:12pt;\">  * Remember to SAVE! </span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Notes"))
        self.saveB.setText(_translate("MainWindow", "Save"))
        self.loadB.setText(_translate("MainWindow", "Load"))



class MatplotlibWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Python Graph Builder")
        self.Graph = self.GraphC(); 
        self.currentState = {'currConnections':{}}
        
        # Button Actions
        self.connectToName.returnPressed.connect(self.addCon)
        self.addConnection.clicked.connect(self.addCon)
        self.addNode.clicked.connect(self.addNode_fun)
        self.makeGraph.clicked.connect(self.makeGraph_fun)  
        self.clearGraph.clicked.connect(self.clearGraph_fun)
        self.graphSummary.addItem('Node Name \t \t Connections')
        self.saveB.clicked.connect(self.save_fun)
        self.loadB.clicked.connect(self.load_fun)
    
    # Define Functions
    def addCon(self):
        to = self.connectToName.text()
        if len(to) == 0:
            return
        if to in self.currentState['currConnections']:
            del(self.currentState['currConnections'][to])
        strength = self.connectStrength.value()
        self.currentState['currConnections'][to] = strength
        self.nodeList.clear()
        for k, v in self.currentState['currConnections'].items():
            self.nodeList.addItem(k+'    ...... \t %.2f' % v)
        self.connectToName.clear()
    
    def addNode_fun(self):
        if self.connectToName.isModified():
            self.addCon()
        name = self.nodeName.text()
        numUnits = self.nodeHiddenUnits.value()
        strength = self.internConnectStrength.value()
        connections = self.currentState['currConnections']
        self.Graph.add_node(name,numUnits,strength,connections.copy())
        self.update_summary()
        self.nodeName.clear(); self.nodeList.clear()
        self.currentState = {'currConnections':{}}
        # Might need to clear variables
    
    def makeGraph_fun(self):
        [adj, G] = self.Graph.build_graph()
        self.MplWidget_summary.canvas.axes.clear()
        ax = self.MplWidget_summary.canvas.axes
        nx.draw_shell(G, font_size=12, ax=ax, with_labels=True, 
                        font_weight='bold', node_color='#81aef7')
        self.MplWidget_summary.canvas.draw()
        self.MplWidget_adj.canvas.axes.clear()
        self.MplWidget_adj.canvas.axes.imshow(adj)
        self.MplWidget_adj.canvas.draw()
        
    def clearGraph_fun(self):
        self.nodeList.clear()
        self.graphSummary.clear()
        self.graphSummary.addItem('Node Name \t \t Connections')
        self.MplWidget_summary.canvas.axes.clear()
        self.MplWidget_adj.canvas.axes.clear()
        self.MplWidget_summary.canvas.draw()
        self.MplWidget_adj.canvas.draw()
        self.Graph = self.GraphC()
        
    def save_fun(self):
        name = QFileDialog.getSaveFileName(self, 'Save File')[0]
        with open(name+'.bin', 'wb') as fp:
            pickle.dump(self.Graph.nodes, fp)
        
    def load_fun(self):
        self.clearGraph_fun()
        name = QFileDialog.getOpenFileName(self, 'Load File')[0]
        with open(name,'rb') as fp:
            self.Graph.nodes = pickle.load(fp)
        self.makeGraph_fun()
        self.update_summary()
    
    def update_summary(self):
        self.graphSummary.clear()
        self.graphSummary.addItem('Node Name \t \t Connections')
        for node in self.Graph.nodes:
            connections = [k+' (%0.2f)' % node[2][k] for k in node[2] if k != 'self' and k != node[0]]
            self.graphSummary.addItem(node[0]+' (%0.2f)' % node[2][node[0]] + '\t \t '+ ', '.join(connections))
        
        
    
    # Some of the graph logic is placed here (could have been seperate)
    class GraphC():
        def __init__(self):
            self.nodes = []
            
        def add_node(self, name, num_units, connect_strength, connections):
            # Check if already present, overwrite
            if name in [k[0] for k in self.nodes]:
                idx = [k[0] for k in self.nodes].index(name)
                print(idx)
                del(self.nodes[idx])
            connections['self'] = name
            connections[name] = connect_strength
            self.nodes.append([name, num_units, connections])
        
        def build_graph(self):
            # Build Summary of Model
            num_nodes = len(self.nodes)
            G = nx.DiGraph()
            for i in range(num_nodes):
                currNode = self.nodes[i]
                for j in range(num_nodes):
                    if currNode[2].get(self.nodes[j][0],False):
                        G.add_edge(currNode[0], self.nodes[j][0], weight=currNode[2][currNode[0]])
                        
            # Build Full Model
            units = []
            for node in self.nodes:
                units.extend( node[1]*[node[2]] )
            num_units = len(units)
            adj = np.zeros((num_units,num_units), dtype=bool)
            for i in range(num_units):
                currUnit = units[i]
                for j in range(num_units):
                    if currUnit.get(units[j]['self'],False):
                        adj[i,j] = np.random.binomial(1, currUnit[units[j]['self']])
            return adj, G



if __name__ == "__main__":
    app = QApplication([])
    window = MatplotlibWidget()
    window.show()
    app.exec_()











## For easier scrolling
