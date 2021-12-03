#!/user/bin/env python3
#_*_ coding: utf8 _*_

import urllib.request
import tempfile
import shutil
from unipath import Path
from os import remove
from GUI_Bing import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QDir
from PyQt5.QtGui import QPalette, QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog, QVBoxLayout, QPushButton, QFileDialog, QColorDialog, QFontDialog, QMessageBox
import sys
from PIL import Image



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.Obtener.clicked.connect(self.descargador)
        self.Ruta.clicked.connect(self.buscarRuta)
        self.Previsualizar.clicked.connect(self.prev)        
        self.setWindowTitle("Bing image downloader")
        self.setWindowIcon(QIcon("bing.jpg"))
        self.show()

    def prev(self):
        f = Path('.prev.txt')
        if f.exists() == False:
            try:
                rutadeldirectorio = file = str(QFileDialog.getExistingDirectory(self, "Select the directory to download the temporarily image."))
                ruta = open(".prev.txt","w")
                ruta.write(rutadeldirectorio + "/")
                ruta.close()
            except TypeError:
                reply = QMessageBox.critical(self, "Error","You have not selected the route.")
                remove(".prev.txt")    
        try:
            with urllib.request.urlopen('https://bing.com') as files:
                with tempfile.NamedTemporaryFile(delete=True) as tmp_file:
                    shutil.copyfileobj(files, tmp_file)
                    html = open(tmp_file.name)
        except:
            QMessageBox.critical(self, "Error","An error occurred.")
            exit()

        inicio = "/th?"
        final = ".jpg"


            
        
        try:
            for l in html.readlines():
                if inicio in l:
                    p = l.find(inicio)
                    f = l.find(final)
                    imagen = l[p:f+4]
            archivo = tempfile.NamedTemporaryFile(delete=True, prefix = ".jpg")
            urllib.request.urlretrieve("https://bing.com{}".format(imagen), archivo.name)
            img = Image.open(archivo.name)
            new_img = img.resize((256,256))
            new_img.save(archivo.name,'png')
            pixmap = QPixmap(archivo.name)
            self.Imagen.setPixmap(pixmap)

        except Exception as e:
            QMessageBox.critical(self, "Error","An error ocurred.")       

        

    def buscarRuta(self):
        try:
            rutadeldirectorio2 = str(QFileDialog.getExistingDirectory(self, "Select the directory."))
            if rutadeldirectorio2 != "":
                ruta = open(".Direccion.txt","w")
                ruta.write(rutadeldirectorio2 + "/")
                ruta.close()
                QMessageBox.information(self, "Accomplished","Path was successfully changed.")
        except:
            pass

    def descargador(self):
        f = Path('.Direccion.txt')
        u = f.exists()
        if u == False:
            try:
                rutadeldirectorio = file = str(QFileDialog.getExistingDirectory(self, "Select the directory."))
                ruta = open(".Direccion.txt","w")
                ruta.write(rutadeldirectorio + "/")
                ruta.close()
            except TypeError:
                reply = QMessageBox.critical(self, "Error","You have not selected the route.")
                remove(".Direccion.txt")
                    
                
        else:
            pass
        try:
            with urllib.request.urlopen('https://bing.com') as files:
                with tempfile.NamedTemporaryFile(delete=True) as tmp_file:
                    shutil.copyfileobj(files, tmp_file)
                    html = open(tmp_file.name)
        except:
            QMessageBox.critical(self, "Error","Web not found.")

        inicio = "/th?"
        final = ".jpg"
        
        try:
            for l in html.readlines():
                if inicio in l:
                    p = l.find(inicio)
                    f = l.find(final)
                    imagen = l[p:f+4]
            archivo = imagen[11:len(imagen)]
            ruta = open('.Direccion.txt','r')
            lista = ruta.read()
            urllib.request.urlretrieve("https://bing.com{}".format(imagen),"{}{}".format(lista,archivo))
            info = QMessageBox.information(self, "Accomplished","Image successfully downloaded.")

        except:
            QMessageBox.critical(self, "Error","An error occurred.")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
