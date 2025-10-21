import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
)
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    """Jendela utama aplikasi PySide6 sederhana."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 - Uji Coba Distribusi")
        self.setGeometry(100, 100, 400, 200) # (x, y, lebar, tinggi)
        
        # Tata Letak Vertikal
        layout = QVBoxLayout()
        
        # Label
        self.label = QLabel("Halo! Aplikasi PySide6 Berhasil Berjalan.", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 16px; margin-bottom: 20px;")
        
        # Tombol
        self.button = QPushButton("Tekan Saya", self)
        self.button.clicked.connect(self.on_button_click)
        
        # Tambahkan Widget ke Layout
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        self.setLayout(layout)

    def on_button_click(self):
        """Fungsi yang dipanggil saat tombol ditekan."""
        self.label.setText("Anda menekan tombol! Distribusi Lintas Platform Sukses!")
        self.button.setEnabled(False) # Nonaktifkan tombol setelah ditekan

# Bagian Utama
if __name__ == "__main__":
    # Buat instance aplikasi
    app = QApplication(sys.argv)
    
    # Buat dan tampilkan jendela utama
    window = MainWindow()
    window.show()
    
    # Jalankan loop event aplikasi
    sys.exit(app.exec())